# 1
print("numbers 12-24:", end=" ")
for i in range(12, 24):
    print(i, end=" ")
print()

# 2
print("numbers 17-31 odds only:", end=" ")
for i in range(17, 31 + 2, 2):
    print(i, end=" ")
print()

# 3
print("numbers 10-(-20) even only:", end=" ")
for i in range(10, -20 - 2, -2):
    print(i, end=" ")
print()

# 4
print("numbers 1-45 Fizz/Bizz/FizzBizz:", end=" ")
for i in range(1, 45):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}:FizzBizz", end=" ")
    elif i % 5 == 0:
        print(f"{i}:Bizz", end=" ")
    elif i % 3 == 0:
        print(f"{i}:Fizz", end=" ")
print()


# 5

def sum_list(l1: list[int]) -> int:
    result: int = 0
    for x in l1:
        result += x
    return result


print("sum of list:", sum_list([1, 13, 22, 123, 49, 34, 5, 24, 57, 45]))

# 6
students_example = [
    {"id": 222,
     "first_name": "shani",
     "last_name": "chasty",
     "age": 76,
     "country": "spain"
     }, {"id": 875,
         "first_name": "Davnu",
         "last_name": "kap",
         "age": 13,
         "country": "USA",
         "city": "milkway"
         }
]


def delete_student_property(students: list[any], student_property: str) -> None:
    for student in students:
        if student_property in list(student.keys()):
            del student[student_property]


delete_student_property(students_example, "city")
print(students_example)


def get_student_properties(students: list[any]):
    for student in students:
        print("student's properties:", list(student.keys()))


get_student_properties(students_example)


def sort_student_by_age(students: list[dict[str, str | int]]) -> list[any]:
    return sorted(students, key=lambda student: student["age"])


print(sort_student_by_age(students_example))

# 7
our_pets = [
    {
        "animal_type": "cat",
        "names": ["Meowzer", "Fluffy", "Kit-Cat"]
    },
    {
        "animal_type": "dog",
        "names": ["Spot", "Bowser", "Frankie"]
    }
]


def cats_animal_type(pets: list[dict[str, str | list[str]]]):
    for pet in pets:
        if pet["animal_type"].lower() == "cat":
            print(f"animalType: {pet["animal_type"].lower()}.")


cats_animal_type(our_pets)


def animal_names_by_type(pets: list[dict[str, str | list[str]]], animal_type: str):
    for pet in pets:
        if pet["animal_type"].lower() == animal_type:
            print(f"for animal type '{animal_type}', the pets name were: {pet["names"]}.")


animal_names_by_type(our_pets, "dog")


def add_animal_name(pets: list[dict[str, str | list[str]]], animal_name: str):
    add_name: str = animal_name.capitalize()
    for pet in pets:
        if not add_name in pet["names"]:
            pet["names"].append(add_name)


add_animal_name(our_pets, "sikipy")
add_animal_name(our_pets, "Frankie")
print(our_pets)


# challenge:
def plusOne(digits: list[int]) -> list[int]:
    remains = None
    for i in range(len(digits) - 1, -1, -1):
        if remains:
            value = digits[i] + remains
        else:
            value = digits[i]
            value += 1
        if value < 10:
            digits[i] = value
            return digits
        digits[i] = value % 10
        remains = int(value / 10)
        continue
    if remains:
        digits.insert(0, 1)
    return digits


print(plusOne([9]))
print(plusOne([1, 2, 3]))
print(plusOne([4, 3, 2, 1]))
print(plusOne([1, 9, 9]))
print(plusOne([9, 9, 9]))
