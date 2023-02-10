def agent(lists):
    zero = 0
    seven = 0
    booler = True
    for i in range(len(lists)):
        if seven != 1 and zero < 3:
            if lists[i] == 0:
                zero += 1
            elif lists [i] == 7:
                seven += 1
        elif (seven == 1 and zero == 2):
            break
        else:
            booler = False
            break
    print( booler)

agent([1,2,4,0,0,7,5])
agent([1,0,2,4,0,5,7])
agent([1,7,2,0,4,5,0])