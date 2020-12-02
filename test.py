from assignment3 import *

# This is the code my project was tested with for the correct output
def test():
    n = 10 # length of list
    p = 31 # range of values
    for i in range(n):
        a = CauchyList(p)
        a.generate_random(n)
        b = CauchyList(p)
        b.generate_random(n)
        c = CauchyList(p)
        c.generate_random(n)
        print(a + b * 13 + a * c)


    print("=====================================")

    a = CauchyList(p)
    b = CauchyList(2 * p)
    try:
        print(a * b)
    except ValueError as ve:
        print(ve)

    print("=====================================")

    a = CauchyList(p)
    a.generate_random(n)
    b = CauchyList(p)
    b.generate_random(2 * n - 2)
    c = a + b
    print(a)
    print(b)
    print(c)



if __name__ == "__main__":
    test()
