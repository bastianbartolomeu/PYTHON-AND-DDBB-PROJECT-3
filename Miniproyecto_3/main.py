from feriados import MP3

def menuPincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print(' ')
            print(' =============== MENU ==========')
            print( '''        
    0-  Mostrar conexion correcta         
    1 - Listar Todos los Todos los Feriados
    2 - Listar Todos los Feriados irrenunciable
    3 - Listar Todas las Feriados civiles
    4 - Listar Feriados con texto Santo
    5 - listar leyes del Plebiscito
    6 - Salir
                   
==============================================
''')
            opcion = int(input(' seleccione alguna opción : '))
            if opcion < 0 or opcion > 6:
                print(' Opcion incorrecta, ingrese nuevamente ')
            else :
                opcionCorrecta = True 
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    DAO = MP3()
    
    if opcion == 1:
        DAO.todos_los_feriados()
    elif opcion == 2:
        DAO.feriados_irrenunciable()
    elif opcion== 3:
        DAO.feriados_civiles()
    elif opcion == 4:
        DAO.texto_santo()
    elif opcion == 5:    
        DAO.leyes_plebiscito()
    elif opcion == 0:
        print('LAS CONEXIONES CON MONGODB SON LAS SIGUENTES :  ')
        DAO.conexion()
    elif opcion ==6:
        print('GRACIAS POR USAR EL SISTEMA DE DIAS FERIADOS DEL AÑO 2020 CHILE ') 
        print('SALIENDO DEL SISTEMA ')
        exit()
    

if __name__ == '__main__':
    menuPincipal()
#menuPincipal()