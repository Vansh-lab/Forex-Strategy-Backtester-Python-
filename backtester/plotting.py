import matplotlib.pyplot as plt

def plot_results(df, equity_curve, results_df, short_sma, long_sma):
    """
    Plots the backtest results including price, signals, and equity curve.
    """
    fig = plt.figure(figsize=(14, 10))
    fig.suptitle('Forex Backtest Results', fontsize=16)

    # Plot 1: Price, SMAs, and Trade Signals
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(df.index, df['Close'], label='Close Price', color='skyblue')
    ax1.plot(df.index, df[f'SMA_{short_sma}'], label=f'SMA {short_sma}', color='orange', linestyle='--')
    ax1.plot(df.index, df[f'SMA_{long_sma}'], label=f'SMA {long_sma}', color='purple', linestyle='--')

    buy_signals = results_df[results_df['type'] == 'BUY']
    ax1.plot(buy_signals['entry_date'], buy_signals['entry_price'], '^', markersize=10, color='g', label='Buy Signal')
    
    if 'exit_date' in results_df.columns:
        sell_signals = results_df.dropna(subset=['exit_date'])
        ax1.plot(sell_signals['exit_date'], sell_signals['exit_price'], 'v', markersize=10, color='r', label='Sell Signal')

    ax1.set_title('Price Chart with Trade Signals')
    ax1.set_ylabel('Price')
    ax1.legend()
    ax1.grid(True)

    # Plot 2: Equity Curve
    ax2 = fig.add_subplot(2, 1, 2, sharex=ax1)
    ax2.plot(equity_curve.index, equity_curve, label='Equity Curve', color='green')
    ax2.set_title('Equity Curve')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Portfolio Value ($)')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
