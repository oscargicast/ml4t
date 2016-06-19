import pandas as pd
import matplotlib.pyplot as plt


def test_run():
    # Plotting the Adjustment Close value.
    df = pd.read_csv('data/AAPL.csv')
    print(df['Adj Close'])
    # The data is plotted inversely as the file.
    df['Adj Close'].plot()
    # Adding title and axis.
    plt.xlabel('N')
    plt.ylabel('Adj. Close')
    plt.title('Adjustment Close Values')
    plt.grid(True)
    # Must be called to show plots.
    plt.show()


if __name__ == '__main__':
    test_run()
