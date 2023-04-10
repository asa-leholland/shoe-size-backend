import json

from enum import Enum


class ShoeSizeCategory(Enum):
    WOMENS = "Women's"
    MENS = "Men's"
    BIG_KIDS = "Big Kids' (7–12 Years)"
    LITTLE_KIDS = "Little Kids' (4–7 Years)"
    TODDLERS = "Toddlers' (9 Months - 4 Years)"
    INFANTS = "Infants' (0–9 Months)"


class ShoeSizeSystem(Enum):
    US_CANADA = "US & Canada"
    UK = "UK"
    EUROPE = "Europe"
    INCHES = "Inches"
    CENTIMETERS = "Centimeters"


def convert_size(data_path: str, unit: ShoeSizeCategory, size: str, location: ShoeSizeSystem, converted_location: ShoeSizeSystem):
    assert unit in ShoeSizeCategory
    assert location in ShoeSizeSystem
    assert converted_location in ShoeSizeSystem
    assert data_path is not None and data_path != "" and data_path.endswith(".json")
    assert size is not None and size != "" and isinstance(size, str)
    with open(data_path) as f:
        data = json.load(f)

    for item in data:
        if item["Unit"] == unit.value:
            print(item[location.value])
            index = item[location.value].index(size)
            return item[converted_location.value][index]
