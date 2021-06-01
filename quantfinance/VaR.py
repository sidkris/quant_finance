import numpy as np
import yfinance as yf 
import pandas as pd
from scipy.stats import norm

def download_data(stock, start, end):

  data = {}
  ticker = yf.download(stock, start, end)
  data[stock] = ticker["Adj Close"]
  return pd.DataFrame(data)

def calculate_daily_var(position, c, mu, sigma): # c = confidence level 
  var = position * (mu - sigma * norm.ppf(1-c))
  return var

def log_daily_returns(data, ticker):
  data["returns"] = np.log(data[ticker] / data[ticker].shift(1))
  data = data[1:]

def mu_sigma(data):
  mu = np.mean(data["returns"])
  sigma = np.std(data["returns"])
  return mu, sigma

def calculate_annualized_var(position, c, mu, sigma):
  annual_var = position * (mu * 252 - sigma * np.sqrt(252) * norm.ppf(1-c))
  return annual_var

