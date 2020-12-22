#Studentschool.py

class Student:
	def __init__(self,name):
		self.name = name
		self.exp = 0
		self.lesson = 0
		# self.AddEXP(10) # CallFunction
		# student1.name
		# self = student1

	def Hello(self):
		print('สวัสดีจ้าาาา  ผมชื่อ{}'.format(self.name))

	def Coding(self):
		print('{}: กำลังเขียนโปรแกรม..'.format(self.name))
		self.exp += 5
		self.lesson += 1

	def ShowEXP(self):
		print('-{} มีประสบการณ์ {} EXP'.format(self.name,self.exp))
		print('-เรียนไป {} ครั้งแล้ว'.format(self.lesson))

	def AddEXP(self,score):
		self.exp += score # self.exp = self.exp + 10
		self.lesson += 1

# class SpecialScore():
	# def __init__(self):
		# self.score = 500

class SpecialStudent(Student):

	def __init__(self,name,father):
		super().__init__(name)
		self.father = father
		mafia = ['Bill Gates','Thomas Edison']
		if father in mafia:
			self.exp += 100
	def AddEXP(self,score):
		self.exp += (score * 3)
		self.lesson += 1
	def AskEXP(self,score = 10):
		print('ครู!! ขอคะแนนพิเศษให้ผมหน่อยสิ สัก{} EXP'.format(score))
		self.AddEXP(score)



if __name__ == '__main__':

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