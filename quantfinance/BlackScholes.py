from scipy import stats
from numpy import log, exp, sqrt


def price_CE(S, K, T, rf, sigma): # european call option
  d1 = (log(S/K) + (rf + sigma *sigma/2) * T) / (sigma * sqrt(T))
  d2 = d1 - sigma * sqrt(T)
  print("d1 : {}".format(round(d1,4)))
  print("d2 : {}".format(round(d2,4)))

  # use standard normal dist function N(x) to calc price of the option
  return S * stats.norm.cdf(d1) - K * exp(-rf*T) * stats.norm.cdf(d2)


def price_PE(S, K, T, rf, sigma): # european put option
  d1 = (log(S/K) + (rf + sigma *sigma/2) * T) / (sigma * sqrt(T))
  d2 = d1 - sigma * sqrt(T)
  print("d1 : {}".format(round(d1,4)))
  print("d2 : {}".format(round(d2,4)))

  # use standard normal dist function N(x) to calc price of the option
  return -S * stats.norm.cdf(-d1) + K * exp(-rf*T) * stats.norm.cdf(-d2)