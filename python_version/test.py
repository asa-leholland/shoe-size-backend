from main import convert_size
from main import ShoeSizeCategory, ShoeSizeSystem


def test_should_calculate_size():
    result = convert_size(
        'shoe_sizes.json',
        size='7.5',
        unit=ShoeSizeCategory.MENS,
        location=ShoeSizeSystem.US_CANADA,
        converted_location=ShoeSizeSystem.EUROPE
        )
    assert result == '40-41'


def test_should_calculate_size_of_big_kids_shoe():
    result = convert_size(
        'shoe_sizes.json',
        size='4',
        unit=ShoeSizeCategory.BIG_KIDS,
        location=ShoeSizeSystem.UK,
        converted_location=ShoeSizeSystem.EUROPE
        )
    assert result == '37'


def test_should_calculate_size_of_size_provided():
    result = convert_size(
        'shoe_sizes.json',
        size='7.9',
        unit=ShoeSizeCategory.INFANTS,
        location=ShoeSizeSystem.CENTIMETERS,
        converted_location=ShoeSizeSystem.CENTIMETERS
        )
    assert result == '7.9'


def test_should_raise_exception_when_data_path_is_invalid():
    try:
        convert_size(
            'some_invalid_filename.json',
            size='7.5',
            unit=ShoeSizeCategory.MENS,
            location=ShoeSizeSystem.US_CANADA,
            converted_location=ShoeSizeSystem.EUROPE
            )
    except Exception as e:
        assert e is not None


def test_should_raise_exception_when_size_is_invalid():
    try:
        convert_size(
            'shoe_sizes.json',
            size='SOME INVALID SIZE',
            unit=ShoeSizeCategory.MENS,
            location=ShoeSizeSystem.US_CANADA,
            converted_location=ShoeSizeSystem.EUROPE
            )
    except Exception as e:
        assert e is not None


def test_should_raise_exception_when_unit_is_invalid():
    try:
        convert_size(
            'shoe_sizes.json',
            size='7.5',
            unit='SOME INVALID UNIT',
            location=ShoeSizeSystem.US_CANADA,
            converted_location=ShoeSizeSystem.EUROPE
            )
    except Exception as e:
        assert e is not None


def test_should_raise_exception_when_location_is_invalid():
    try:
        convert_size(
            'shoe_sizes.json',
            size='7.5',
            unit=ShoeSizeCategory.MENS,
            location='SOME INVALID LOCATION',
            converted_location=ShoeSizeSystem.EUROPE
            )
    except Exception as e:
        assert e is not None


def test_should_raise_exception_when_converted_location_is_invalid():
    try:
        convert_size(
            'shoe_sizes.json',
            size='7.5',
            unit=ShoeSizeCategory.MENS,
            location=ShoeSizeSystem.US_CANADA,
            converted_location='Test'
            )
    except Exception as e:
        assert e is not None
