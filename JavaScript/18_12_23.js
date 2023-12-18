// 8 kyu 'Reversed Strings' by Jhoffner.
/* Complete the solution so that it reverses the string passed into it.
'world'  =>  'dlrow'
'word'   =>  'drow' */

function solution(str) {
    let result = '';
    for (let n = str.length  - 1; n >= 0; n--) {
        result += str[n];
    }
    return result;
  }
  