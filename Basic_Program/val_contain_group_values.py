def is_group_ele(lst, n):
    for i in lst:
        if i == n:
            return True
    return False
lst=[1, 5, 8, 3]
print(is_group_ele(lst, 3))
print(is_group_ele(lst, -1))
