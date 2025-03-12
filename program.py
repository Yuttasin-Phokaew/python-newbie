'''#nested-if
username = input("ป้อนชื่อผู้ใช้")
password = input("ป้อนรหัสผ่าน")

if username=="member" and password=="1234" :
    print("เข้าสู้ระบบสำเร็จ")
    service=input("ป้อนหมายเลขบริการ(1-2):")
    if service=="1":
        print("ถอนเงิน")
    elif service=="2":
        print("ฝากงเิน")
    else:
        print("หมายเลขบริการไม่ถูกต้อง")
else:
    print("หมายเลขบริการไม่ถูกต้อง")


#match statement
service = input("ป้อนหมายเลขบริหาร(1-3):")

match service:
    case "1":print("ถอนเงิน")
    case "2":print("ฝากเงิน")
    case "3":print("สอบถามยอดเงินคงเหลือในบัญชี")
    case "":print("หมายเลขบริการไม่ถูกต้อง")

#while loop
counter = 0
while counter<10:
    counter+=1
    print(counter)

print("จบการทำงาน")

#for loop
for counter in range(1,6):
    print("hello python",counter)

for counter in range(10,0,-1): #ถอยหลัง
    print(counter)

#break / continue
for counter in range(1,11):
    if counter==9:
        break #ไม่ทำหลังเข้าเงื่อนไข
    elif counter%2==0:
        continue #ข้ามตัวเงื่อนไข
    print(counter)

print("จบการทำงาน")

#แม่สูตรคูณ
number = int(input("ป้อนตัวเลขสูตรคูณ:"))
#รอบทำการแบบตายตัว 1-12 ใช้ for loop
for i in range(1,13):
    print(number,"x",i,"=",number*i)

#หาผลรวมของตัวเลข 5 จำนวน
total = 0
for i in range(1,6):
    number = int(input("ลำดับที่ "+str(i)+":"))
    total+=number
print("ผลรวม = ",total)

#หาผลรวมของตัวเลขไม่จำกัดจำนวน
total = 0
while True:
    number = int(input("ป้อนตัวเลข:"))
    if number<=0:
        break #เงื่อนไขหลุด loop
    total+=number
print("ผลรวม = ",total)

#nested loop
for i in range(2):
    print("count i to ",i)
    for j in range(3):
        print("count j to ",j)

#แม่สูตรคูณแบบกำหนดช่วง
start = int(input("แม่สูตรคูณเริ่มต้น :"))
end = int(input("แม่สูตรคูณสุดท้าย :"))

for number in range(start,end+1):
    print("สูตรคูณแม่ ",number)
    print("---------------")
    for i in range(1,13):
        print(number,"x",i,"=",number*i)

#string
text = "Hello Python"
print(text.lower()) #เปลี่ยนเป็นตัวพิมพ์เล็ก
print(text.startswith("Hell")) #ตรวจสอบคำแรก คำนำหน้า
print(text.endswith("on")) #ตรวจสอบคำท้าย เดือน 
print(text.find("Python")) #หาลำดับ index
print(text.count("o")) #หาว่ามีกี่คำ


#list
color1=["ดำ","แดง","เหลือง","เขียว","น้ำเงิน"]
color2=list(("ขาว","ฟ้า","ม่วง"))

color1.append("น้ำตาล") #แอดหลัง
color1.extend(["ชมพู","ส้ม"]) #แอดหลัง
color1.insert(2,"ขาว") #แอดตำแหน่ง
color2.remove("ขาว") #เอาคำนี้ออก
fullcolors = color1+color2
# fullcolors.clear()
fullcolors.sort() #น้อยไปมาก
fullcolors.reverse() #มากไปน้อย
print(fullcolors)
print(fullcolors.count("ขาว")) #นับจำนวนข้อมูล'

'''