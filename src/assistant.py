from src.employee import Employee

class Assistant(Employee):
    def __init__(self, name, age, salary, tasks):
        super().__init__(name, age, 'Assistant', salary)
        self.__tasks = tasks

    def get_tasks(self):
        return self.__tasks

    def display_info(self):
        return f'{super().display_info()}, Tareas: {self.__tasks}'