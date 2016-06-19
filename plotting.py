import pandas as pd
import matplotlib.pyplot as plt


def test_run():
    df = pd.read_csv('data/AAPL.csv')

    # Plotting the Adjustment Close value.
    df['Adj Close'].plot()
    # Adding title and axis.
    plt.figure(1)
    plt.xlabel('N')
    plt.ylabel('Adj. Close')
    plt.title('Adjustment Close Values')
    plt.grid(True)

    # Plotting 2 Columns.
    df[['Close', 'Adj Close']].plot()
    # Adding title and axis.
    plt.figure(2)
    plt.xlabel('N')
    plt.title('Close + Adjustment Close')
    plt.grid(True)

    # Must be called to show plots.
    plt.show()


if __name__ == '__main__':
    test_run()
