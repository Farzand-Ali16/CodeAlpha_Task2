import csv
def stock_tracker():
    stock_prices = {
        "AAPL": 180,   
        "TSLA": 250,   
        "GOOG": 120,  
        "MSFT": 330,   
        "AMZN": 140   
        }
    portfolio = []          
    total_investment = 0    
    print("Welcome to the Stock Tracker!")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print()
    while True:
        symbol = input("Enter stock symbol (or type 'done' to finish): ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in stock_prices:
            print("❌ Symbol not found. Try again.")
            print("Available:", ", ".join(stock_prices.keys()))
            print()
            continue
        try:
            qty = int(input(f"Enter quantity of {symbol}: "))
        except ValueError:
            print("❌ Invalid quantity. Enter a number.")
            print()
            continue
        price = stock_prices[symbol]
        total = price * qty
        total_investment += total
        portfolio.append((symbol, qty, price, total))
        print(f"Added: {symbol} | Qty: {qty} | Price: ${price} | Total: ${total}")
        print()
        more = input("Do you want to add another stock? (y/n): ").strip().lower()
        if more != "y":
            break
        print()
    print("\nYour Portfolio Summary:")
    print("-" * 45)
    for sym, qty, price, total in portfolio:
        print(f"{sym:5}  Qty: {qty:<5}  Price: ${price:<5}  Total: ${total}")
    print("-" * 45)
    print(f"Total Investment Value: ${total_investment}")
    save = input("\nDo you want to save results to CSV? (y/n): ").strip().lower()
    if save == "y":
        with open("portfolio.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "Price", "Total"])
            writer.writerows(portfolio)
        print("✅ Portfolio saved as 'portfolio.csv'.")
    print("\nThank you for using the Stock Tracker!")
if __name__ == "__main__":
    stock_tracker()
