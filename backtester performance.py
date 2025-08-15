backtester/performance.py
import numpy as np

def calculate_metrics(results_df, equity_curve, initial_capital=10000):
    """
    Calculates key performance metrics from backtest results.

    Args:
        results_df (pd.DataFrame): DataFrame of completed trades.
        equity_curve (pd.Series): Series representing equity over time.
        initial_capital (float): The starting capital.

    Returns:
        dict: A dictionary of performance metrics.
    """
    if results_df.empty:
        return {
            "Total Return (%)": 0,
            "Total Trades": 0,
            "Win Rate (%)": 0,
            "Max Drawdown (%)": 0,
            "Sharpe Ratio": 0,
        }
        
    total_return = ((equity_curve.iloc[-1] - initial_capital) / initial_capital) * 100
    total_trades = len(results_df)
    
    wins = results_df[results_df['pnl'] > 0]
    win_rate = (len(wins) / total_trades) * 100 if total_trades > 0 else 0

    # Max Drawdown
    cumulative_max = equity_curve.cummax()
    drawdown = (equity_curve - cumulative_max) / cumulative_max
    max_drawdown = drawdown.min() * 100

    # Sharpe Ratio (assuming risk-free rate is 0)
    returns = equity_curve.pct_change().dropna()
    sharpe_ratio = (returns.mean() / returns.std()) * np.sqrt(252) if returns.std() != 0 else 0 # Annualized for daily data assumption

    metrics = {
        "Total Return (%)": f"{total_return:.2f}",
        "Total Trades": total_trades,
        "Win Rate (%)": f"{win_rate:.2f}",
        "Max Drawdown (%)": f"{max_drawdown:.2f}",
        "Sharpe Ratio": f"{sharpe_ratio:.2f}",
    }
    
    return metrics
