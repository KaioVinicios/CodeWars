/* 6 kyu "Pyramid Array" by Sahglie

Write a function that when given a number >= 0, returns an Array of ascending length subarrays.

pyramid(0) => [ ]
pyramid(1) => [ [1] ]
pyramid(2) => [ [1], [1, 1] ]
pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]
Note: the subarrays should be filled with 1s */

using System;
using System.Collections.Generic;

public class Kata {
  public static int[][] Pyramid(int n) {
    int[][] result = new int[n][];
    for(int i = 0; i < n; i++) {
        List<int> list = new List<int>();
        for(int j = 0; j <= i; j++) {
            list.Add(1);
        }
        result[i] = list.ToArray();
    }
    return result;
  }
}
