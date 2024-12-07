import pandas as pd
from pyspark.sql import SparkSession


def load_data_pandas(file_path):
    return pd.read_csv(file_path)

def load_data_pyspark(file_path):
    spark = SparkSession.builder.appName("FireCalls").getOrCreate()
    return spark.read.csv(file_path, header=True, inferSchema=True)

def process_data(df):
    df['CallDate'] = pd.to_datetime(df['CallDate'])
    df['Year'] = df['CallDate'].dt.year
    return df 


if __name__ == "__main__":
    file_path = "./data/sf-fire-calls.csv"
    df = load_data_pandas(file_path)
    df = process_data(df)
    print(df.head())