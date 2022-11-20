
def histogram(lst):
    for i in lst:
        oupt = ''
        while i > 0:
            oupt = oupt + '*'
            i -= 1
        print(oupt)
lst=[3,2,4,1]
histogram(lst)
