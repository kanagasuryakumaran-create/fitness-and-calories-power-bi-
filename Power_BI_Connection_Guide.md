# Power BI Connection & Setup Manual
## How to Connect Power BI to MySQL Database & CSV Files

This guide provides beginner-friendly, step-by-step instructions to connect **Power BI Desktop** to your data source.

---

### Method 1: Connecting Power BI to MySQL Database

#### Prerequisites
1. **MySQL Server & Workbench**: Ensure MySQL is running on your machine (default port: `3306`).
2. **MySQL Connector/NET (Critical)**:
   - Power BI Desktop requires the **MySQL Connector/NET** (version 8.0.28 or later recommended).
   - Download free from: [MySQL Official Connector/NET](https://dev.mysql.com/downloads/connector/net/)
   - *Note:* Install the version that matches your Power BI Desktop architecture (usually **64-bit**).
3. **Microsoft Visual C++ Redistributable**: Ensure Visual C++ 2015-2022 x64 is installed.

---

#### Step 1: Initialize Database in MySQL
1. Open **MySQL Workbench** or command line client.
2. Open and run [fitness_db_setup.sql](file:///d:/project/power%20bi%20data/fitness_db_setup.sql).
3. Confirm by executing:
   ```sql
   USE fitness_tracker_db;
   SELECT COUNT(*) FROM fitness_activity_logs;
   ```
   *Expected result: 697 rows.*

---

#### Step 2: Connect Power BI to MySQL
1. Launch **Power BI Desktop**.
2. On the **Home** ribbon, click **Get Data** -> **More...**
3. Select **Database** -> **MySQL database** -> Click **Connect**.
4. In the dialog box:
   - **Server**: `localhost:3306` (or `127.0.0.1:3306`)
   - **Database**: `fitness_tracker_db`
   - **Data Connectivity mode**: Select **Import** (Recommended for fast local DAX computations and full visual flexibility).
   - Click **OK**.
5. **Authentication**:
   - In the left pane, click **Database**.
   - **User name**: `root` (or your MySQL username).
   - **Password**: Enter your MySQL password.
   - Click **Connect**.
   - If an "Unencrypted Connection" prompt appears, click **OK** to proceed for localhost.

---

#### Step 3: Select and Transform Data
1. In the **Navigator** window, check the box next to `fitness_activity_logs`.
2. A preview will appear on the right showing all 15 columns.
3. Click **Transform Data** (Power Query Editor opens).
4. Verify column data types:
   - `Record_ID`: Whole Number (`Int64.Type`)
   - `Date`: Date (`type date`)
   - `Age`, `Workout_Duration_Minutes`, `Calories_Burned`, `Calories_Consumed`, `Steps`: Whole Number
   - `Weight_Kg`, `Height_Cm`, `Water_Intake_Liters`, `Sleep_Hours`: Decimal Number
   - `User_ID`, `Gender`, `Activity_Type`, `Food_Category`: Text
5. Click **Close & Apply** on the Home tab.

---

### Method 2: Alternative Connection via CSV (Zero-Setup Workflow)
If MySQL is not installed or you experience server permission/firewall restrictions, use the direct CSV import:

1. Open **Power BI Desktop**.
2. Click **Get Data** -> **Text/CSV**.
3. Navigate to `D:\project\power bi data\fitness_data.csv` and click **Open**.
4. Power BI will display a preview window.
5. Ensure:
   - **File Origin**: `65001: Unicode (UTF-8)`
   - **Delimiter**: `Comma`
   - **Data Type Detection**: `Based on first 200 rows`
6. Click **Transform Data** to inspect types, or click **Load** directly.
7. Both methods produce the exact same data model, DAX calculation compatibility, and visual outputs!

---

### Step 4: Create the Dedicated DAX Measures Table
To keep your data model professional and organized:
1. In Power BI Desktop, click **Home** -> **Enter Data**.
2. Set Name to `_Measures`.
3. Click **Load**.
4. Follow [DAX_Measures.dax](file:///d:/project/power%20bi%20data/DAX_Measures.dax) to create each measure inside this table.
5. Hide the empty placeholder column `Column1` by right-clicking it -> **Hide**.

---

### Step 5: Data Validation Checklist
Before building visuals, run this quick validation in Power BI Data View:
- [x] Total rows loaded = 697.
- [x] Date column contains dates from `2024-01-01` to `2024-02-09`.
- [x] No `(blank)` or `null` values in `Calories_Burned` or `Calories_Consumed`.
- [x] Drop `[Total Calories Consumed]` into a card visual -> Should read **1.53M**.
- [x] Drop `[Total Calories Burned]` into a card visual -> Should read **297.49K**.

---

### Step 6: How to Refresh Dashboard Data
- **Manual Refresh**: Click the **Refresh** button on the **Home** tab in Power BI Desktop.
- **Scheduled Refresh (Power BI Service)**:
  - If published to Power BI Service (app.powerbi.com), configure an **On-premises Data Gateway** for local MySQL, or upload the CSV to **OneDrive/SharePoint** for automated hourly/daily cloud refresh without needing a local gateway.

---

### Common Connection Errors & How to Fix Them

| Error Message / Issue | Root Cause | Solution |
| :--- | :--- | :--- |
| **"This connector requires one or more additional components to be installed"** | MySQL Connector/NET is missing | Download and install MySQL Connector/NET 8.0.x (x64) from official MySQL site and restart Power BI. |
| **"Authentication plugin 'caching_sha2_password' cannot be loaded"** | MySQL 8.0 uses new default password hashing not recognized by older connectors | Run in MySQL: `ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password'; FLUSH PRIVILEGES;` |
| **"Unable to connect to any of the specified MySQL hosts"** | MySQL service stopped or port 3306 blocked | Open Windows Services (`services.msc`), locate `MySQL80` (or `MySQL`), right-click and choose **Start**. |
| **"Details: An error happened while reading data from the provider: 'Timeout expired'"** | Database network latency or query lock | In Power BI MySQL connection dialog, expand "Advanced options" and set **Command timeout in minutes** to `30`. |
| **"Character encoding issues / Special characters corrupt"** | Incorrect CSV encoding | In Power Query, select the Source step, change encoding to `65001 (UTF-8)`. |
