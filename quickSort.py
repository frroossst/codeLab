arr = [17,20,1,2,3,4,5,9,7,8,6,10,13,12,11]

def quickSort(li,toSort=[]):

    if len(li) <= 1:
        return li

    piv = [li[-1]]

    smallerThanPiv = [x for x in li if x < piv[0]]
    equalToPiv = [x for x in li if x == piv[0]]
    greaterThanPiv = [x for x in li if x > piv[0]]

#    print(smallerThanPiv,equalToPiv,greaterThanPiv)

    return quickSort(smallerThanPiv) + quickSort(piv) + quickSort(greaterThanPiv)

print(quickSort(arr))