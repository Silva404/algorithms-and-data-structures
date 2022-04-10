function insert_sort(list: number[]): number[] {
    for (let j = 1; j < list.length; j++) {
        const key = list[j];
        let preKey = j - 1;

        while (preKey >= 0 && list[preKey] > key) {
            list[preKey + 1] = list[preKey];
            preKey -= 1;
            list[preKey + 1] = key;
        }
    }
    return list;
}

// 2.1-1
// Using Figure 2.2 as a model, illustrate the operation of INSERTION-SORT on the
// array A D h31; 41; 59; 26; 41; 58i.

const input = [31, 41, 59, 26, 41, 58];
// console.log(input, 'unsorted list');
// console.log(insert_sort(input), 'sorted list');


// 2.1-2
// Rewrite the INSERTION-SORT procedure to sort into nonincreasing
//  instead of nondecreasing order.
function insert_sort_descrising(list: number[]): number[] {
    for (let j = 1; j < list.length; j++) {
        let key = list[j];
        let preKey = j - 1;

        console.log('interaction', j, list);
        while (preKey >= 0 && list[preKey] < key) {
            list[preKey + 1] = list[preKey];
            preKey -= 1;
            list[preKey + 1] = key;
        }
    }
    return list;
}

const input2 = Array.from({length: 6}, () => Math.floor(Math.random() * 1000));

insert_sort_descrising(input2);
console.log(input2, 'unsorted list');
console.log(insert_sort(input2), 'sorted list');