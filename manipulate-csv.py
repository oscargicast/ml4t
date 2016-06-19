import pandas as pd


def test_run():
    # Read CSV.
    df = pd.read_csv('data/AAPL.csv')
    # Print firt 3 rows of the data frame.
    print(df.head(3))
    # Print last 5 rows of the data frame.
    print(df.tail(5))
    # Rows between index 10 and 20.
    print(df[10:21])


if __name__ == '__main__':
    test_run()
