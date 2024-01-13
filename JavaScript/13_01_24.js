/*8 kyu "Square(n) Sum" by jhoffner
Complete the square sum function so that it squares each number passed into it and then sums the results together.*/

function squareSum(numbers){
    let result = 0
    for (let n of numbers){
      result += n*n
    }
    return result
}
