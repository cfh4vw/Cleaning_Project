# Cleaning_Project

### Executive Summary
I got this idea from the first case study we did, and from all of the other data science classes I have taken that require data cleaning and manipulation. The problem that I aim to solve with this project is dealing with messy datasets, containing missing values and non-uniform data types. This tool is meant for anyone analyzing data looking to optimize their cleaning process. Overall, the webapp that I have built will consume a csv file, clean it, and return a new cleaned csv file and a summary of how many rows were removed. The cleaning process that I employ with this app is simple, it either removes or fills missing data points. It also standardizes names and values of the dataset, as well as data types within rows.

### System Overview
To complete this project, I used the data cleaning concepts from the first case study about NYC 311 service requests. I worked in my computer's terminal, Cursor, Docker, Azure, and pushed and pulled data from my Github Repository. The datasets I have provided as examples for cleaning were pulled from Kaggle, or some of the smaller ones (grocery.csv and example.csv) I made on my own in an Excel file. I have laid out the structure of my app in the linked architecture diagram which is also linked in the assets file. Lastly, this Github Repo has an MIT license. \
<img src = "assets/CSV_Cleaning.png" width="300" height="400">

### How to Run (Local)
See run.sh file. I have made this file executable as code so it is ready to go. 

### Design Decisions
I ultimately landed on my data cleaning idea because to me, this is one of the most important steps in analyzing and exploring data. This is really what got me interested in Data Science, as I held the power to clean and manipulate my dataset with just a few lines of Python code. I considered doing something similar to some of the case studies we had done in class, like the lanternfly image uploading, but I wanted to challenge myself and allow my creativity and practicality to shine through in this project. While this app runs locally on my computer, I decided to deploy it to Azure as well so that it was publicly accessible when I choose to have it running. The limitations of this project are pretty simple: the tool does not have any specific industry knowledge, so any who use it will have to scan over the cleaned dataaset to make sure the data still makes sense. There was no way to remove "unusual" values from the csv files uploaded, because the definition of an unusual value will vary from dataset to dataset.

### Results and Evaluation
Sample cleaned datasets are provided in the assets folder. I tested this tool with simple datasets first that only contained a few rows, for example, my example and grocery csvs. Then, I started using bigger datasets with more realistic data, and I hit a few errors. The first error I got was that my app didn't know how to deal with boolean data. I fixed this by including it in my category column designation, so that any rows with missing boolean data would also be dropped. The next issue I ran into was that my tool would only drop data if there was a truly empty cell. My example cafe_sales csv had many cells reading "error" or "unknown", so I included different variations of those words in my dropping criteria. The next thing I added was a simple dashboard showing how many rows were removed from the dataset. It should be understood to the user that besides removing/filling cells, this tool also converts all labels and values to lowercase, and replaces spaces with underscores in the column names. 

### What's Next
This app is really just a prototype at this point. I would like to learn a bit more about HTML code so I can make the interface more user-friendly, and more aesthetically pleasing. I could also expand this tool into one that makes easily accessible subsets of the data. Something that I have run into a few times in my classes has been filtering dataframes to only inclue a specific subset of data without altering the original. I think my app could make this a lot easier by including some of the "grep" logic we used in the first case study to filter dataframes on only the rows of interest. 

### Links
[Github Repo Link](https://github.com/cfh4vw/Cleaning_Project.git)
