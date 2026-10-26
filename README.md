# 🏋️ Fitness and Calorie Analysis Dashboard Using Power BI and SQL

![Power BI](https://img.shields.io/badge/Power_BI-Desktop-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![DAX](https://img.shields.io/badge/DAX-Calculated_Measures-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)
![Data Analysis](https://img.shields.io/badge/Analytics-Healthcare_&_Fitness-10B981?style=for-the-badge)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)

An end-to-end Data Analytics and Business Intelligence project analyzing daily calorie intake, active calories burned, workout efficiency, ambulatory steps, sleep hygiene, and hydration habits across 697 chronological fitness logs.

---

## 📌 Project Overview
- **Objective:** Enable users and coaches to evaluate fitness performance, monitor energy expenditure across diverse activities, correlate sleep with recovery, and benchmark daily steps against health standards.
- **Data Source:** Realistic synthetic sample dataset of **697 records** across **20 distinct users** spanning 40 days.
- **Database:** MySQL relational database (`fitness_tracker_db`).
- **BI Tool:** Microsoft Power BI Desktop featuring 6 KPI cards, 7 dynamic visuals, 3 interactive slicers, and a dedicated DAX measures repository.

---

## 📁 Repository Structure
```text
power-bi-data/
│
├── fitness_data.csv                 # Clean sample dataset (697 rows, 15 attributes)
├── fitness_db_setup.sql             # MySQL DDL schema + full data insertion script
├── fitness_analysis_queries.sql     # 10 core SQL analytical queries with explanations
├── DAX_Measures.dax                 # Complete, production-ready DAX measure formulas
├── Power_BI_Dashboard_Guide.md      # Visual specifications, color palette & layout mockups
├── Power_BI_Connection_Guide.md     # Step-by-step MySQL & CSV connection walkthrough
├── Data_Analysis_Findings.md        # Detailed analytical answers & health insights
├── Project_Report.md                # Comprehensive academic project report
├── Resume_Project_Points.md         # Resume bullet points & portfolio summaries
├── Viva_Interview_Questions_Answers.md # 25+ Viva and technical interview Q&A
└── README.md                        # Project documentation and guide
```

---

## 📊 Dashboard Architecture & Layout

```text
+----------------------------------------------------------------------------------------------------+
|  🏋️ Fitness & Calorie Analytics Dashboard                       [📅 Date] [🏃 Activity] [👤 User] |
+----------------------------------------------------------------------------------------------------+
|  [ 1.53M kcal ]     [ 297.5K kcal ]    [ 8,275 steps ]    [ 52.9 mins ]     [ 7.2 hrs ]   [ 3.2 L ]|
|  Calories Consumed  Calories Burned    Avg Daily Steps    Avg Workout Dur   Avg Sleep     Avg Water|
+---------------------------------------------------+------------------------------------------------+
|  📈 Line Chart: Daily Intake vs. Burned Trend     |  📊 Bar Chart: Calories Burned by Activity     |
|  (Blue: Consumed kcal, Orange: Burned kcal)       |  (HIIT: 663 kcal, Running: 572 kcal, etc.)     |
+---------------------------------------------------+------------------------------------------------+
|  🍩 Donut Chart: Workout Discipline Share (%)     |  📈 Line Chart: Weekly Fitness Progress        |
|  (Yoga 17.4%, Walk 14.5%, Running 14.1%, etc.)    |  (Weekly Total Burn vs. Weekly Steps)          |
+---------------------------------------------------+------------------------------------------------+
|  📊 Column Chart: Daily Steps vs 10k Goal Target  |  📊 Bar Chart: Calorie Intake by Food Category |
|  (Green Columns with Red Dashed 10,000 Step Line) |  (Proteins, Veggies, Fruits, Carbs, etc.)      |
+---------------------------------------------------+------------------------------------------------+
|  📋 Table: Comprehensive Daily Activity Detail Log                                                 |
|  [Date | User_ID | Activity | Duration | Calories Burned | Calories Consumed | Steps | Water | Sleep]|
+----------------------------------------------------------------------------------------------------+
```

---

## 🗄️ Database Schema & SQL Highlights

The table `fitness_activity_logs` includes:
- `Record_ID`: INT PRIMARY KEY
- `User_ID`: VARCHAR(10)
- `Date`: DATE
- `Age`: INT
- `Gender`: VARCHAR(10)
- `Weight_Kg`, `Height_Cm`: DECIMAL(5,2)
- `Activity_Type`: VARCHAR(50)
- `Workout_Duration_Minutes`: INT
- `Calories_Burned`: INT
- `Food_Category`: VARCHAR(50)
- `Calories_Consumed`: INT
- `Water_Intake_Liters`: DECIMAL(3,1)
- `Steps`: INT
- `Sleep_Hours`: DECIMAL(3,1)

### Key SQL Queries Included:
1. Cohort-wide Calorie Aggregations & Daily Intake.
2. Calorie Burn Efficiency Rate per Minute (`Calories_Burned / Workout_Duration_Minutes`).
3. Ambulatory Step Classification (Sedentary vs. Moderate vs. Active via `CASE WHEN`).
4. Weekly Trend Analysis using `YEARWEEK(Date, 1)`.
5. User Adherence & Activity Ranking (`DENSE_RANK()`).

---

## 📐 Core DAX Measures

| Measure Name | DAX Expression | Purpose |
| :--- | :--- | :--- |
| **Total Calories Consumed** | `SUM(fitness_activity_logs[Calories_Consumed])` | Total dietary energy intake |
| **Total Calories Burned** | `SUM(fitness_activity_logs[Calories_Burned])` | Total active exercise expenditure |
| **Average Daily Steps** | `AVERAGEX(KEEPFILTERS(SUMMARIZE(...)), [Daily_Steps])` | Precise daily average without duplicate bias |
| **Average Calories Per Session** | `DIVIDE([Total Calories Burned], [Total Workout Sessions], 0)` | Session energy benchmark |
| **Calorie Difference** | `[Total Calories Consumed] - [Total Calories Burned]` | Intake vs. active exercise gap |
| **Step Goal Progress %** | `DIVIDE([Average Daily Steps], 10000, 0)` | % of WHO 10,000 steps/day target |

---

## 🚀 Quick Start Guide

### Step 1: Initialize Database (MySQL)
```bash
# Log in to MySQL
mysql -u root -p

# Run the setup script
source d:/project/power bi data/fitness_db_setup.sql;
```

### Step 2: Open Power BI Desktop
1. Click **Get Data** -> **MySQL Database** (or select **Text/CSV** -> `fitness_data.csv`).
2. Server: `localhost:3306`, Database: `fitness_tracker_db`.
3. In Navigator, select `fitness_activity_logs` -> Click **Load**.
4. In the **Modeling** tab, create a new table `_Measures` and paste DAX measures from [DAX_Measures.dax](file:///d:/project/power%20bi%20data/DAX_Measures.dax).
5. Build the visual canvas following [Power_BI_Dashboard_Guide.md](file:///d:/project/power%20bi%20data/Power_BI_Dashboard_Guide.md).

---

## 🔍 Key Analytical Findings
1. **Most Efficient Calorie Burn**: **HIIT** is the highest burning activity, averaging **662.9 kcal/session** (11.89 kcal/min), followed by **Running** (**571.5 kcal/session**, 11.05 kcal/min).
2. **Mobility Impact**: Participants logging >10,000 steps burned **35% more active calories** on average than those walking <7,000 steps.
3. **Recovery Nexus**: Longer workouts (60–90 mins) correlated with deeper sleep (7.6–7.9 hours) and increased fluid intake (>3.5 L/day).
4. **Dietary Split**: Protein-rich meals and vegetables accounted for **37%** of all recorded dietary calories.

---

## ⚠️ Disclaimers
- **Synthetic Data**: All data is synthetically generated for analytical demonstration.
- **Calorie Balance Scope**: `Calorie Difference` accounts for dietary intake minus workout expenditure and excludes Basal Metabolic Rate (BMR) and Non-Exercise Activity Thermogenesis (NEAT).

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).
