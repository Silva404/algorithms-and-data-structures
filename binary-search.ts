function binary_search_iterative(array: number[], item: number): boolean {
    let left = 0;
    let right = array.length - 1;

    while (left <= right) {
        const mid = (right - left) / 2;
        if (array[mid] === item) {
            return true
        } else if (item < array[mid]) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }


    return false;
}

function binary_search_recursive(array: number[], item: number, left: number, right: number): boolean {
    if (left > right) {
        return false;
    }

    const mid = (right - left) / 2;
    if (array[mid] === item) {
        return true
    } else if (item < array[mid]) {
        return binary_search_recursive(array, item, left, mid - 1);
    } else {
        return binary_search_recursive(array, item, mid + 1, right);
    }
}

const input2 = Array.from({length: 6}, () => Math.floor(Math.random() * 1000));
console.log(input2, 'unsorted list');
console.log(binary_search_recursive(input2, 2, 0, input2.length - 1), 'sorted list');