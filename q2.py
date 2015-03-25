def find_threes(parameter):
    acumulator=0
    for c in parameter:
        if(c%3==0):
             acumulator=acumulator+c
        else:
            acumulator= acumulator+0
    return acumulator

numbers=[1,2,3,4,5,6,7,8,9,10]
print(find_threes(numbers))
