import numpy as np
from scipy.stats import norm
import yfinance as yf
import pandas as pd


user_choice = input("would you like call or put option? (c or p)")


ticker = input("enter the stock ticker symbol (example NVDA for NVIDIA) ")
stock = yf.Ticker(ticker)
todays_data = stock.history(period="1d")
S = todays_data["Close"].iloc[0]


manual = input("would you like historical volatility, or manual input? (h,m) ")
if manual == "h":
    history_data = stock.history(period="1y")
    close_data = pd.DataFrame({"Close": history_data["Close"]})
    close_dataLog = np.log(close_data["Close"] / close_data["Close"].shift(1))
    daily_volat = close_dataLog.std(ddof=1)
    sigma = daily_volat*np.sqrt(251)

else:
    sigma = float(input("enter your manual volatility "))

interestrate_ticker = input("enter the risk-free rate ticker (for instance ^TNX) ")
riskFree_ticker = yf.Ticker(interestrate_ticker)
interestweeks_data = riskFree_ticker.history(period="5d")
r_discontinous = (interestweeks_data["Close"].iloc[-1])/100
r = np.log(1 + r_discontinous)

K = float(input("enter the strike price "))
T = float(eval(input("enter the time to maturity (0.5 or 6/12 for 6 months )")))

d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)

pdf_d1 = norm.pdf(d1)

gamma = pdf_d1 / (S * sigma * np.sqrt(T))
vega = (S * np.sqrt(T) * pdf_d1) / 100


if user_choice == "c":
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    print("call price: "+str(call_price))

    delta = norm.cdf(d1)
    theta = (- (S * pdf_d1 * sigma) / (2 * np.sqrt(T)) - r * K * np.exp(-r * T) * norm.cdf(d2)) / 365 
    rho = (K * T * np.exp(-r * T) * norm.cdf(d2)) / 100



else:
    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    print("put price: "+str(put_price))

    delta = norm.cdf(d1) - 1
    theta = (- (S * pdf_d1 * sigma) / (2 * np.sqrt(T)) + r * K * np.exp(-r * T) * norm.cdf(-d2)) / 365 
    rho = (-K * T * np.exp(-r * T) * norm.cdf(-d2)) / 100

print("delta: "+str(delta))
print("gamma: "+str(gamma))
print("theta: "+str(theta))
print("vega: "+str(vega))
print("rho: "+str(rho))


    