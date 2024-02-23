''' 6 kyu "Find The Parity Outlier" by Obnounce

You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
'''

def find_outlier(integers):
    even = []
    odd = []
    for n in integers:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
    if len(even) > 1:
        return odd[0]
    else:
        return even[0]
