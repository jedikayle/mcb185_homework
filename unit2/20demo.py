# tuples
t = 1, 2 # This is a tuple: collection of values separated by a comma
print(t)
print(type(t))

person = 'Steve', 21, 57891.50 # name, age, yearly income
print (person)

def midpoint(x1,y1,x2,y2):
    x = (x1 + x2)/2
    y = (y1 + y2)/2
    return x,y

print(midpoint(1,2,3,4)) # call midpoint fxn
m = midpoint(1,2,3,4) # assigns variable m to return of midpoint fxn, m is a tuple
mx, my = midpoint(1,2,3,4) # unpacks tuple
print(m[0],m[1]) 

# iteration: repeating set of instructions multiple times
i = 0
while True: # while loop runs as long as condition remains true
    i = i + 1
    print('hey',i)
    if i == 3: break # break stops a loop

i = 0
while i < 3:
    i = i + 1
    print('hey',i) # stops when i reaches 3

i = 1 #this iteration starts at 1, ends before 10, skips by 3s
while i < 10:
    print(i)
    i = i + 3 # increments i by 3 each time
print('final value of i is', i)

# range(start, stop, set)
for i in range(1,10,3): # The range() fxn gives integers given an initial val (1), an end-before limit (10), and an increment (3).
    print(i) # output 1,4,7

# all code below does the same thing
for i in range(5): print(i) # output 0,1,2,3,4
for i in range(0,5): print(i) # output 0,1,2,3,4
for i in range(0,5,1): print(i) # output 0,1,2,3,4

for i in range (4,-1,-1): print(i) # counts backwards, output 4,3,2,1,0

# for item in container
basket = 'milk','eggs','bread' # tuple containing grocery items
for thing in basket:
    print(thing)

for i in range (len(basket)): # len() returns # of items in basket
    print(basket[i])

# nesting: placing a structure (like loops or conditionals) inside another
for i in range(7): # loops through #s 0 to 6
    if i % 2 == 0: # checks if number if divisible by 2
        print(i, 'is even')
    else:
        print(i, 'is odd')