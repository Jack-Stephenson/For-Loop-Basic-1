#Basic
for x in range(151):
    print(x)
    pass

#Multiples of Five
for x in range(5,1000):
    if x%5==0:
        print(x)
    pass

#Counting, the Dojo Way
for x in range(1,100):
    if x%5==0:
        print("Coding")
    else:
        print(x)
    pass

#Whoa. That Sucker's Huge
for x in range(500000):
    final = 0
    if x%2!=0:
        final += x
    pass
print(final)

#Countdown by Fours
for x in range(2018, 0, -4):
    print(x)
    pass

#Flexible Counter
lowNum=4
highNum=50
mult=6
for x in range(lowNum, highNum):
    if x%mult==0:
        print(x)
    pass
