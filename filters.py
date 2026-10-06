def filter_by_change(data, minimum_change=0):

    filtered_data = []

    for item in data:

        try:

            value = item.get("change_24h", "0")

            value = (
                value
                .replace("%", "")
                .replace("+", "")
                .strip()
            )

            change = float(value)

            if change >= minimum_change:

                filtered_data.append(item)

        except Exception:

            continue

    return filtered_data