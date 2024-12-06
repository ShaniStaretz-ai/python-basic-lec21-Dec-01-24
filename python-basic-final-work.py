# 1
print("1.numbers 12-24:", end=" ")
for i in range(12, 24):
    print(i, end=" ")
print()

# 2
print("2.numbers 17-31 odds only:", end=" ")
for i in range(17, 31 + 2, 2):
    print(i, end=" ")
print()

# 3
print("3.numbers 10-(-20) even only:", end=" ")
for i in range(10, -20 - 2, -2):
    print(i, end=" ")
print()

# 4
print("4.numbers 1-45 Fizz/Bizz/FizzBizz:", end=" ")
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


list_sum = [1, 13, 22, 123, 49, 34, 5, 24, 57, 45]
print(f"5.sum of list {list_sum}:", sum_list(list_sum))

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


print("6.origin students example:")
print(students_example)

delete_student_property(students_example, "city")
print(f"6.1.after delete 'city' property: {students_example}")


def get_student_properties(students: list[any]) -> None:
    for student_index, student in enumerate(students):
        print(f"for student #{student_index + 1}:student's properties are: {list(student.keys())}")


def get_student_details(students: list[any]) -> None:
    for student_index, student in enumerate(students):
        print(f"for student #{student_index + 1}:")
        for key, value in student.items():
            print(f"{' '.join(key.split("_"))}:{value}")


print("6.2 student properties, no values:")
get_student_properties(students_example)
print("6.2 student properties, with values:")
get_student_details(students_example)


def sort_student_by_age(students: list[dict[str, str | int]]) -> list[any]:
    return sorted(students, reverse=True, key=lambda student: student["age"])


print("6.3. sort students by age old to young", sort_student_by_age(students_example))

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
            print(f"{pet}")


print("7.1 print the pet properties only if the type is 'cat': ")
cats_animal_type(our_pets)


def animal_names_by_type(pets: list[dict[str, str | list[str]]], animal_type: str):
    for pet in pets:
        if pet["animal_type"].lower() == animal_type:
            print(f"for animal type '{animal_type}', the pets name were: {pet["names"]}.")


print("7.2 print the pet properties only if the type is 'dog': ")
animal_names_by_type(our_pets, "dog")


def add_animal_name(pets: list[dict[str, str | list[str]]], animal_name: str):
    add_name: str = animal_name.capitalize()
    for pet in pets:
        if not add_name in pet["names"]:
            pet["names"].append(add_name)


print("7.3 added name of pets if not exist: ")
add_animal_name(our_pets, "sikipy")
add_animal_name(our_pets, "Frankie")
print(our_pets)

# 8

student_example = {
    'name': 'John',
    'age': 20,
    'hobbies': ['reading', 'games', 'coding'],
}


# 8.1
def student_print(student_1: dict[str, str | int]) -> None:
    print("\033[1;92mstudent details:\033[0m")

    for key, value in student_1.items():
        print(f"{' '.join(key.split("_"))}: {value}")


print("8.1.start student details:")
student_print(student_example)


# 2
def add_hobby(student_1: dict[str, str | list[str] | int], hobby: str) -> None:
    if not hobby in student_1['hobbies']:
        student_1['hobbies'].append(hobby)


add_hobby(student_example, "paint")

# 3
print("8.2-3.after added 'paint' to hobbies")
student_print(student_example)


# 4
def delete_hobby(student_1: dict[str, str | list[str] | int], hobby: str) -> dict[str, str | list[str] | int]:
    student_1_copy = student_1.copy()
    if hobby in student_1['hobbies']:
        student_1_copy['hobbies'].remove(hobby)
    return student_1_copy


student = delete_hobby(student_example, 'games')
# 5
print("8.4-5.after deleted 'games' from hobbies:")
student_print(student)


# 6
def add_student_family_name(student_1: dict[str, str | list[str] | int], property_value: str) -> None:
    student_1['family_name'] = property_value.capitalize()


add_student_family_name(student, 'staretz')
print("8.6.after adding 'family_name' property:")
student_print(student)

# 9

matrix: list[list[int]] = [
    [1, 2],
    [3, 4],
    [5, 6]
]


def print_matrix(mat: list[list[int]]) -> None:
    for row in mat:
        for col in row:
            print(col, end=" ")
    print()


print("9.print matrix values:")
print_matrix(matrix)

# 10
matrix2: list[list[0 | 1]] = [[0, 1, 1], [0, 1, 0], [1, 0, 0]]


def zero_count(mat: list[list[int]]) -> int:
    count: int = 0
    for row in mat:
        for col in row:
            if not col:
                count += 1
    return count


print(f"10. in {matrix2} you have :{zero_count(matrix2)} zeros")


# 11
def find_dup(l1: list[int]) -> list[int]:
    dic1: dict[int, int] = {}
    result = []
    for x in l1:
        if dic1.get(x):
            dic1[x] += 1
        else:
            dic1[x] = 1
    for key, value in dic1.items():
        if value > 1:
            result.append(key)
    return result


l2: list[int] = [4, 2, 34, 4, 1, 12, 1, 4]
print(f"11.{find_dup(l2)} are the duplicate of {l2}")


# 12
def reverse_list(l2_input: list[any]) -> list[any]:
    return [l2_input[i] for i in range(len(l2_input) - 1, -1, -1)]


arr: list[any] = [43, "what", 9, True, "cannot", False, "be", 3, True];
print("12. before reverse list", arr)
print("after reverse list", reverse_list(arr))


# 13
def sum_values(l1, l2_input) -> list[int]:
    return [l1[i] + l2_input[i] for i in range(len(l1))]


first_array: list[int] = [4, 6, 7];
second_array: list[int] = [8, 1, 9];
print(
    f"13.the sum values by index of the lists {first_array} and {second_array} are {sum_values(first_array, second_array)}")


# 14
def is_polindrom(str1):
    return str1 == str1[::-1]


def is_two_polindroms(st1, st2):
    print(f"{is_polindrom(st1)}:for '{st1}'")
    print(f"{is_polindrom(st2)}:for '{st2}'")


first_str = "racecar"
second_str = "Java"
print(f"14.check if {first_str} and {second_str} are polindroms:")
is_two_polindroms(first_str, second_str)


# 15
def print_nums_mul_by_2() -> None:
    counter = 1
    while counter < 100:
        print(counter, end=" ")
        counter *= 2
    print()


print("15.print nums mul by 2 from 1 to 100(not include)")
print_nums_mul_by_2()


# 16
def print_nums_div_by_2() -> None:
    counter = 900000
    while counter > 50:
        print(counter, end=" ")
        counter /= 2
    print()


print("16.print nums div by 2 from 900000 to 50 (not include)")
print_nums_div_by_2()


# aid function for questions 17-19
def build_dict_for_string_list(l1: list[str]) -> dict[str, int]:
    dic1: dict[str, int] = {}

    i: int = 0
    while i < len(l1):
        x = l1[i]
        if dic1.get(x):
            dic1[x] += 1
        else:
            dic1[x] = 1
        i += 1
    return dic1


# 17
def duplicate_strings(l1: list[str]) -> list[str]:
    dic1: dict[str, int] = build_dict_for_string_list(l1)
    result: list[str] = []
    i: int = 0
    keys: list[str] = list(dic1.keys())
    while i < len(keys):
        k = keys[i]
        if dic1.get(k) > 1:
            result.append(k)
        i += 1
    return result


tested_dup_list = ["ssss", "2", "ssss", "pete", "Sss", "2", "aba", "a", "aa"]
print("origin list:", tested_dup_list)
print("17.the duplicate strings in the origin list are:",
      duplicate_strings(["ssss", "2", "ssss", "Sss", "2", "aba", "a", "aa"]))


# 18
def remove_string_duplicate(l1: list[str]):
    dict1: dict[str, int] = build_dict_for_string_list(l1)
    result: list[str] = []
    i: int = 0
    keys: list[str] = list(dict1.keys())
    while i < len(keys):
        k = keys[i]
        value = dict1.get(k)
        if value == 1:
            result.append(k)
        i += 1
    return result


print("18.the unique strings from the origin list:", remove_string_duplicate(tested_dup_list))


# 19
def remove_string_duplicate_without_pete(l1: list[str]):
    dict1: dict[str, int] = build_dict_for_string_list(l1)
    result: list[str] = []
    i: int = 0
    keys: list[str] = list(dict1.keys())
    while i < len(keys):
        k = keys[i]
        if k == "pete":
            i += 1
            continue
        value = dict1.get(k)
        if value == 1:
            result.append(k)
        i += 1
    return result


print("19.the unique strings from the origin list WITHOUT 'pete':",
      remove_string_duplicate_without_pete(tested_dup_list))


# 20
def get_index_of_first_duplicate_booleans(l1: list[bool]) -> int:
    index: int = 1
    while index < len(l1):
        if l1[index] == l1[index - 1]:
            return index
        index += 1
    return -1


print("20.find the first pair in boolean lists: ")
bool1 = [True, False, False, True, True, False]

result_bool1 = get_index_of_first_duplicate_booleans(bool1)
print(f"the first pair is in index {result_bool1}" if result_bool1 != -1 else "no boolean", f"in the list:{bool1}")

bool2 = [True, False, True, False, True, True];
result_bool2 = get_index_of_first_duplicate_booleans(bool2)
print(f"the first pair is in index {result_bool2}" if result_bool2 != -1 else "no boolean", f"in the list:{bool2}")

bool3 = [True, False, True, False, True, False];
result_bool3 = get_index_of_first_duplicate_booleans(bool3)
print(f"the first pair is in index {result_bool3}" if result_bool3 != -1 else "no boolean", f"in the list:{bool3}")


# 21

def validate_full_name(full_name_input: str) -> bool:
    return type(full_name_input) == str and len(full_name_input.split()) == 2


def validate_age(age_input: str) -> bool:
    try:
        return type(int(age_input)) == int and 1 < int(age_input) < 130
    except ValueError:
        return False


def validate_email(email_input: str) -> bool:
    return type(email_input) == str and '@' in email_input


dict1_functions = {
    "full_name": validate_full_name,
    "age": validate_age,
    "email": validate_email

}


def validate_details() -> None:
    keys: list[str] = ["full_name", "age", "email"]
    for key in keys:

        while True:
            value = input(f"enter your {' '.join(key.split("_"))}:")
            func = dict1_functions.get(key)
            if func(value):
                print(f"{key} is valid")
                break
            print("try again")


print("21.validate input details:")
validate_details()


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
