import csv
import random
from datetime import date, timedelta

# Set random seed for reproducibility
random.seed(42)

# Define User Profiles (20 Users to provide realistic demographic distribution)
users = []
genders = ['Male', 'Female']
activities = ['Running', 'Cycling', 'Swimming', 'Walking', 'Strength Training', 'Yoga', 'HIIT']
food_categories = ['Proteins', 'Carbohydrates', 'Vegetables', 'Fruits', 'Dairy', 'Snacks & Fats']

# Base user demographics
for i in range(1, 21):
    user_id = f"USR{100 + i}"
    gender = 'Male' if i % 2 == 1 else 'Female'
    if gender == 'Male':
        age = random.randint(22, 52)
        height_cm = random.randint(168, 188)
        base_weight = random.randint(68, 92)
    else:
        age = random.randint(21, 48)
        height_cm = random.randint(154, 172)
        base_weight = random.randint(52, 74)
    
    users.append({
        'user_id': user_id,
        'gender': gender,
        'age': age,
        'height_cm': height_cm,
        'base_weight': base_weight
    })

# Calorie burn rates (approximate kcal per minute by activity)
burn_rates = {
    'Running': (9.5, 12.5),
    'Cycling': (7.5, 10.5),
    'Swimming': (8.0, 11.5),
    'Walking': (4.0, 6.0),
    'Strength Training': (5.5, 8.5),
    'Yoga': (3.0, 5.0),
    'HIIT': (10.0, 14.0)
}

# Generate 650 records spanning from 2024-01-01 to 2024-03-15
records = []
record_id = 1
start_date = date(2024, 1, 1)

# We will generate daily logs for users across dates
num_days = 40  # 40 days for 20 users -> ~650 active records (some rest days)

for day_offset in range(num_days):
    curr_date = start_date + timedelta(days=day_offset)
    for u in users:
        # 85% probability user logged activity and meals on any given day
        if random.random() < 0.85:
            activity = random.choice(activities)
            duration = random.choice([25, 30, 40, 45, 50, 60, 75, 90])
            
            # Realistic calories burned based on activity duration & user weight factor
            rate_min, rate_max = burn_rates[activity]
            rate = random.uniform(rate_min, rate_max)
            weight_factor = u['base_weight'] / 70.0
            calories_burned = int(round(duration * rate * weight_factor))
            
            # Steps correlation: walking/running produce high steps, swimming/yoga moderate/low
            if activity in ['Running', 'Walking']:
                steps = random.randint(7500, 16000)
            elif activity in ['Cycling', 'HIIT']:
                steps = random.randint(5500, 11000)
            else:
                steps = random.randint(3200, 8500)
                
            # Food category primary for the day
            food_cat = random.choice(food_categories)
            
            # Realistic daily calorie intake (1600 to 2900 kcal)
            if u['gender'] == 'Male':
                calories_consumed = random.randint(2000, 2900)
            else:
                calories_consumed = random.randint(1550, 2350)
                
            # Water intake liters (1.8 to 4.5 L, slightly higher if duration > 50 mins)
            base_water = random.uniform(2.0, 3.8)
            if duration >= 50:
                base_water += random.uniform(0.3, 0.7)
            water_liters = round(base_water, 1)
            
            # Sleep hours (5.5 to 8.8)
            sleep_hours = round(random.uniform(5.5, 8.8), 1)
            
            # Weight slight natural variance (+- 0.8 kg)
            weight_kg = round(u['base_weight'] + random.uniform(-0.8, 0.8), 1)
            
            records.append({
                'Record_ID': record_id,
                'User_ID': u['user_id'],
                'Date': curr_date.strftime('%Y-%m-%d'),
                'Age': u['age'],
                'Gender': u['gender'],
                'Weight_Kg': weight_kg,
                'Height_Cm': u['height_cm'],
                'Activity_Type': activity,
                'Workout_Duration_Minutes': duration,
                'Calories_Burned': calories_burned,
                'Food_Category': food_cat,
                'Calories_Consumed': calories_consumed,
                'Water_Intake_Liters': water_liters,
                'Steps': steps,
                'Sleep_Hours': sleep_hours
            })
            record_id += 1

print(f"Generated {len(records)} realistic fitness records.")

# Save CSV
csv_filename = "fitness_data.csv"
fieldnames = [
    'Record_ID', 'User_ID', 'Date', 'Age', 'Gender', 'Weight_Kg', 'Height_Cm',
    'Activity_Type', 'Workout_Duration_Minutes', 'Calories_Burned', 'Food_Category',
    'Calories_Consumed', 'Water_Intake_Liters', 'Steps', 'Sleep_Hours'
]

with open(csv_filename, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)

print(f"Successfully saved {csv_filename}")

# Generate SQL Script (Schema + Table + Complete INSERT statements)
sql_filename = "fitness_db_setup.sql"
with open(sql_filename, mode='w', encoding='utf-8') as f:
    f.write("-- =========================================================\n")
    f.write("-- Project: Fitness and Calorie Analysis Database Setup\n")
    f.write("-- Database: fitness_tracker_db\n")
    f.write("-- Total Records: " + str(len(records)) + "\n")
    f.write("-- Synthetic Sample Data for Demonstration Purposes\n")
    f.write("-- =========================================================\n\n")
    f.write("CREATE DATABASE IF NOT EXISTS fitness_tracker_db;\n")
    f.write("USE fitness_tracker_db;\n\n")
    f.write("DROP TABLE IF EXISTS fitness_activity_logs;\n\n")
    f.write("CREATE TABLE fitness_activity_logs (\n")
    f.write("    Record_ID INT PRIMARY KEY,\n")
    f.write("    User_ID VARCHAR(10) NOT NULL,\n")
    f.write("    Date DATE NOT NULL,\n")
    f.write("    Age INT NOT NULL,\n")
    f.write("    Gender VARCHAR(10) NOT NULL,\n")
    f.write("    Weight_Kg DECIMAL(5,2) NOT NULL,\n")
    f.write("    Height_Cm DECIMAL(5,2) NOT NULL,\n")
    f.write("    Activity_Type VARCHAR(50) NOT NULL,\n")
    f.write("    Workout_Duration_Minutes INT NOT NULL,\n")
    f.write("    Calories_Burned INT NOT NULL,\n")
    f.write("    Food_Category VARCHAR(50) NOT NULL,\n")
    f.write("    Calories_Consumed INT NOT NULL,\n")
    f.write("    Water_Intake_Liters DECIMAL(3,1) NOT NULL,\n")
    f.write("    Steps INT NOT NULL,\n")
    f.write("    Sleep_Hours DECIMAL(3,1) NOT NULL\n")
    f.write(");\n\n")
    f.write("-- Inserting sample records into fitness_activity_logs\n")
    
    # Write inserts in batches of 50 for clean execution in MySQL Workbench
    batch_size = 50
    for i in range(0, len(records), batch_size):
        batch = records[i:i+batch_size]
        f.write("INSERT INTO fitness_activity_logs (\n")
        f.write("    Record_ID, User_ID, Date, Age, Gender, Weight_Kg, Height_Cm,\n")
        f.write("    Activity_Type, Workout_Duration_Minutes, Calories_Burned, Food_Category,\n")
        f.write("    Calories_Consumed, Water_Intake_Liters, Steps, Sleep_Hours\n")
        f.write(") VALUES\n")
        val_lines = []
        for r in batch:
            val_lines.append(
                f"({r['Record_ID']}, '{r['User_ID']}', '{r['Date']}', {r['Age']}, '{r['Gender']}', "
                f"{r['Weight_Kg']}, {r['Height_Cm']}, '{r['Activity_Type']}', {r['Workout_Duration_Minutes']}, "
                f"{r['Calories_Burned']}, '{r['Food_Category']}', {r['Calories_Consumed']}, "
                f"{r['Water_Intake_Liters']}, {r['Steps']}, {r['Sleep_Hours']})"
            )
        f.write(",\n".join(val_lines) + ";\n\n")

print(f"Successfully saved {sql_filename}")
