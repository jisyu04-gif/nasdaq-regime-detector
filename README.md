# Nasdaq Regime Detector

Backtesting and automation tools for TQQQ and Nasdaq trading strategies.

## Overview

This project analyzes Nasdaq market regimes using:

- Trend signals
- Breadth indicators
- Volatility filters
- Moving averages
- Risk-on / Risk-off conditions

The goal is to build a practical regime detection system for leveraged ETF trading such as TQQQ.

---

## Features

- Nasdaq regime classification
- TQQQ signal detection
- 200-day moving average filter
- Breadth divergence alerts
- Volatility regime analysis
- Backtesting framework
- Risk management rules

---

## Planned Indicators

### Trend
- 200DMA
- 50DMA
- Breakout detection

### Breadth
- Advance / Decline
- New Highs vs New Lows
- Market participation

### Volatility
- VIX regime
- ATR expansion
- Volatility compression

### Macro
- Yield curve
- Credit spreads
- Liquidity conditions

---

## Example Strategy

```python
if price > MA200 and breadth == "strong":
    signal = "risk_on"
else:
    signal = "risk_off"
```

---

## Future Plans

- Real-time dashboard
- Automated alerts
- Python backtesting engine
- AI-generated market summaries
- GitHub Actions automation

---

## Disclaimer

This project is for research and educational purposes only.

---

## Author

GitHub: @jisyu04-gif
