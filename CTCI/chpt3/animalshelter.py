from collections import deque

# this is a queue question
# there will be a dogs queue and a cats queue


class Animal():
    def __init__(self, type="Dog", age=0):
        self.type = type
        self.age = age
    #     self.order = order

    # def isOlderThan(self, animal):
    #     return self.order < animal.getOrder()

    # def getOrder(self):
    #     return self.order
    # def setOrder(self, order):
    #     self.order = order


class AnimalShelter():
    def __init__(self, animals=[]):
        self.animals = deque(animals)

    def enequeue(self, animal):
        self.animals.appendleft(animal)

    def dequeueDog(self):
        return self.dequeueSpecific("Dog")

    def dequeueCat(self):
        return self.dequeueSpecific("Cat")

    def dequeueSpecific(self, choice):
        temp_list = []
        temp_animal = Animal()
        for _ in range(len(self.animals)):
            temp_animal = self.animals.pop()
            if temp_animal.type == choice:
                for i in range(len(temp_list) - 1, 0, -1):
                    self.animals.append(temp_list[i])
                # print(temp_animal)
                return temp_animal
            temp_list.append(temp_animal)

        for j in range(0, len(temp_list) - 1, -1):
            self.animals.append(temp_list[j])

        return False

    def dequeueAny(self):
        return self.animals.pop()

    def show_queue(self):
        return self.animals


bob = Animal("Dog", 2)
# mary = Animal("Cat", 3)
# alex = Animal("Dog", 4)
# stephania = Animal("Cat", 5)
# roy = Animal("Dog", 6)

# when the deque is popped it removes the element
animals = deque([bob])  # , mary, alex, stephania, roy])
shelter = AnimalShelter(animals)

print(shelter.show_queue())
print(shelter.dequeueDog())
shelter.enequeue(Animal("Cat", 12))
print(shelter.show_queue())
