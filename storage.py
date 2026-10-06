import csv
import os


def save_to_csv(data, csv_file):

    if not data:
        print("No data to save.")
        return

    # Create folder if necessary
    folder = os.path.dirname(csv_file)

    if folder:
        os.makedirs(folder, exist_ok=True)

    file_exists = os.path.exists(csv_file)

    fieldnames = [
        "timestamp",
        "name",
        "price",
        "change_24h",
        "market_cap"
    ]

    try:

        with open(
            csv_file,
            "a",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            # Header only first time
            if not file_exists or os.path.getsize(csv_file) == 0:

                writer.writeheader()

            for item in data:

                writer.writerow({
                    "timestamp": item.get("timestamp", ""),
                    "name": item.get("name", ""),
                    "price": item.get("price", ""),
                    "change_24h": item.get("change_24h", ""),
                    "market_cap": item.get("market_cap", "")
                })

        print("\nData stored successfully.")
        print("File:", csv_file)

    except Exception as e:

        print("\nError saving CSV:")
        print(e)