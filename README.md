# Introducción

Proyecto final SGE con Odoo, Docker, Docker Compose, Git y GitHub.

- [Introducción](#introducción)
- [Preparación del repo y del entorno](#preparación-del-repo-y-del-entorno)
  - [_Fork_ del repositorio original](#fork-del-repositorio-original)
  - [Creación de rama de desarrollo y clonación del repositorio en local](#creación-de-rama-de-desarrollo-y-clonación-del-repositorio-en-local)
  - [Instalación de extensiones útiles](#instalación-de-extensiones-útiles)
  - [Inicialización de Odoo y creación de la primera base de datos](#inicialización-de-odoo-y-creación-de-la-primera-base-de-datos)
  - [Primer _commit_](#primer-commit)
  - [Comando _odoo scaffold_](#comando-odoo-scaffold)
- [Próximos pasos...](#próximos-pasos)

# Preparación del repo y del entorno

## _Fork_ del repositorio original

Inicia sesión en tu cuenta de GitHub, haz un _fork_ de [javnitram/SGE-odoo-it-yourself](https://github.com/javnitram/SGE-odoo-it-yourself) y llama al tuyo SGE-odoo-dev-**XX** (el valor correspondiente a tu número de puesto, según **los dígitos del hostname de clase**).

![Fork](https://github.com/javnitram/SGE-odoo-it-yourself/assets/1954675/f6a5bdea-70f4-47a2-98a6-dd4fd4d8547d)

## Creación de rama de desarrollo y clonación del repositorio en local

En tu repositorio, además de tener una rama _main_ o _master_, crea una rama con nombre **develop**. Esta será tu rama de desarrollo.

![Branch](https://github.com/javnitram/SGE-odoo-it-yourself/assets/1954675/b5fd46e7-9214-46e2-bc04-d0b4eb0b3997)

Vas a usar esa rama para desarrollar tu propio módulo de Odoo. Para ello, deberás clonar la rama en local con Visual Studio Code.

Primero, si no lo has hecho anteriormente, deberás autorizar el acceso a GitHub desde Visual Studio Code.

![Autorizar GitHub en Visual Studio Code](https://user-images.githubusercontent.com/1954675/214658283-2563168c-9a89-4950-b5d8-3b492c748d0a.gif)

A continuación, clona el repositorio (es posible que GitHub te pida autorizar permisos adicionales)

![Git Clone](https://user-images.githubusercontent.com/1954675/214662378-484a9aaa-1be2-4ded-ac78-b3b997bc2fb7.gif)

Asegúrate de estar apuntando a la rama de desarrollo: **develop**

![Checkout](https://user-images.githubusercontent.com/1954675/214665198-03e8f2b6-670c-4384-9ced-557ea86e6632.gif)

Considera guardar tu workspace (área de trabajo) de Visual Studio Code.

## Instalación de extensiones útiles

A diferencia de anteriores proyectos basados en el repo [javnitram/SGE-odoo-dockerized](https://github.com/javnitram/SGE-odoo-dockerized), en esta última entrega, vamos a prescindir de pgAdmin 4 y del script que usábamos para gestionar Docker Compose. En su lugar, hay que usar las extensiones oportunas de Visual Studio Code. Busca por estos identificadores, de modo que por cada uno encontrarás exactamente una extensión para instalar:

- ```jigar-patel.OdooSnippets```
- ```ms-python.python```
- ```ms-azuretools.vscode-Docker```
- ```ckolkman.vscode-postgres```

Tras instalar estas extensiones, obtendrás nuevas funciones en Visual Studio Code, a las cuales puedes acceder rápidamente desde la paleta de comandos con el atajo ```Control + Shift + P```. Asimismo, también podrás observar dos nuevos iconos en la barra de actividad (a la izquierda), uno correspondiente a la extensión de Docker y otro a la de PostgreSQL, nos familiarizaremos con ellas durante las demostraciones en clase.

![Iconos barra lateral](https://user-images.githubusercontent.com/1954675/214654250-62f53d6f-4200-4bf4-89fb-b20d320a1f95.gif)

## Inicialización de Odoo y creación de la primera base de datos

![Inicialización de Odoo](https://user-images.githubusercontent.com/1954675/214669540-193c94c0-81d8-451e-9cac-f8a8c3a03afd.gif)

Lanza los contenedores usando la extensión de Docker en Visual Studio. Desde la propia extensión puedes lanzar también tu navegador por defecto para conectar al servicio Odoo en su puerto expuesto.

Crea tu base de datos de Odoo con la configuración que consideres oportuna.

![Primera base de datos Odoo](https://user-images.githubusercontent.com/1954675/214677032-1a1958ef-8f9e-4942-9cdf-8a09673c50b5.png)

Como recuerdas de anteriores prácticas, es razonable que en ocasiones tengas problemas para acceder desde la máquina anfitriona a ficheros creados desde un contenedor (o viceversa). Cuando haya importantes cambios en el contenido de los volúmenes compartidos entre host y contenedores, ejecuta ```./set_permissions.sh```.

Dicho script te orientará para que arranques los contenedores y vuelvas a invocarlo si es el único modo de recuperar el acceso completo. Esto es necesario en aquellos equipos Linux en los que no podemos ser root ni ejecutar sudo.

## Primer _commit_

Al iniciar Odoo por primera vez y configurar nuestra primera base de datos, hemos asignado una _master password_. Como recuerdas, esta contraseña queda cifrada en el fichero de configuración ```odoo.conf```, que también se ha actualizado para eliminar comentarios. Todo esto hace que Git detecte que el fichero ha sido modificado respecto a su contenido previo. Puedes observar cómo el fichero queda en estado **M** (_Modified_, modificado) y comparar las diferencias producidas en la modificación.

![Odoo conf modificado y diff](https://user-images.githubusercontent.com/1954675/214678982-2358dff2-57ab-47ed-a57d-6371750c886d.png)

Este repositorio está configurado para sincronizar únicamente código y configuración, por lo que ningún _commit_ hará un _backup_ del estado de tu servidor Odoo ni del servidor de base de datos. Recuerda que un sistema de control de versiones no está para esas cosas y, por eso, se han configurado reglas específicas en ficheros _.gitignore_ en algunos directorios.

```text
.vscode
# Python byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Backups and sql dump files
*.sql
*.tgz
*.tar.gz
*.zip
```

Haz tu primer _commit_ (esto es confirmar los cambios en el repositorio local de Git) y _push_ (sincronizar cambios locales hacia el repositorio remoto, en este caso GitHub).

## Comando _odoo scaffold_

Usando la extensión de Docker de Visual Studio Code, localiza la función que te permita abrir una shell en el contenedor de Odoo.

Dentro del contenedor, ejecuta:

```bash
odoo scaffold prueba /mnt/extra-addons
```

![odoo scaffold](https://user-images.githubusercontent.com/1954675/214684898-0bcdea9c-887e-4224-aba1-7e842a223883.gif)

Observa el contenido de ese directorio desde el propio contenedor y desde el volumen mapeado en el anfitrión. Este comando ha generado una estructura mínima de directorios y ficheros para agilizar el desarrollo de un módulo en Odoo. Explora el contenido del directorio _prueba_ desde Visual Studio Code, si tienes algún problema para modificar los ficheros, recuerda ejecutar ```./set_permissions.sh```.

# Próximos pasos...

Crea tu propio módulo de Odoo de acuerdo a los apuntes de clase y al enunciado de la práctica que se te ha proporcionado en el aula virtual.

Debes utilizar Git y GitHub. Para ello, se espera que hagas varios _commits_ y _pushes_ en tu rama de desarrollo y finalmente hagas un _merge_ a tu rama _main_ cuando hayas desarrollado y probado tu módulo.

Si finalizas tu desarrollo con éxito y aprovechas la potencia de Git y GitHub, podrás realizar un _pull request_, es decir, una petición al propietario del repositorio original para que valore tu propuesta e integre tus cambios (_merge_). Es especialmente conveniente que tu proyecto proporcione datos de demo o hagas un _export_ de la base de datos con ```pg_dump``` o alguna utilidad gráfica.

Quien clone el repositorio original y despliegue el entorno podrá probar tu módulo y todos los otros que hayan quedado integrados.

# ✅ Módulo desarrollado: Encuestas personalizadas

Este es el módulo que he desarrollado como parte del proyecto final de SGE. Permite crear y gestionar encuestas en Odoo con diferentes tipos de preguntas, opciones personalizadas y visualización de resultados.

## 📝 Módulo de Encuestas en Odoo

Este proyecto es un **módulo personalizado de encuestas** desarrollado en **Odoo 16** como parte del módulo de *Sistemas de Gestión Empresarial* en el CFGS de Desarrollo de Aplicaciones Multiplataforma.

Permite a los usuarios crear, gestionar y responder encuestas dinámicas y personalizadas, incluyendo soporte para distintos tipos de preguntas y visualización de resultados mediante vistas Kanban y gráficas.

## 🚀 Funcionalidades Principales

- Creación y edición de encuestas con título, descripción e imagen.
- Gestión de preguntas con múltiples tipos: texto, selección simple.
- Definición de opciones de respuesta personalizadas.
- Vistas disponibles:
  - **Form y Tree** en todas las clases.
  - **Kanban y Graph** para visualizar el estado de las encuestas.
- Filtros de búsqueda por nombre o estado.
- Control del estado de las encuestas (borrador, publicadas, finalizadas).
- Restricciones (constraints) para evitar duplicados y garantizar consistencia.

## 🧱 Estructura de Clases (Modelo de Datos)

- **Encuesta**
  - `name`, `descripcion`, `preguntas_ids`, `imagen`, `estado`

- **Pregunta**
  - `name`, `encuestas_ids`, `tipo`, `respuesta_t_ids`, `respuesta_s_ids`

- **RespuestaT** (respuesta de tipo texto)
  - `name`, `pregunta_id`, `respuesta`

- **RespuestaS** (respuesta de selección)
  - `name`, `pregunta_id`, `opciones_ids`, `elegida`

- **OpcionSeleccion**
  - `name`, `respuesta_id`, `opcion`

## 📊 Vistas

- **Kanban**: muestra estado visual de las encuestas con agrupación.
- **Graph**: representación del número de encuestas por estado.
- **Form y Tree**: en todas las entidades para gestión detallada.
- **Búsqueda avanzada**: por estado y nombre de encuesta.

## 🖼️ UML
![UML](https://github.com/user-attachments/assets/f5ce6d6d-614c-4df3-ac16-cb4107304805)

## 🖼️ Vista Kanban

![Vista Kanban](https://github.com/user-attachments/assets/28355ee8-0d8e-4899-bd3c-16154cb48b11)

## 📊 Vistas Graph

![Vista Graph 1](https://github.com/user-attachments/assets/33f03fb7-090d-42fc-a796-a5c10897486c)
![Vista Graph 2](https://github.com/user-attachments/assets/b5b5e9c6-5089-4e25-8ecb-6a989afdb631)

## ➕ Filtros

![Filtros](https://github.com/user-attachments/assets/14fab23b-c940-4435-a4b9-de7c79270262)

## ⚠️ Problemas Encontrados

Durante el desarrollo, se presentó dificultad al implementar respuestas de selección personalizadas usando `fields.Selection`. La solución fue crear una clase intermedia `OpcionSeleccion`, permitiendo flexibilidad y reutilización a través de relaciones `Many2one` con filtrado mediante `domain`.

## 💡 Mejoras Futuras

- Exportación de encuestas.
- Informes automáticos de resultados al finalizar una encuesta.
- Soporte para:
  - Preguntas de opción múltiple (checkbox/radio)
  - Preguntas tipo sí/no
- Fechas de inicio y finalización de encuestas (activación automática).
- Mejoras visuales y de accesibilidad en las vistas.

## 📚 Bibliografía y Recursos

- [Documentación oficial de Odoo 16](https://www.odoo.com/documentation/16.0/)
- [Widgets y vistas en Odoo](https://www.odoo.com/documentation/16.0/developer/reference/backend/views.html)
- [Stack Overflow – filtros y constraints](https://stackoverflow.com/)
- Más referencias en la [memoria del proyecto][jwz_encuestas_Jiaxin_Wei.pdf](https://github.com/user-attachments/files/20444537/jwz_encuestas_Jiaxin_Wei.pdf)
