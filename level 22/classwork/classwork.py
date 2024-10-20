# 

def manual_min(listn):
    min_num = listn[0]

    for i in listn:
        if min_num > i:
            min_num = i

    return min_num

print(manual_min([3, 4, 5]))

    
