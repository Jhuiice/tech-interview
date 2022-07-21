# CTCI 7.2 Call-center

# three classes
# respondent
# manager
# director

# a director is a director and a manager and is a respondent
# a manager is a manger and a respondent
# a respondent is a respondent

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


respondent = Respondent("Foo")
manager = Manager("Bar")
director = Director("Baz")

print(respondent.name, manager.name, director.name)
print(respondent.level, manager.level, director.level)
print(respondent.available)
