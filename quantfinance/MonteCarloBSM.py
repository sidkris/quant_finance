import numpy as np 
import math
import time

class MCOptionPricing:

  def __init__(self, S, K, T, rf, sigma, iterations):
    self.S = S
    self.K = K
    self.T = T
    self.rf = rf
    self.sigma = sigma
    self.iterations = iterations


  def CE(self):

    # we'll have 2 columns : 1st containing 0s and 2nd with the payoffs. payoff = max(0, S-K)
    option_data = np.zeros([self.iterations,2])
    rand = np.random.normal(0, 1, [1, self.iterations])

    stock_price = self.S * np.exp(self.T * (self.rf - 0.5 * self.sigma ** 2) + self.sigma * np.sqrt(self.T) * rand)

    option_data[:, 1] = stock_price - self.K

    # monte carlo average
    average = np.sum(np.amax(option_data, axis = 1)) / float(self.iterations)

    return np.exp(-1.0 * self.rf * self.T) * average

  
  def PE(self):

    # we'll have 2 columns : 1st containing 0s and 2nd with the payoffs. payoff = max(0, S-K)
    option_data = np.zeros([self.iterations,2])
    rand = np.random.normal(0, 1, [1, self.iterations])

    stock_price = self.S * np.exp(self.T * (self.rf - 0.5 * self.sigma ** 2) + self.sigma * np.sqrt(self.T) * rand)

    option_data[:, 1] = self.K - stock_price

    # monte carlo average
    average = np.sum(np.amax(option_data, axis = 1)) / float(self.iterations)

    return np.exp(-1.0 * self.rf * self.T) * average