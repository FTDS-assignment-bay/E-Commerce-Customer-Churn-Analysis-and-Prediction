

import pandas as pd
from sqlalchemy import create_engine

'''
Membuat fungsi fetching_data. Fungsi ini bertugas untuk menarik data dari postgres
'''
def fetching_data():
    # Koneksi ke postgres
    engine = create_engine("postgresql+psycopg2://airflow:airflow@postgres:5432/airflow")
    conn = engine.connect()

    df = pd.read_sql_query("select * from table_final_project", conn) # Memilih kolom yang akan di tarik datanya

    df.to_csv('/opt/airflow/data/data_raw.csv' , sep=',', index=False) # Menyimpan data yang ditarik