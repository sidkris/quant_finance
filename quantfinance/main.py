#from ZeroCouponBonds import ZeroCouponBonds
#from CouponBonds import CouponBonds


# zero coupon bond ----------------------------------------------

#amount = float(input("Principal Amount : "))
#mat = float(input("Maturity : "))
#int_rate = float(input("Market Rate of Interest (in decimals) : "))

#bond = ZeroCouponBonds(amount, mat, int_rate)

#price = round(bond.calculate_price(), 2)

#print("the price of the zero coupon bond is {}".format(price))

#----------------------------------------------------

# coupon bearing bond
#c_bond = CouponBonds(1000, 0.10, 3, 0.04)
#c_price = round(c_bond.calculate_price(), 2)
#print("the price of the coupon bearing bond is {}".format(c_price))

#----------------------------------------------------

#import ModernPortfolioTheory as MPT 

#stocks = ["AAPL", "WMT", "TSLA", "GE", "AMZN", "MSFT"]
#weights = [0.20, 0.20, 0.10, 0.10, 0.25, 0.15]
#start_date = "2010-01-01"
#end_date = "2021-05-28"

#x = MPT.download_data(stocks, start_date, end_date)
#daily_log_ret = MPT.daily_log_return(x)
#MPT.show_stats(daily_log_ret)
#MPT.show_data(x)

#random_weights, means, risks = MPT.portfolio_generator(daily_log_ret)
#MPT.show_portfolios(means, risks)
#optimum = MPT.optimize_portfolio(random_weights, daily_log_ret)
#MPT.print_optimal_portfolio(optimum, daily_log_ret)
#MPT.show_optimum_portfolio(optimum, daily_log_ret, means, risks)

#-----------------------------------------------------------------------

#from CAPM import CAPM

#start = "2010-01-01"
#end = "2021-05-28"
# ^GSPC = S&P 500 index
#stocks = ["AAPL", "^GSPC"]
#capm = CAPM(stocks, start, end)
#capm.initialize()
#capm.calculate_beta()
#capm.regression()

#--------------------------------------------------------------------------

#import BlackScholes as bsm
#from MonteCarloBSM import MCOptionPricing as MCBSM

#S = 100 # stock price
#K = 100 # strike price
#T = 1 #expiry in yrs
#rf = 0.05 # risk free rate
#sigma = 0.2 # vol of the underlying stock

#call_option_price = bsm.price_CE(S, K, T, rf, sigma)
#print("The price of the call options is : {}".format(round(call_option_price,2)))

#put_option_price = bsm.price_PE(S, K, T, rf, sigma)
#print("The price of the put option is : {}".format(round(put_option_price,2)))


#option = MCBSM(S, K, T, rf, sigma, 1000000)
#mc_call_price = option.CE()
#print("The monte-carlo option price (call) is : {}".format(round(mc_call_price,2)))

#mc_put_price = option.PE()
#print("The monte-carlo option price (put) is : {}".format(round(mc_put_price,2)))

#------------------------------------------------------------------------------------

#import VaR
#from MCVaR import MCVaR as mcv

#ticker = "C" 
#start = "2014-01-01"
#end = "2018-01-01"
#amount_invested = 1000000
#confidence_level = 0.99

#data = VaR.download_data(ticker, start, end)
#log_returns_daily = VaR.log_daily_returns(data, ticker)
#print(log_returns_daily) 

#mu, sigma = VaR.mu_sigma(data)
#var = VaR.calculate_daily_var(amount_invested, confidence_level, mu, sigma)
#annual_var = VaR.calculate_annualized_var(amount_invested, confidence_level, mu, sigma)

#print("VaR (daily) is : ${}".format(round(var,2)))
#print("VaR (annual) is : ${}".format(round(annual_var,2)))

#x = mcv(amount_invested, mu, sigma, confidence_level, 1, 1000000)
#print("The MC simulated VaR is : ${}".format(round(x.simulation(), 2)))

#-----------------------------------------------------------------------------------------