def check_condition(value):
    if value > 10:
        return True
    else:
        return False
result = check_condition(15)
print(f"Condition result: {result}")
my_list = ["apple", 42, True]
print(f"List: {my_list}")
my_tuple = ("banana", 50, False)
print(f"Tuple: {my_tuple}")
my_set = {"cherry", 7, True}
print(f"Set: {my_set}")
my_dict = {
    "fruit": "mango",
    "quantity": 5,
    "is_ripe": True
}
print(f"Dictionary: {my_dict}")