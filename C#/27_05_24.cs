/* 7 kyu "List Filtering" by Cmgerber

In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
Example
ListFilterer.GetIntegersFromList(new List<object>(){1, 2, "a", "b", "aasf", "1", "123", 123}) => {1, 2, 231} */

using System.Collections;
using System.Collections.Generic;

public class ListFilterer
{
   public static IEnumerable<int> GetIntegersFromList(List<object> listOfItems)
   {
        List<int> numbersList = new List<int>();
        foreach (object item in listOfItems){
            if (item is int) numbersList.Add((int)item);
        }
        return numbersList;
   }
}
