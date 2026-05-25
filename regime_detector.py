import pandas as pd

def detect_regime(price, ma200):
    if price > ma200:
        return "RISK_ON"
    return "RISK_OFF"

print(detect_regime(22000, 21000))
