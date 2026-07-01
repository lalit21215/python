i = 5
while i >= 1:
    j = 5
    while j >= i:
        print(i, end="")
        j -= 1
    print()
    i -= 1
    
    """
    i=5
    j=5
    5>=5 V
    print 5
    j-1=4
    4>=5 X
    i-1=4
    4>=5 V
    5>=4 V
    print 4
    j-1=4
    4>=4 V
    print 4
    j-i+3
    3>=4 X
    repeat till i=0
    """