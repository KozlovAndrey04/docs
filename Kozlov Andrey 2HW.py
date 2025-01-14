arg1 = ["my", "name", "is", "Masha"]
arg2 = ["a", "ab", "abc"]
arg3 = ["her", "name", "is", "Masha", "Masha", "is", "a", "sister", "of", "Zhenya"]
arg41 = ["my", "name", "is", "Masha"]
arg42 = ["my", "name", "is", "Zhenya"]
arg5 = ["aaa", "aaa", "bbb", "ccc", "bbb"]
arg6 = ["abcd", "a", "ab", "abc", "bazinga", "bar"]


def reverse(array):
    a = []
    for i in range(len(array)):
        if i != 0:
            a.append(array[i * -1])
    a.append(array[0])
    print("result =", a)


def avglen(array):
    s = 0
    k = 0
    for i in range(len(array)):
        a = len(array[i])
        s += a
        k += 1
    if k != 0:
        print("result =", s/k)
    else:
        print("Error")


def index(array):
    dictionary = {}
    for value, key in enumerate(array):
        if key not in dictionary.keys():
            dictionary[key] = [value]
        else:
            dictionary[key].append(value)
    for key in dictionary.keys():
        if len(dictionary[key]) == 1:
            copy = dictionary[key][0]
            dictionary[key] = copy
    print("result =", dictionary)


def coincidence(array1, array2):
    a = []
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                a.append(array1[i])
    print("result =", a)


def count(array):
    dictionary = {}
    for value, key in enumerate(array):
        if key not in dictionary.keys():
            dictionary[key] = 1
        else:
            dictionary[key] += 1
    print("result =", dictionary)


def lensort(array):
    a = []
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if len(array[j]) > len(array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
    print("result =", array)


reverse(arg1)
avglen(arg2)
index(arg3)
coincidence(arg41, arg42)
count(arg5)
lensort(arg6)