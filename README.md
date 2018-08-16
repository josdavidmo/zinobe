# Zinobe

Technical Test Zinobe

## Ambiente de la Aplicación

Considerando los requerimientos presentados y la experiencia previa en proyectos de python, se decidió crear un marco de trabajo para el desarrollo de la prueba apoyado en las siguientes tecnologías:

-   Beaker
-   funcsigs
-   Jinja2
-   MarkupSafe
-   resolver
-   selector
-   SQLAlchemy
-   sqlite

Al igual que los proyectos desarrollados en Django, el framework maneja el archivo manage.py, el cual gestiona la ejecución del servidor, las pruebas unitarias y la base de datos.

## Instalación de la Aplicación

Los comandos presentados a continuación corresponden a los ejecutados en ubuntu 16.04. Para instalar la aplicación se debe disponer de git y virtualenv previamente instalado.

    git clone https://github.com/josdavidmo/zinobe.git
    cd zinobe
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

##¿Cómo ejecutar la aplicación?

Ejecutar la aplicación es sencillo, basta con ejecutar el comando:

    python manage.py run

Inmediatamente en la consola mostrará los siguientes mensajes:

    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.375s

    OK
    Serving HTTP on 0.0.0.0 port 8080 ...

Posteriormente ingresar al navegador a la url localhost:8080

## Requerimientos

Queremos que construya un directorio de usuarios sencillo. La interfaz de usuario no debe ser bonita, no importa en realidad como luzca, pero debe funcionar.

## Características

-   Registro de usuario
-   Login de usuario
-   Logout de un usuario
-   Búsqueda de usuarios

## Reglas

-   Abstenerse de usar Django o cualquier otro framework
-   Cualquiera puede registrarse
-   La búsqueda de usuario debe ser hecha en un solo campo de texto
-   La búsqueda de usuario debe encontrar usuarios por nombre o correo electrónico
-   Usuarios no logueados puede llenar el formulario de registro
-   Sólo los usuarios logueados pueden hacer búsquedas y ver sus resultados
-   Usuarios logueados NO deben ver los formularios de login o de registro

## Datos de usuario

-   Nombre - requerido - min 3 caracteres
-   Email - requerido - unico - dirección válida
-   País - requerido (Se deben proveer opciones, puede sacar la lista de algún servicio que sirva el listado ISO-3166-2 como <http://data.okfn.org/data/core/country-list>)
-   Password - requerido - cualquier caracter válido - min 6 caracteres - al menos 1 dígito

## Criterio de evaluación

-   Uso de paquetes de Python
-   La aplicación debe funcionar. Por favor proveer instrucciones de como instalarla y correrla.
-   Principios SOLID, en especial SRP e Inyección de dependencias
-   Pruebas
-   Seguridad

## Plus

-   Una descripcion muy precisa al hacer el Merge Request
-   Instalación de la aplicación con una sola linea de comandos o con un script
-   Enrutar con url amigables
-   Uso de ORM
-   Uso de un motor de plantillas
-   Historia de git (aún cuando sea corta) con mensajes de commit claros y concisos
