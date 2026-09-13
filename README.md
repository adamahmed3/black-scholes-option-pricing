# Black-Scholes Option Pricing & Greeks Calculator

A code in python for pricing European options, using the calculated historical volatility from market data and giving the Greeks using the Black-Scholes model.
Note: The code case-sensitive (eg if it says c, type c not C)

## Features

- **Live Market Data**: Gathers up to date stock prices and risk-free rates on yahoo finance using python's yfinance.
- **Alternative Volatilities**: Can calculate annualized historical volatility from daily log returns over a 1-year period, or giving the option for a manual entry.
- **European Option Values**: Calculates the theoretical fair price for both call and put options according to the model.
- **Greeks**: Calculates Delta(price sensitivity), Gamma (Deltas sensitivity) , Theta (Time Decay) , Vega (Volatility Sensitivity) and Rho (Risk free rate Sensitivity)

## Dependencies

- ``yfinance`` : To collect stock price and risk-free rates
- ``numpy`` : For mathematical calculations
- ``scipy`` : For standard normal distribution functions (such as cdf and pdf)
- ``pandas`` : For manipulating historical price dataframes.

## Mathematics behind the code (using LaTex)

**Historical Volatility Calculations:** If chosen, the code calculates the annualized standard deviations of daily logarithmic returns over the number of trading days in a year (252)

- Daily Logarithmic Returns ($R_t$):

$$R_t = \ln\left(\frac{S_t}{S_{t-1}}\right)$$

- Sample Standard Deviation ($s$):

  $$s = \sqrt{\frac{1}{N - 1} \sum_{t=1}^{N} (R_t - \bar{R})^2}$$ (Where N is the number of observations and R is the mean log return)
  
- Annualized Volatility ($\sigma$):

  $$\sigma = s \times \sqrt{252}$$



**Risk-Free Rate Conversion:** Discontinuous market rates taken from Treasury tickers are converted into continuously compounded rates (r): 

- $$r = \ln(1 + r_{discontinuous})$$

**Black-Scholes Core Equations:** Calculations for d1,d2 and optioni prices with the standard normal cumulative distribution function N(x),

- $$d_1 = \frac{\ln\left(\frac{S}{K}\right) + \left(r + \frac{1}{2}\sigma^2\right)T}{\sigma\sqrt{T}}$$
  
- $$d_2 = d_1 - \sigma\sqrt{T}$$
  
- Call Option Price ($C$):
  
  $$C = S \cdot N(d_1) - K \cdot e^{-rT} \cdot N(d_2)$$

- Put Option Price ($P$):
  
  $$P = K \cdot e^{-rT} \cdot N(-d_2) - S \cdot N(-d_1)$$

**The Greeks:** Calculations for all greeks which show how option values respond to different changes in market inputs
- Delta ($\Delta$): Sensitivity to underlying price changes.
  - Call: $\Delta = N(d_1)$
  - Put: $\Delta = N(d_1) - 1$
 
- Gamma ($\Gamma$): Rate of change of Delta per change in stock price (N' is the standard normal probablility density function):
  
  $$\Gamma = \frac{N'(d_1)}{S \sigma \sqrt{T}}$$

- Theta ($\Theta$): Time decay scaled to a daily conversion 
  - Call: $\Theta = \frac{-\frac{S \cdot N'(d_1) \cdot \sigma}{2\sqrt{T}} - r K e^{-rT} N(d_2)}{365}$
  - Put: $\Theta = \frac{-\frac{S \cdot N'(d_1) \cdot \sigma}{2\sqrt{T}} + r K e^{-rT} N(-d_2)}{365}$

- Vega ($\nu$): Sensitivity to a 1% change in volatility
  
  $$\nu = \frac{S \sqrt{T} N'(d_1)}{100}$$

- Rho ($\rho$): Sensitivity to a 1% change in the risk free rate
  - Call: $\rho = \frac{K T e^{-rT} N(d_2)}{100}$
  - Put: $\rho = \frac{-K T e^{-rT} N(-d_2)}{100}$
