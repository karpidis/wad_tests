"""Create class 'Person' with 2 properties: name and age."""
import random

name_list = ["Angel", "Vanessa", "Georgia", "Konstantinos", "Wadim", "Stavros", "Yannis",
                                                                                "Victoria", "Ioanna"]


class Person:
    def __init__(self, name="", age=""):
        """

        :type age: int
        """
        self.name = name
        self.age = age
        pass


def main():
    person1 = Person(random.choice(name_list), random.randint(10, 81))
    print(person1.name, person1.age)
    person2 = Person(random.choice(name_list), random.randint(10, 81))
    print(person2.name, person2.age)
    person3 = Person(random.choice(name_list), random.randint(10, 81))
    print(person3.name, person3.age)
    person4 = Person(random.choice(name_list), random.randint(10, 81))
    print(person4.name, person4.age)
    person5 = Person(random.choice(name_list), random.randint(10, 81))
    print(person5.name, person5.age)
    people = [person1, person2, person3, person4, person5]
    print(person_older_than(people, 30))


def person_older_than(person_list, minimum_age):
    older_than = []
    for human_person in person_list:
        if human_person.age > minimum_age:
            older_than.append(human_person.name)
    return older_than


if __name__ == "__main__":
    main()
