from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

db_connection = {
    "database": "eusko_basket",
    "user": "admin_basket",
    "password": "Dinahosting2209@",
    "host": "pgsql03.dinaserver.com",
    "port": "5432"
}

engine = create_engine(
    f'postgresql://{db_connection["user"]}:{db_connection["password"]}@{db_connection["host"]}:{db_connection["port"]}/{db_connection["database"]}'
)
Base = declarative_base()


class Partido(Base):
    __tablename__ = 'partido'
    IDPartido = Column(Integer, primary_key=True)
    Fecha = Column(Date)
    Lugar = Column(String)
    EquipoLocalID = Column(Integer, ForeignKey('equipo.EquipoID'))
    EquipoVisitanteID = Column(Integer, ForeignKey('equipo.EquipoID'))
    Jornada = Column(Integer)


class Registro(Base):
    __tablename__ = 'registro'
    RegistroID = Column(Integer, primary_key=True)
    PartidoID = Column(Integer, ForeignKey('partido.IDPartido'))
    JugadorID = Column(Integer, ForeignKey('jugador.JugadorID'))
    MinutosJugados = Column(Integer)
    PuntosMarcados = Column(Integer)


class Jugador(Base):
    __tablename__ = 'jugador'
    JugadorID = Column(Integer, primary_key=True)
    Nombre = Column(String)
    Apellido = Column(String)
    Edad = Column(Integer)
    EquipoID = Column(Integer, ForeignKey('equipo.EquipoID'))
    Altura = Column(Integer)


class Usuario(Base):
    __tablename__ = 'usuario'
    UsuarioID = Column(Integer, primary_key=True)
    NombreUsuario = Column(String)
    Contraseña = Column(String)
    CorreoElectronico = Column(String)
    Admin = Column(Boolean)


class Acciones(Base):
    __tablename__ = 'acciones'
    AccionID = Column(Integer, primary_key=True)
    Descripcion = Column(String)


class Campos(Base):
    __tablename__ = 'campos'
    CampoID = Column(Integer, primary_key=True)
    Nombre = Column(String)
    Ubicacion = Column(String)
    Direccion = Column(String)


class Equipo(Base):
    __tablename__ = 'equipo'
    EquipoID = Column(Integer, primary_key=True)
    Nombre = Column(String)
    Ciudad = Column(String)


class Publicacion(Base):
    __tablename__ = 'publicacion'
    PublicacionID = Column(Integer, primary_key=True)
    Titulo = Column(String)
    Contenido = Column(String)
    FechaPublicacion = Column(Date)
    UsuarioID = Column(Integer, ForeignKey('usuario.UsuarioID'))


class Fechas(Base):
    __tablename__ = 'fechas'
    Fecha = Column(Date, primary_key=True)


Session = sessionmaker(bind=engine)
session = Session()
