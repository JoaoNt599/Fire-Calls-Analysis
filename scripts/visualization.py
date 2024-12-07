import matplotlib.pyplot as plt
import pandas as pd


def plot_calls_per_year(df):
    calls_per_year = df.groupby('Year').size()
    calls_per_year.plot(kind='bar', figsize=(10, 6), color='skyblue')
    plt.title("Number of Calls per Year")
    plt.xlabel("Year")
    plt.ylabel("Call Number")
    plt.show()


if __name__ == "__main__":
    file_path = "./data/sf-fire-calls.csv"
    df = pd.read_csv(file_path)
    df['CallDate'] = pd.to_datetime(df['CallDate'])
    df['Year'] = df['CallDate'].dt.year
    plot_calls_per_year(df)