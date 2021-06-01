import numpy as np

class MCVaR:

  def __init__(self, investment, mu, sigma, c, n, iterations):
    self.investment = investment
    self.mu = mu
    self.sigma = sigma
    self.c = c # confidence level
    self.n = n # number of days
    self.iterations = iterations


  def simulation(self):
    #data = np.zeros([self.iterations, 1])
    rand = np.random.normal(0, 1, [1, self.iterations])

    stock_price = self.investment * np.exp(self.n * (self.mu - 0.5 * self.sigma**2) + self.sigma * np.sqrt(self.n) * rand)

    percentile = np.percentile(stock_price, (1 -  self.c) * 100)

    return self.investment - percentile

