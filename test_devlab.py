#พิละมิด * รับ input
number = int(input())

for i in range(1,number+1):
    print("*" * i)

#เกรด A-F
score = int(input())

if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"
print(grade)

#บวกลบเลขธรรมดา
# รับค่าจำนวนเต็ม a และ b
a = int(input())
b = int(input())
print(a + b)

#ลำดับเลขไหนมากกว่าโช A & B เท่ากันโช AB
A = int(input())
B = int(input())

if A > B:
    print("A")
elif B > A:
    print("B")
elif A == B:
    print("AB")

#รับ input แล้วโช
name = input()

print("Welcome", name ,"!")
print("Sommai 108 Eleven Shop")

#บวก ลบ คูณ หาร
num1 = int(input())
num2 = int(input())

print( num1 ,"+", num2, "=" ,num1+num2)
print( num1 ,"-", num2, "=" ,num1-num2)
print( num1 ,"*", num2, "=" ,num1*num2)
print( num1 ,"/", num2, "=" ,num1//num2)

#เทียบค่าตัวเลข 2จำนวนไหนมากน้อย
a = int(input("ป้อนจำนวนที่ 1: "))
b = int(input("ป้อนจำนวนที่ 2: "))

if a > b:
    print(f"MAX = {a}")
    print(f"MIN = {b}")
elif b > a:
    print(f"MAX = {b}")
    print(f"MIN = {a}")