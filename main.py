#create object oriented for student
import csv
# class student:
#   @classmethod
#   def data_from_csv(cls):
#     with open('data.csv', 'r') as mydata:
#       reader=csv.DictReader(mydata)
#       data=list(reader)
  
#     for i in data:
#       i(
#         name=i.get('name'),
#         dob=int(i.get('dob')),
#         course=i.get('course'),
#       )

class student:
  discount_amount=0.8
  all=[]
  def __init__(self, name, dob, course):
    self.name=name
    self.dob=dob
    self.course=course
    #print(f'Name: {name}, Year: {dob},Course: {course}')
    student.all.append(self)
  def bill(self, hour:int, amount:int):
    assert amount>1000 and amount<10000
    self.hour=hour
    self.amount=amount
    # print(hour*amount)
    # print(hour*amount*self.discount_amount)
  def discount_fee(self,discount_amount):
    print(f'Student Name:{self.name}, and discount fees: {self.amount*discount_amount}')
  ##representing the data in student.all[] 
  @classmethod
  def data_from_csv(cls):
    with open('data.csv', 'r') as mydata:
      reader=csv.DictReader(mydata)
      data=list(reader)

    for i in data:
      print(i)
      # i(
      #   name=i.get('name'),
      #   dob=i.get('dob'),
      #   course=i.course('course'),
      # )
  @staticmethod
  def is_integer(num):
    #we will count out floats that are point zero
    if isinstance(num, float):
      return num.is_integer()
    elif isinstance(num, int):
      return True
    else:
      return False
  
  def __repr__(self):
    return self.name
  
print(student.is_integer(9))
student.data_from_csv()
# student1=student('tobi',1986, 'Science')
# student2=student('Oluwagbenro',2002,'data tech')
# student3=student('Ayomide',2002,'Doctor')
# student4=student('Mike',1980,'Marketing')
# student5=student('Loveth',1984,'Social Worker')
print('===================================')

# student2.discount_amount=0.5
# student2.bill(12,8000)
# student2.discount_fee(0.9)
print(student.all)
for i in student.all:
  print(i.name)





