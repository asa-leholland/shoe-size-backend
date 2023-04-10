from main import convert_size

import pytest

def test_convert_size():
    result = convert_size('shoe_sizes.json')
    assert len(result) == 5
    for item in result:
        assert "Unit" in item
        assert "US & Canada" in item
        assert "UK" in item
        assert "Europe" in item
        assert "Inches" in item
        assert "Centimeters" in item


def test_should_filter_to_unit():
    result = convert_size('shoe_sizes.json', gender="Women's",)
    assert len(result) == 1
    assert result[0]["Unit"] == "Women's"

