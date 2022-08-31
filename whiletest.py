'''
    Test code for matrix calculation
    Date: 30-8-22
'''

def whileTest():
    limit = 100
    # While Loop
    while(limit):
        limit -= 1
        if limit % 2:   # Skip Odd numbers
            continue
        print(limit+2)
    return None


def test1():
    for i in range(5):
        print(i+6)
