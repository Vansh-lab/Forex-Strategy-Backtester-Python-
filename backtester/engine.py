import pandas as pd

def run_backtest(df, short_sma, long_sma, rsi_buy_threshold, rsi_sell_threshold, initial_capital=10000):
    """
    Runs the backtest for the SMA crossover with RSI filter strategy.

    Args:
        df (pd.DataFrame): DataFrame with price data and indicators.
        short_sma (int): The period for the short-term SMA.
        long_sma (int): The period for the long-term SMA.
        rsi_buy_threshold (int): RSI level to confirm buy signals.
        rsi_sell_threshold (int): RSI level to confirm sell signals.
        initial_capital (float): The starting capital for the simulation.

    Returns:
        tuple: A tuple containing the results DataFrame and the equity curve Series.
    """
    capital = initial_capital
    position = 0  # 0: no position, 1: long
    trades = []
    equity = []

    sma_short_col = f'SMA_{short_sma}'
    sma_long_col = f'SMA_{long_sma}'

    for i in range(1, len(df)):
        # Conditions for entry
        buy_signal = df[sma_short_col].iloc[i-1] < df[sma_long_col].iloc[i-1] and \
                     df[sma_short_col].iloc[i] > df[sma_long_col].iloc[i] and \
                     df['RSI'].iloc[i] > rsi_buy_threshold

        sell_signal = df[sma_short_col].iloc[i-1] > df[sma_long_col].iloc[i-1] and \
                      df[sma_short_col].iloc[i] < df[sma_long_col].iloc[i] and \
                      df['RSI'].iloc[i] < rsi_sell_threshold

        # Open a position
        if position == 0 and buy_signal:
            position = 1
            entry_price = df['Close'].iloc[i]
            entry_date = df.index[i]
            trades.append({'type': 'BUY', 'entry_price': entry_price, 'entry_date': entry_date})

        # Close a position
        elif position == 1 and sell_signal:
            exit_price = df['Close'].iloc[i]
            exit_date = df.index[i]
            trade = trades[-1]
            trade.update({'exit_price': exit_price, 'exit_date': exit_date})
            
            # Calculate P/L and update capital
            pnl = (exit_price - trade['entry_price']) * (capital / trade['entry_price']) # Simple position sizing
            capital += pnl
            trade['pnl'] = pnl
            position = 0

        equity.append(capital)

    results_df = pd.DataFrame(trades)
    equity_curve = pd.Series(equity, index=df.index[1:])
    
    return results_df, equity_curve
