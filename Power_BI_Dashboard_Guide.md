# Power BI Dashboard Design & Implementation Guide
## Project: Fitness and Calorie Analysis Dashboard

---

### 1. Visual Theme and Color Palette
To ensure a modern, executive, and healthcare-grade light theme, apply the following design system:

| UI Element | Color Name | Hex Code | Visual Application |
| :--- | :--- | :--- | :--- |
| **Canvas Background** | Slate White | `#F8FAFC` | Main dashboard canvas background |
| **Card & Visual Fill** | Pure White | `#FFFFFF` | Background for KPI cards and charts |
| **Primary Typography**| Deep Navy | `#0F172A` | Visual titles, main KPI figures, page header |
| **Secondary Typography**| Muted Slate | `#64748B` | Subtitles, axis labels, card category labels |
| **Burn Metric / Energy**| Coral Orange | `#F97316` | Calories Burned lines, bars, and indicators |
| **Intake Metric / Diet**| Cerulean Blue | `#0284C7` | Calories Consumed line, food category bars |
| **Movement / Steps** | Emerald Green | `#10B981` | Daily steps visual, health progress indicators |
| **Hydration / Sleep** | Violet / Cyan | `#6366F1` | Water and sleep indicators |
| **Card Borders / Dividers**| Soft Border | `#E2E8F0` | Subtle rounded 8px card borders |

---

### 2. Dashboard Canvas Layout Architecture (1920 x 1080 or 16:9 Standard)

```
+----------------------------------------------------------------------------------------------------+
|  [Header & Brand Logo] Fitness & Calorie Analytics Dashboard     [Slicer: Date] [Activity] [User]  |
+----------------------------------------------------------------------------------------------------+
|  [ KPI 1 ]        [ KPI 2 ]       [ KPI 3 ]       [ KPI 4 ]        [ KPI 5 ]       [ KPI 6 ]       |
|  Total Calories   Total Calories  Avg Daily Steps Avg Workout Dur  Avg Sleep Hours Avg Water Intake|
|   1.53M kcal       297.5K kcal      8,275 steps     52.9 mins        7.2 hrs         3.2 Liters    |
+---------------------------------------------------+------------------------------------------------+
|  VISUAL 1: Daily Calorie Intake vs Burned (Line)  |  VISUAL 2: Calories Burned by Activity (Bar)   |
|  (Blue: Consumed, Orange: Burned over 40 Days)    |  (HIIT, Running, Swimming, Cycling, etc.)      |
+---------------------------------------------------+------------------------------------------------+
|  VISUAL 3: Activity Distribution (Donut Chart)    |  VISUAL 4: Weekly Fitness Progress (Line)      |
|  (% of Sessions: Yoga, Walk, HIIT, Run, etc.)     |  (Weekly Total Burn vs Weekly Avg Steps)       |
+---------------------------------------------------+------------------------------------------------+
|  VISUAL 5: Daily Steps vs 10k Target (Column)     |  VISUAL 6: Calories by Food Category (Bar)     |
|  (Green Columns with Reference Line at 10k)       |  (Proteins, Veggies, Fruits, Carbs, etc.)      |
+---------------------------------------------------+------------------------------------------------+
|  VISUAL 7: Comprehensive Daily Fitness Summary Table                                               |
|  [Date | User_ID | Activity | Duration | Calories Burned | Calories Consumed | Steps | Water | Sleep]|
+----------------------------------------------------------------------------------------------------+
```

---

### 3. Step-by-Step Configuration of Every Visual

#### Slicers Bar (Top Right)
1. **Date Slicer**:
   - Visual Type: **Slicer**
   - Field: `fitness_activity_logs[Date]`
   - Style: **Between (Slider)** or **Relative Date**
   - Background: Pure White (`#FFFFFF`), Border: 1px `#E2E8F0`
2. **Activity Type Slicer**:
   - Visual Type: **Slicer**
   - Field: `fitness_activity_logs[Activity_Type]`
   - Style: **Dropdown** or **Tile** (Multi-select enabled with Ctrl)
3. **User ID Slicer**:
   - Visual Type: **Slicer**
   - Field: `fitness_activity_logs[User_ID]`
   - Style: **Dropdown** (Allows drilling down into individual personal health progress)

---

#### Section A: Top KPI Cards (Row 1)
Use the **Card (New)** or standard **Card** visual for each:

1. **KPI 1: Total Calories Consumed**
   - Field: `[Total Calories Consumed]`
   - Callout Value Font: Bold, 28pt, Color: `#0284C7` (Blue)
   - Category Label: "Total Calories Consumed" (9pt, `#64748B`)
2. **KPI 2: Total Calories Burned**
   - Field: `[Total Calories Burned]`
   - Callout Value Font: Bold, 28pt, Color: `#F97316` (Coral)
   - Category Label: "Total Calories Burned"
3. **KPI 3: Average Daily Steps**
   - Field: `[Average Daily Steps]`
   - Callout Value Font: Bold, 28pt, Color: `#10B981` (Emerald)
   - Category Label: "Avg Daily Steps"
4. **KPI 4: Average Workout Duration**
   - Field: `[Average Workout Duration]`
   - Callout Value Font: Bold, 28pt, Color: `#0F172A` (Navy)
   - Category Label: "Avg Workout Duration (Mins)"
5. **KPI 5: Average Sleep Hours**
   - Field: `[Average Sleep Hours]`
   - Callout Value Font: Bold, 28pt, Color: `#6366F1` (Indigo)
   - Category Label: "Avg Sleep Hours"
6. **KPI 6: Average Water Intake**
   - Field: `[Average Water Intake]`
   - Callout Value Font: Bold, 28pt, Color: `#0284C7` (Sky Blue)
   - Category Label: "Avg Water Intake (L)"

---

#### Section B: Core Visualizations

##### Visual 1: Daily Calorie Intake vs. Calories Burned
- **Visual Type**: **Line Chart**
- **X-Axis**: `fitness_activity_logs[Date]`
- **Y-Axis**:
  - `[Total Calories Consumed]` (Line Color: `#0284C7`, Solid line, 2.5px width)
  - `[Total Calories Burned]` (Line Color: `#F97316`, Solid line, 2.5px width)
- **Formatting**:
  - Title: "Daily Calorie Intake vs. Calories Burned Trend"
  - Data points: Turn On markers (subtle circle markers).
  - Y-Axis title: "Calories (kcal)"

##### Visual 2: Calories Burned by Activity Type
- **Visual Type**: **Clustered Bar Chart** (Horizontal)
- **Y-Axis**: `fitness_activity_logs[Activity_Type]`
- **X-Axis**: `[Total Calories Burned]`
- **Bar Color**: Gradient / `#F97316`
- **Formatting**:
  - Data Labels: **On** (Position: Outside End, Value: Display units in Thousands 'K')
  - Title: "Total Calories Burned by Workout Discipline"

##### Visual 3: Distribution of Workout Activities
- **Visual Type**: **Donut Chart**
- **Legend**: `fitness_activity_logs[Activity_Type]`
- **Values**: `[Total Workout Sessions]`
- **Formatting**:
  - Detail labels: **Category + Percent of total**
  - Donut Hole Radius: **60%**
  - Title: "Workout Session Distribution"

##### Visual 4: Weekly Fitness Progress
- **Visual Type**: **Line Chart** or **Line and Clustered Column Chart**
- **X-Axis**: `fitness_activity_logs[Date]` (Hierarchy set to Week or Month)
- **Y-Axis (Column)**: `[Total Calories Burned]`
- **Y-Axis (Line)**: `[Average Daily Steps]`
- **Formatting**:
  - Title: "Weekly Fitness Progress (Burn & Movement)"
  - Legend: Top-center

##### Visual 5: Daily Steps Comparison
- **Visual Type**: **Column Chart**
- **X-Axis**: `fitness_activity_logs[Date]`
- **Y-Axis**: `[Average Daily Steps]`
- **Color**: `#10B981` (Green)
- **Analytics Pane**:
  - Add **Constant Line** at `10000`
  - Name: "Daily Goal: 10,000 Steps"
  - Line style: Dashed, Color: `#EF4444` (Red), Transparency: 20%
  - Data label: On

##### Visual 6: Calories Consumed by Food Category
- **Visual Type**: **Clustered Bar Chart**
- **Y-Axis**: `fitness_activity_logs[Food_Category]`
- **X-Axis**: `[Total Calories Consumed]`
- **Bar Color**: `#0284C7`
- **Formatting**:
  - Data Labels: **On**
  - Title: "Dietary Calorie Intake by Food Category"

##### Visual 7: Daily Fitness Summary Table
- **Visual Type**: **Table**
- **Values / Columns**:
  1. `fitness_activity_logs[Date]` (Format: Short Date `YYYY-MM-DD`)
  2. `fitness_activity_logs[User_ID]`
  3. `fitness_activity_logs[Activity_Type]`
  4. `fitness_activity_logs[Workout_Duration_Minutes]`
  5. `fitness_activity_logs[Calories_Burned]`
  6. `fitness_activity_logs[Calories_Consumed]`
  7. `fitness_activity_logs[Steps]`
  8. `fitness_activity_logs[Water_Intake_Liters]`
  9. `fitness_activity_logs[Sleep_Hours]`
- **Formatting**:
  - Style Preset: **Alternating rows** (White & `#F8FAFC`)
  - Gridlines: Horizontal light grey (`#E2E8F0`)
  - Column alignment: Numeric columns right-aligned, text left-aligned.

---

### 4. Interactivity and Cross-Filtering
- **Cross-Filtering**: Clicking on any slice in the Donut Chart (e.g., "Running") automatically filters:
  - The Daily Line Chart to show only Running days.
  - The KPI cards to show Running session counts, duration, and burn.
  - The Steps Chart to highlight Running steps.
- **Drill-Through / Slicing by User**:
  - Selecting `USR101` in the User Slicer turns the entire executive dashboard into a personalized **Personal Fitness Report Card** for that specific individual.
