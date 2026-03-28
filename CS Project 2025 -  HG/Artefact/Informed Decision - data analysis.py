# Seperate Data Analysis - Find the device model with lowest battery drain to help users to make an informed decision
# Import libaries 
import pandas as pd

# Read contents from CSV file and choose the columns needed for data analysis
df = pd.read_csv("E:/CS Project 2025 -  HG/Artefact/user_behavior_dataset_raw - in.csv", usecols=["Device Model","Battery Drain (mAh/day)"])

# Change pandas dataframe into list format 
list_of_rows = [list(row) for row in df.values]

# Set variables
battery_drain_per_group = [0,0,0,0,0]
num_of_people = [0,0,0,0,0]

for x in range(len(list_of_rows)):
    phone_brand = list_of_rows[x][0]  # The phone brand (first column)
    battery_drain = list_of_rows[x][1]  # The battery drain (in mAh) for the user (second column)

    # Add the battery drain to the corresponding brand's total
    if phone_brand[0] == "G":
        battery_drain_per_group[0] += battery_drain
        num_of_people[0] += 1
    elif phone_brand[0] == "S":
        battery_drain_per_group[1] += battery_drain
        num_of_people[1] += 1
    elif phone_brand[0] == "i":
        battery_drain_per_group[2] += battery_drain
        num_of_people[2] += 1
    elif phone_brand[0] == "O":
        battery_drain_per_group[3] += battery_drain
        num_of_people[3] += 1
    elif phone_brand[0] == "X":
        battery_drain_per_group[4] += battery_drain
        num_of_people[4] += 1

# Find the average battery drain per phone brand 
average_batter_drain = [0,0,0,0,0]
for x in range(len(battery_drain_per_group)):
    average_batter_drain[x] = round(battery_drain_per_group[x] / num_of_people[x])
print(average_batter_drain)