class Employee:
    def __init__(self, name, age, role, salary):
        self.__name = name
        self.__age = age
        self.__role = role
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_role(self):
        return self.__role

    def get_salary(self):
        return self.__salary

    def annual_salary(self):
        return self.__salary * 12

    def display_info(self):
        return f'Nombre: {self.__name}, Edad: {self.__age}, Rol: {self.__role}, Salario Anual: {self.annual_salary()}'