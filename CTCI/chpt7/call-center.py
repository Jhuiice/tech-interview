# CTCI 7.2 Call-center

# three classes
# respondent
# manager
# director

# a director is a director and a manager and is a respondent
# a manager is a manger and a respondent
# a respondent is a respondent
# ? how does a call center work
# ? What do they have to keep track of?
# ? Who is in what rolls?

# * From looking at the solution i saw that calls in need to be handled by a queue
# * The team needs to work as a stack with the respondents at the top of the stack,
# * managers in the middle, and directors in the end
# * Each employee type is its own class that inherits the basic cemployee of credentials
# * the levels are assigned upon the class they are located. 3 classes for three different types of employees
# ? Would there be one source of data authentication here? One on the emplyee level and one that checks the
# ? employees level to promote them?
# * classes are as followed, CallHandler to handle levels of employees, queues of calls, dispatchCall, getHandlerForCall
# ! remember everything can be broken in to bite sized chunks
# * The next class is call, Rank of call, Person who is calling, employee who is calling, public call with methods
# * of reply, getRank, setRank, incrementRank, Disconnect.
# NOTE every call is its own object to be handled that is part of the bigger picture. It is created with every call
# * The next call is employee, it check if the current call is happening and the rank of the employee.
# * it has actions fo receive call, call completed, escalate and reassign, assign new call, is free
# * Then three subclasses of types of employees as the respondent, manager, and director.

# ? Can this be practice for systems designs?

class Employee():
    def __init__(self, name, lvl):
        self.name = name
        self.level = 1 if lvl == 1 else 2 or 3 if lvl == 3 else None
        self.available = True


class Respondent(Employee):
    def __init__(self, name):
        super().__init__(name, 1)


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 2)


class Director(Employee):
    def __init__(self, name):
        super().__init__(name, 3)


class CallCenter():
    def __init__(self):
        self.employees = []
        self.respondents = []
        self.managers = []
        self.directors = []

    def add_employee(self, type):
        self.employees.append(type)
        self.respondents.append(type)
        self.managers.append(type)
        self.directors.append(type)

    def dispatchCall(self):
        # brute force will be O(r + m + d)
        # this will keep the callers in order
        employees = self.respondents.concat(self.managers, self.directors)
        canHandle = 3 | 2 | 1
        callIsActive = False
        for i in range(len(self.respondents)):
            if employees[i].available:
                print(
                    f"{employees[i].name}, a level {employees[i].level}, has taken call")
                callIsActive = True
                break

        while callIsActive:
            # there would be a randomizer in here and the call would be delayed an x amount of time to handle the call
            # if the call escalates than the call would be handed off to the manager
            # if the manager could not handle it than the call would be handed off to the director.
            # end call when theyre done

            # how would I handle the call? The call will always go though the respondent before it can be given to the manager

            # respondent = Respondent("Foo")/
            # manager = Manager("Bar")
            # director = Director("Baz")

            # print(respondent.name, manager.name, director.name)
            # print(respondent.level, manager.level, director.level)
            # print(respondent.available)
