import csv
import json

data = []
with open('fitness_data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append({
            'Record_ID': int(row['Record_ID']),
            'User_ID': row['User_ID'],
            'Date': row['Date'],
            'Age': int(row['Age']),
            'Gender': row['Gender'],
            'Weight_Kg': float(row['Weight_Kg']),
            'Height_Cm': float(row['Height_Cm']),
            'Activity_Type': row['Activity_Type'],
            'Workout_Duration_Minutes': int(row['Workout_Duration_Minutes']),
            'Calories_Burned': int(row['Calories_Burned']),
            'Food_Category': row['Food_Category'],
            'Calories_Consumed': int(row['Calories_Consumed']),
            'Water_Intake_Liters': float(row['Water_Intake_Liters']),
            'Steps': int(row['Steps']),
            'Sleep_Hours': float(row['Sleep_Hours'])
        })

with open('fitness_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

with open('fitness_data.js', 'w', encoding='utf-8') as f:
    f.write("window.FITNESS_DATA = " + json.dumps(data) + ";\n")

print(f"Exported {len(data)} records to fitness_data.json and fitness_data.js")
