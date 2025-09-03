
a = int(input("1\n"))
b = int(input("2\n"))

c = 0
rem =a

while a > 1:
    a = a // 2
    c += 1
comp = 1
div = [1]
print("bit needed",c)
for i in range(c):
    comp *= 2
    div.append(comp)
print("list of exponents of 2",div)
plc = []
cnt = len(div)-1
while cnt >= 0:
    if div[cnt] <= rem:
        plc.append(div[cnt])
        rem -= div[cnt]
        cnt -=1
    else:
        cnt -= 1
print("numbers that form input",a,plc)

calc=0
for ans in range(len(plc)):
    calc=calc+b*plc[ans]
    print (calc,"\n")
print("answer is",calc)
    