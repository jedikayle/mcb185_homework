# 22fibonacci.py by Jedikayle

a = 0 # set initial vals
b = 1
print(a,b) # first two fibonacci values
for i in range(4): # this will give us 4 x 2 values totaling 8 more values for fibonacci
    a += b # this means a = a + b
    b = a + b
    print(a,b)