Apache Airflow ETL Mini Project
Project Overview
 This project demonstrates a simple ETL (Extract, Transform, Load) workflow using Apache Airflow. The workflow extracts data from a SQLite database, processes it using Pandas, and exports the results to an Excel file.

Architecture
  SQLite Database
    ↓
  Data Extraction
    ↓
  Pandas Transformation
    ↓
  Excel Report Generation
    ↓
  Apache Airflow Automation
  
Technologies Used
 Apache Airflow, Python, Pandas, SQLite, Excel
 
Project Structure
  Airflow ETL Mini Project/
  │
  ├── Airflow ETL Mini Project.py
  ├── sample.db
  ├── Destination.xlsx
  ├── README.md

Dataset
  Source database: sample.db
  Source table: Orders
  Sample fields: order_id, customer_id, amount

ETL Workflow
 Extract: Read data from SQLite database:
          Python: pd.read_sql_query("SELECT * FROM Orders", conn)
 Transform: Process data using Pandas DataFrames.
 Load: Export processed data into: Destination.xlsx

Apache Airflow
  The workflow was automated using an Airflow DAG.
  Features: Scheduled execution, Task monitoring, Workflow automation, Execution logging
  
Output
  Generated report: Destination.xlsx
  Example output:
  order_id	customer_id 	amount
   1	        1	          5000
   2	        1	          2000
   3        	2         	3000

Skills Demonstrated: ETL Development, Apache Airflow, Python, Pandas, SQLite, Data Automation, Workflow Monitoring

Author: Bhupendra Kumar
LinkedIn: https://www.linkedin.com/in/bhupendra-kumar-552276129/
GitHub: https://github.com/bhupendra901
