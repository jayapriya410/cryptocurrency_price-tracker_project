import os
import sys


# -----------------------------------------
# PATH SETUP
# -----------------------------------------

CURRENT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

PROJECT_DIR = os.path.dirname(
    CURRENT_DIR
)

sys.path.insert(
    0,
    CURRENT_DIR
)

sys.path.insert(
    0,
    PROJECT_DIR
)


# -----------------------------------------
# IMPORTS
# -----------------------------------------

from scraper import (
    create_driver,
    scrape_crypto_data
)

from storage import (
    save_to_csv
)

from filters import (
    filter_by_change
)

from config import (
    TOP_COINS,
    HEADLESS,
    CSV_FILE
)


# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------

def main():

    print("=" * 60)

    print(
        "          CRYPTOCURRENCY PRICE TRACKER"
    )

    print("=" * 60)

    driver = None

    try:

        # ---------------------------------
        # START CHROME
        # ---------------------------------

        print("\nStarting Chrome...")

        driver = create_driver(
            headless=HEADLESS
        )

        print(
            "Chrome started successfully."
        )

        # ---------------------------------
        # SCRAPE DATA
        # ---------------------------------

        print(
            "\nScraping cryptocurrency data..."
        )

        data = scrape_crypto_data(
            driver,
            TOP_COINS
        )

        # ---------------------------------
        # CHECK DATA
        # ---------------------------------

        if not data:

            print(
                "\nNo cryptocurrency data found."
            )

            return

        # ---------------------------------
        # DISPLAY DATA
        # ---------------------------------

        print("\n" + "=" * 60)

        print("SCRAPED DATA")

        print("=" * 60)

        for index, coin in enumerate(
            data,
            start=1
        ):

            print(
                f"\n{index}. "
                f"{coin['name']}"
            )

            print(
                f"   Price      : "
                f"{coin['price']}"
            )

            print(
                f"   24H Change : "
                f"{coin['change_24h']}"
            )

            print(
                f"   Market Cap : "
                f"{coin['market_cap']}"
            )

            print(
                f"   Timestamp  : "
                f"{coin['timestamp']}"
            )

        # ---------------------------------
        # SAVE DATA
        # ---------------------------------

        print("\n" + "=" * 60)

        print("SAVING DATA")

        print("=" * 60)

        save_to_csv(
            data,
            CSV_FILE
        )

        # ---------------------------------
        # FILTER
        # ---------------------------------

        positive_coins = filter_by_change(
            data,
            minimum_change=0
        )

        print(
            "\nPositive 24H change coins:",
            len(positive_coins)
        )

        # ---------------------------------
        # FINISHED
        # ---------------------------------

        print("\n" + "=" * 60)

        print(
            "CRYPTOCURRENCY PRICE TRACKER"
        )

        print(
            "COMPLETED SUCCESSFULLY"
        )

        print("=" * 60)

    except Exception as e:

        print("\nERROR:")
        print(type(e).__name__)
        print(e)

    finally:

        # ---------------------------------
        # CLOSE CHROME
        # ---------------------------------

        if driver is not None:

            print(
                "\nClosing Chrome..."
            )

            driver.quit()

        print(
            "\nProgram finished."
        )


# -----------------------------------------
# RUN
# -----------------------------------------

if __name__ == "__main__":

    main()