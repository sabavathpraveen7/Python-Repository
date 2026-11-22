/**
 * Removes duplicate elements while preserving first-seen order.
 * @param {Array} items
 * @returns {Array}
 */
function uniquePreserveOrder(items) {
    if (!Array.isArray(items)) {
        throw new TypeError("Expected an array");
    }
    return [...new Set(items)];
}

/**
 * Counts how many times each element appears in an array.
 * @param {Array} items
 * @returns {Object}
 */
function countFrequencies(items) {
    if (!Array.isArray(items)) {
        throw new TypeError("Expected an array");
    }
    return items.reduce((acc, item) => {
        const key = String(item);
        acc[key] = (acc[key] || 0) + 1;
        return acc;
    }, {});
}

// Example usage:
const tags = ["git", "python", "js", "git", "github", "python", "git"];
console.log("Unique tags:", uniquePreserveOrder(tags));
console.log("Tag frequencies:", countFrequencies(tags));
