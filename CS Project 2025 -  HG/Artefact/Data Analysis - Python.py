# Import libaries 
import pandas as pd
import matplotlib.pyplot as plt
import statistics

# Read contents from CSV file and choose the columns needed for data analysis
df = pd.read_csv("E:/CS Project 2025 -  HG/Artefact/user_behavior_dataset_raw - in.csv", usecols=["Operating System", "Screen On Time (hours/day)", "Age"])
# Code to create a cleaned version of dataset with the chosen columns 
df.to_csv('cleaned.csv', index=False)

# First analysis -  Find average screen time per age group
# Set variables 
count_per_age_group = [0,0,0,0,0]
screen_time_per_group = [0,0,0,0,0]

# Change pandas dataframe into list format 
list_of_rows = [list(row) for row in df.values]

# Loop through every row 
for x in range(len(list_of_rows)):
    if list_of_rows[x][2] <= 19:
        screen_time_per_group[0] += list_of_rows[x][1]
        count_per_age_group[0] += 1
       
    elif 20 <= list_of_rows[x][2] <= 29:
        screen_time_per_group[1] += list_of_rows[x][1]
        count_per_age_group[1] += 1
       
    elif 30 <= list_of_rows[x][2] <= 39:
        screen_time_per_group[2] += list_of_rows[x][1]
        count_per_age_group[2] += 1
    
    elif 40 <= list_of_rows[x][2] <= 49:
        screen_time_per_group[3] += list_of_rows[x][1]
        count_per_age_group[3] += 1
       
    elif 50 <= list_of_rows[x][2] <= 60:
        screen_time_per_group[4] += list_of_rows[x][1]
        count_per_age_group[4] += 1
       
#print("Average Screen On Time (hours/day) for 10-19 years :", round((screen_time_per_group[0]/count_per_age_group[0]),1))
#print("Average Screen On Time (hours/day) for 20-29 years :", round((screen_time_per_group[1]/count_per_age_group[1]),1))
#print("Average Screen On Time (hours/day) for 30-39 years :", round((screen_time_per_group[2]/count_per_age_group[2]),1))
#print("Average Screen On Time (hours/day) for 40-49 years :", round((screen_time_per_group[3]/count_per_age_group[3]),1))
#print("Average Screen On Time (hours/day) for 50-60 years :", round((screen_time_per_group[4]/count_per_age_group[4]),1))

average_screen_time = [0,0,0,0,0] 
age_ranges = ["10-19", "20-29", "30-39", "40-49", "50-60"]

for x in range(len(average_screen_time)):
    if count_per_age_group[x] > 0:
        average_screen_time[x] = round(screen_time_per_group[x] / count_per_age_group[x],1)
#print("The average screen time per age group is:", average_screen_time)

# Display the results on a line graph
plt.plot(age_ranges, average_screen_time, "y-")
plt.xlabel("Age groups")
plt.ylabel("Screen On time (hrs/day)")
plt.title("Average Screen On Time for Age Groups")
#plt.show()

# Second analysis - Find the most used operating system per age group
# Set variables
OS_group1 = []
OS_group2 = []
OS_group3 = []
OS_group4 = []
OS_group5 = []
groups = [("10-19 years",OS_group1), ("20-29 years",OS_group2), ("30-39 years",OS_group3), ("40-49 years",OS_group4), ("50-60 years", OS_group5)]
group_names = []
most_common_os = []
counts = []

# Loop through each row
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


plt.bar(age_ranges, counts, color="cyan")
plt.title("OS used by Age Groups - Android")
plt.xlabel("Age Groups")
plt.ylabel("Count of Most Used OS")
#plt.show()
