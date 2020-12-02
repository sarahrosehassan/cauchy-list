from assignment3 import *

def readmeTest():
	n = 10
	p = 31
	a = CauchyList(p)
	b = CauchyList(p)
	c = CauchyList(p)
	c.generate_random(n)
	
	a.content = [14, 0, 17, 7, 2, 17, 19, 28, 26, 16]
	b.content = [2, 10, 22, 13, 10, 25, 15, 16, 22, 6, 12, 21, 8, 15, 0 , 21, 1, 2]

	print("===The Original Lists===")
	print(a)
	print(b)
	print()

	print("===The Sum===")
	listSum = a + b
	print(listSum.content)
	print()

	print("===The Difference===")
	listDifference = a - b
	print(listDifference.content)
	print()

	print("===The Product===")
	listProduct = a * b
	print(listProduct.content)
	print()

	print("===The Scalar Product (*2)===")
	scalarProduct = a * 2
	print(scalarProduct.content)
	print()

	print("===Multiple Operations (a + b * 13 + a * c)===")
	multipleOperations = a + b * 13 + a * c
	print(multipleOperations.content)
	print()

if __name__ == "__main__":
    readmeTest()
