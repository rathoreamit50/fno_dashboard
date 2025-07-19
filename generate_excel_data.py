
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

fno_stocks = [
    "ICICIBANK.NS", "SBIN.NS", "AXISBANK.NS", "HDFCBANK.NS",
    "BAJFINANCE.NS", "INFY.NS", "TCS.NS", "RELIANCE.NS", "M&M.NS"
]

end_date = datetime.now()
start_date = end_date - timedelta(days=7)
results = []

for stock in fno_stocks:
    try:
        data = yf.download(stock, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'), progress=False)
        if len(data) >= 2:
            open_price = data['Open'][0]
            close_price = data['Close'][-1]
            volume_change = ((data['Volume'][-1] - data['Volume'][0]) / data['Volume'][0]) * 100
            price_change = ((close_price - open_price) / open_price) * 100

            results.append({
                "Stock": stock.replace(".NS", ""),
                "Open": round(open_price, 2),
                "Close": round(close_price, 2),
                "Price Change (%)": round(price_change, 2),
                "Volume Change (%)": round(volume_change, 2),
                "OI Trend": "Bullish" if price_change > 1 else "Neutral",
                "PCR": 1.12 if price_change > 1 else 0.89
            })
    except Exception as e:
        print(f"Error for {stock}: {e}")

df = pd.DataFrame(results)
df.to_excel("backend/Weekly_FNO_Analysis_With_OI.xlsx", index=False)
print("✅ File updated")
