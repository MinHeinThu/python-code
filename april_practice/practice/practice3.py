
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
# l1 = [2,4,3]
# l2 = [5,6,4]


# l1 = [0], l2 = [0]

def addTwoNumbers(l1,l2):
        result = []
        l1 = int(''.join(map(str, l1)))
        l2 = int(''.join(map(str, l2)))
        n = str(l1 + l2)
        print(type(n))
        print(len(n))
        for i in range(len(n)-1, -1,-1):
                result.append(n[i])
        print(result)
                
        
        
                    
addTwoNumbers(l1,l2)