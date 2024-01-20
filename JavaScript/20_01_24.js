/*8 kyu "Find the smallest integer in the array" by Dukeofgarda 
Given an array of integers your solution should find the smallest integer.*/

class SmallestIntegerFinder {
    findSmallestInt(args) {
        // return Math.min(...args)
        let result = args[0]
      for (let num of args) {
        if (num < result) {
            result = num
        }
      }
      return result
    }
  }