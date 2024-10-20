# manual_replace
def manual_replace(str1, pre, aft):
    res = ""

    for i in str1:
        if i == pre:
            res += aft
        else:
            res += 1
    return res


def manual_append(list1, item):
    return list1 + [item]

print(manual_append([1, 2]) 3)
print([1, 2] + [3, 4])


