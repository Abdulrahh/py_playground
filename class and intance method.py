class Student:
    
    count = 0 
    total_gpa = 0 
    
    def __init__(self, name, gpa):
        self.name = name 
        self.gpa = gpa 
        Student.count += 1
        Student.total_gpa += gpa
        
    # instance method 
    def get_info(self):
        return f"{self.name} = {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return F" Total Number of students: {cls.count}"
    
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0 
        else:
            return F"Average gpa: {cls.total_gpa / cls.count:.2f}"
    
    
student1 = Student("SpongeBob", 2.8)
student2 = Student("patrick", 0.9)
student3 = Student("Sandy", 4.0)


print(Student.get_count())
print(Student.get_average_gpa())