import sqlite3

class PalabraCRUD(object):
  """
  Clase para realizar las operaciones CRUD sobre la tabla palabra
  La tabla palabra esta compuesta por nombre y significado
  """
  def __init__(self) -> None:
    """
    Conexion autmatica a la base de datos
    """
    self.conexion = sqlite3.connect("diccionario.db")
    self.cursor = self.conexion.cursor()
  
  def mostrar(self):
    try:
      self.cursor.execute('select * from palabra')
      return self.cursor.fetchall()
    except Exception as error:
      print(error)
      return []
  def agregar(self, nombre, significado):
    try:
      if(self.existe(nombre)) == None:
        self.cursor.execute(f"insert into palabra values('{nombre}','{significado}')")
        self.conexion.commit()
        return True
      print('Error: La palabra ya existe!')
      return False
    except Exception as error:
      print(error)
      return False
  
  def actualizar(self, nombre, significado):
    try:
      if(self.existe(nombre)):
        self.cursor.execute(f"update palabra set significado='{significado}' where nombre='{nombre}'")
        self.conexion.commit()
        return True
      print('Error: La palabra no existe!')
      return False
    except Exception as error:
      print(error)
      return False

  def eliminar(self, nombre):
    try:
      if(self.existe(nombre)):
        self.cursor.execute(f"delete from palabra where nombre='{nombre}'")
        self.conexion.commit()
        return True
      print('Error: El nombre de la palabra no existe!')
      return False
    except Exception as error:
      print(error)
      return False

  def existe(self, nombre):
    try:
      self.cursor.execute(f"select * from palabra where nombre='{nombre}'")
      return self.cursor.fetchone()
    except:
      return None
