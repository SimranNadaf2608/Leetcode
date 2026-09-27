/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const result = {};
    
    for (const item of this) {
        const key = fn(item);
        
        // If the key doesn't exist yet, initialize it with an empty array
        if (result[key] === undefined) {
            result[key] = [];
        }
        
        // Push the current item into its matching group array
        result[key].push(item);
    }
    
    return result;
};

/**
 * Example usage:
 * const array = [{"id":"1"}, {"id":"1"}, {"id":"2"}];
 * const fn = function (item) { return item.id; };
 * array.groupBy(fn); 
 * // Output: { "1": [{"id": "1"}, {"id": "1"}], "2": [{"id": "2"}] }
 */
