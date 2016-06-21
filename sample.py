import pandas as pd


def test_run():
    # Defines date range.
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)
    # Creates an empty data frame with dates as index.
    df1 = pd.DataFrame(index=dates)
    # Reads SPY data into temporary dataframe.
    dfSPY = pd.read_csv(
        'data/SPY.csv',
        index_col='Date',
        parse_dates=True,
        usecols=['Date', 'Adj Close'],
        na_values=['nan'],
    )

    # # Joins the 2 dataframes using DataFrame.join().
    # # This is a left join by default.
    # df1 = df1.join(dfSPY)
    # # Drops NaN values.
    # df1 = df1.dropna()

    # The 2 steps above can be summed up like this:
    df1 = df1.join(dfSPY, how='inner')
    print(df1)


if __name__ == '__main__':
    test_run()
