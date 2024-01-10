
import pandas as pd

'''
Membuat fungsi cleaning_data. fungsi ini akan menghapus data duplicate, merubah tipe data,
merubah nama kolom, mengganti 'spasi' dengan '_', menghilangkan missing value, dan
akan menyimpan data csv baru.
'''

def cleaning_data():
    df= pd.read_csv('/opt/airflow/data/data_raw.csv') # read data csv kotor
    
    df.drop_duplicates(inplace=True) # delete duplicate data
    df.rename(columns={"CustomerID": "Customer ID", 
                       "PreferredLoginDevice": "Preferred Login Device",
                       "CityTier": "City Tier",
                       "WarehouseToHome": "Warehouse To Home",
                       "PreferredPaymentMode": "Preferred Payment Mode",
                       "HourSpendOnApp": "Hour Spend On App",
                       "NumberOfDeviceRegistered": "Number Of Device Registered",
                       "PreferedOrderCat": "Prefered Order Cat",
                       "SatisfactionScore": "Satisfaction Score",
                       "MaritalStatus": "Marital Status",
                       "NumberOfAddress": "Number Of Address",
                       "OrderAmountHikeFromlastYear": "Order Amount Hike From last Year",
                       "CouponUsed": "Coupon Used",
                       "OrderCount": "Order Count",
                       "DaySinceLastOrder": "Day Since Last Order",
                       "CashbackAmount": "Cashback Amount",
                       }, inplace=True)

    df.columns = df.columns.map(str.lower) # membuat nama kolom menjadi lowercase

    # mengganti 'spasi' dengan '_'
    trans_table = str.maketrans(' ', '_')
    df.columns = [col.translate(trans_table) for col in df.columns]

    df['tenure'] = df['tenure'].fillna(df['tenure'].median())
    df['warehouse_to_home'] = df['warehouse_to_home'].fillna(df['warehouse_to_home'].median())
    df['hour_spend_on_app'] = df['hour_spend_on_app'].fillna(df['hour_spend_on_app'].mean())
    df['order_amount_hike_from_last_year'] = df['order_amount_hike_from_last_year'].fillna(df['order_amount_hike_from_last_year'].median())
    df['coupon_used'] = df['coupon_used'].fillna(df['coupon_used'].median())
    df['order_count'] = df['order_count'].fillna(df['order_count'].median())
    df['day_since_last_order'] = df['day_since_last_order'].fillna(df['day_since_last_order'].median())









    # df.dropna(inplace=True) # Delete missing value
    df.to_csv('/opt/airflow/data/data_clean.csv', index=False) # menyimpan data yang sudah clean
