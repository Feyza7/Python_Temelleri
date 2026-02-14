# inheritance (Kalıtım) : Miras alma

# Person => name, lastname, age, eat(),run(),drink()

# Student(Person), Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self ,fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Created')

    def who_am_i(self):
        print('I am a person')

    def eating(self):
        print('I am eating')

class Student():
    pass

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print('Student Created')

    # override
    def who_am_i(self):
        print('I am a student')

    def sayHello(self):
        print('Hello everyone')

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname,lname)
        self.branch = branch

    def who_am_i(self):
        print(f'I am a {self.branch} teacher')

p1 = Person('Ahmet', 'Yılmaz')
s1 = Student('Ali', 'Yıldırım','1235')
t1 = Teacher('Walter', 'White', 'chemistry')

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()

p1.eating()
s1.eating()

s1.sayHello()

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + s1.studentNumber)
print(t1.firstName + ' ' + t1.lastName + ' ' + t1.branch)