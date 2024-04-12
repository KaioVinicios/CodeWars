''' 5 kyu "Human Readable Time" by BattleRattle
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)'''

def make_readable(seconds):
    hours = seconds // 3600
    seconds -= 3600 * hours
    min = seconds // 60
    seconds -= 60 * min
    return f"{hours:02d}:{min:02d}:{seconds:02d}"
