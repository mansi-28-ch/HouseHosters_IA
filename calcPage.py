import tkinter as tk
from tkinter import ttk

result = "..."

# Property class with attributes for calculation
class Property:
    def __init__(self, base, rating, season, commission, price):
        self.base = base
        self.rating = rating
        self.season = season
        self.commission = commission
        self.price = price

    def calcPrice(self):
        self.price = self.base + (self.base * self.rating) + (self.base * self.season) + (self.base * self.commission)
        return self.price

# Function to handle button click
def calculate_price():
    # Get input values from the UI
    base = float(baseEntry.get())
    rating = convert_rating(ratingEntry.get())
    season = convert_season(seasonBox.get())
    commission = convert_platform(platformBox.get())

    # Create an instance of the Property class
    my_instance = Property(base, rating, season, commission, 0.0)

    # Call the calcPrice method and update the result label
    calculated_price = my_instance.calcPrice()
    resultLabel1.config(text=f"Result: {calculated_price:.2f}")

# Function to convert rating string to numerical value
def convert_rating(rating_str):
    try:
        rating = float(rating_str)
        if rating < 2.4:
            return -0.05
        elif rating < 4.4:
            return 0
        elif 4.5 <= rating <= 5:
            return 0.05
    except ValueError:
        # Handle the case where the entry is not a valid float
        return 1.0  # Default to 1.0 if not a valid float

# Function to convert season string to numerical value
def convert_season(season_str):
    season_values = {"low": -0.05, "mid": 0.0, "high": 0.05}
    return season_values.get(season_str, 1.0)  # Default to 1.0 if not found in mapping

# Function to convert platform string to numerical value
def convert_platform(platform_str):
    platform_values = {"Airbnb": 0.03, "Booking.com": 0.15}
    return platform_values.get(platform_str, 1.0)  # Default to 1.0 if not found in mapping

def openCalcWin():
    calcWindow = tk.Tk()
    calcWindow.title("Price Recommendation")
    calcFrame = tk.Frame(calcWindow)
    calcFrame.pack()

    calcFrame = tk.LabelFrame(calcFrame, text="Enter your property details:")
    calcFrame.grid(row=0, column=0, padx=20, pady=20)

    baseLabel = tk.Label(calcFrame, text="base price:")
    baseLabel.grid(row=1, column=0)

    global baseEntry  # Made baseEntry a global variable for accessibility
    baseEntry = tk.Entry(calcFrame)
    baseEntry.grid(row=2, column=0)

    global ratingEntry  # Made ratingEntry a global variable for accessibility
    ratingLabel = tk.Label(calcFrame, text="average rating:")
    ratingLabel.grid(row=3, column=0)

    ratingEntry = tk.Entry(calcFrame)
    ratingEntry.grid(row=4, column=0)

    global platformBox  # Made platformBox a global variable for accessibility
    platformLabel = tk.Label(calcFrame, text="platform:")
    platformLabel.grid(row=5, column=0)

    platformBox = ttk.Combobox(calcFrame, values=["Airbnb", "Booking.com"])
    platformBox.grid(row=6, column=0)

    global seasonBox  # Made seasonBox a global variable for accessibility
    seasonLabel = tk.Label(calcFrame, text="season:")
    seasonLabel.grid(row=7, column=0)

    seasonBox = ttk.Combobox(calcFrame, values=["low", "mid", "high"])
    seasonBox.grid(row=8, column=0)

    global resultLabel1  # Made resultLabel1 a global variable for accessibility
    resultLabel = tk.Label(calcFrame, text="result:")
    resultLabel.grid(row=9, column=0)

    resultLabel1 = tk.Label(calcFrame, text=result)
    resultLabel1.grid(row=10, column=0)

    calcButton = tk.Button(calcFrame, text="Calculate Price", command=calculate_price)
    calcButton.grid(row=11, column=0, padx=20, pady=10)

    calcWindow.mainloop()

openCalcWin()
