from student import student

class course_acc(student):
  all=[]
  def __init__(self, name, dob, course, hobby):
    super().__init__(
      name, dob, course
    )
    self.hobby=hobby
    print('love')
    print(f'Name: {name}, Year: {dob},Course: {course}, hobby:{hobby}')
    course_acc.all.append(self)
  # def __repr__(self):
  #   print(self.name)