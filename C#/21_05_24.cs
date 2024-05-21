/* 6 kyu "Build Tower" by 8fdafs2
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.
For example, a tower with 3 floors looks like this:
[
  "  *  ",
  " *** ", 
  "*****"
] */

using System;

public class Kata
{
  public static string[] TowerBuilder(int nFloors)
  {
    string[] result = new string[nFloors];
    int baseWidth = (2 * nFloors) - 1;
    
    for (int i = 0; i < nFloors; i++)
    {
      int elements = 2 * i + 1;
      int spaces = (baseWidth - elements) / 2;
      
      string row = new string(' ', spaces) + new string('*', elements) + new string(' ', spaces);
      result[i] = row;
    }
    
    return result;
  }
}
