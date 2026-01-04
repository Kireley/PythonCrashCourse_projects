def func1(array: list = []):
    array.extend([1])
    return array


print(func1([1]))
print(func1())
print(func1())
print(func1([]))