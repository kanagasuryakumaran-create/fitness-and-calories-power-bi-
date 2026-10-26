# Viva Voce & Technical Interview Questions & Answers
## Project: Fitness and Calorie Analysis Dashboard Using Power BI and SQL

This guide contains **25 essential questions and answers** frequently asked by university examiners, project review committees, and technical hiring managers.

---

### Section 1: Project Overview & Architecture

#### Q1: What is the primary objective of this project?
**Answer:**  
The objective is to build an end-to-end analytics solution that aggregates, cleanses, analyzes, and visualizes multidimensional fitness data (calorie intake, calories burned, workout duration, steps, hydration, and sleep) across a 20-user cohort. The project enables users to evaluate exercise efficiency, monitor lifestyle habits, and make data-driven wellness decisions.

#### Q2: Why use both SQL and Power BI instead of doing everything in Excel?
**Answer:**  
- **SQL (MySQL)** is engineered for relational integrity, ACID compliance, structured querying, handling large datasets without freezing, and enforcing strict data types.
- **Power BI Desktop** provides an in-memory columnar database engine (VertiPaq), advanced DAX modeling, dynamic cross-filtering, and executive-level interactive visuals that far surpass static Excel charts.
- Using both reflects real-world enterprise architectures where data is stored in relational data warehouses and queried by BI visualization layers.

#### Q3: What is the nature and size of your dataset?
**Answer:**  
The dataset consists of **697 records** spanning 40 continuous calendar days (`2024-01-01` to `2024-02-09`) across **20 distinct users** (10 male, 10 female). It contains 15 fields capturing demographics, workout metrics, dietary categories, hydration, ambulatory steps, and nocturnal sleep. It is synthetic sample data created for demonstration purposes without exposing real private health information.

---

### Section 2: SQL & Database Design

#### Q4: What is the Primary Key in your table, and why is it important?
**Answer:**  
The Primary Key is `Record_ID`. It uniquely identifies every individual log entry, prevents duplicate records, ensures entity integrity in MySQL, and facilitates fast indexing and query execution.

#### Q5: What is the difference between `WHERE` and `HAVING` clauses in SQL?
**Answer:**  
- `WHERE` filters individual rows **before** any aggregation takes place.
- `HAVING` filters grouped rows **after** aggregation (`GROUP BY`) has been computed.  
*Example:* Filtering by `WHERE Gender = 'Male'` vs. `HAVING SUM(Calories_Burned) > 10000`.

#### Q6: How did you calculate the calorie burn efficiency of activities in SQL?
**Answer:**  
By dividing `Calories_Burned` by `Workout_Duration_Minutes` within an aggregate `AVG()` function:
```sql
SELECT Activity_Type, 
       ROUND(AVG(Calories_Burned / Workout_Duration_Minutes), 2) AS Calorie_Burn_Rate_Per_Minute
FROM fitness_activity_logs
GROUP BY Activity_Type
ORDER BY Calorie_Burn_Rate_Per_Minute DESC;
```
This revealed that HIIT burned **11.89 kcal/min**, while Walking burned **5.02 kcal/min**.

#### Q7: How does `YEARWEEK(Date, 1)` work in your weekly trend query?
**Answer:**  
`YEARWEEK(Date, 1)` extracts the year and 2-digit week number from a date, where mode `1` designates Monday as the first day of the week (ISO 8601 standard). This groups scattered daily sessions into standardized weekly buckets for trend analysis.

#### Q8: What is the difference between `RANK()` and `DENSE_RANK()` in MySQL?
**Answer:**  
Both assign a rank based on an ordered column. However:
- `RANK()` leaves gaps after ties (e.g., 1, 2, 2, 4).
- `DENSE_RANK()` assigns consecutive ranks without skipping numbers (e.g., 1, 2, 2, 3). In our activity popularity analysis, `DENSE_RANK()` was used to rank workout frequencies smoothly.

---

### Section 3: Power BI, Power Query & DAX

#### Q9: What data connectivity mode did you use in Power BI, and why?
**Answer:**  
We used **Import Mode**. In Import Mode, data is loaded into Power BI's in-memory VertiPaq engine, which compresses the data into a columnar format. This enables lightning-fast DAX calculations, full DAX formula support (unlike DirectQuery which restricts certain functions), and disconnected offline report development.

#### Q10: What is the difference between a Calculated Column and a DAX Measure?
**Answer:**  
- **Calculated Column:** Evaluated at the **row level during data refresh** and stored in the data model, consuming RAM.
- **DAX Measure:** Evaluated **on-the-fly at query time** based on the current filter context (what the user selects in slicers or charts). Measures consume no RAM for storage and are the best practice for aggregations like sums and averages.

#### Q11: Why did you use `DIVIDE([Total Calories Burned], [Total Workout Sessions], 0)` instead of the `/` operator?
**Answer:**  
The `DIVIDE()` function in DAX is safe against **division-by-zero errors**. If the denominator is zero or blank, it returns the optional third argument (`0`) or `BLANK()` instead of returning an unsightly `NaN` or crashing the visual card.

#### Q12: Why did you use `AVERAGEX` with `SUMMARIZE` for Average Daily Steps instead of simple `AVERAGE(fitness_activity_logs[Steps])`?
**Answer:**  
A simple `AVERAGE()` computes the mean across all table rows. If a user logs multiple activities or entries per day, a simple average would artificially skew the daily step count. By first using `SUMMARIZE` to aggregate total steps by `Date` and `User_ID`, and then taking `AVERAGEX`, we calculate the genuine average daily steps per person-day.

#### Q13: What is the purpose of creating a separate `_Measures` table?
**Answer:**  
Creating an empty dedicated table (prefixed with an underscore so it sorts to the very top of the Data pane) consolidates all business logic and KPIs in one central repository. It separates data columns from calculation logic, making the model maintainable, clean, and enterprise-ready.

#### Q14: How does cross-filtering work between visuals in Power BI?
**Answer:**  
Power BI utilizes an underlying semantic engine where interactive user selections act as temporary filters on the data model. When a user clicks on the "Running" slice in the Donut Chart, Power BI propagates an implicit filter context `fitness_activity_logs[Activity_Type] = "Running"` to all other visuals on the canvas, instantly recalculating all measures.

---

### Section 4: Domain Knowledge, Business Logic & Findings

#### Q15: Why should "Calorie Difference" not be treated as a complete measure of weight gain or loss?
**Answer:**  
`Calorie Difference` was computed as `Total Calories Consumed - Total Calories Burned`.  
However:
1. `Calories_Consumed` represents total 24-hour food intake.
2. `Calories_Burned` in this tracking schema strictly measures **active exercise exertion**.
3. It does not account for **Basal Metabolic Rate (BMR)**—the 1,400 to 1,900 calories the human body expends naturally to maintain vital organ functions—nor **NEAT** (non-exercise activity thermogenesis like fidgeting or standing).  
Therefore, a mathematical surplus does not imply pure body fat gain. Stating this distinction demonstrates high analytical maturity.

#### Q16: Which activity was the most frequently performed in your dataset?
**Answer:**  
**Yoga** was the most frequently logged activity (121 sessions, 17.4% of all sessions), followed by **Walking** (101 sessions, 14.5%) and **Running** (98 sessions, 14.1%). While Yoga burns fewer calories per minute, its high adoption rate indicates its role as a sustainable, low-impact restorative routine for users.

#### Q17: What correlation was observed between workout duration, sleep, and hydration?
**Answer:**  
Users participating in sessions lasting 60 minutes or longer recorded higher average sleep durations (**7.6 to 7.9 hours**) and higher water intake (**3.6 to 4.2 Liters**), demonstrating the biological link between intense exertion and bodily recovery demands.

#### Q18: How does the dashboard benchmark daily steps against health standards?
**Answer:**  
The Daily Steps column chart incorporates an analytical constant threshold line set at **10,000 steps** (the WHO recommended benchmark for active adults), allowing viewers to immediately identify which days met or fell short of the daily target.

---

### Section 5: Real-World Deployment & Advanced Concepts

#### Q19: If this project were deployed in an enterprise environment, how would data refresh automatically?
**Answer:**  
1. Publish the `.pbix` report to the cloud-based **Power BI Service**.
2. Install and configure an **On-Premises Data Gateway (Standard Mode)** on the server hosting the MySQL database.
3. Configure scheduled refresh (e.g., daily at 6:00 AM) in Power BI Service dataset settings, authenticating via stored database credentials.

#### Q20: What are the main limitations of this project?
**Answer:**  
1. **Synthetic data:** The records are computer-generated simulations.
2. **Missing BMR/Heart Rate streams:** Real-world tracking devices (e.g., Apple Watch, Whoop) capture continuous heart rate variability (HRV) and estimated VO2 max, which were not part of this tabular schema.
3. **Single table design:** While sufficient for 700 rows, an enterprise data warehouse would adopt a Star Schema with separate Dimension tables (`Dim_User`, `Dim_Date`, `Dim_Activity`, `Dim_Food`) and a central Fact table (`Fact_Activity_Log`).

---

### Quick Fire Viva Checklist for Students
- [x] Know your row count: **697 rows**.
- [x] Know your user count: **20 users** over **40 days**.
- [x] Know your total calories: **1.53M consumed**, **297.5K burned**.
- [x] Know the top calorie burner: **HIIT (~663 kcal / 11.89 kcal/min)**.
- [x] Know your average steps: **8,275 steps/day**.
- [x] Understand why `DIVIDE()` and `AVERAGEX()` were chosen over basic operators.
