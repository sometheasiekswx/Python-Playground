# Use special methods to compare objects to each other


class Employee():
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsService

    # TODO: implement comparison functions by emp level
    def __ge__(self, other):
        return self.level >= other.level

    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        else:
            return self.level > other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        else:
            return self.level < other.level

    def __le__(self, other):
        return self.level <= other.level

    def __eq__(self, other):
        pass


def main():
    # define some employees
    dept = [Employee("Somethea", "Siek", 6, 1),
            Employee("Tim", "Sims", 5, 9),
            Employee("John", "Doe", 4, 12),
            Employee("Jane", "Smith", 6, 6),
            Employee("Rebecca", "Robinson", 5, 13),
            Employee("Tyler", "Durden", 5, 12)]

    # TODO: Who's more senior?
    print(dept[0] > dept[1])
    print(dept[0] <= dept[2])
    print(dept[-2] >= dept[-1])
    print(dept[-2] > dept[-1])

    # TODO: sort the items
    dept = sorted(dept, reverse=True)
    for d in dept:
        print(f'{d.fname} {d.lname}')


if __name__ == "__main__":
    main()
