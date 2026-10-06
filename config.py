import os

# Project root folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data folder
DATA_DIR = os.path.join(BASE_DIR, "data")

# Create data folder automatically
os.makedirs(DATA_DIR, exist_ok=True)

# CSV file
CSV_FILE = os.path.join(DATA_DIR, "crypto_data.csv")

# Number of cryptocurrencies
TOP_COINS = 10

# Chrome visible mode
HEADLESS = False