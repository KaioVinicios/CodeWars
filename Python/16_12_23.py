# 8kyu 'Enumerable Magic #25 - Take the First N Elements'
# Create a function that accepts a list/array and a number n, and returns a list/array of the first n elements from the list/array.

def take(arr,n):
    pass
    l = []
    for c in range(0, n, 1):
        if n > len(arr):
            return arr 
        l.append(arr[c])
    return l
    