from src.employee import Employee

class Engineer(Employee):
    def __init__(self, name, age, salary, specialization):
        super().__init__(name, age, 'Engineer', salary)
        self.__specialization = specialization

    def get_specialization(self):
        return self.__specialization

    def display_info(self):
        return f'{super().display_info()}, Especialización: {self.__specialization}'