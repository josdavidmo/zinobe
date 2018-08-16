# zinobe
Technical Test Zinobe

## Requerimientos

Queremos que construya un directorio de usuarios sencillo. La interfaz de usuario no debe ser bonita, no importa en realidad como luzca, pero debe funcionar.

## Características

* Registro de usuario
* Login de usuario
* Logout de un usuario
* Búsqueda de usuarios

## Reglas

* Abstenerse de usar Django o cualquier otro framework
* Cualquiera puede registrarse
* La búsqueda de usuario debe ser hecha en un solo campo de texto
* La búsqueda de usuario debe encontrar usuarios por nombre o correo electrónico
* Usuarios no logueados puede llenar el formulario de registro
* Sólo los usuarios logueados pueden hacer búsquedas y ver sus resultados
* Usuarios logueados NO deben ver los formularios de login o de registro

## Datos de usuario

* Nombre - requerido - min 3 caracteres
* Email - requerido - unico - dirección válida
* País - requerido (Se deben proveer opciones, puede sacar la lista de algún servicio que sirva el listado ISO-3166-2 como http://data.okfn.org/data/core/country-list)
* Password - requerido - cualquier caracter válido - min 6 caracteres - al menos 1 dígito

## Criterio de evaluación

* Uso de paquetes de Python
* La aplicación debe funcionar. Por favor proveer instrucciones de como instalarla y correrla.
* Principios SOLID, en especial SRP e Inyección de dependencias
* Pruebas
* Seguridad

## Plus

* Una descripcion muy precisa al hacer el Merge Request
* Instalación de la aplicación con una sola linea de comandos o con un script
* Enrutar con url amigables
* Uso de ORM
* Uso de un motor de plantillas
* Historia de git (aún cuando sea corta) con mensajes de commit claros y concisos
