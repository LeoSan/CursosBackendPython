---
name: "🐛 Bug Report"

about: "Reportar un error para ayudarnos a mejorar el proyecto."

title: "[BUG] - Descripción corta del error"

labels: bug

assignees: ""
---

## 🐛 Bug Report

### Descripción

Describe claramente el error que has encontrado. Incluye detalles sobre cómo se presenta el problema.

### Pasos para reproducir

1. Ir a '...'

2. Hacer clic en '...'

3. Describir cualquier otra acción hasta que ocurra el problema.

4. Error que aparece: '...'

### Comportamiento esperado

Describe lo que esperabas que ocurriera al realizar los pasos anteriores.

### Capturas de pantalla o registros

Si es posible, añade capturas de pantalla o registros de errores.

### Entorno

- Sistema operativo: [p. ej., Windows 10, macOS Catalina]

- Navegador y versión: [p. ej., Chrome 87, Safari 14]

- Versión del proyecto: [p. ej., 1.0.0]

### Información adicional

Cualquier otra información relevante.

En la imagen puedes ver que git está ofreciéndote tres opciones para poder hacer la fusión entre las ramas, estas tres opciones son:

git config pull.rebase false: Esta estrategia es la que git utilizará por defecto, la que git sugiere siempre, se encargará de fusionar la rama local y la remota, lo ideal es usarla para mantener el historial de cambios y francamente la más sencilla.

git config pull.rebase true: Esta opción hará que Git intente hacer un rebase que es exactamente como suena, la rama remota va a rebasar a las locales sobreescribiendo sus cambios haciendo que si la rama local quiere subir sus cambios entonces deberá hacerlos de nuevo, con una buena constancia de cambios esta estrategia es la más práctica.

git config pull.ff only: Esta opción se refiere a un fast-forward, esto ocurre cuando la rama local está por detrás en los cambios de la rama remota y los commits de esta última rama pueden aplicarse sin crear un commit de fusión. Demasiado complicado ¿no? En otras palabras, se trata de poner los cambios de la rama local por encima de los de la remota, lo que no es la mejor idea porque podría afectar los cambios de otros miembros del equipo.

Como puedes ver, cada estrategia es diferente y se adapta perfectamente a diferentes escenarios. ¿Quieres un tip final? Si tu equipo no tiene una política acerca de esto, lo ideal es que consideren usar la mecánica por defecto para así adaptarse a lo que ya sabrán que va a suceder en todos los casos.


1.
¿Qué comando usarías para clonar un repositorio desde GitHub a tu máquina local?
`git clone `
2.
¿Cuál es el propósito de `git merge` en Git?
Unir ramas en un solo historial
3.
¿Qué comando permite añadir todos los cambios en el área de preparación en un solo paso?
`git add .`
4.
Después de realizar cambios en tu repositorio local, ¿qué comando usas para actualizar el remoto?
`git pull`
REPASAR 

5.
¿Qué comando en Git muestra el historial de commits de una rama?
`git log`
6.
Al crear un nuevo repositorio en GitHub, ¿qué archivo es opcional para especificar instrucciones de instalación?
`README.md`
7.
Si deseas deshacer el último commit pero mantener los cambios en el área de preparación, ¿qué comando usarías?
`git reset --soft HEAD~1`
8.
¿Cuál es la mejor práctica al iniciar un proyecto colaborativo en GitHub?
Crear un repositorio y un archivo README con instrucciones iniciales
9.
¿Para qué se usa `git stash` en Git?
Guardar temporalmente los cambios sin hacer commit
10.
Si quieres colaborar en un proyecto público de GitHub, ¿cuál es el primer paso recomendado?
Hacer un fork del repositorio en tu cuenta
11.
¿Cuál de las siguientes opciones describe mejor la finalidad de un 'pull request' en GitHub?
Proponer cambios en el repositorio principal
12.
¿Cuál comando fusionaría todos los commits en uno solo antes de enviarlos al remoto?
`git rebase -i HEAD~`
13.
¿Qué diferencia hay entre `git reset --hard` y `git reset --soft`?
`git reset --hard` elimina los cambios, mientras que `git reset --soft` los mantiene en staging

14.
Si deseas ver los archivos modificados desde el último commit, ¿qué comando utilizarías?
`git log --since`
REPASAR 

15.
¿Cuál es la diferencia entre `git fetch` y `git pull`?
`git fetch` obtiene cambios sin aplicarlos, `git pull` los aplica automáticamente
16.
¿Qué significa el mensaje de error 'merge conflict' en Git?
Dos ramas tienen cambios en la misma línea de un archivo
17.
Si deseas eliminar una rama local que ya no necesitas, ¿qué comando utilizas?
`git branch -d `
18.
¿Qué archivo se suele usar en GitHub Pages para configurar el sitio?
`_config.yml`
19.
En GitHub Actions, ¿qué archivo define el flujo de trabajo de automatización?
`.github/workflows/.yml`
20.
Si quieres habilitar GitHub Pages en un repositorio, ¿dónde configuras el origen del contenido?
En la configuración de GitHub Pages del repositorio
21.
¿Para qué se utiliza el archivo `.github/workflows/main.yml` en GitHub Actions?
Definir los pasos para automatizar tareas como tests o despliegues
22.
¿Cuál es el propósito de una Wiki en GitHub?
Documentar el proyecto para que los colaboradores tengan información detallada
23.
Si deseas deshacer el último commit pero mantener los cambios en el área de preparación, ¿qué comando usas?
`git reset --soft HEAD~1`

24.
Si deseas ver los archivos modificados desde el último commit, ¿qué comando utilizas?
`git log --since`

REPASAR 

25.
En GitHub Actions, ¿cómo se llama el archivo YAML que define un 'job' para ejecutar pruebas?
`.github/workflows/.yml`

26. 
¿Cómo configuras GitHub Pages para desplegar desde la rama `docs` en lugar de `main`?
En la configuración de GitHub Pages, seleccionando `docs` en lugar de `main`

27.
¿Qué representa `HEAD` en Git?
La referencia al commit actual en la rama activa

28. 
¿Qué sucede si intentas hacer `push` sin permisos en el repositorio remoto?
La operación es rechazada con un mensaje de error

29. 
¿Qué ocurre cuando usas `git push origin main` en tu terminal?
Se envían los cambios locales de `main` al repositorio remoto

