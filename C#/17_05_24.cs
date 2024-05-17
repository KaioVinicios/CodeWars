/* 6 kyu "Create Phone Number" by xDranik

Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
Kata.CreatePhoneNumber(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}) // => returns "(123) 456-7890" */

public class Kata
{
  public static string CreatePhoneNumber(int[] numbers)
  {
    if(numbers.Length != 10){
      throw new ArgumentException("The list of numbers must have exactly 10 integers"); 
    }
    foreach (int number in numbers)
        {
            if (number < 0 || number > 9)
            {
                throw new ArgumentException("All numbers in the array must be integers between 0 and 9.");
            }
        }
    return $"({numbers[0]}{numbers[1]}{numbers[2]}) {numbers[3]}{numbers[4]}{numbers[5]}-{numbers[6]}{numbers[7]}{numbers[8]}{numbers[9]}";
  }
}
