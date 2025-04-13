import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, messagebox

#ask user for the stock symbol
def fetch_and_plot():
    ticker = entry.get().upper()
    try:
#download stock data
        data = yf.download(ticker, period='30d')
#check if data was returned and if empty show error and ask again
        if data.empty:
             raise ValueError("No data found for.")
#Calculate 7-day moving average
        data['7-day MA'] = data['Close'].rolling(window=7).mean()
#Plot closing prices
        plt.figure(figsize=(10, 5))
        plt.plot(data['Close'], label='Closing Price', color='blue')
        plt.title(f"{ticker} - Last 30 Days Closing Prices")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
#Save and show plot
        plt.savefig("stock_chart.png")
        plt.show()
    except Exception as e:
           messagebox.showerror("Error," f"Failed to fetch data for '{ticker}'. Please try again")

#GUI setup
root = Tk()
root.title('Stock Price visualizer')

Label(root, text='Enter stock Ticker:').grid(row=0, column=0, padx=10, pady=10)
entry = Entry(root)
entry.grid(row=0, column=1, padx=0, pady=0)

Button(root, text="Fetch & Plot", command=fetch_and_plot).grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()