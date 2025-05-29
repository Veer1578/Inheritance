class person():
    def __init__(self, name, id_no):
        self.name = name
        self.id_no = id_no

    def display(self):
        print(self.name)
        print(self.id_no)

class employee(person):
    def __init__(self, name, id_no, salary, post):
        self.salary = salary
        self.post = post
        
        person.__init__(self, name, id_no)

a = employee('Rahul', 886012, 200000, 'Intern')
a.display()