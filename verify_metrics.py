import sqlite3
import csv

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE fitness_activity_logs (
    Record_ID INT PRIMARY KEY,
    User_ID VARCHAR(10) NOT NULL,
    Date DATE NOT NULL,
    Age INT NOT NULL,
    Gender VARCHAR(10) NOT NULL,
    Weight_Kg DECIMAL(5,2) NOT NULL,
    Height_Cm DECIMAL(5,2) NOT NULL,
    Activity_Type VARCHAR(50) NOT NULL,
    Workout_Duration_Minutes INT NOT NULL,
    Calories_Burned INT NOT NULL,
    Food_Category VARCHAR(50) NOT NULL,
    Calories_Consumed INT NOT NULL,
    Water_Intake_Liters DECIMAL(3,1) NOT NULL,
    Steps INT NOT NULL,
    Sleep_Hours DECIMAL(3,1) NOT NULL
);
""")

with open('fitness_data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        cursor.execute("INSERT INTO fitness_activity_logs VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row)
conn.commit()

def run(title, query):
    print(f"\n================ {title} ================")
    cursor.execute(query)
    cols = [d[0] for d in cursor.description]
    rows = cursor.fetchall()
    print(" | ".join(cols))
    print("-" * 60)
    for r in rows[:7]:
        print(" | ".join(str(x) for x in r))
    if len(rows) > 7:
        print(f"... ({len(rows)} total rows)")

# 1. Total KPI Metrics
run("KPI Metrics (Overall Summary)", """
SELECT 
    COUNT(*) AS Total_Sessions,
    COUNT(DISTINCT User_ID) AS Total_Users,
    COUNT(DISTINCT Date) AS Distinct_Days,
    SUM(Calories_Consumed) AS Total_Calories_Consumed,
    SUM(Calories_Burned) AS Total_Calories_Burned,
    ROUND(AVG(Steps), 0) AS Avg_Daily_Steps,
    ROUND(AVG(Workout_Duration_Minutes), 1) AS Avg_Workout_Duration_Min,
    ROUND(AVG(Sleep_Hours), 1) AS Avg_Sleep_Hours,
    ROUND(AVG(Water_Intake_Liters), 1) AS Avg_Water_Intake_Liters,
    (SUM(Calories_Consumed) - SUM(Calories_Burned)) AS Calorie_Difference
FROM fitness_activity_logs;
""")

# 2. Activity breakdown
run("Activity Breakdown", """
SELECT 
    Activity_Type,
    COUNT(*) AS Session_Count,
    ROUND(AVG(Workout_Duration_Minutes), 1) AS Avg_Duration_Min,
    SUM(Calories_Burned) AS Total_Calories_Burned,
    ROUND(AVG(Calories_Burned), 1) AS Avg_Calories_Burned,
    ROUND(AVG(Calories_Burned * 1.0 / Workout_Duration_Minutes), 2) AS Cal_Burn_Rate_Per_Min
FROM fitness_activity_logs
GROUP BY Activity_Type
ORDER BY Avg_Calories_Burned DESC;
""")

# 3. Food Category breakdown
run("Food Category Breakdown", """
SELECT 
    Food_Category,
    COUNT(*) AS Logged_Count,
    SUM(Calories_Consumed) AS Total_Calories,
    ROUND(AVG(Calories_Consumed), 1) AS Avg_Calories
FROM fitness_activity_logs
GROUP BY Food_Category
ORDER BY Total_Calories DESC;
""")

# 4. Weekly Trend
run("Weekly Trends", """
SELECT 
    strftime('%Y-%W', Date) AS Year_Week,
    COUNT(*) AS Total_Sessions,
    SUM(Calories_Burned) AS Total_Burned,
    SUM(Calories_Consumed) AS Total_Consumed,
    ROUND(AVG(Steps), 0) AS Avg_Steps
FROM fitness_activity_logs
GROUP BY Year_Week
ORDER BY Year_Week ASC;
""")

# 5. Top 5 Users
run("Top 5 Active Users", """
SELECT 
    User_ID,
    Gender,
    COUNT(*) AS Active_Days,
    SUM(Calories_Burned) AS Total_Burned,
    ROUND(AVG(Workout_Duration_Minutes), 1) AS Avg_Duration,
    ROUND(AVG(Steps), 0) AS Avg_Steps
FROM fitness_activity_logs
GROUP BY User_ID, Gender
ORDER BY Total_Burned DESC
LIMIT 5;
""")
