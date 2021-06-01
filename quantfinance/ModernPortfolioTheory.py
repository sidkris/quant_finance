import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as optimization

TRADING_DAYS = 252
NUM_PORTFOLIO_RANDOM = 1000

# stock universe
stocks = ["AAPL", "WMT", "TSLA", "GE", "AMZN", "MSFT"]
start_date = "2010-01-01"
end_date = "2021-05-28"

def download_data(stocks, start_date, end_date):
  data = {}
  for i in stocks:
    ticker = yf.Ticker(i)
    data[i] = ticker.history(start = start_date, end = end_date)["Close"]

  return pd.DataFrame(data)


def show_data(data):
  data.plot(figsize = (10, 5))
  plt.show()


def daily_log_return(data):
  log_return = np.log(data/data.shift(1))
  return log_return[1:] #skip first row since it contains NaNs


def show_stats(returns):
  print("The mean of annual log returns is : \n{}".format(returns.mean() * TRADING_DAYS))
  print("-------------------------\n")
  print("-------------------------\n")
  print("The covariance of annual log returns is : \n{}".format(returns.cov() * TRADING_DAYS))


def show_mean_variance(returns, weights):
  annual_portfolio_return = np.sum(returns.mean() * weights) * TRADING_DAYS
  portfilio_variance = np.dot(weights.T, np.dot(returns.cov() * TRADING_DAYS, weights))
  portfolio_vol = np.sqrt(portfilio_variance)
  print("Expected portfolio mean returns : {}".format(annual_portfolio_return))
  print("Expected portfolio volatility (std dev) : {}".format(portfolio_vol))


def portfolio_generator(returns):
  portfolio_weights = []
  portfolio_means = []
  portfolio_risks = []
  for _ in range(NUM_PORTFOLIO_RANDOM):
    w = np.random.random(len(stocks))
    w /= np.sum(w)
    portfolio_weights.append(w)
    portfolio_means.append(np.sum(returns.mean() * w) * TRADING_DAYS)
    portfolio_risks.append(np.sqrt(np.dot(w.T, np.dot(returns.cov() * TRADING_DAYS, w))))

  return np.array(portfolio_weights), np.array(portfolio_means), np.array(portfolio_risks)


def show_portfolios(returns, vol):
  plt.figure(figsize = (10, 6))
  plt.scatter(vol, returns, c = returns/vol, marker = 'o')
  plt.grid(True)
  plt.xlabel("Expected Volatility")
  plt.ylabel("Expected Return")
  plt.colorbar(label = "Sharpe Ratio")
  plt.show()


def stats(weights, returns):
  portfolio_return = np.sum(returns.mean() * weights) * TRADING_DAYS
  portfolio_vol = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * TRADING_DAYS, weights)))
  sharpe = portfolio_return / portfolio_vol
  return np.array([portfolio_return, portfolio_vol, sharpe])


# using scipy.optimize to find the minimum of a given function
def min_function_sharpe(weights, returns):
  return -stats(weights, returns)[2]


def optimize_portfolio(weights, returns):
  constraints = {"type": "eq", "fun": lambda x: np.sum(x) - 1} 
  bounds = tuple((0,1) for _ in range(len(stocks)))
  return optimization.minimize(fun = min_function_sharpe, x0 = weights[0], args = returns, method = "SLSQP", bounds = bounds, constraints = constraints)


def print_optimal_portfolio(optimum, returns):
  print("Optimal Portfolio : ", optimum["x"].round(3))
  print("Expected return, volatility and sharpe ratio: ", stats(optimum["x"].round(3), returns))


def show_optimum_portfolio(optimal , returns, portfolio_returns, portfolio_vols):
  plt.figure(figsize = (10, 6))
  plt.scatter(portfolio_vols, portfolio_returns, c = portfolio_returns/portfolio_vols, marker = 'o')
  plt.grid(True)
  plt.xlabel("Expected Volatility")
  plt.ylabel("Expected Return")
  plt.colorbar(label = "Sharpe Ratio")
  plt.plot(stats(optimal['x'], returns)[1], stats(optimal['x'], returns[0], "g*", markersize = 20))
  plt.show()