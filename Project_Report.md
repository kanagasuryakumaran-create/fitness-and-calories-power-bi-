# ACADEMIC PROJECT REPORT

## **FITNESS AND CALORIE ANALYSIS DASHBOARD USING POWER BI AND SQL**

**Course:** Data Analytics & Business Intelligence  
**Domain:** Healthcare, Fitness Informatics & BI Systems  
**Technologies Used:** MySQL 8.0, Microsoft Power BI Desktop, DAX, CSV/Excel  
**Submission Date:** October 2026  
**Document Status:** Complete & Evaluated  

---

### **TABLE OF CONTENTS**
1. [Abstract](#1-abstract)
2. [Introduction & Problem Statement](#2-introduction--problem-statement)
3. [Technology Stack & Tool Selection](#3-technology-stack--tool-selection)
4. [Dataset Architecture & Data Dictionary](#4-dataset-architecture--data-dictionary)
5. [Database Implementation in MySQL](#5-database-implementation-in-mysql)
6. [Power BI Data Modeling & DAX Formulations](#6-power-bi-data-modeling--dax-formulations)
7. [Dashboard Design Architecture & UI Layout](#7-dashboard-design-architecture--ui-layout)
8. [Data Analysis, Findings & Visual Insights](#8-data-analysis-findings--visual-insights)
9. [Limitations, Scope & Ethical Disclaimers](#9-limitations-scope--ethical-disclaimers)
10. [Conclusion & Future Enhancements](#10-conclusion--future-enhancements)
11. [References & Appendix](#11-references--appendix)

---

### **1. ABSTRACT**
In the contemporary digital wellness era, personal fitness tracking devices and mobile health applications generate voluminous multidimensional streams of biometric and lifestyle data. However, raw data logs—encompassing daily calorie intake, active energy expenditure, ambulatory steps, sleep hygiene, and fluid consumption—frequently remain siloed and uninterpretable for non-technical users. 

This project presents an end-to-end Business Intelligence and Data Analytics solution that ingests, cleanses, analyzes, and visualizes fitness habits across a 20-user cohort over 697 chronological activity logs. Utilizing **MySQL** for robust relational querying and data aggregation, and **Microsoft Power BI Desktop** for high-impact interactive visualization and DAX modeling, this system provides actionable intelligence. Key performance indicators (KPIs) and cross-filtered charts enable individuals and health coaches to diagnose energy expenditure efficiency, pinpoint peak workout days, correlate physical activity with nocturnal recovery, and track adherence to standard physical activity guidelines.

---

### **2. INTRODUCTION & PROBLEM STATEMENT**

#### 2.1 Background
Personal fitness analytics bridges behavioral health science and data engineering. While users regularly log dietary meals and workout sessions, they struggle to answer basic questions:
- *Am I burning more calories in HIIT or Running relative to the time invested?*
- *How does my sleep duration correlate with next-day exercise capacity?*
- *What percentage of my daily caloric intake comes from proteins versus simple carbohydrates?*

#### 2.2 Problem Statement
Without structured relational schemas and interactive reporting dashboards, health records suffer from:
1. Fragmented data across disparate spreadsheets.
2. Inability to perform dynamic time-intelligence and cohort slicing.
3. Lack of unified KPI tracking (e.g., benchmark comparisons against 10,000 steps/day).

#### 2.3 Project Objectives
- Architect a normalized MySQL database schema to store and aggregate daily fitness metrics.
- Formulate 10 targeted SQL queries to uncover workout trends, caloric ratios, and cohort behaviors.
- Model data in Power BI Desktop with an optimized DAX measures repository.
- Deliver an executive-grade, light-themed dashboard featuring interactive slicers, line charts, donut distributions, and tabular breakdowns.

---

### **3. TECHNOLOGY STACK & TOOL SELECTION**

| Technology | Role in Project | Justification |
| :--- | :--- | :--- |
| **MySQL 8.0** | Relational Database Engine | Open-source, industry standard, highly reliable for transactional health logging, supports standard SQL aggregation. |
| **MySQL Workbench** | Database Administration | Visual GUI for executing DDL/DML scripts and validating query performance. |
| **Power BI Desktop** | Business Intelligence & Visuals | Free enterprise-grade BI tool, powerful data modeling engine (VertiPaq), rich visualization palette. |
| **DAX (Data Analysis Expressions)** | Formula & Calculation Language | Enables dynamic calculation of daily averages, cumulative totals, and context-aware ratios. |
| **Power Query (M Language)** | ETL & Data Transformation | Cleanses headers, enforces column data typing, handles missing values, and ensures clean imports. |
| **CSV / Excel** | Data Interchange Format | Lightweight, portable, allows fallback connectivity when direct database ports are restricted. |

---

### **4. DATASET ARCHITECTURE & DATA DICTIONARY**

The dataset consists of **697 complete records** spanning a 40-day observation window (`2024-01-01` to `2024-02-09`) across 20 distinct users (`USR101` to `USR120`).

#### Data Dictionary

| Column Name | Data Type | Nullable | Description / Domain Constraints |
| :--- | :--- | :--- | :--- |
| `Record_ID` | INT (Primary Key) | NO | Unique integer identifier (1 to 697), strictly non-duplicate. |
| `User_ID` | VARCHAR(10) | NO | Alphanumeric user code (`USR101` – `USR120`). |
| `Date` | DATE | NO | Observation date in ISO 8601 format (`YYYY-MM-DD`). |
| `Age` | INT | NO | User age in completed years (Range: 21 – 52). |
| `Gender` | VARCHAR(10) | NO | Biological sex (`Male`, `Female`). |
| `Weight_Kg` | DECIMAL(5,2) | NO | Body mass in kilograms (Range: 51.5 – 92.5 kg). |
| `Height_Cm` | DECIMAL(5,2) | NO | Stature in centimeters (Range: 154.0 – 188.0 cm). |
| `Activity_Type` | VARCHAR(50) | NO | Exercise discipline: *Running, Cycling, Swimming, Walking, Strength Training, Yoga, HIIT*. |
| `Workout_Duration_Minutes` | INT | NO | Total active exercise session length (25 – 90 minutes). |
| `Calories_Burned` | INT | NO | Energy expended during the workout (150 – 850 kcal). |
| `Food_Category` | VARCHAR(50) | NO | Primary dietary category: *Proteins, Carbohydrates, Vegetables, Fruits, Dairy, Snacks & Fats*. |
| `Calories_Consumed` | INT | NO | Total daily dietary intake (1,550 – 2,900 kcal). |
| `Water_Intake_Liters` | DECIMAL(3,1) | NO | Total fluid intake recorded (1.8 – 4.5 Liters). |
| `Steps` | INT | NO | Daily ambulatory step count (3,200 – 16,000 steps). |
| `Sleep_Hours` | DECIMAL(3,1) | NO | Nocturnal sleep duration (5.5 – 8.8 hours). |

---

### **5. DATABASE IMPLEMENTATION IN MYSQL**

#### 5.1 Schema Generation (DDL)
```sql
CREATE DATABASE IF NOT EXISTS fitness_tracker_db;
USE fitness_tracker_db;

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
```

#### 5.2 Key Analytical Queries
The system implements 10 analytical queries targeting core business and wellness questions:
1. **Total Caloric Expenditure & Intake**: Evaluates cohort-wide cumulative totals.
2. **Burn Rate per Minute by Activity**:
   ```sql
   SELECT 
       Activity_Type,
       COUNT(*) AS Total_Sessions,
       ROUND(AVG(Workout_Duration_Minutes), 1) AS Avg_Duration_Minutes,
       SUM(Calories_Burned) AS Total_Calories_Burned,
       ROUND(AVG(Calories_Burned / Workout_Duration_Minutes), 2) AS Calorie_Burn_Rate_Per_Minute
   FROM fitness_activity_logs
   GROUP BY Activity_Type
   ORDER BY Calorie_Burn_Rate_Per_Minute DESC;
   ```
   *Result:* HIIT leads with **11.89 kcal/min**, followed by Running at **11.05 kcal/min**.
3. **Weekly Progress Aggregation**: Uses `YEARWEEK(Date, 1)` to group performance metrics chronologically without day-level noise.
4. **Step Activity Categorization**: Employs `CASE WHEN` to segment users into Sedentary (<7k), Moderate (7k-10k), and Highly Active (10k+) brackets.

---

### **6. POWER BI DATA MODELING & DAX FORMULATIONS**

#### 6.1 Architecture
The data model uses a clean schema centered around `fitness_activity_logs`, complemented by a decoupled, dedicated `_Measures` table housing all analytical logic.

#### 6.2 Key DAX Formulations
- **Average Daily Steps (Context-Safe Distinct Aggregation):**
  ```dax
  Average Daily Steps = 
  AVERAGEX(
      KEEPFILTERS(
          SUMMARIZE(
              fitness_activity_logs,
              fitness_activity_logs[Date],
              fitness_activity_logs[User_ID],
              "Daily_Steps", SUM(fitness_activity_logs[Steps])
          )
      ),
      [Daily_Steps]
  )
  ```
- **Average Calories Burned Per Session (Safe Division):**
  ```dax
  Average Calories Burned Per Session = 
  DIVIDE([Total Calories Burned], [Total Workout Sessions], 0)
  ```
- **Calorie Difference:**
  ```dax
  Calorie Difference = [Total Calories Consumed] - [Total Calories Burned]
  ```

---

### **7. DASHBOARD DESIGN ARCHITECTURE & UI LAYOUT**

The dashboard adopts an executive healthcare aesthetic:
- **Light Theme**: Soft off-white canvas (`#F8FAFC`), crisp white visual cards (`#FFFFFF`), deep navy typography (`#0F172A`).
- **Semantic Accents**: Energetic Coral (`#F97316`) for active calorie expenditure, Sky Blue (`#0284C7`) for dietary calorie intake, and Emerald Green (`#10B981`) for ambulatory movement.

#### Visual Hierarchy
1. **Header & Interactive Controls**: Dynamic date slider, activity multi-select tiles, user drill-down dropdown.
2. **Row 1 - KPI Summary Ribbon**: 6 responsive KPI cards showcasing:
   - Total Calories Consumed: **1.53M kcal**
   - Total Calories Burned: **297.5K kcal**
   - Average Daily Steps: **8,275 steps**
   - Average Workout Duration: **52.9 mins**
   - Average Sleep Hours: **7.2 hrs**
   - Average Water Intake: **3.2 L**
3. **Row 2 - Caloric Dynamics & Activity Efficiency**:
   - Dual-axis Line Chart showing Daily Intake vs. Burned.
   - Horizontal Clustered Bar Chart ranking energy burn across workout disciplines.
4. **Row 3 - Behavioral Composition & Benchmarking**:
   - Donut Chart representing session share across 7 activities.
   - Column Chart tracking daily steps against a 10,000-step target threshold line.
   - Bar Chart of dietary intake by food category.
5. **Row 4 - Tabular Detail Log**: A paginated, alternating-row data grid displaying granular records for micro-level inspection.

---

### **8. DATA ANALYSIS, FINDINGS & VISUAL INSIGHTS**

1. **Cardiorespiratory Efficiency**: HIIT and Running demonstrate the highest metabolic returns, delivering ~11 to 12 kcal per minute of exercise. Restorative exercises such as Yoga average ~3.9 kcal/min but provide vital flexibility and joint recovery.
2. **Step Threshold Correlation**: Users maintaining >10,000 steps daily exhibit a 35% higher baseline active calorie burn compared to users logging <7,000 steps.
3. **Nocturnal Recovery Patterns**: Extended exercise duration (>60 minutes) correlates positively with sleep duration, averaging 7.6 to 7.9 hours, accompanied by elevated hydration needs (>3.5 Liters/day).
4. **Nutritional Balance**: Proteins (285k kcal) and Vegetables (282k kcal) constitute over 37% of recorded dietary selections, reflecting health-conscious nutritional intake across active participants.

---

### **9. LIMITATIONS, SCOPE & ETHICAL DISCLAIMERS**

1. **Synthetic Nature of Dataset**: All participant demographics, biometrics, and activity records were algorithmically synthesized for academic modeling. They do not constitute actual medical records or clinical health outcomes.
2. **Calorie Difference vs. Energy Balance**: The metric `Calorie Difference` calculates dietary intake minus workout burn. It deliberately excludes Basal Metabolic Rate (BMR) and Non-Exercise Activity Thermogenesis (NEAT). A positive difference reflects expected maintenance energy requirements rather than pure adipose accumulation.
3. **Privacy Compliance**: No personally identifiable information (PII) or protected health information (PHI) was used, adhering to HIPAA and GDPR research ethics.

---

### **10. CONCLUSION & FUTURE ENHANCEMENTS**

#### 10.1 Conclusion
The **Fitness and Calorie Analysis Dashboard** successfully validates the synergy of SQL and Power BI. By structuring raw activity streams into a clean relational database and delivering an intuitive, interactive visual interface, the project empowers users to diagnose fitness performance, optimize workout routines, and sustain healthy recovery habits.

#### 10.2 Future Scope
- **IoT & Wearable Integration**: Connect Power BI via REST APIs directly to Apple HealthKit, Fitbit, or Garmin Cloud databases.
- **Predictive Analytics**: Integrate Azure Machine Learning / Python scripts in Power BI to forecast user weight trajectory and recommend personalized calorie targets.
- **Mobile Layout**: Design a responsive mobile view in Power BI Mobile for on-the-go athlete monitoring.

---

### **11. REFERENCES & APPENDIX**
1. Microsoft Power BI Documentation: *DAX Reference Guide & Data Modeling Best Practices* (2024).
2. MySQL 8.0 Reference Manual: *Optimization, Window Functions, and Aggregate Queries*.
3. World Health Organization (WHO): *Global Recommendations on Physical Activity for Health*.
4. Project Files Repository:
   - Schema & Setup: `fitness_db_setup.sql`
   - Analytical Queries: `fitness_analysis_queries.sql`
   - DAX Measures: `DAX_Measures.dax`
   - Data Source: `fitness_data.csv`
