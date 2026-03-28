from flask import Flask, render_template
import json
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("E:/CS Project 2025 -  HG/Artefact/user_behavior_dataset_raw - in.csv", usecols=["Operating System", "Screen On Time (hours/day)", "Age"])
df.to_csv('cleaned.csv', index=False)
count_per_age_group = [0,0,0,0,0]
screen_time_per_group = [0,0,0,0,0]
age_ranges = ["10-19", "20-29", "30-39", "40-49", "50-60"]
list_of_rows = [list(row) for row in df.values]

OS_group1 = []
OS_group2 = []
OS_group3 = []
OS_group4 = []
OS_group5 = []
groups = [("10-19 years",OS_group1), ("20-29 years",OS_group2), ("30-39 years",OS_group3), ("40-49 years",OS_group4), ("50-60 years", OS_group5)]
group_names = []
most_common_os = []
counts = []

for x in range(len(list_of_rows)):
    if list_of_rows[x][2] <= 19:
        OS_group1.append(list_of_rows[x][0])
        
    elif 20 <= list_of_rows[x][2] <= 29:
        OS_group2.append(list_of_rows[x][0])
        
    elif 30 <= list_of_rows[x][2] <= 39:
        OS_group3.append(list_of_rows[x][0])
        
    elif 40 <= list_of_rows[x][2] <= 49:
        OS_group4.append(list_of_rows[x][0])
        
    elif 50 <= list_of_rows[x][2] <= 60:
        OS_group5.append(list_of_rows[x][0])
        
for group_name, group in groups:
    most_common = None
    max_count = 0
    for string in group:
        count = group.count(string)
        if count > max_count:
            most_common = string
            max_count = count
            
    group_names.append(group_name)
    most_common_os.append(most_common)
    counts.append(max_count)
    #print("The most common OS used in", group_name , most_common,"with a number of", max_count)

# Python code to launch website through Thonny  
app = Flask(__name__,)

@app.route('/')
def index():
    list1 = json.dumps(age_ranges)
    list2 = json.dumps(counts)
    return render_template("index.html", list1=list1, list2=list2)

@app.route("/form1")
def form1_page():
    return render_template('form_page1.html')

@app.route("/form2")
def form2_page():
    return render_template('form_page2.html')

app.run(host='0.0.0.0',port=6001, debug = False)

