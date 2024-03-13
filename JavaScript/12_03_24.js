/* 7 kyu "Remove the minimum" by Bkaes
Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with the lowest index. If you get an empty array/list, return an empty array/list.
Don't change the order of the elements that are left. 

Ex: 
Input: [5,3,2,1,4], output = [5,3,2,4] 
*/

function removeSmallest(numbers) {
    if (!numbers.length) return [];
   
    let minNumber = numbers[0];
    let minIndex = 0; 
    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] < minNumber) {
            minNumber = numbers[i];
            minIndex = i;
        }
    }
  
    let result = numbers.slice();
    result.splice(minIndex, 1);
    return result;
}