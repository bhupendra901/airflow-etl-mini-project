def etl_job():
    import pandas as pd
    import sqlite3

    conn = sqlite3.connect(
        "/mnt/d/Learn/python/Project/Airflow ETL Mini Project/sample.db"
    )

    query = "SELECT * FROM Orders"

    df = pd.read_sql_query(query, conn)

    df.to_excel(
        "/mnt/d/Learn/python/Project/Airflow ETL Mini Project/Destination.xlsx",
        index=False
    )

    conn.close()

    print("ETL completed successfully")



