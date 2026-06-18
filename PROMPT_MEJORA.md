# Prompt para Mejorar el Codigo Base

Copia y pega el siguiente contenido completo en un asistente de IA (Claude, ChatGPT, etc.)
para obtener un ZIP con el proyecto corregido y listo para compilar.

---

```
Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación o descripciones sin código, genera los archivos
correspondientes sin aplicar análisis de compilación
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:
// === ARCHIVO: src/employee.py ===
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

// === ARCHIVO: src/manager.py ===
from src.employee import Employee

class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, 'Manager', salary)
        self.__department = department

    def get_department(self):
        return self.__department

    def display_info(self):
        return f'{super().display_info()}, Departamento: {self.__department}'

// === ARCHIVO: src/engineer.py ===
from src.employee import Employee

class Engineer(Employee):
    def __init__(self, name, age, salary, specialization):
        super().__init__(name, age, 'Engineer', salary)
        self.__specialization = specialization

    def get_specialization(self):
        return self.__specialization

    def display_info(self):
        return f'{super().display_info()}, Especialización: {self.__specialization}'

// === ARCHIVO: src/assistant.py ===
from src.employee import Employee

class Assistant(Employee):
    def __init__(self, name, age, salary, tasks):
        super().__init__(name, age, 'Assistant', salary)
        self.__tasks = tasks

    def get_tasks(self):
        return self.__tasks

    def display_info(self):
        return f'{super().display_info()}, Tareas: {self.__tasks}'

// === ARCHIVO: tests/test_employee.py ===
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
```
