''' 6 kyu "Turn String Input into Hash" by user4655293
Please write a function that will take a string as input and return a hash. The string will be formatted as such. The key will always be a symbol and the value will always be an integer.
"a=1, b=2, c=3, d=4"

This string should return a hash that looks like
{ 'a': 1, 'b': 2, 'c': 3, 'd': 4} '''

def str_to_hash(st): 
    values = {}
    if st == '':
        return values
    st = st.replace(' ', '').split(',')
    for set in st:
        set = set.split('=')
        if set[0] not in values.keys():
            values[set[0]] = int(set[1])
    return values