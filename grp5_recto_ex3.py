def calculate_length(s):
    return len(s)

# 1
input_string = "Wonderful Life"
print("Length of string:", calculate_length(input_string))


def count_characters(s):
    return len(s)

# 2
input_string = "Wonderful Life"
print("Number of characters:", count_characters(input_string))


def replace_char(s):
    if len(s) < 2:
        return s
    first_char = s[0]
    return first_char + s[1:].replace(first_char, '$')

# 3
input_string = "Buzzer Beater"
print("Modified string:", replace_char(input_string))


def swap_and_concatenate(s1, s2):
    if len(s1) < 2 or len(s2) < 2:
        return s1 + " " + s2
    s1_swapped = s2[0] + s1[1:] + " " + s1[0] + s2[1:]
    return s1_swapped

# 4
str1 = "Strength"
str2 = "Weakness"
print("Concatenated string:", swap_and_concatenate(str1, str2))


def concatenate_with_spaces(a, b, c, d):
    return f"{a} {b} {c} {d}"

# 5
var1 = "Are"
var2 = "you"
var3 = "ready"
var4 = "kids"
print("Concatenated string:", concatenate_with_spaces(var1, var2, var3, var4))


def concatenate_user_input():
    str1 = input("Please input the first string: ")
    str2 = input("Please Input the second string: ")
    return str1 + " " + str2

# 6
print("Concatenated string:", concatenate_user_input())


def concatenate_name_age(name, age):
    return f"My name is {name} and I am {age} years old."

# 7
your_name = "Jan Mark"
your_age = 22
print(concatenate_name_age(your_name, your_age))
