import os

IsActive = True

while IsActive :
    print("\n 1. Administrador de Generos " ) 
    print("2.Administrador de Actores")
    print("3.Administradores de Formatos")
    print("4.Gestor de peliculas")
    print("5.Gestro de informes")
    print("6.Salir")
    try :
            Opcions = (int(input("Bienevenidos Ingrese Al Sistema")))
           
    except ValueError :
        print ("Numero Incorrecto Vuelva ingresarlo")
        
    else :
            os.system("cls")
            if Opcions == 1 :
                
                while IsActive :

    
                    print("\n 1. Gestor de genero " ) 
                    print("2.Listar genersos")
                    print("3.ir Menu principal")
                    
            
                    Opcion = int(input("Bienevenidos Ingrese Al Sistema"))
                    os.system("pause")

                    if Opcion == 1 :
                           pass
                    elif Opcion == 2 :
                           print("Bienvenido a la lista de genero")
                    elif Opcion == 3 :
                        False 
                        break
                        
                
            elif Opcions == 2 :
                os.system ("cls")
                while IsActive :
                    opmenus=("\n 1. Crear Actor " "2.Listar Actor""3.ir Menu principal")
                try : 
                        print (opmenus)
                        opmenu = int(input("Bienevenidos Ingrese Al Sistema"))
                        
                except ValueError :
                    print ("Numero Incorrecto Vuelva ingresarlo")

                else :
                        if opmenu == 1 :
                            print("Bienvenidos")
                        elif opmenu == 2 :
                            print("2bienvenidos")
                        elif opmenu == 3 :
                            print("3Bienvenidos")
                            False 
                            break
            elif Opcions == 3 :
                os.system ("cls")
                while IsActive :

                    try :
                            print("\n 1. Crear formatos " ) 
                            print("2.Listar formatos")
                            print("3.ir Menu principal")
                            
                    
                            Opcion = int(input("Bienevenidos Ingrese Al Sistema :"))
                            
                    except ValueError :
                        print ("Numero Incorrecto Vuelva ingresarlo")

                    else :
                            if Opcion == 1 :
                                print("Bienvenidos")
                            elif Opcion == 2 :
                                print("2bienvenidos")
                            elif Opcion == 3 :
                                 False 
                                 break
            elif Opcions == 4 :
                os.system ("cls")
                while IsActive :
                    try :
                            print("\n 1. Agregar pelicula " ) 
                            print("2.Editar pelicula")
                            print("3.Eliminar pelicula")
                            print("4.Eliminar Actor")
                            print("5.Buscar pelicula")
                            print("6.Usar Todas las peliculas")
                            print("7.Menu principal")
                    
                            Opcion = int(input("Bienevenidos Ingrese Al Sistema"))
                            
                    except ValueError :
                        print ("Numero Incorrecto Vuelva ingresarlo")

                    else :
                            if Opcion == 1 :
                                print("Bienvenidos")
                            elif Opcion == 2 :
                                pass
                            elif Opcion == 3 :
                                pass
                            elif Opcion == 4 :
                                pass
                            elif Opcion == 5 :
                                pass
                            elif Opcion == 6 :
                                pass
                            elif Opcion == 7 :
                                    False 
                                    break
            elif Opcions == 5 :
                os.system ("cls")
                while IsActive :

                    try :
                            print("\n1. Listar las peliculas de un genero especifico " ) 
                            print("\n2.Listar las peliculas donde el protagonista sea Silvestre Stailone")
                            print("\n3.Buscar pelicula y mostrar la sinopsis y los actores")
                            print("\n4.ir Menu principal")
                        
                    
                            Opcion = int(input("Bienevenidos Ingrese Al Sistema :"))
                            
                    except ValueError :
                        print ("Numero Incorrecto Vuelva ingresarlo")

                    else :
                            if Opcion == 1 :
                                print("Bienvenidos")
                            elif Opcion == 2 :
                                print("2bienvenidos")
                            elif Opcion == 3 :
                                 print("3Bienvenidos")
                            elif Opcion == 4 :
                                 False 
                                 break
            elif Opcions == 6 :
                False
                break