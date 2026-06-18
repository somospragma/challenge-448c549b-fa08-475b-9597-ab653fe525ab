import pytest
from src.employee import Employee
from src.manager import Manager
from src.engineer import Engineer
from src.assistant import Assistant

def test_employee_annual_salary():
    employee = Employee('John Doe', 30, 'Employee', 5000)
    assert employee.annual_salary() == 60000

def test_manager_display_info():
    manager = Manager('Jane Doe', 40, 8000, 'HR')
    assert manager.display_info() == 'Nombre: Jane Doe, Edad: 40, Rol: Manager, Salario Anual: 96000, Departamento: HR'

def test_engineer_display_info():
    engineer = Engineer('Jim Beam', 25, 6000, 'Software')
    assert engineer.display_info() == 'Nombre: Jim Beam, Edad: 25, Rol: Engineer, Salario Anual: 72000, Especialización: Software'

def test_assistant_display_info():
    assistant = Assistant('Jill Smith', 22, 3000, 'Support')
    assert assistant.display_info() == 'Nombre: Jill Smith, Edad: 22, Rol: Assistant, Salario Anual: 36000, Tareas: Support'