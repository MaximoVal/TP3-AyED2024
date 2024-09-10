#Trabajo Practico 2
#Santiago Felicetti, Travesani Alejo,Valvasoni Maximo, Zurdo Juan Manuel.

#--------------------------------------------------------------------------DECLARATIVA---------------------------------------------------------------------------------------------------
# TYPE
# ESTUDIANTE: Array [0..7,0..6] of string
# MODERADOR: Array [0..3,0..2] of string
# LIKES: Array [0..7,0..7] of enteros
# REPORTES: Array [0..3] of string
# EDAD: Array [0..5] of enteros



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------VARIABLES-----------------------------------------------------------------------------------------------------
# ENTEROS:cont,opc,op,opc2,opc3,oped,oped1,opb,eleccion,opce,opgu,opgu2,num,verificacion,nmatch,opu,contlike,totmatch,contmismatch,contnomatch,porcent,dado,recibido,cantest,cantmod,candidato,idmoderador,idestudiante,file,film,filasE,filasM,columE,columM,busq,busqlike,busqid,fillike,filid,FILA,reportante,reportado,like,matcheos_posibles
# STRING:me_gusta,usuario,psw,user,identificador_candidato,motivo
# FORMATO FECHA:fecha1,fecha2,fecha3,hoy
# ESTUDIANTE: E
# MODERADOR: M
# LIKES: L
# REPORTES: R
# EDAD: edades

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import getpass
import os
import datetime
import random

class Estudiante:
    def __init__ (self):
            self.nombre=['']*32
            self.mail_est=['']*32
            self.psw_est=['']*32
            self.est_estd=bool
            self.sexo=''
            self.hobby=['']*255
            self.biografia=['']*255
            self.fechanacimiento=['']*10
            self.edad=0
            self.id_est=0

class Moderador:
      def __init__(self):
            self.mail_mod=['']*32
            self.psw_mod=['']*32
            self.est_mod=bool
            self.id_mod=0

E=[None]*8
M=['']*4
L= [[random.choice([0, 1]) for i in range(8)] for j in range(8)]
R = ['']*4
edades=[21,18,20,19,23,24]

filasE=3
columE=9
filasM= 3
columM=3
cantest=0
cantmod=0
hoy=datetime.datetime.today()
      
def cargausuario(A,B):
      global cantest, cantmod
      os.system("cls")
      print('-----Carga de usuarios-----')
      print('1-Estudiante\n2-Moderador\n')
      opu = int(input("\nIngrese su opcion: ")) 
      while (opu<0 or opu>3): 
            print('Opcion incorrecta')
            opu = int(input("Ingreso nuevamente la opcion ")) 
      match opu:
                  case 1: 
                        os.system("cls")
                        print('-----CARGA ESTUDIANTES-----\n')
                        cantest=int(input('Ingrese cantidad de estudiantes a registrar(min 4 y max 8):'))
                        # while cantest<4 or cantest>8:
                        #       cantmod=int(input('Cantidad de estudiantes ingresada fuera de rango, reintente (min 4 y max 8):'))
                        for i in range (cantest):
                              A[i]=Estudiante()
                        for i in range (cantest):
                            os.system("cls")
                            print('---Cargando datos del '+str(i+1)+'° estudiante ---\n')
                            A[i].nombre=input('Ingrese nombre del '+str(i+1)+'° estudiante:')
                            A[i].mail_est=input('Ingrese el mail del '+str(i+1)+'° estudiante:')
                            A[i].psw_est=input("Ingrese la contraseña del "+str(i+1)+"° estudiante: ")
                            A[i].est_estd=True
                            # A[i].fechanacimiento=input("Ingrese el fecha de nacimieto del "+str(i+1)+"° estudiante (YYYY-MM-DD): ")
                            # A[i].fechanacimiento = datetime.datetime.strptime(A[i].fechanacimiento, "%Y-%m-%d").date()
                            # A[i].sexo=input("Ingrese el sexo del "+str(i+1)+"° estudiante: ")
                            # A[i].hobby=input("Ingrese hobby del "+str(i+1)+"° estudiante: ")
                            # A[i].biografia=input("Ingrese la biografía del "+str(i+1)+"° estudiante: ")
                            # if (hoy.month, hoy.day) < (A[i].fechanacimiento.month, A[i].fechanacimiento.day):
                            #     A[i].edad= str((hoy.year - A[i].fechanacimiento.year)-1)
                            # else:
                            #     A[i].edad=str((hoy.year - A[i].fechanacimiento.year))
                            # A[i].id_est=str(i)
                  case 2:
                        os.system("cls")
                        print('-----CARGANDO MODERADORES-----\n')
                        cantmod=int(input('Ingrese cantidad de moderadores a registrar(min 1 y max 4):'))
                        # while cantmod<1 or cantmod>4:
                        #       cantmod=int(input('Cantidad de moderadores ingresada fuera de rango, reintente (min 1 y max 4):'))
                        for i in range(cantmod):
                              B[i]=Moderador()
                       
                        for i in range (cantmod):
                              os.system("cls")
                              print('---Cargando datos del moderador'+str(i+1)+'---\n')
                              B[i].mail_mod=input("Ingrese el  mail del "+str(i+1)+"° moderador:")
                              B[i].psw_mod=input("Ingrese la contraseña del "+str(i+1)+"° moderador:")
                              B[i].est_mod=True
                              B[i].id_mod=i

def inicio():
      global op
      op=1
      cont=0
      while op!=0 :
            os.system("cls")
            print('---BIENVENIDO---\n\n')
            print('1-Registrarse\n2-Log In\n3-Bonus\n0-Cerrar programa')
            op = int(input("\nIngrese su opcion: ")) 
            while (op<0 or op>3): 
                  print('Opcion incorrecta')
                  op = int(input("Ingreso nuevamente la opcion ")) 
            match op:
                        case 1: 
                              os.system("cls")
                              cargausuario(E,M)
                        case 2: 
                                os.system("cls")
                            #   if cantest<4:
                            #         print('Cantidad minima de Estudiante incorrecta')
                            #         cartel2()
                            #         input()
                            #   elif cantmod<1:
                            #         print('Cantidad minima de Moderadores incorrecta')
                            #         cartel2()
                            #         input()
                            #   else:
                                login(E,M)
                        case 3:
                              os.system("cls")
                              print('1-Bonus 1\n2-Bonus 2\n3-Salir')
                              opb = int(input("\nIngrese su opcion: ")) 
                              while (opb<1 or opb>3): 
                                    print('Opcion incorrecta')
                                    opb = int(input("Ingreso nuevamente la opcion ")) 
                              match opb:

                                    case 1:
                                          os.system("cls")
                                          BONUS1(edades)
                                    case 2:
                                          os.system("cls")
                                          if cantest<1:
                                                print('No hay usuarios ingresados')
                                                cartel2()
                                                input()
                                          else:
                                                BONUS2(cantest)
                                                cartel2()
                                                input()
                        
                        case 0: print('\n\n ---FIN DEL PROGRAMA---')        

def busqueda(A,B,usuario):
      global file, film
      file=0
      film=0

      while A[file].mail_est!= usuario and file<(cantest-1):
            file=file+1
      
      while B[film].mail_mod!= usuario and film<(cantmod-1):
            film=film+1

      if A[file].mail_est!= usuario:
            if B[film].mail_mod== usuario:
                  busq=2
            else:
                  busq=-1
      else:
            busq=1
      
      return busq

def busquedalike(A,usuario):
      fillike=0

      while A[fillike][8]!= usuario and fillike<(cantest-1):
            fillike=fillike+1
      
      if A[fillike][8]== usuario:
            busqlike=fillike
      else:
            busqlike=-1
      
      return busqlike

def busquedaid(A,ID):
      global filid
      filid=0

      while A[filid][8]!= ID and filid<(cantest-1):
            filid=filid+1
      
      if A[filid][8]== ID:
            busqid=1
      else:
            busqid=-1
      
      return busqid

def login(A,B):
      global usuario, psw
      cont=0
      os.system("cls")
      print('---LOG IN---\n\n')
      usuario = input('Ingrese su mail:')
      psw=getpass.getpass('Ingrese su contraseña:')
      opc=1
      eleccion=1
      FILA=busqueda(A,B,usuario)
      print('Busqueda:',FILA)
      while  cont<3 and opc!=0 and eleccion!=3: 
            if FILA!=-1:
                  if FILA==1 :
                        if A[file].est_estd==True and op!=0 and cont<3 and opc!=0:
                            if A[file].psw_est==psw:
                                                MENU()
                                                opc = int(input("\nIngrese su opcion: ")) 
                                                while (opc<0 or opc>4) and op!=0: 
                                                      print('Opcion incorrecta')
                                                      opc = int(input("Ingreso nuevamente la opcion ")) 
                                                match opc: 
                                                      case 1: GEST_PERFIL(A)
                                                      case 2: GEST_CANDIDATOS()
                                                      case 3:
                                                            os.system("cls")
                                                            print('---MATCHEOS---')
                                                            CARTEL()
                                                            cartel2()
                                                            input()
                                                      case 4:
                                                            os.system("cls")
                                                            print('---Reportes Estadisticos---')
                                                            REPORTES(L[:])
                            else:
                                    if cont<2:
                                          print('Contraseña o usuario incorrectos-Reintente(quedan',2-cont,'intentos)')
                                          usuario = input('Ingrese su mail:')
                                          psw=getpass.getpass('Ingrese su contraseña:')
                                          cont=cont+1
                                    else:
                                          print('Ha excedido el número de intentos')
                                          cont=cont+1
                                          cartel2()
                                          input()
                        else:
                              A[file].est_estd==bool(0) and op!=0 and opce!=2
                              print('No se puede iniciar sesion debido a que el estado del estudinte esta Inactivo')
                              cartel2()
                              opc=0
                              input()
                        
                  else:
                        os.system("cls")
                        eleccion=1
                        while op!=0 and eleccion!=3 and opc!=0:
                              os.system("cls")
                              print('-----------------Moderador---------------------------\n\n')
                              eleccion = int(input("1_Gestionar usuarios\n2 Gestionar reportes\n3_Volver\n\nIngrese una opcion:"))
                              while (eleccion<1 or eleccion>3):
                                    eleccion = int(input("Ingrese una opcion correcta:"))
                              match eleccion:
                                    case 1:
                                          desactivarusuario(E)
                                    case 2:
                                          VERREPORTES(E,R)
            else:
                                    if cont<2:
                                          print('Contraseña o usuario incorrectos-Reintente(quedan',2-cont,'intentos)')
                                          usuario = input('Ingrese su mail:')
                                          psw=getpass.getpass('Ingrese su contraseña:')
                                          cont=cont+1
                                          FILA=busqueda(A[:],B[:],usuario)
                                    else:
                                          print('Ha excedido el número de intentos')
                                          cont=cont+1
                                          cartel2()
                                          input()                     
                   
def MENU():
      os.system("cls")
      print('------MENU PRINCIPAL------')
      print('1-Gestionar mi perfil ')
      print('2-Gestionar candidatos ')
      print('3-Matcheos ')
      print('4-Reportes estadisticos ')
      print('0-Salir')

def SUBMENU1():
      os.system("cls")
      print('---Gestion de perfil---')
      print('1-Editar mis datos personales ')
      print('2-Eliminar mi perfil')
      print('3-Volver ')

def SUBMENU2():
      os.system("cls")
      print('---Gestion de candidatos---')
      print('1-Ver candidatos')
      print('2-Reportar candidatos')
      print('3-Volver ')

def CARTEL(): 
      print('-----En construcción-----') 

def cartel2():
      print('\nPresione enter para volver')

def  desactivarusuario (E):
      verificacion=0
      user=''
      opgu=1
      opgu2=1
      os.system("cls")
      print('-----------------Gestion de usuario-----------------------')
      opgu = int(input("1_Desactivar usuarios\n2_Volver\n\nIngrese opcion:"))
      while opgu<1 or opgu>2:
            opgu = int(input("Ingrese opcion\n1_Desactivar usuarios\n2_Volver:"))
      while opgu!=2:
                  os.system("cls")
                  print('-----------------Desactivacion de usuario----------------\n\n')
                  user = input("Ingrese ID de usuario: ")
                  verificacion = busquedaid(E, user)
                  if verificacion==1:
                        print('Desea eliminar el perfil:\n1_Si\n2_No')
                        opgu2 = int(input("\nIngrese su opcion: "))
                        while (opgu2<1 or opgu2>2): 
                                    print('Opcion incorrecta')
                        match opgu2:
                              case 1:
                                    E[file][2]='Inactivo'
                                    print('Estado actualizado a : ',E[file][2])
                                    cartel2()
                                    input()
                                    opgu=2
                  else:
                        print('Usuario incorrecto')

def VERREPORTES (E,R):

      num=1
      while num!=2:
            os.system("cls")
            print('---------Gestion reportes-------\n\n')
            num = int(input("1_Ver reportes\n2_Volver\n\nIngrese opcion: "))
            while num<1 or num>2:
                  num = int(input("Ingrese opcion una correcta: "))
            match num:
                  case 1:     
                              os.system("cls")
                              print('--------------REPORTES--------------\n')
                              if R[0]=='':
                                    print('No hay reportes efectuados')
                                    cartel2()
                                    input()
                              else: 
                                    reportante=R[0]
                                    reportado=R[1]
                                    reportante=int(reportante)
                                    reportado=int(reportado)
                                    while E[reportado][2]=='Activo' and E[reportante][2]=='Activo':
                                          if R [3]=='0':   
                                                print('Reporte efectuado por usuario de ID:',R[0])
                                                print('Reporte dirigido hacia el usuario de ID:',R[1])
                                                print('Motivo del reporte:',R[2])
                                                reporte=int(input('Que quiere hacer con dicho reporte\n1_ Ignorar\n2_Bloquear\n\nIngrese una opcion:'))
                                                while reporte<1 or reporte>2:
                                                      reportante=int(input('Ingrese una opcion valida'))
                                                if reportante==1:
                                                      R[3]='2'
                                                      print('Reporte ignorado')
                                                      cartel2()
                                                      input()
                                                else:
                                                      R[3]='1'
                                                      E[reportado][2]='Inactivo'
                                                      print('Estudiante bloqueado')
                                                      cartel2()
                                                      input()

def GEST_PERFIL(A):
      global opce
      opc2=1
      while opc2!=3:
            SUBMENU1()
            opc2 = int(input("\nIngrese su opcion: ")) 
            while (opc2<1 or opc2>3): 
                  print('Opcion incorrecta')
                  opc2 = int(input("Ingreso nuevamente la opcion ")) 
            match opc2:
                  case 1: 
                        os.system("cls")
                        print('---Edicion de datos personales---\n')
                        EDICIONDATOS(A)  
                  case 2:
                        opce=1
                        while opce!=2:
                              os.system("cls")
                              print('---Eliminacion de perfil---\n')
                              print('Desea eliminar su perfil:\n1_Si\n2_No')
                              opce = int(input("\nIngrese su opcion: ")) 
                              while (opce<1 or opce>2): 
                                    print('Opcion incorrecta')
                                    opce = int(input("Ingreso nuevamente la opcion ")) 
                              match opce:
                                    case 1: 
                                          E[file][2]='Inactivo'
                                          print('Estado actualizado a : ',E[file][2])
                                          print('Al ser eliminado el perfil, se cierra sesión')
                                          cartel2()
                                          input()
                                          opc=0
                                          opce=2
                                          opc2=3

def EDICIONDATOS(A):
      oped=1
      while oped!=2:
            os.system("cls")
            print('Sus datos actuales:\n')
            for j in range (columE):
                                          
                        if j==3:
                              print('Fecha de nacimiento:',str(A[file][j]))                         
                        elif j==4:
                              print('Sexo:',A[file][j])
                        elif j==5:
                              print("Hobby:",A[file][j])
                        elif j==6:
                              print("Biografia:",A[file][j])
                        elif j==7:
                              print("Edad:",A[file][j])
                        elif j==8:
                              print("ID:",A[file][j])
            print('\nDeseas modificar tus datos: \n1_Si\n2_No')
            oped = int(input("\nIngrese su opcion: ")) 
            while (oped<1 or oped>2): 
                  print('Opcion incorrecta')
                  oped = int(input("Ingreso nuevamente la opcion ")) 
            match oped:
                  case 1:
                        oped1=1
                        while oped1!=5:
                              os.system("cls")
                              print('\nQue dato desea modificar: \n1_Fecha de nacimiento\n2_Sexo\n3_Hobby\n4_Biografia\n5_Volver')
                              oped1 = int(input("\nIngrese su opcion: ")) 
                              while (oped1<1 or oped1>5): 
                                    print('Opcion incorrecta')
                                    oped1= int(input("Ingreso nuevamente la opcion ")) 
                              match oped1:
                                    case 1:
                                          A[file][3]=input("Ingrese fecha de nacimieto (YYYY-MM-DD): ")
                                          A[file][3] = datetime.datetime.strptime(A[file][3], "%Y-%m-%d").date()
                                          if (hoy.month, hoy.day) < (A[file][3].month, A[file][3].day):
                                                A[file][7]= str((hoy.year - A[file][3].year)-1)
                                          else:
                                                A[file][7]=str((hoy.year - A[file][3].year))
                                          print('Fecha de nacimiento actualizada')
                                          cartel2()
                                          input()

                                    case 2:
                                          A[file][4]=input("Ingrese el sexo : ")
                                          print('Sexo actualizado')
                                          cartel2()
                                          input()
                                    case 3:
                                          A[file][5]=input("Ingrese Hobby : ")
                                          print('Hobby actualizado')
                                          cartel2()
                                          input()
                                    case 4: 
                                          A[file][6]=input("Ingrese Biofrafia : ")
                                          print('Biografia actualizada')
                                          cartel2()
                                          input()
                                    
def matchtotal(L):
    contlike=0
    for i in range (cantest):
        if L[file][i]==1 and i!=file:
            if L[i][file]==1:
                contlike=contlike+1
                print('El estudiante',str(i),'matcheo con nosotros')
      
    
    totmatch=(contlike/(cantest-1))*100
    return totmatch

def matchdado(L):
      contmismatch=0
      for i in range (cantest):
            if L[file][i]==1 and i!= file:
                  if L[i][file]==0:
                        contmismatch=+1
      return contmismatch

def matchrecibido(L):
      contnomatch=0
      for i in range (cantest):
            if L[file][i]==0 and i!= file:
                  if L[i][file]==1:
                        contnomatch=contnomatch+1
      
      return contnomatch

def REPORTES(L):
      porcent=matchtotal(L[:])
      dado=matchdado(L[:])
      recibido=matchrecibido(L[:])
      print('Matcheados sobre el % posible es: ',str(porcent)+'%')
      print('Likes dados y no recibidos: ',dado)
      print('Likes recibidos y no respondidos: ',recibido)
      cartel2()
      input()

def reportar_candidato(R):
      identificador_candidato = input("Ingresar el ID del usuario a reportar:")
      motivo = input("Ingrese el motivo del reporte:")

      candidato = busquedaid(E[:],identificador_candidato) 
      if candidato!=-1:
            R[0]=file
            R[1]=filid
            R[2]=motivo
            R[3]='0'
            print("Reporte registrado exitosamente.")
            cartel2()
            input()
      else: 
            print('El usuario que intentas reportar no existe')
            cartel2()
            input()   

def GEST_CANDIDATOS():
      opc3=1
      while opc3!= 3 and op!=0  :   
            SUBMENU2()
            opc3 = int(input("\nIngrese su opcion: ")) 
            while (opc3<1 or opc3>3): 
                  print('Opcion incorrecta')
                  opc3 = int(input("Ingreso nuevamente la opcion: ")) 
            match opc3:
                  case 1: 
                         os.system("cls")
                         print('---Candidatos---\n')
                         CANDIDATOS(E[:],L)
                         cartel2()
                         input()
                  case 2:
                        os.system("cls")
                        print('---Reportar candidatos---\n')
                        reportar_candidato(R)

def CANDIDATOS(A,L):
      for i in range (cantest):
            if i!= file: 
                  print('---- Estudiante '+str(i+1)+'-------\n')
                  print('Nombre de usuario: ',A[i][0])
                  print('Fecha de nacimiento: ',A[i][3])
                  print('Sexo: ',A[i][4])
                  print('Hobby: ', A[i][5])
                  print('Biografia: ',A[i][6])
                  print('Edad: ',A[i][7])
                  print('ID: ',A[i][8])
                              
      me_gusta=input('ID del estudiante quieres matchear: ')
      like=busquedalike(E[:],me_gusta)
      while like<0:
            print('Nombre incorrecto-Reintente')
            me_gusta=input('Con que estudiante quieres matchear: ')
      print('Match realizado con exito')
      L[file][like]=1
                        

def BONUS1(edades):

      for i in range (6):
            j=i+1
            for j in range (6):
                  if edades[i]<edades[j]:
                        aux=edades[i]
                        edades[i]=edades[j]
                        edades[j]=aux
    

      hueco=0
      huecos=[0]*6
      j=0
      for i in range (5):
            if edades[i]+1!=edades[i+1]:
                  hueco=hueco+1
                  huecos[j]=edades[i]+1
                  j=j+1
      print(' Dado el reporte: ')
      for i in range (6):
            print(edades[i])
      print('Se encontraron '+str(hueco)+' huecos en la matriz')
      print('Los numeros faltantes son:')
      for i in range (hueco):
            print(huecos[i])
      cartel2()
      input()

def BONUS2(estudiantes):
      

      matcheos_posibles = estudiantes * (estudiantes - 1) // 2
      

      print("Número de estudiantes ",estudiantes)
      print("Cantidad de matcheos posibles",matcheos_posibles)

#INICIO DEL PROGRAMA PRINCIPAL

inicio()