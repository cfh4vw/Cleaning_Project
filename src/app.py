from flask import Flask, request, send_file, render_template_string
import pandas as pd
import numpy as np
from io import BytesIO

app = Flask(__name__)

# Health check
@app.route("/health")
def health():
    return {"status": "ok"}

# Web form for uploading CSV
@app.route("/", methods=["GET"])
def index():
    return render_template_string("""
    <!doctype html>
    <title>Upload CSV for Cleaning</title>
    <h1>Upload CSV for Cleaning</h1>
    <form action="/clean" method="post" enctype="multipart/form-data">
      <input type="file" name="file" required>
      <input type="submit" value="Clean">
    </form>
    """)

# Cleaning function: fill NaN with 0
def clean_dataframe(df):
    df = df.copy()
    
    #standardize column names and data
    df.columns = (df.columns.str.strip().str.lower().str.replace(" ","_"))
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype(str).str.strip().str.lower()
        
    #identifying columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    category_cols = df.select_dtypes(exclude=[np.number]).columns
    
    #clean missing values
    df = df.replace(["nan", "none", "", "error", "unknown", "N/A"], pd.NA)
    df[numeric_cols] = df[numeric_cols].fillna(0)
    df = df.dropna(subset=category_cols)
    
    #remove duplicate rows
    df = df.drop_duplicates()

    #Convert Data Types
    df = df.convert_dtypes()
    
    return df

# Cleaning endpoint
@app.route("/clean", methods=["POST"])
def clean():
    uploaded_file = request.files.get("file")
    if not uploaded_file:
        return "No file uploaded", 400

    # Read CSV
    df = pd.read_csv(uploaded_file)

    #Calculate Original Row Numbers
    original_shape = df.shape
    
    # Clean data
    cleaned_df = clean_dataframe(df)

    #Calculate changes:
    new_shape = cleaned_df.shape
    rows_removed = original_shape[0] - new_shape[0]
    changes = {"original_rows": original_shape[0], "rows_removed": rows_removed}
    
    # Prepare file for download
    buffer = BytesIO()
    cleaned_df.to_csv(buffer, index=False)
    buffer.seek(0)

    session["cleaned_csv"] = cleaned_df.to_csv(index=False)
    
    # Get original filename
    original_name = uploaded_file.filename
    cleaned_name = f"cleaned_{original_name}"

    # Show changes dashboard and allow user to download cleaned file
    return render_template_string("""
        <!doctype html>
        <title>Cleaning Summary</title>
        <h1>Dataset Cleaned</h1>

        <p><strong>Original rows:</strong> {{ changes.original_rows }}</p>
        <p><strong>Rows removed:</strong> {{ changes.rows_removed }}</p>

        <h3>Download Cleaned CSV:</h3>
        <a href="/download">Click here to download</a>

        <br><br>
        <a href="/">Back</a>
    """, changes=changes, cleaned_name=cleaned_name)

# Download endpoint
@app.route("/download")
def download():
    csv_data = session.get("cleaned_csv")
    if not csv_data:
        return "No cleaned file available", 400

    buffer = BytesIO()
    buffer.write(csv_data.encode("utf-8"))
    buffer.seek(0)

    return send_file(buffer,
                     as_attachment=True,
                     download_name="cleaned_file.csv",
                     mimetype="text/csv")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
