# Author: Ashton Lee
# Github User: ashton01L
# Date: 7/25/2024
# Description: Define a class named 'Person' that has two private
# data members - the person's 'name' and 'age'.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age


def std_dev(person_list):
    """
    Calculates the population standard deviation of the ages of Person objects in the list.

    Parameters: person_list A list of Person objects.

    Returns: (float or None) The population standard deviation of the ages, or None if the list is empty.
    """
    if not person_list:
        return None

    ages = [person.get_age() for person in person_list]
    n = len(ages)

    if n == 0:
        return None

    # Calculate mean
    mean_age = sum(ages) / n

    # Calculate variance
    variance = sum((age - mean_age) ** 2 for age in ages) / n

    # Calculate standard deviation using exponentiation
    standard_deviation = variance ** 0.5

    # returns the standard calculated deviation
    return standard_deviation

# Example usage:
# p1 = Person("Kyoungmin", 73)
# p2 = Person("Mercedes", 24)
# p3 = Person("Beatrice", 48)
# person_list = [p1, p2, p3]
# answer = std_dev(person_list)
# print(f"{answer:.5f}");
