# 8
student = {
    'name': 'John',
    'age': 20,
    'hobbies': ['reading', 'games', 'coding'],
}


# 1
def student_print(student_1: dict[str, str | int]):
    print("\033[1;92mstudent details:\033[0m")

    for key, value in student_1.items():
        print(f"{key}: {value}")


student_print(student)


# 2
def add_hobby(student_1, hobby):
    if not hobby in student_1['hobbies']:
        student_1['hobbies'].append(hobby)


add_hobby(student, "paint")
# 3
student_print(student)


# 4
def delete_hobby(student_1, hobby):
    if hobby in student_1['hobbies']:
        student_1['hobbies'].remove(hobby)


delete_hobby(student, 'games')
# 5
student_print(student)


# 6
def add_student_family_name(student_1, property_value):
    student_1['family_name'] = property_value.capitalize()


add_student_family_name(student, 'staretz')
student_print(student)

# 9

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]


def print_matrix(mat: list[list[int]]):
    for row in mat:
        for col in row:
            print(col, end=" ")


print()

print_matrix(matrix)
print()
# 10
matrix2 = [[0, 1, 1], [0, 1, 0], [1, 0, 0]]


def zero_count(mat: list[list[int]]):
    count = 0
    for row in mat:
        for col in row:
            if not col:
                count += 1
    return count


print(f"count zero:{zero_count(matrix2)}")


# 11
def find_dup(l1: list[int]):
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


print(find_dup([4, 2, 34, 4, 1, 12, 1, 4]))


# 12
def reverse_list(l2: list[any]):
    result = []
    for i in range(len(l2) - 1, -1, -1):
        result.append(l2[i])
    return result


arr = [43, "what", 9, True, "cannot", False, "be", 3, True];
print(reverse_list(arr))


# 13
def sum_values(l1, l2):
    result = []
    for i in range(len(l1)):
        result.append(l1[i] + l2[i])
    return result


first_array = [4, 6, 7];
second_array = [8, 1, 9];
print(sum_values(first_array, second_array))


# 14
def is_polindrom(str1):
    return str1 == str1[::-1]


def is_two_polindroms(st1, st2):
    print(f"{is_polindrom(st1)}:for {st1}")
    print(f"{is_polindrom(st2)}:for {st2}")


first_str = "racecar"
second_str = "Java"
is_two_polindroms(first_str, second_str)

# 15
counter = 1
while counter < 100:
    print(counter, end=" ")
    counter *= 2
print()

# 16
counter = 900000
while counter > 50:
    print(counter, end=" ")
    counter /= 2
print()


# 17
def duplicate_strings(l1: list[str]):
    dic1: dict[str, int] = {}
    result = []
    i = 0
    while i < len(l1):
        x = l1[i]
        if dic1.get(x):
            dic1[x] += 1
        else:
            dic1[x] = 1
        i += 1
    i = 0
    keys = list(dic1.keys())
    while i < len(keys):
        k = keys[i]
        value = dic1.get(k)
        if value > 1:
            result.append(k)
        i += 1
    return result


print(duplicate_strings(["ssss", "2", "ssss", "Sss", "2", "aba", "a", "aa"]))


# 18
def remove_string_duplicate(l1: list[str]):
    pass
