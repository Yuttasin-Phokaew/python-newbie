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

#พิละมิดขวา
rows = int(input())

for i in range(1, rows + 1):
    print("*" * i)

#พิละมิดที่เพิ่มฐานทีละเท่าตัว
rows = int(input())

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

#เลขยกกำลัง
base = int(input())
exponent = int(input())

# คำนวณเลขยกกำลัง
result = base ** exponent

# แสดงผลลัพธ์
print(result)

#ทำสี่เหลี่ยมจัสตุรัส
n = int(input())

# วาดกรอบสี่เหลี่ยม
for i in range(n):
    if i == 0 or i == n - 1:  # แถวบนและแถวล่าง
        print("#" * n)
    else:  # แถวตรงกลาง
        print("#" + " " * (n - 2) + "#")


#รีเวิดคำจากหลังไปหน้า coming i'm hello เป็น hello i'm coming
# รับข้อความจากผู้ใช้
text = input()

# แยกคำและกลับลำดับ
reversed_text = ' '.join(text.split()[::-1])

# แสดงผลลัพธ์
print(reversed_text)

#รับค่าตัวเลขเท่าไรก็ได้ หยุดด้วย 0 และเลือก min max เพื่อเรียงเลข
numbers = []

while True:
  num = int(input())
  if num == 0:
    break
  numbers.append(num)

order = input()    
if order.lower() == 'min':
  numbers.sort()
elif order.lower() == 'max':
  numbers.sort(reverse=True)
print(' '.join(map(str, numbers))) #ทำให้ไม่มี []

#รับจำนวนเต็ม 1-1000 แสดงตัวเองตามจำนวนเต็ม ตรวจหาตัวเลขนั้นมีในจำนวนไหม
# รับค่า n
n = int(input())

# ตรวจสอบเงื่อนไขว่า n ต้องอยู่ในช่วง 1 ถึง 1000
if not (0 < n <= 1000):
    exit()

# รับตัวเลข n ตัว และเก็บใน list
numbers = list(map(int, input().split()))

# ตรวจสอบว่าป้อนจำนวนครบหรือไม่
if len(numbers) != n:
    exit()

# รับค่าที่ต้องการค้นหา
target = int(input())

# ตรวจสอบว่ามี target อยู่ใน list หรือไม่
if target in numbers:
    print("Yes")
else:
    print("No")

#ผลรวม a b แต่คำตอบจะย้อนหลังกลับ
# รับค่า a และ b
a = int(input())
b = int(input())

# หาผลรวม
sum_ab = a + b

# แปลงผลรวมเป็นสตริงแล้วกลับตัวเลข
reversed_sum = str(sum_ab)[::-1]

# แสดงผล
print(reversed_sum)



