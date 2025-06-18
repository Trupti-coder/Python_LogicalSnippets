function findUniqueElements(arr) {
    let xor = 0;
    for (let i = 0; i < arr.length; i++) {
        xor ^= arr[i];
    }

