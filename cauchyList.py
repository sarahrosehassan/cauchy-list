class CauchyList:
    def __init__(self, p):
    	self.p = p # range of the values
    	self.content = []

    def generate_random(self, n):
        import random
        for integer in range(n):
            self.content.append(random.randrange(0, self.p - 1))

    def length(self):
    	return len(self.content)

    def get(self, i):
        if i < len(self.content):
            return self.content[i]
        return 0

    def __add__(self, other):
        if self.p != other.p:
            raise ValueError('The CauchyLists have different values of p')
        else:
            sum_list = CauchyList(self.p)
            sum_list_length = self.length() if self.length() > other.length() else other.length()

            for i in range (sum_list_length):
                sum_list.content.append((self.get(i) + other.get(i)) % self.p)

            return sum_list

    def __sub__(self, other):
        if self.p != other.p:
            raise ValueError('The CauchyLists have different values of p')
        else:
            difference_list = CauchyList(self.p)
            difference_list_length = self.length() if self.length() > other.length() else other.length()

            for i in range (difference_list_length):
                difference_list.content.append((self.get(i) - other.get(i)) % self.p)

            return difference_list

    def __mul__(self, other):
        if type(other) == int:
            product_list = CauchyList(self.p)

            for num in self.content:
                product_list.content.append((num * other) % self.p)
                
            return product_list

        elif self.p != other.p:
            raise ValueError('The CauchyLists have different values of p')

        else:
            product_list = CauchyList(self.p)
            product_list_length = (self.length() + other.length() - 1)

            for i in range(product_list_length):
                product_list.content.append(0)
                for (index_a, index_b) in zip(range(self.length()), range(i, -1, -1)):
                    product_list.content[i] += (self.get(index_a) * other.get(index_b))
                product_list.content[i] %=  self.p

            return product_list
        
    def __str__(self):
        return f"p: {self.p}\nlength: {self.length()}\ncontent: {self.content}"
