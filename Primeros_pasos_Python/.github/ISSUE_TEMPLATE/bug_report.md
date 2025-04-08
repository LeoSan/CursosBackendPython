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