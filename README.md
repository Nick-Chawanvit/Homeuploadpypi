# นี้คือตัวอย่างโปรแกรมสำหรับการเรียน     OOP

### วิธีติดตั้ง

เปิด CMD / Terminal

```python
pip install HomeUploadpypi
```

### วิธีเล่น

เปิด IDLE ขึ้นมาแล้วพิมพ์...

```python
from HomeUploadpypi import Student,SpecialStudent

print('==========1 Jan ==========')
student0 = SpecialStudent('Mark Zuckerberg','Bill Gates')
student0.AskEXP()
student0.ShowEXP()
student1 = Student('Albert')
print(student1.name)
student1.Hello()

print('-----------------')

student2 = Student('Steve')
print(student2.name)
student2.Hello()

print('==========2 Jan ==========')
print('------ใครอยากเรียนโค้ดดิ้ง?-----(10 exp)-----')
student1.AddEXP(10)
# student1.exp += 10 # student1.exp = student1.exp + 10
# student1.lesson += 1

print('==========3 Jan ==========')
print('ตอนนี้ exp ของแต่ละคนได้เท่าไรกันแล้ว')
print(student1.name, student1.exp)
print(student2.name, student2.exp)

print('==========4 Jan ==========')
for i in range(5):
	student2.Coding()
# print('-{} มีประสบการณ์ {} EXP\n-เรียนไป {} ครั้งแล้ว'.format(student2.name,student2.exp,student2.lesson))
# print('-{} มีประสบการณ์ {} EXP\n-เรียนไป {} ครั้งแล้ว'.format(student1.name,student1.exp,student1.lesson))
student1.ShowEXP()
student2.ShowEXP()

```



พัฒนาโดย: ลุงวิศวกร สอนคำนวณ
FB: https://www.facebook.com/UncleEngineer
YouTube: https://www.youtube.com/UncleEngineer

ปล. ขออภัย version 0.1 ลุงใช้เวลาพัฒนาแค่คืนเดียว เลยไม่ได้สมบูรณ์จ้าาาา
ปล2. ใน Mac เล่นได้ แต่ฟังชั่นคีย์บอร์ดยังติดปัญหา ไฟล์ data.csv อยู่ใน /Users/ชื่อusername
ปล3. Windows จะเก็บไฟล์ data.csv ไว้ในโฟลเดอร์ที่ติดตั้ง Python เช่น C:\Python38\data.csv หรือ แนะนำให้สร้างไฟล์ test.py แล้วพิมพ์ว่า import pimsampas แล้วรัน ไฟล์ data.csv จะอยู่ในโฟลเดอร์เดียวกับที่เซฟ


| เพจ "ลุงวิศวกร สอนคำนวณ"  | https://www.facebook.com/UncleEngineer] |
