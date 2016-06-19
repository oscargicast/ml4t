import pandas as pd


def get_max_close(symbol):
    """
    Return the maximum closing value for stock indicated by symbol.

    Note: Data for a stock is store in file: data/<symbol>.csv
    """
    # Read the file.
    df = pd.read_csv('data/{}.csv'.format(symbol))
    # Compute and return max.
    return df['Close'].max()


def get_mean_volume(symbol):
    """
    Return the mean volumne for stock indicated by symbol.

    Note: Data for a stock is store in file: data/<symbol>.csv
    """
    # Read the file.
    df = pd.read_csv('data/{}.csv'.format(symbol))
    # Compute and return the mean volume for this stock.
    return df['Volume'].mean()


def test_run():
    for symbol in ['AAPL', 'IBM']:
        # Get max close value.
        print('Max close')
        print(symbol, get_max_close(symbol))

        print(20*'-*')  # Separator.

        # Get mean volume.
        print('Mean volume')
        print(symbol, get_mean_volume(symbol))


if __name__ == '__main__':
    test_run()
