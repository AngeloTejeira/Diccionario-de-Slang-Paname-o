from modelo import PalabraCRUD

palabraCRUD = PalabraCRUD()
opcion = -1
while opcion != 0:
  print('========= MENU ========')
  print('[1] Mostrar')
  print('[2] Agregar')
  print('[3] Actualizar')
  print('[4] Eliminar')
  print('[5] Buscar')
  print('[0] Salir')
  opcion = int(input('Opcion: '))

  if opcion == 1:
    palabras = palabraCRUD.mostrar()
    if len(palabras) == 0:
      print('No hay palabras ingresadas!')
    else:
      for i in palabras:
        print('-'*30)
        print(f'Nombre: {i[0]}\nSignificado: {i[1]}')
  
  elif opcion == 2:
    resultado = palabraCRUD.agregar(
      nombre=input('Ingrese el nombre: '),
      significado=input('Ingrese el significado: ')
    )
    if resultado:
      print('Agregada!')

  elif opcion == 3:
    resultado = palabraCRUD.actualizar(
      nombre=input('Ingrese el nombre: '),
      significado=input('Ingrese el significado: ')
    )
    if resultado:
      print('Actualizada!')
  
  elif opcion == 4:
    resultado = palabraCRUD.eliminar(
      nombre=input('Ingrese el nombre: '),
    )
    if resultado:
      print('Eliminada!')
  
  elif opcion == 5:
    palabra = palabraCRUD.existe(
      nombre=input('Ingrese el nombre: ')
    )
    if palabra:
      print(f'Significado: {palabra[1]}')
  elif opcion == 0:
    print('Adios!')
    
  else:
    print('Opcion incorrecta!')