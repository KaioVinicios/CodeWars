// 8 kyu 'Sum Arrays' by Richardhsu.
// Objective: take an array of numbers and add them.

// Sum Numbers
function sum (numbers) {
    if (numbers == false) {
        return 0 
    }
    let cont = 0
    let result = 0
    while (cont < numbers.length) {
        result += numbers[cont]
        cont += 1
    }
    return result
};