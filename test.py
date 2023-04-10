from main import convert_size
from main import ShoeSizeCategory, ShoeSizeSystem


def test_should_filter_to_size():
    result = convert_size(
        'shoe_sizes.json',
        size='7.5',
        unit=ShoeSizeCategory.MENS,
        location=ShoeSizeSystem.US_CANADA,
        converted_location=ShoeSizeSystem.EUROPE
        )
    assert result == '40-41'
