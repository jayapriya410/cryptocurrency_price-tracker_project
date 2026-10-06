import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_driver(headless=False):

    options = webdriver.ChromeOptions()

    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-notifications")

    options.page_load_strategy = "eager"

    driver = webdriver.Chrome(options=options)

    driver.set_page_load_timeout(60)

    return driver


def scrape_crypto_data(driver, limit=10):

    url = "https://coinmarketcap.com/"

    print("\nOpening CoinMarketCap...")

    try:
        driver.get(url)

    except Exception as e:
        print("Page loading warning:", e)

    print("Waiting for cryptocurrency data...")

    time.sleep(8)

    crypto_data = []

    # Wait for table
    try:

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "table")
            )
        )

    except Exception:
        print("Table was not detected immediately.")

    # Additional time for JavaScript
    time.sleep(5)

    # Find rows
    rows = driver.find_elements(
        By.CSS_SELECTOR,
        "table tbody tr"
    )

    print("Rows found:", len(rows))

    if len(rows) == 0:

        print("\nNo cryptocurrency rows found.")
        print("CoinMarketCap may not have loaded correctly.")

        return []

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    for row in rows:

        if len(crypto_data) >= limit:
            break

        try:

            cells = row.find_elements(
                By.TAG_NAME,
                "td"
            )

            # Skip incomplete rows
            if len(cells) < 8:
                continue

            # ---------------------------------
            # NAME
            # ---------------------------------

            name = ""

            try:

                # Try CoinMarketCap link
                links = row.find_elements(
                    By.CSS_SELECTOR,
                    'a[href*="/currencies/"]'
                )

                if links:
                    name = links[0].text.strip()

            except Exception:
                pass

            # Fallback
            if not name:

                name = cells[2].text.strip()

            # Sometimes name contains symbol
            name_lines = name.split("\n")

            if len(name_lines) > 0:
                name = name_lines[0].strip()

            if not name:
                continue

            # ---------------------------------
            # PRICE
            # ---------------------------------

            price = cells[3].text.strip()

            if not price:
                continue

            # ---------------------------------
            # 24 HOUR CHANGE
            # ---------------------------------

            change_24h = cells[4].text.strip()

            if not change_24h:
                continue

            # ---------------------------------
            # MARKET CAP
            # ---------------------------------

            market_cap = cells[7].text.strip()

            if not market_cap:

                # Fallback
                market_cap = cells[-3].text.strip()

            if not market_cap:
                continue

            # ---------------------------------
            # SAVE DATA
            # ---------------------------------

            crypto_data.append({

                "timestamp": timestamp,

                "name": name,

                "price": price,

                "change_24h": change_24h,

                "market_cap": market_cap

            })

            print(
                f"{len(crypto_data)}. "
                f"{name} | "
                f"Price: {price} | "
                f"24H: {change_24h} | "
                f"Market Cap: {market_cap}"
            )

        except Exception as e:

            print(
                "Error reading row:",
                e
            )

    print(
        "\nNumber of coins found:",
        len(crypto_data)
    )

    return crypto_data