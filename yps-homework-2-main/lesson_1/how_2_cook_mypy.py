#!venv/bin/python
import argparse
import random
from typing import Optional

parser = argparse.ArgumentParser(description="How 2 cook mypy")
parser.add_argument("-c", "--currency", help="Currency", required=True)
args = parser.parse_args()

CURRENCY_MAPPING = {
    "USD": ("AL", "AK", "AZ", "AR", "CO", "CT", "DE"),
    "GER": ("",),
    "PLN": "Poland",
    "UAH": {
        "Poltava": ("Poltava", "Kremenchuk", "Myrhorod", "Lubny"),
        "Dnipro":  ("Dnipro", "Kryvyi Rih", "Pavlohrad"),
    }
}


def find_location(currency: str) -> Optional[str]:
    if currency in ("USD", "GER"):
        return random.choice(CURRENCY_MAPPING[currency])
    elif currency == "UAH":
        regions: list = list(CURRENCY_MAPPING["UAH"])
        region = random.choice(regions)
        print(f"Selected region is {region}")
        district = random.choice(CURRENCY_MAPPING["UAH"][region])
        return f"{region}, {district}"
    return CURRENCY_MAPPING.get(currency)


if __name__ == "__main__":
    print("Args is -> {args}".format(args=args))
    location: Optional[str] = find_location(currency=args.currency)
    location = location.strip()
    if location is None:
        print("Location is None")
    else:
        print(f"The location is -> '{location}'")
