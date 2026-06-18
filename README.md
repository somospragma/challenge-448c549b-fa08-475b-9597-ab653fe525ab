# Implementación de un Sistema de Gestión de Empleados con OOP

Una empresa necesita un sistema para gestionar la información de sus empleados. El sistema debe permitir registrar empleados con diferentes roles (gerente, ingeniero, asistente) y aplicar conceptos de Programación Orientada a Objetos como herencia, polimorfismo, encapsulamiento y abstracción. Cada empleado tiene atributos como nombre, edad, rol y salario. El sistema debe ser capaz de calcular el salario anual de cada empleado y mostrar información específica según su rol.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Programación Orientada a Objetos |
| **Nivel** | junior-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 3-4 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición de Clases Base

**Objetivo:** Definir las clases base para empleados y roles específicos.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Identifica los atributos comunes y específicos de cada tipo de empleado.
- Define una clase base para empleados y clases derivadas para cada rol.

**Entregable:** Clases base y derivadas definidas.

<details>
<summary>Pistas de conocimiento</summary>

- Piensa en cómo los atributos y métodos se heredan y se pueden sobrescribir.
- Considera cómo proteger la información sensible.

</details>

### Fase 2: Implementación de Métodos

**Objetivo:** Implementar métodos para calcular el salario anual y mostrar información específica.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Implementa métodos en las clases para calcular el salario anual.
- Agrega métodos para mostrar información específica según el rol del empleado.

**Entregable:** Métodos implementados en las clases.

<details>
<summary>Pistas de conocimiento</summary>

- Utiliza polimorfismo para manejar diferentes tipos de empleados.
- Considera cómo encapsular la lógica de cálculo del salario.

</details>

### Fase 3: Pruebas y Validación

**Objetivo:** Realizar pruebas y validar el funcionamiento del sistema.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Crea instancias de diferentes tipos de empleados y prueba los métodos implementados.
- Valida que los cálculos y la información mostrada sean correctos.

**Entregable:** Instancias de empleados creadas y métodos probados.

<details>
<summary>Pistas de conocimiento</summary>

- Realiza pruebas con diferentes escenarios para asegurar la correcta implementación.
- Verifica que los métodos funcionan como se espera en todos los casos.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es la herencia en el contexto de este reto?
- **paraQueSirve**: ¿Para qué sirve el polimorfismo en este sistema de gestión de empleados?
- **comoSeUsa**: ¿Cómo se usa el encapsulamiento para proteger la información sensible en las clases?
- **erroresComunes**: ¿Cuáles son los errores comunes al implementar métodos en las clases?
- **queDecisionesImplica**: ¿Qué decisiones implica la implementación de métodos para calcular el salario anual?

## Criterios de Evaluacion

- Definición correcta de clases base y derivadas.
- Implementación de métodos para calcular el salario anual y mostrar información específica.
- Uso correcto de herencia, polimorfismo, encapsulamiento y abstracción.
- Realización de pruebas y validación del sistema.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
