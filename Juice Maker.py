#The program enables adding of two Juice objects, resulting in a new Juice object with the combined capacity and names of the two juices being added.
class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')

    def __add__(self,other):
        new_name = self.name+"&"+other.name
        new_capacity = self.capacity+other.capacity
        return Juice(new_name,new_capacity)
a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)
