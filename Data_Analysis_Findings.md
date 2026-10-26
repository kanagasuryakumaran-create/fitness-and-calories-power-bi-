# Data Analysis Findings & Health Insights
## Project: Fitness and Calorie Analysis Using Power BI and SQL

> **IMPORTANT ANALYTICAL DISCLAIMER:**  
> The findings, distributions, and numerical correlations described below are derived from a synthetic, computer-generated sample dataset created specifically for technical demonstration and educational training. They represent data engineering and analytical workflows rather than clinical or real-world medical conclusions.

---

### Key Analytical Questions & Answers

#### Question 1: Which activity burns the most calories in the sample?
* **Answer**: **HIIT (High-Intensity Interval Training)** burns the most calories both per session and per minute.
* **Evidence from SQL & DAX Analysis**:
  - **HIIT**: Averages **662.9 calories burned per session** with a burn rate of **11.89 kcal/minute**.
  - **Running**: Follows closely in second place with **571.5 calories per session** (**11.05 kcal/minute**).
  - **Swimming**: Averages **518.3 calories per session** (**9.71 kcal/minute**).
  - **Cycling**: Averages **488.6 calories per session** (**8.61 kcal/minute**).
  - **Strength Training**: Averages **349.3 calories per session** (**6.98 kcal/minute**).
  - **Walking**: Averages **263.9 calories per session** (**5.02 kcal/minute**).
  - **Yoga**: Averages **196.9 calories per session** (**3.91 kcal/minute**).
* **Analytical Takeaway**: High-cardiorespiratory demand exercises (HIIT and Running) yield 2.5x to 3x higher metabolic burn efficiency per unit time compared to low-impact restorative activities like Yoga.

---

#### Question 2: On which days is workout activity highest?
* **Answer**: Across the 40-day observation window, weekly activity peaks during the middle of the week (Wednesdays and Thursdays) and sustained high volume across Weeks 4 and 5.
* **Evidence**:
  - **Week 5** recorded the highest cumulative workout energy expenditure: **56,861 calories burned** across 126 completed sessions.
  - **Week 4** recorded **56,250 calories burned** across 125 sessions.
  - Active participation was consistently sustained at 85% attendance across the 20-user cohort.

---

#### Question 3: How does calorie intake change over time?
* **Answer**: Daily calorie intake remained relatively stable, fluctuating between **35,000 and 42,000 total calories per day across the 20 users**, averaging **2,201 calories per user day**.
* **Observations**:
  - There is a slight weekly cyclicality where weekends show mild caloric surplus (+4% to +8% over weekday averages), reflecting habitual dietary patterns.
  - Calorie consumption is well-balanced across gender cohorts: Male users averaged ~2,450 kcal/day while female users averaged ~1,950 kcal/day, mirroring baseline standard nutritional guidelines.

---

#### Question 4: Which food categories contribute the most calories?
* **Answer**: **Proteins** and **Vegetables** (with complex carbs) contribute the largest total logged calories.
* **Data Breakdown**:
  1. **Proteins**: 285,013 kcal (18.6% of cohort total, 131 logged days, avg 2,175.7 kcal/day)
  2. **Vegetables**: 282,134 kcal (18.4% of cohort total, 127 logged days, avg 2,221.5 kcal/day)
  3. **Fruits**: 265,456 kcal (17.3% of cohort total, 117 logged days, avg 2,268.9 kcal/day)
  4. **Carbohydrates**: 251,055 kcal (16.4% of cohort total, 116 logged days, avg 2,164.3 kcal/day)
  5. **Snacks & Fats**: 228,766 kcal (14.9% of cohort total, 106 logged days, avg 2,158.2 kcal/day)
  6. **Dairy**: 221,740 kcal (14.5% of cohort total, 100 logged days, avg 2,217.4 kcal/day)
* **Nutritional Significance**: The balanced distribution demonstrates that active users prioritize protein-rich and whole-food selections to support exercise recovery.

---

#### Question 5: What is the relationship between steps and calories burned?
* **Answer**: There is a strong positive correlation ($r \approx 0.68$) between daily steps and total calories burned.
* **Detailed Breakdown**:
  - On days when users recorded running or walking activities, average step count surged to **11,240 steps**, and active calorie burn reached **560+ kcal**.
  - On days with lower ambulatory motion (e.g., Yoga or rest), steps averaged **5,120 steps**, with active workout burn dropping below **250 kcal**.
  - **Threshold Finding**: Achieving the standard benchmark of **10,000 steps** was associated with an average daily active energy burn increase of over **35%**.

---

#### Question 6: How do workout duration and sleep vary?
* **Answer**: Workout duration averages **52.9 minutes** (ranging from 25 to 90 minutes), while sleep averages **7.2 hours** (ranging from 5.5 to 8.8 hours).
* **Correlation**:
  - Users engaging in longer workouts (60–90 minutes) exhibited higher sleep duration (averaging **7.6 to 7.9 hours**) and higher water intake (**3.6 to 4.2 Liters**), demonstrating that physical fatigue promotes deeper nocturnal recovery and greater hydration needs.
  - Users who logged under 6 hours of sleep showed lower workout durations (averaging 35–40 minutes) on subsequent exercise days.

---

#### Question 7: Which users have the highest activity levels?
* **Answer**: The top 5 most active users in the dataset based on total calories burned and consistency are:

| User ID | Gender | Active Days Tracked | Total Workout Burn (kcal) | Avg Workout Duration | Avg Daily Steps |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **USR117** | Male | 35 days | **20,731 kcal** | 55.3 mins | 7,939 steps |
| **USR111** | Male | 38 days | **19,471 kcal** | 57.4 mins | 8,232 steps |
| **USR109** | Male | 37 days | **18,822 kcal** | 49.7 mins | 8,678 steps |
| **USR119** | Male | 37 days | **18,253 kcal** | 55.3 mins | 8,474 steps |
| **USR115** | Male | 37 days | **16,971 kcal** | 54.6 mins | 8,022 steps |

* **Insight**: User **USR111** demonstrated the highest adherence consistency (active on 38 of 40 days) and the highest average session duration (57.4 minutes).

---

### Critical Analytical Note: Calorie Balance & Energy Gap Interpretation
In this dataset:
- Total Calories Consumed = **1,534,164 kcal**
- Total Calories Burned = **297,489 kcal**
- Mathematical Difference = **+1,236,675 kcal**

**Why this is not a pure fat surplus:**
1. **Basal Metabolic Rate (BMR)**: A human body expends roughly 1,400 to 1,900 kcal every day just staying alive (breathing, cellular repair, organ function), which is funded by food intake.
2. **Measurement Scope**: The `Calories_Burned` field tracks **active exercise exertion only**, not total 24-hour total daily energy expenditure (TDEE).
3. In actual data analytics practice, understanding the exact scope and limitations of tracking attributes is essential to prevent false clinical conclusions.
