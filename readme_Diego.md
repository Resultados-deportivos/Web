# Documentación del Proyecto

## Descripción General

Este proyecto utiliza Python y WSGI para crear una aplicación web que gestiona información relacionada con deportes, incluyendo publicaciones, eventos, jugadores, usuarios, ligas, estadios, equipos, likes, registros, comentarios y puntos.

## Estructura de la Base de Datos
### Publicaciones
 - id: Identificador único (entero)
 - img: Ruta de la imagen (cadena de texto)
 - titulo: Título de la publicación (cadena de texto)
 - descripcion: Descripción de la publicación (cadena de texto)
### Eventos
 - id: Identificador único (entero)
 - nombre: Nombre del evento (cadena de texto)
 - fecha: Fecha del evento (fecha)
 - horainicio: Hora de inicio del evento (hora)
 - horafin: Hora de finalización del evento (hora)
 - temporada: Temporada del evento (cadena de texto)
 - idestadios: Identificador del estadio asociado (entero)
 - idliga: Identificador de la liga asociada (entero)
### Jugadores
 - id: Identificador único (entero)
 - nombre: Nombre del jugador (cadena de texto)
 - apellido: Apellido del jugador (cadena de texto)
 - fechanacim: Fecha de nacimiento del jugador (fecha)
 - equipoid: Identificador del equipo asociado (entero)
 - altura: Altura del jugador (cadena de texto)
 - peso: Peso del jugador (cadena de texto)
 - numero: Número del jugador (entero)
### Usuarios
 - id: Identificador único (entero)
 - nombre: Nombre del usuario (cadena de texto)
 - contrasena: Contraseña del usuario (cadena de texto)
 - correo: Correo electrónico del usuario (cadena de texto)
 - admin: Indicador de administrador (booleano)
### Ligas
 - id: Identificador único (entero)
 - nombre: Nombre de la liga (cadena de texto)
 - logo: Ruta del logo de la liga (cadena de texto)
 - temporadaactual: Temporada actual de la liga (entero)
 - youtube: Enlace de YouTube de la liga (cadena de texto)
 - web: Sitio web de la liga (cadena de texto)
### Estadios
 - id: Identificador único (entero)
 - localizacion: Localización del estadio (cadena de texto)
 - capacidad: Capacidad del estadio (entero)
### Equipos
 - id: Identificador único (entero)
 - nombre: Nombre del equipo (cadena de texto)
 - ciudad: Ciudad del equipo (cadena de texto)
 - logo: Ruta del logo del equipo (cadena de texto)
 - id_liga: Identificador de la liga asociada (entero)
### Likes
 - id: Identificador único (entero)
 - publicacionid: Identificador de la publicación asociada (entero)
 - usuarioid: Identificador del usuario asociado (entero)
 - likecount: Conteo de likes (entero)
### Registros
 - id: Identificador único (entero)
 - eventoid: Identificador del evento asociado (entero)
 - jugadorid: Identificador del jugador asociado (entero)
 - accion: Acción registrada (cadena de texto)
 - minuto: Minuto en que ocurrió la acción (entero)
### Comentarios
 - id: Identificador único (entero)
 - idusuario: Identificador del usuario que comentó (entero)
 - publicacionid: Identificador de la publicación asociada (entero)
 - descripcion: Descripción del comentario (cadena de texto)

## Métodos de Inserción
Se han proporcionado métodos para insertar datos en cada una de las tablas mencionadas anteriormente. Estos métodos facilitan la incorporación de nueva información al sistema.

CRUD de la Aplicación
Se ha implementado un conjunto de operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para cada entidad del sistema. Estas operaciones permiten gestionar eficientemente la información almacenada en la base de datos.

## Operaciones CRUD
1. Crear (Create)
 - insert_publicacation_data(data): Crea una nueva publicación con los datos proporcionados.
 - insert_event_data(data): Crea un nuevo evento con los datos proporcionados.
 - insert_player_data(data): Crea un nuevo jugador con los datos proporcionados.
 - insert_user_data(data): Crea un nuevo usuario con los datos proporcionados.
 - insert_league_data(data): Crea una nueva liga con los datos proporcionados.
 - insert_stadium_data(data): Crea un nuevo estadio con los datos proporcionados.
 - insert_team_data(data): Crea un nuevo equipo con los datos proporcionados.
 - insert_likes_data(data): Crea un nuevo like con los datos proporcionados.
 - insert_register_data(data): Crea un nuevo registro con los datos proporcionados.
 - insert_commentas_data(data): Crea un nuevo comentario con los datos proporcionados.
1. Leer (Read)
 - get_all_publicaciones(): Obtiene todas las publicaciones almacenadas.
 - get_all_eventos(): Obtiene todos los eventos almacenados.
 - get_all_jugadores(): Obtiene todos los jugadores almacenados.
 - get_all_usuarios(): Obtiene todos los usuarios almacenados.
 - get_all_ligas(): Obtiene todas las ligas almacenadas.
 - get_all_estadios(): Obtiene todos los estadios almacenados.
 - get_all_equipos(): Obtiene todos los equipos almacenados.
 - get_all_likes(): Obtiene todos los likes almacenados.
 - get_all_registros(): Obtiene todos los registros almacenados.
 - get_all_comentarios(): Obtiene todos los comentarios almacenados.