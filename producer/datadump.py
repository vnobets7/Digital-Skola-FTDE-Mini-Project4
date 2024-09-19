import pandas as pd
import urllib.parse

from sqlalchemy import create_engine

def insert_data_to_postgresql(df, table_name, db_url):
    try:
        engine = create_engine(db_url)

        df.to_sql(table_name, engine, if_exists='append', index=False)
        print(f"Data telah dimasukkan ke tabel {table_name}.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    csv_path = "Old_Information.csv"
    data = pd.read_csv(csv_path)
    
    # Informasi koneksi ke PostgreSQL
    username = "ftde02"
    password = "ftde02!@#"
    host = "localhost"
    port = "6543"
    database = "stream_processing"
    password = urllib.parse.quote_plus(password)

    # URL koneksi ke PostgreSQL
    db_url = f"postgresql://{username}:{password}@{host}:{port}/{database}"

    table_name = "old_information"
    insert_data_to_postgresql(data, table_name, db_url)