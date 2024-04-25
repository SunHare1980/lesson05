

class Task():
    def __init__(self):
        self.tasklist = list()
    def addTask(self, name, description, deadline=None):
        self.tasklist.append({'name': name, 'description': description, 'deadline': deadline, 'done': False})

    def complete(self, name):
        for task in self.tasklist:
            if task['name'] == name:
                task['done'] = True

    def showTasks(self):
        for task in self.tasklist:
            if not task['done'] == True:
                print(task)


t1 = Task()
t1.addTask("Задачв1", "проснуться",'2024 04 25')
t1.addTask("Задачв2", "позавтракать",'2024 04 25')
t1.addTask("Задачв3", "сделать домашку",'2024 04 25')

print ("Задачи на утро:")
t1.showTasks()
t1.complete("Задачв1")
t1.complete("Задачв2")
print ("Задачи на сейчас:")
t1.showTasks()

############################################## Доп

class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = dict()
    def addArticle(self, name, price):
        self.items[name] = price
    def deleteArticle(self, name):
        del self.items[name]
    def PriceArticles(self, name):
        print("Ценв "+ name +" :" + str(self.items.get(name, None)) )

Mag01 = Store("Mag01","Улица северная")
Mag02 = Store("Mag02","Улица южная")
Mag03 = Store("Mag03","Улица западная")

Mag01.addArticle("Яблоко", 100)
Mag02.addArticle("Яблоко", 110)
Mag03.addArticle("Яблоко", 120)
Mag01.addArticle("Груша", 200)
Mag02.addArticle("Груша", 210)
Mag03.addArticle("Груша", 220)

Mag01.addArticle("Слива", 300)
Mag01.PriceArticles("Слива")
Mag01.addArticle("Слива", 250)
Mag01.PriceArticles("Слива")
Mag01.deleteArticle("Слива")
Mag01.PriceArticles("Слива")