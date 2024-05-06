/* 7 kyu "Is this a triangle?" by silentZaika

Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case. */
public class Triangle
{
    public static bool IsTriangle(int a, int b, int c)
    {
        if (a + b > c && a + c > b && b + c > a) {
            return true;
        }
        return false;
    }
}
