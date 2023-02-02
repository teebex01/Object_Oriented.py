from student import student
from dept import course_acc


student2=student('micheal', 1999, 'olosho')
#student3=student.data_from_csv()
#print(student.data_from_csv())
print(student.all)
print(student2.name)
print("==========================")
student2.name="olowojaba"
print(student.all)

print("==========================")
print(student2.dob)
student2.dob=1998
print(student2.all)
print("==========================")
print(student2.course)
student2.course="ABCFS"
print(student2.all)
print("==========================")
#print(student2.bill(5,20))
student2.bill(5,499)
print(student2.student_fees(20))




# print(student2.view_only)
#student2.view_only="not your problem"


#print(course_acc())
#print(student2)
# print(student2.name)
# student2.name="oluwadamilare"
# print(student2.name)
# print(student2)
#print(student.data_from_csv())
# participant1=course_acc('Oluwajide',654,'computer','sex')
# print(participant1)
# print(participant1.discount_fee())
#student2=student('micheal', 1999, 'olosho')
# print(student2)





