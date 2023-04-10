const { convertSize, ShoeSizeCategory, ShoeSizeSystem } = require('./main');



test('should calculate size', () => {
    console.log(ShoeSizeCategory);
    console.log(ShoeSizeSystem);
  const result = convertSize(
    'shoe_sizes.json',
    ShoeSizeCategory.MENS,
    '7.5',
    ShoeSizeSystem.US_CANADA,
    ShoeSizeSystem.EUROPE
  );
  expect(result).toBe('40-41');
});

test('should calculate size of big kids shoe', () => {
  const result = convertSize(
    'shoe_sizes.json',
    ShoeSizeCategory.BIG_KIDS,
    '4',
    ShoeSizeSystem.UK,
    ShoeSizeSystem.EUROPE
  );
  expect(result).toBe('37');
});

test('should calculate size of provided size', () => {
  const result = convertSize(
    'shoe_sizes.json',
    ShoeSizeCategory.INFANTS,
    '7.9',
    ShoeSizeSystem.CENTIMETERS,
    ShoeSizeSystem.CENTIMETERS
  );
  expect(result).toBe('7.9');
});

test('should raise exception when data path is invalid', () => {
  expect(() => {
    convertSize(
      'some_invalid_filename.json',
      ShoeSizeCategory.MENS,
      '7.5',
      ShoeSizeSystem.US_CANADA,
      ShoeSizeSystem.EUROPE
    );
  }).toThrow();
});

test('should raise exception when size is invalid', () => {
  expect(() => {
    convertSize(
      'shoe_sizes.json',
      ShoeSizeCategory.MENS,
      'SOME INVALID SIZE',
      ShoeSizeSystem.US_CANADA,
      ShoeSizeSystem.EUROPE
    );
  }).toThrow();
});

test('should raise exception when unit is invalid', () => {
  expect(() => {
    convertSize(
      'shoe_sizes.json',
      'SOME INVALID UNIT',
      '7.5',
      ShoeSizeSystem.US_CANADA,
      ShoeSizeSystem.EUROPE
    );
  }).toThrow();
});

test('should raise exception when location is invalid', () => {
  expect(() => {
    convertSize(
      'shoe_sizes.json',
      '7.5',
      ShoeSizeCategory.MENS,
      'SOME INVALID LOCATION',
      ShoeSizeSystem.EUROPE
    );
  }).toThrow();
});

test('should raise exception when converted location is invalid', () => {
  expect(() => {
    convertSize(
      'shoe_sizes.json',
      '7.5',
      ShoeSizeCategory.MENS,
      ShoeSizeSystem.US_CANADA,
      'Test'
    );
  }).toThrow();
});