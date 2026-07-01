"""

1
23
456
78910

"""

i = 1
j = 1
while i <= 4:
    k = 1
    while k <= i:
        print(j, end="")
        j += 1
        k += 1
    print()
    i += 1
    
"""
i=1 
J=1
1<=4 T
k=1
1<=1 T
print j =1
j+1=2
k+1=2
k=2<=i=1 F
i+1=2
i=2<=4 t
k=1<i=2 t
print j =2

"""
    