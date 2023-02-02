
#create object oriented for student
import csv
class student:
  discount_amount=0.8
  #amount=25
  all=[]
  def __init__(self, name, dob, course):
    self.__name=name
    self.__dob=dob
    self.__course=course
    #print(f'Name: {name}, Year: {dob},Course: {course}')
    student.all.append(self)

  @property
  def course(self):
    return self.__course
  @course.setter
  def course(self, new_course):
    if new_course=="ABC":
      self.__course=new_course
    elif new_course!="ABC":
      print('you have enter wrong course')  
    else:
      print('RE-ENTER THE LETTER')

  @property
  def dob(self):
    return self.__dob

  @dob.setter
  def dob(self, new_dob):
    if new_dob<1999:
      self.__dob=new_dob
    else:
      print('you need to be above 21')
  @property #this is read only attribute
  def name(self):
    return self.__name #your are about to change the name

  @name.setter
  def name(self, new_name):
    if len(new_name)<3:
      print('you just change the student name')
      self.__name=new_name
    else:
      print('kindly enter your initial name')
    
  def bill(self, hour:int, amount:int):
    #assert amount>1000 and amount<10000
    self.hour=hour
    self.amount=amount
    print(hour*amount)
    # print(hour*amount*self.discount_amount)
  def student_fees(self, increment_money):
    if self.amount<500:
      return increment_money*self.hour*self.amount
    else:
      print('the amount is greater than 500')
    
  def discount_fee(self):
    #return self.dob
    print(f'Student Name:{self.name}')
  ##representing the data in student.all[] 
  @classmethod
  def data_from_csv(cls):
    with open('data1.csv', 'r') as mydata:
      reader=csv.DictReader(mydata)
      data=list(reader)
    for item in data:
      #print(item)
      item(name=item.get('name'),
           dob=item.get('dob'),
           course=item.get('course'),
          )
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
    return f"item({self.name},{self.dob},{self.course})"
    
  def connect(self, sample_server):
    pass

  def prepare_body(self):
    return f"""
    Hello {self.name},
    thank you for contacting us
    Regards
    """
  def send(self):
    pass
    
  def send_reply(self):
    self.connect()
    self.prepare_body()
    self.send()
    pass

  # @property
  # def view_only(self):
  #   return "Oluwatobilobami"
  
#print(student.is_integer(10.10))

# student.data_from_csv()
# print(student.all)
print('===================================')
# participant1=course_acc('Oluwajide',654,'computer','sex')
# print(participant1)
# print(participant1.discount_fee())
#print(course_acc('olu',123,'mkt','kissing'))
#print(course_acc.all)
# for i in student.all:
#   print(i.name)



