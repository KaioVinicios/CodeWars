/* 7 kyu "Especially Joyful Numbers" by Abelard_Snazz 
Positive integers that are divisible exactly by the sum of their digits are called Harshad numbers.
We are interested in Harshad numbers where the product of its digit sum s and s with the digits reversed, gives the original number n. For example consider number 1729:
its digit sum, s = 1 + 7 + 2 + 9 = 19
reversing s = 91
and 19 * 91 = 1729 --> the number that we started with.
Complete the function which tests if a positive integer n is Harshad number, and returns True if the product of its digit sum and its digit sum reversed equals n; otherwise return False. */

function numberJoy(n) {
    let sum = 0
    let numberStr = String(n)
    for(let c = 0; c < numberStr.length; c++){
        sum += Number(numberStr[c])
    }
    let somaReversa = parseInt(sum.toString().split('').reverse().join(''));
    if(sum * somaReversa == n){
        return true
    }
    else {
        return false
    }
}
