'''tribonacci series'''



def tribonacci(s, n):

    n1 = s[0]
    n2 = s[1]
    n3 = s[2]
  
    count = 0
    if n == 0:
        print([])
    elif n == 1:
        print([1])
    else:
        while count < n:
            print(n1, end=' , ')
            nth = n1 + n2 + n3
            #update values
            n1 = n2
            n2 = n3
            n3 = nth
            count += 1
        
            

