# Forex-Strategy-Backtester-Python-
This project is a Python-based tool for backtesting forex trading strategies using historical market data. It simulates trades based on a defined strategy, using technical indicators to make decisions. The primary goal is to evaluate the historical performance of a strategy by calculating key metrics like total return, win rate, and max drawdown, and visualizing the results.

Technology Stack: Python, Pandas, NumPy, Matplotlib

Strategy Implemented: A dual Simple Moving Average (SMA) crossover strategy with a Relative Strength Index (RSI) filter for trade confirmation.

Key Features:

Loads historical price data from a CSV file.

Calculates necessary technical indicators.

Executes trades based on predefined strategy rules.

Calculates and displays key performance metrics.

Generates a plot showing the equity curve and trade signals on the price chart
# Forex Strategy Backtester

A Python-based tool to simulate currency pair trades using historical data and technical indicators to evaluate profitability and risk. This project provides a framework for testing quantitative trading strategies before deploying them in a live environment.

!

##  Description

This backtester implements a trading strategy based on a **Simple Moving Average (SMA) crossover** confirmed by the **Relative Strength Index (RSI)**. It processes historical OHLCV (Open, High, Low, Close, Volume) data for a given currency pair, simulates trades, and provides a detailed performance analysis.

##  Features

-   **Data Handling:** Loads historical forex data from CSV files.
-   **Indicator Calculation:** Includes built-in functions for common technical indicators like SMA and RSI.
-   **Backtesting Engine:** A core engine that iterates through historical data candle-by-candle to simulate trading decisions.
-   **Performance Metrics:** Calculates essential metrics such as:
    -   Total Return (%)
    -   Win Rate (%)
    -   Total Number of Trades
    -   Maximum Drawdown (%)
    -   Sharpe Ratio
-   **Visualization:** Generates a comprehensive plot showing the price history, SMA indicators, buy/sell signals, and the portfolio's equity curve over time.

## 🛠Technology Stack

-   **Python 3.x**
-   **Pandas:** For data manipulation and analysis.
-   **NumPy:** For numerical operations.
-   **Matplotlib:** For data visualization and plotting results.

##  Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/forex-backtester.git](https://github.com/your-username/forex-backtester.git)
    cd forex-backtester
    ```

2.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

##  Usage

1.  **Add Data:**
    Place your historical data CSV file in the `data/` directory. The CSV must contain `Date`, `Time`, `Open`, `High`, `Low`, and `Close` columns. A sample filename is `EURUSD_H1.csv`.

2.  **Configure the Strategy:**
    Open `main.py` and modify the parameters in the configuration section to change the SMA periods, RSI settings, or initial capital.
    ```python
    # Strategy Parameters
    SHORT_SMA = 50
    LONG_SMA = 100
    RSI_PERIOD = 14
    RSI_BUY_THRESHOLD = 50
    RSI_SELL_THRESHOLD = 50
    ```

3.  **Run the Backtest:**
    Execute the main script from the root directory of the project.
    ```bash
    python main.py
    ```

The script will print the performance metrics to the console and display a plot with the backtest results.

##  Future Improvements

-   [ ] Implement more complex strategies and technical indicators (e.g., MACD, Bollinger Bands).
-   [ ] Add risk management features like stop-loss and take-profit levels.
-   [ ] Account for transaction costs (spreads and commissions) for a more realistic simulation.
-   [ ] Develop a more modular strategy class structure to easily switch between different strategies.
-   [ ] Add parameter optimization capabilities (e.g., using Grid Search or genetic algorithms)..
