/* 7 kyu "Square Every Digit" by MysteriousMagenta
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81) */

function squareDigits(num){
    num = num.toString();
    let result = "";
    for(let cont = 0; cont < num.length; cont++ ){
        console.log(Number(num[cont]));
        result += (Number(num[cont]) ** 2).toString();
    }
    return Number(result);
}
