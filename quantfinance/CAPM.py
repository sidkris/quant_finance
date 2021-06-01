# CAPM Equation = Expected Return = RF + beta (RM - RF)

# where : RF : Risk Free RoR; RM : Market RoR

# beta = cov(Stock Return, RM) / Var(RM)


import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

class CAPM:

  def __init__(self, stocks, start, end):
    self.stocks = stocks
    self.start = start
    self.end = end

  
  def download_data(self):

    data = {}

    for i in self.stocks:
      ticker = yf.download(i, self.start, self.end)
      data[i] = ticker["Adj Close"]

    return pd.DataFrame(data)


  def initialize(self):
    stock_data = self.download_data()
    #stock_data = stock_data.resample("M").last() # monthly data
    self.data = pd.DataFrame({"stock_adj_close" : stock_data[self.stocks[0]],
                              "mkt_adj_close" : stock_data[self.stocks[1]]})
    
    #log monthly returns
    self.data[["stock_returns", "mkt_returns"]] = np.log(self.data[["stock_adj_close", "mkt_adj_close"]] / self.data[["stock_adj_close", "mkt_adj_close"]].shift(1))

    # remove returns NaNs
    self.data = self.data[1:]
    print(self.data)


  def calculate_beta(self):
    cov_matrix = np.cov(self.data["stock_returns"], self.data["mkt_returns"])
    beta = cov_matrix[0,1] / cov_matrix[1,1]
    print("The beta factor is {}".format(beta))


  def regression(self):

    # using linear regression to fit a line to the data (beta)
    beta, alpha = np.polyfit(self.data["mkt_returns"], self.data["stock_returns"], deg = 1)
    # deg = 1 (linear), 2 (quadratic), 3 (cubic)
    print("The regressed beta factor (linear) is {}".format(beta))
    print("The regressed alpha factor (linear) is {}".format(alpha))
    self.plot_regression(alpha, beta)

  
  def plot_regression(self, alpha, beta):
    fig, axis = plt.subplots(1, figsize = (20, 10))
    axis.scatter(self.data["mkt_returns"], self.data["stock_returns"], label = "Data Points")
    axis.plot(self.data["mkt_returns"], beta * self.data["mkt_returns"] + alpha, color = "red", label = "CAPM Line")
    plt.title("Capital Asset Pricing Model -- Alpha & Beta")
    plt.xlabel("Market Returns")
    plt.ylabel("Stock Returns")
    plt.legend()
    plt.grid(True)
    plt.show()

