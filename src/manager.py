from src.employee import Employee

class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, 'Manager', salary)
        self.__department = department

    def get_department(self):
        return self.__department

    def display_info(self):
        return f'{super().display_info()}, Departamento: {self.__department}'