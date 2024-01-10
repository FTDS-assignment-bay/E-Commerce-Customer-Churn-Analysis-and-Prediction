# '''
# ================================================================================================================================================================

# Nama : Saepul Hilal

# Batch : HCK - 010

# File ini bertujuan untuk membuat proses upload ke ealsticserch

# ================================================================================================================================================================
# '''

# import pandas as pd
# from elasticsearch import Elasticsearch
# from elasticsearch.helpers import bulk

# '''
# Membuat fungsi push_to_elastic. Fungsi ini dibuat untuk mengupload data yang sudah di cleaning
# kedalam elasticserch untuk dilakukan visualisasi
# '''
# def push_to_elastic():
#     es = Elasticsearch(hosts=["http://elasticsearch:9200"])

#     df = pd.read_csv('/opt/airflow/data/P2M3_saepul_hilal_data_clean.csv')
#     actions = [
#         {
#             "_index": "milestone3_saepul_hilal_data_clean",
#             "_source": row.to_dict()
#         }
#         for i, row in df.iterrows()
#     ]
#     bulk(es, actions)