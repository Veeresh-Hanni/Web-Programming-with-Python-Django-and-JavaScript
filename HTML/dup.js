const removeDuplicates = (array) => {
    const map = new Map();
    array.forEach(item => map.set(item, true));
    return Array.from(map.keys());
};

console.log(removeDuplicates([1, 2, 2, 3, 4, 4])); // Output: [1, 2, 3, 4]
