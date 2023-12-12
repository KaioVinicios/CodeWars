# 8 kyu 'Beginner Series #2 Clock' by Vortus
# Your task is to write a function which returns the time since midnight in milliseconds.

def past(h, m, s):
    # Good Luck!
    h *= 3600000
    m *= 60000
    s *= 1000

    t = h + m + s
    return (t)
