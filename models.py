from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

db_connection = {
    "database": "eusko_basket",
    "user": "admin_basket",
    "password": "Reto@123",
    "host": "pgsql03.dinaserver.com",
    "port": "5432"
}

engine = create_engine(
    f'postgresql://{db_connection["user"]}:{db_connection["password"]}@{db_connection["host"]}:{db_connection["port"]}/{db_connection["database"]}'
)

Base = declarative_base()


class Publicacion(Base):
    __tablename__ = 'Publicaciones'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Img = Column(String(255))
    Titulo = Column(String(255))
    Descripcion = Column(String(255))


class Comentario(Base):
    __tablename__ = 'Comentarios'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Idusuario = Column(Integer, ForeignKey('Usuarios.Id'))
    Publicacionid = Column(Integer, ForeignKey('Publicaciones.Id'))
    Descripcion = Column(Text)


class Like(Base):
    __tablename__ = 'Likes'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Publicacionid = Column(Integer, ForeignKey('Publicaciones.Id'))
    Usuarioid = Column(Integer, ForeignKey('Usuarios.Id'))
    LikeCount = Column(Integer)


if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(Publicacion).all()
    for result in results:
        print(
            f"Id: {result.Id}, Img: {result.Img.decode('latin-1')}, Titulo: {result.Titulo.decode('latin-1')}, Descripcion: {result.Descripcion.decode('latin-1')}")

    for result in results:
        try:
            img = result.Img.decode('utf-8')
            titulo = result.Titulo.decode('utf-8')
            descripcion = result.Descripcion.decode('utf-8')
            print(f"Id: {result.Id}, Img: {img}, Titulo: {titulo}, Descripcion: {descripcion}")
        except UnicodeDecodeError as e:
            print(f"Error decoding data: {e}")

