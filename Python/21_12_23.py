# 7 kyu 'Quicksum' by wilsoncastiblanco
'''A checksum is an algorithm that scans a packet of data and returns a single number. The idea is that if the packet is changed, the checksum will also change, so checksums are often used for detecting transmission errors, validating document contents, and in many other situations where it is necessary to detect undesirable changes in data.

For this problem, you will implement a checksum algorithm called Quicksum. A Quicksum packet allows only uppercase letters and spaces. It always begins and ends with an uppercase letter.

Otherwise, spaces and uppercase letters can occur in any combination, including consecutive spaces.

A Quicksum is the sum of the products of each characters position in the packet times the characters value. A space has a value of zero, while letters have a value equal to their position in the alphabet.

So, A = 1, B = 2, etc., through Z = 26. Here are example Quicksum calculations for the packets "ACM" and "A C M":

ACM
1 * 1 + 2 * 3 + 3 * 13 = 46 

A C M
1 * 1 + 3 * 3 + 5 * 13 = 75
When the packet doesn't have only uppercase letters and spaces or just spaces the result to quicksum have to be zero (0).

AbqTH #5 = 0'''

def quicksum(packet):
    pass
    data = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    value = []
    position = []
    result = 0
    for n in range(0, len(packet)): 
        if packet[n] == ' ':
            position.append(n + 1)
            value.append(0)
        elif packet[n] in data:
            value.append(data.find(packet[n]))
            position.append(n + 1)
            result += (position[n] * value[n])
        else:
            return 0
    return result 
