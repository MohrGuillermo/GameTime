# GameTime
Actualmente está lista la logica de la pagina (formularios, registro, login, logout etc), lo que sigue es buscar una plantilla de bootstrap
y empezar a preparar el template 'Padre'. 
Tuve algunos inconvenientes con los permisos de usuario (@login_request) asi que por ahora decidi prescindir de esa herramienta para no atrasarme
hasta lograr entenderla bien. 

El objetivo de la pagina es elaborar un entorno donde el usuario pueda realizar las siguientes acciones: 
- Generar y buscar FAQ'S acerca de los servicios brindados (alquiler de juegos para eventos)
- Rellenar un formulario de contacto para poder adquirir alguno de los servicios.
- Ver un listado de los eventos realizados.
- Ver un listado de los juegos disponibles con sus respectivas especificaciones. 

Por ahora no supe diferenciar el perfil de usuario del de administrador y en base a eso generar vistas diferentes para cada uno de ellos. Es por eso que 
(al menos temporalmente) decidi que voy a usar las vistas de logueo unicamente para el administrador y desarrolladores.
De ésta manera el administrador podrá realizar las siguientes acciones:
- Usar todos los CRUDS de FAQ'S
- Usar todos los CRUDS de events
- Usar todos los CRUDS de games
- Crear, eliminar, buscar y editar usuarios
- Crear, eliminar, buscar y editar eventos realizados
- Crear, eliminar, buscar y editar contactos de usuarios, que se guardaran como models en la base de datos, dado que pertenecen a una CreateView


Es probable que me falten algunas cosas dado que no hice una planificacion tan minuciosa, porque hay algunas cosas que no me acuerdo entonces prefiero ir 
incorporando las cosas a medida que recuerdo lo que se o aprendo cosas nuevas.
