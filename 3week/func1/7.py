def dublicates(lists):
    a = 0
    for i in range(len(lists) -1):
        if lists[i] == lists[i+1] and lists[i] == 3:
            a += 1
    tf = ""
    if a >= 1:
        tf = "True"
    else:
        tf = "False"

    print(tf)
    
dublicates([1, 3, 3])
dublicates([1, 3, 1, 3])
dublicates([1, 3, 1])
