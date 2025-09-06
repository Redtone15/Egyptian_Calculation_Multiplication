#Acqire Two Numbers to be Multiplied
a = int(input("First number\n"))
b = int(input("Second number\n"))
c = 0
Remaining =a
#Finding out the number of bits needed to store input one
while a > 1:
    a = a // 2
    c += 1
comp = 1
div = [1]

print("bit(s) needed",c)
#listing out the exponents
for i in range(c):
    comp *= 2
    div.append(comp)
print("list of exponents of 2",div)
#finding out the numbers needed to form input a
plc = []
cnt = len(div)-1
while cnt >= 0:
    if div[cnt] <= Remaining:
        plc.append(div[cnt])
        Remaining -= div[cnt]
        cnt -=1
    else:
        cnt -= 1
print("numbers that form input",a,plc)
#Adding each number after multiplying exponent with input b
calc=0
for ans in range(len(plc)):
    print(b, "*", plc[ans], "=", b*plc[ans])
    calc=calc+b*plc[ans]

    print ("Sum of previous numbers",calc,"\n")
print("answer is",calc)
