import yfinance as yf
import pandas as pd
import datetime
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

def generate_weekly_fno_file():
    try:
        # Sample F&O stock list - replace with actual list if needed
        stock_list = ["ICICIBANK.NS", "SBIN.NS", "AXISBANK.NS", "HDFCBANK.NS",
    "BAJFINANCE.NS", "INFY.NS", "TCS.NS", "RELIANCE.NS", "M&M.NS"]

        final_data = []

        for symbol in stock_list:
            try:
                ticker = yf.Ticker(symbol)
                hist = ticker.history(period="7d")

                if hist.empty or len(hist) < 2:
                    continue

                price_change = ((hist['Close'].iloc[-1] - hist['Close'].iloc[0]) / hist['Close'].iloc[0]) * 100
                volume_change = ((hist['Volume'].iloc[-1] - hist['Volume'].iloc[0]) / hist['Volume'].iloc[0]) * 100

                final_data.append({
                    "Stock": symbol.replace(".BO", ""),
                    "Price Change (%)": round(price_change, 2),
                    "Volume Change (%)": round(volume_change, 2),
                    "OI Trend": "Up" if price_change > 0 else "Down",
                    "PCR": round(abs(price_change / 100), 2)
                })
            except yf.YFRateLimitError:
                print(f"Rate limited while processing {symbol}. Skipping...")
            except Exception as e:
                print(f"Error processing {symbol}: {e}")

        df = pd.DataFrame(final_data)

        wb = Workbook()
        ws = wb.active
        ws.title = "Weekly FNO Data"

        for r in dataframe_to_rows(df, index=False, header=True):
            ws.append(r)

        wb.save("backend/Weekly_FNO_Analysis_With_OI.xlsx")
        print("✅ Excel generated successfully.")
    except Exception as e:
        print(f"Error generating weekly FNO file: {e}")

if __name__ == "__main__":
    generate_weekly_fno_file()
