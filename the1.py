class Employee:
  def __init__(self, name, post, salary):
    self.name = name
    self.post = post
    self.salary = salary
    
  def calculate_salary(self):
    return self.salary * 1.15
  
  def display_info(self):
    print(self.name, self.post, self.calculate_salary())

class Manager(Employee):
  def __init__(self, name, post, salary, slaves):
    super().__init__(name, post, salary)
    self.slaves = slaves
  
  def calculate_salary(self):
    return super().calculate_salary() * 1.3
  
  def display_info(self):
    print(self.name, self.post, self.calculate_salary(), self.slaves)
  
class Developer(Employee):
  def __init__(self, name, post, salary, bet):
    super().__init__(name, post, salary)
    self.post = post
    self.salary = salary
    self.bet = bet

  def calculate_salary(self):
    return self.bet * super().calculate_salary()
  
  def display_info(self):
    print(self.name, self.post, self.calculate_salary())
  
employee1 = Employee('Alex', 'Worker', 10000)
employee2 = Manager('Aleg', 'Manager', 10000, 3)
employee3 = Developer('Lana', 'dev', 500, 400)
employee1.display_info()
employee2.display_info()
employee3.display_info()