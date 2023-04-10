const ShoeSizeCategory = Object.freeze({
    WOMENS: "Women's",
    MENS: "Men's",
    BIG_KIDS: "Big Kids' (7–12 Years)",
    LITTLE_KIDS: "Little Kids' (4–7 Years)",
    TODDLERS: "Toddlers' (9 Months - 4 Years)",
    INFANTS: "Infants' (0–9 Months)"
});

const ShoeSizeSystem = Object.freeze({
    US_CANADA: "US & Canada",
    UK: "UK",
    EUROPE: "Europe",
    INCHES: "Inches",
    CENTIMETERS: "Centimeters"
});

function convertSize(dataPath, unit, size, location, convertedLocation) {
    if (!Object.values(ShoeSizeCategory).includes(unit)) throw new Error(`Invalid unit ${unit}`);
    if (!Object.values(ShoeSizeSystem).includes(location)) throw new Error(`Invalid location ${location}`);
    if (!Object.values(ShoeSizeSystem).includes(convertedLocation)) throw new Error(`Invalid convertedLocation ${convertedLocation}`);
    if (!dataPath || !dataPath.endsWith(".json")) throw new Error(`Invalid dataPath ${dataPath}`);
    if (!size || typeof size !== 'string') throw new Error(`Invalid size ${size}`);


    const path = require('path');
    const data = require(path.join(__dirname, dataPath));

    for (const item of data) {
        if (item.Unit.slice(0, 8) === unit.slice(0, 8)) {
            const index = item[location].indexOf(size);
            if (index === -1) throw new Error(`Invalid size ${size}`);
            return item[convertedLocation][index];
        }
    }
    throw new Error(`Invalid unit ${unit}`);
}



module.exports = {
    ShoeSizeCategory,
    ShoeSizeSystem,
    convertSize
};