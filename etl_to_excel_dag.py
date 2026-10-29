def etl_job():
    import pandas as pd
    import sqlite3

    conn = sqlite3.connect(
        "/mnt/d/Learn/python/Project/Airflow ETL Mini Project/sample.db"
    )

    df = pd.read_sql_query(
        "SELECT * FROM Orders",
        conn
    )

    df.to_excel(
        "/mnt/d/Learn/python/Project/Airflow ETL Mini Project/Destination.xlsx",
        index=False
    )

    conn.close()

    print("ETL completed successfully")