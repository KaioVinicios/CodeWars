/* 5 kyu "ROT13" by hvaara

How can you tell an extrovert from an introvert at NSA?
   Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.
   
   I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
   According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.
   
   For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.
   
   Test examples:
   
   "EBG13 rknzcyr." -> "ROT13 example." */

using System;

public class Kata
{
    public static string Rot13(string input)
    {
        char[] array = input.ToCharArray();
        for (int c = 0; c < array.Length; c++)
        {
            int number = (int)array[c];
            if (number >= 'a' && number <= 'z')
            {
                if (number <= 'm')
                {
                    number += 13;
                }
                else
                {
                    number -= 13;
                }
            }
            else if (number >= 'A' && number <= 'Z')
            {
                if (number <= 'M')
                {
                    number += 13;
                }
                else
                {
                    number -= 13;
                }
            }

            array[c] = (char)number;
        }
        return new string(array);
    }
}