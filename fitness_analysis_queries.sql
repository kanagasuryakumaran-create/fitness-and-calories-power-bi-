-- =====================================================================================
-- PROJECT: Fitness and Calorie Analysis Using Power BI and SQL
-- SCRIPT: fitness_analysis_queries.sql
-- DIALECT: MySQL 8.0+
-- AUTHOR: Professional Data Analyst & Power BI Developer
-- PURPOSE: Provide 10 essential analytical queries for health & fitness tracking
-- DISCLAIMER: All data used here is synthetic and intended for educational demonstration.
-- =====================================================================================

USE fitness_tracker_db;

-- -------------------------------------------------------------------------------------
-- 1. DATABASE & TABLE CREATION
-- Explanation: Sets up a dedicated database and defines the table schema with strict
-- data types (INT, VARCHAR, DECIMAL, DATE) and primary key constraints.
-- -------------------------------------------------------------------------------------
CREATE DATABASE IF NOT EXISTS fitness_tracker_db;
USE fitness_tracker_db;

CREATE TABLE IF NOT EXISTS fitness_activity_logs (
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

-- -------------------------------------------------------------------------------------
-- 2. VERIFY DATA IMPORT / RECORD INTEGRITY
-- Explanation: Validates that all records are loaded, checks for nulls, and inspects
-- the overall date span and distinct user count.
-- -------------------------------------------------------------------------------------
SELECT 
    COUNT(*) AS Total_Records,
    COUNT(DISTINCT User_ID) AS Total_Users,
    MIN(Date) AS Start_Date,
    MAX(Date) AS End_Date,
    COUNT(DISTINCT Date) AS Total_Days_Covered
FROM fitness_activity_logs;


-- -------------------------------------------------------------------------------------
-- 3. RETRIEVE DAILY CALORIE INTAKE
-- Objective: Understand daily dietary intake patterns across the participant cohort.
-- Explanation: Aggregates total and average calories consumed grouped by date.
-- -------------------------------------------------------------------------------------
SELECT 
    Date,
    COUNT(DISTINCT User_ID) AS Users_Logged,
    SUM(Calories_Consumed) AS Total_Calories_Consumed,
    ROUND(AVG(Calories_Consumed), 2) AS Avg_Calories_Consumed_Per_User
FROM fitness_activity_logs
GROUP BY Date
ORDER BY Date ASC;


-- -------------------------------------------------------------------------------------
-- 4. CALCULATE TOTAL CALORIES BURNED & AVERAGE BURN PER SESSION
-- Objective: Assess total physical energy expenditure during recorded workouts.
-- Explanation: Uses SUM() for cohort total and AVG() for session benchmarks.
-- -------------------------------------------------------------------------------------
SELECT 
    SUM(Calories_Burned) AS Total_Calories_Burned,
    ROUND(AVG(Calories_Burned), 2) AS Avg_Calories_Burned_Per_Session,
    MIN(Calories_Burned) AS Min_Calories_Burned_In_Session,
    MAX(Calories_Burned) AS Max_Calories_Burned_In_Session
FROM fitness_activity_logs;


-- -------------------------------------------------------------------------------------
-- 5. CALCULATE AVERAGE WORKOUT DURATION
-- Objective: Determine the average exercise time across users and gender segments.
-- Explanation: Uses AVG() and GROUP BY Gender to compare exercise habits.
-- -------------------------------------------------------------------------------------
SELECT 
    Gender,
    COUNT(*) AS Total_Workouts,
    ROUND(AVG(Workout_Duration_Minutes), 1) AS Avg_Duration_Minutes,
    MIN(Workout_Duration_Minutes) AS Min_Duration_Minutes,
    MAX(Workout_Duration_Minutes) AS Max_Duration_Minutes
FROM fitness_activity_logs
GROUP BY Gender;


-- -------------------------------------------------------------------------------------
-- 6. ANALYZE ACTIVITY TYPES (EFFICIENCY & EXPENDITURE)
-- Objective: Evaluate which activities burn the most energy per minute and overall.
-- Explanation: Groups by Activity_Type, calculating total calories, average calories,
-- and calorie burn rate per minute (Calories_Burned / Workout_Duration_Minutes).
-- -------------------------------------------------------------------------------------
SELECT 
    Activity_Type,
    COUNT(*) AS Total_Sessions,
    ROUND(AVG(Workout_Duration_Minutes), 1) AS Avg_Duration_Minutes,
    SUM(Calories_Burned) AS Total_Calories_Burned,
    ROUND(AVG(Calories_Burned), 1) AS Avg_Calories_Burned,
    ROUND(AVG(Calories_Burned / Workout_Duration_Minutes), 2) AS Calorie_Burn_Rate_Per_Minute
FROM fitness_activity_logs
GROUP BY Activity_Type
ORDER BY Calorie_Burn_Rate_Per_Minute DESC;


-- -------------------------------------------------------------------------------------
-- 7. CALCULATE AVERAGE DAILY STEPS ACROSS USERS
-- Objective: Benchmark daily walking/running mobility and classify into activity tiers.
-- Explanation: Evaluates mean steps and classifies step count into sedentary,
-- moderate, or active tiers using CASE WHEN.
-- -------------------------------------------------------------------------------------
SELECT 
    ROUND(AVG(Steps), 0) AS Overall_Average_Steps,
    MIN(Steps) AS Lowest_Step_Count,
    MAX(Steps) AS Highest_Step_Count,
    SUM(CASE WHEN Steps >= 10000 THEN 1 ELSE 0 END) AS High_Activity_Days_10k_Plus,
    SUM(CASE WHEN Steps BETWEEN 7000 AND 9999 THEN 1 ELSE 0 END) AS Moderate_Activity_Days,
    SUM(CASE WHEN Steps < 7000 THEN 1 ELSE 0 END) AS Low_Activity_Days
FROM fitness_activity_logs;


-- -------------------------------------------------------------------------------------
-- 8. COMPARE CALORIES CONSUMED AGAINST CALORIES BURNED
-- Objective: Analyze net calorie balance across the cohort and per user.
-- Explanation: Computes Total_Consumed minus Total_Burned. Note: Workout burn
-- captures exercise expenditure, whereas consumption covers total daily basal metabolic
-- maintenance and active exertion.
-- -------------------------------------------------------------------------------------
SELECT 
    User_ID,
    Gender,
    COUNT(DISTINCT Date) AS Days_Tracked,
    SUM(Calories_Consumed) AS Total_Calories_Consumed,
    SUM(Calories_Burned) AS Total_Calories_Burned,
    (SUM(Calories_Consumed) - SUM(Calories_Burned)) AS Calorie_Surplus_or_Deficit,
    ROUND(AVG(Calories_Consumed - Calories_Burned), 1) AS Avg_Daily_Net_Balance
FROM fitness_activity_logs
GROUP BY User_ID, Gender
ORDER BY Total_Calories_Burned DESC;


-- -------------------------------------------------------------------------------------
-- 9. IDENTIFY THE MOST FREQUENTLY PERFORMED ACTIVITIES
-- Objective: Discover user preferences for workout routines.
-- Explanation: Calculates session counts and percentage contribution of each activity
-- relative to total workouts using a subquery.
-- -------------------------------------------------------------------------------------
SELECT 
    Activity_Type,
    COUNT(*) AS Session_Count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM fitness_activity_logs), 2) AS Percentage_Of_All_Sessions,
    DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS Popularity_Rank
FROM fitness_activity_logs
GROUP BY Activity_Type
ORDER BY Session_Count DESC;


-- -------------------------------------------------------------------------------------
-- 10. ANALYZE FITNESS TRENDS BY WEEK AND MONTH
-- Objective: Track cohort fitness progression over time (Weekly and Monthly aggregation).
-- Explanation: Uses MySQL's YEARWEEK() and DATE_FORMAT() to aggregate calorie burn,
-- intake, duration, and steps chronologically.
-- -------------------------------------------------------------------------------------
-- 10A. Weekly Trend
SELECT 
    YEARWEEK(Date, 1) AS Year_Week,
    MIN(Date) AS Week_Start_Date,
    COUNT(*) AS Total_Workouts,
    SUM(Calories_Burned) AS Total_Weekly_Burn,
    SUM(Calories_Consumed) AS Total_Weekly_Intake,
    ROUND(AVG(Steps), 0) AS Avg_Weekly_Steps,
    ROUND(AVG(Workout_Duration_Minutes), 1) AS Avg_Weekly_Workout_Duration
FROM fitness_activity_logs
GROUP BY YEARWEEK(Date, 1)
ORDER BY Year_Week ASC;

-- 10B. Monthly Trend
SELECT 
    DATE_FORMAT(Date, '%Y-%m') AS Year_Month,
    COUNT(DISTINCT User_ID) AS Active_Users,
    COUNT(*) AS Total_Sessions,
    SUM(Calories_Burned) AS Total_Monthly_Burn,
    SUM(Calories_Consumed) AS Total_Monthly_Intake,
    ROUND(AVG(Steps), 0) AS Avg_Monthly_Steps,
    ROUND(AVG(Sleep_Hours), 1) AS Avg_Monthly_Sleep_Hours
FROM fitness_activity_logs
GROUP BY DATE_FORMAT(Date, '%Y-%m')
ORDER BY Year_Month ASC;

-- =====================================================================================
-- 11. BONUS DEEP-DIVE: FOOD CATEGORY & SLEEP / HYDRATION CORRELATION
-- Objective: Determine dietary split and holistic recovery metrics (Hydration & Sleep).
-- -------------------------------------------------------------------------------------
SELECT 
    Food_Category,
    COUNT(*) AS Intake_Logs,
    SUM(Calories_Consumed) AS Total_Category_Calories,
    ROUND(AVG(Calories_Consumed), 1) AS Avg_Calories_Per_Meal,
    ROUND(AVG(Water_Intake_Liters), 2) AS Avg_Daily_Hydration_Liters,
    ROUND(AVG(Sleep_Hours), 2) AS Avg_Sleep_Duration_Hours
FROM fitness_activity_logs
GROUP BY Food_Category
ORDER BY Total_Category_Calories DESC;
