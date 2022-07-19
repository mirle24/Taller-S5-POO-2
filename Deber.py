from datetime import date
import os
class Empresa:
  def __init__(self,ruc,nombre,telefono,dir,correo):
    self.ruc=ruc
    self.nombre=nombre
    self.tel=telefono
    self.direccion=dir
    self.correo=correo
class Usuario:
  def __init__(self, nombre, cedula, telefono, direccion, correo):
    self.nombre=nombre
    self.cedula=cedula
    self.tel=telefono
    self.direccion=direccion
    self.correo=correo
  def mostrarUsuario(self):
    print(f"Usuario: {self.cedula} {self.nombre} {self.correo}")

class Cliente(Usuario):
  def __init__(self, nombre, cedula, telefono, direccion, correo): 
        super().__init__(nombre, cedula, telefono, direccion, correo)
  def mostrarCliente(self):
    print(f"""Cliente: {self.nombre:15} {self.tel:15} Cedula: {self.cedula}
Direccion: {self.direccion:29} Correo: {self.correo}""")

class Administrador(Usuario):
  def __init__(self, nombre, cedula, telefono, direccion, correo):
        super().__init__(nombre, cedula, telefono, direccion, correo)   

  def mostrarAdministrativo(self):
    print(f"""Administrativo: {self.nombre:24} Cedula: {self.cedula} {self.tel} 
Direccion: {self.direccion:29} Correo: {self.correo}""")


from abc import ABC, abstractclassmethod 
class Usuario(ABC): 
  def __init__(self,nombre, cedula, telefono, direccion, email):
    self.nombre=nombre
    self.cedula=cedula
    self.telefono=telefono
    self.direccion=direccion
    self.correo=email
  @abstractclassmethod  
  def mostrarUsuario(self):
    print(f"Usuario: {self.nombre} {self.cedula} {self.correo}") 
class Rol:
  def __init__(self,id,descr,est):
    self.id=id
    self.descr=descr
    self.est=est
  def mostrarRol(self):
    print(self.id, self.descr, self.est)
class Modulo:
  _transaccion=0
  def __init__(self, mod):
    Modulo._transaccion += 1
    self._transaccion="#09000-"+str(Modulo._transaccion)
    self.fecha = date.today()
    self.mod = mod
  def agregarDetalle(self, cod,descr,value,esta,cupo,crear):
        self.cod=cod
        self.descr=descr
        self.value=value
        self.esta=esta
        self.cupo=cupo
        self.crear=crear
  def mostrarModuloAdministrativo(self, nomb, ruc):
        print("*"*39,"Ver pagos","*"*39)
        print("Empresa: {:30}  Ruc: {} ".format(nomb, ruc))
        print(f"Transaccion:{self._transaccion:29}Fecha: {self.fecha}")
        self.mod.mostrarAdministrativo()
        print("*"*89)
        print("Código transaccion         Descripcion        Monto   Estado  Agregar cupo de la tarjeta")
        print(f"{self.cod:22} {self.descr:23} {self.esta:6} {self.value:13} {self.cupo}")
        print("*"*89)
  def modificarFechaPago(self, nomb, ruc):
        print("*"*39,"Modificar fecha de pago","*"*39)
        print("Empresa: {:30}  Ruc: {} ".format(nomb, ruc))
        print(f"Transaccion:{self._transaccion:29}Fecha: {self.fecha}")
        self.mod.mostrarAdministrativo()
        print("*"*89)
        print("Código transaccion       Descripcion        Monto   Estado     Fecha de pago")
        print(f"{self.cod:22} {self.descr:22} {self.esta:5} {self.value:13} {self.fecha}")
        print("*"*89)
  def crearFactura(self, nomb, ruc):
        print("*"*39,"Crear factura","*"*39)
        print("Empresa: {:30}  Ruc: {} ".format(nomb, ruc))
        print(f"Transaccion:{self._transaccion:29}Fecha: {self.fecha}")
        self.mod.mostrarAdministrativo()
        print("*"*89)
        print("Código transaccion         Descripcion        Monto   Estado     Agregar factura")
        print(f"{self.cod:22} {self.descr:23} {self.esta:6} {self.value:13} {self.crear}")
        print("*"*89)
  def mostrarFechaPago(self, nomb, ruc):
        print("*"*39,"Fecha de pago","*"*39)
        print("Empresa: {:30}  Ruc: {} ".format(nomb, ruc))
        print(f"Transaccion:{self._transaccion:29}Fecha: {self.fecha}")
        self.mod.mostrarCliente()
        print("*"*89)
        print("Código transaccion       Descripcion        Monto   Estado     Fecha de pago")
        print(f"{self.cod:22} {self.descr:22} {self.esta:5} {self.value:13} {self.fecha}")
        print("*"*89)
  def mostrarModuloCliente(self, nomb, ruc):
        print("*"*33,"Pagar","*"*33)
        print("Empresa: {:30}  Ruc: {} ".format(nomb, ruc))
        print(f"Transaccion: {self._transaccion:27} Fecha:  {self.fecha}")
        self.mod.mostrarCliente()
        print("*"*74)
        print("Código transaccion         Descripcion          Monto         Estado  ")
        print(f"{self.cod:22} {self.descr:26} {self.esta:10} {self.value:9}")
        print("*"*74)
  def mostrarServicio(self, nomb, ruc):
        print("*"*33,"Servicio","*"*33)
        print("Empresa: {:30}  Ruc: {} ".format(nomb, ruc))
        print(f"Transaccion: {self._transaccion:27} Fecha:  {self.fecha}")
        self.mod.mostrarCliente()
        print("*"*74)
        print("Código transaccion         Descripcion          Monto         Estado  ")
        print(f"{self.cod:22} {self.descr:26} {self.esta:10} {self.value:9}")
        print("*"*74)
while True:
    
    print()
    print("Banca Movil Pichincha")
    print("""
Tipos de usuarios

1) Cliente
2) Administrador
3) Salir
    """)
    opc= input("Ingrese su rol en nuetra empresa: ")
    if opc =='1':
        os.system("cls")
        print("Bienvenido usuario: Cliente")
        print("1) Pagar ")
        print("2) Fecha pago")
        print("3) Servicio")
        print("4) Regresar")
        print("5) Presione cualquier tecla para salir")
        opc2=input("Seleccione la operacion que desea realizar: ")
        if opc2 == '1':
            os.system("cls")
            empresa1 = Empresa("0907067890","Banco Pichincha", "0835363232", "Milagro", "josd@hotmail.com") 
            cliente = Cliente("Alexander", "0904091100","","Guayaquil","amorenom@unemi.edu.ec") 
            modulo = Modulo(cliente)
            modulo.agregarDetalle("0905","Pago tarjeta credito","Cancelado","$20","","")      
            modulo.mostrarModuloCliente(empresa1.nombre,empresa1.ruc)
            opc3=input("Seleccione cualquier tecla para regresar al menu principal: ")
            if opc3 ==opc3:
                os.system("cls")
            else:
                os.system("cls")
                print("Opcion no valida... inserte una opcion valida")
        elif opc2 =='2':
            os.system("cls")
            empresa1 = Empresa("0907067890","Banco Pichincha", "0835363232", "Milagro", "josd@hotmail.com") 
            cliente = Cliente("Alexander", "0904091100","","Guayaquil","amorenom@unemi.edu.ec") 
            modulo = Modulo(cliente)
            modulo.agregarDetalle("0905","Pago tarjeta credito","Por pagar","$20","","")      
            modulo.mostrarFechaPago(empresa1.nombre,empresa1.ruc)
            opc3=input("Seleccione cualquier tecla para regresar al menu principal: ")
            if opc3 ==opc3:
                os.system("cls")
            else:
                os.system("cls")
                print("Opcion no valida... inserte una opcion valida")
        elif opc2=='3':
              os.system("cls")
              empresa1 = Empresa("0907067890","Banco Pichincha", "0835363232", "Milagro", "josd@hotmail.com") 
              cliente = Cliente("Alexander", "0904091100","","Guayaquil","amorenom@unemi.edu.ec") 
              modulo = Modulo(cliente)
              modulo.agregarDetalle("0905","Pago tarjeta credito","Activo","$20","","")      
              modulo.mostrarServicio(empresa1.nombre,empresa1.ruc)
              opc3=input("Seleccione cualquier tecla para regresar al menu principal: ")
              if opc3 ==opc3:
                  os.system("cls")
              else:
                  os.system("cls")
                  print("Opcion no valida... inserte una opcion valida")
        elif opc2=='4':
              os.system("cls")
        elif opc2==opc2:
            os.system("cls")
            print("Gracias por utilizar nuestro servicio")
            break
        else:
            os.system("cls")
            print("Opcion no valida... favor ingrese una opcion valida")
    elif opc =='2':
        os.system("cls")
        print(f"Bienvenido usuario: Administrador")
        print("1) Ver pagos")
        print("2) Modificar fecha de pago")
        print("3) Crear factura")
        print("4) Regresar")
        print("5) Presione cualquier tecla para salir")
        opc4=input("Seleccione la operacion que desea realizar: ")
        if opc4 == '1':
            os.system("cls")
            empresa = Empresa("0907067890","Banco Pichincha", "0835363232", "Milagro", "josd@hotmail.com") 
            administrador = Administrador("Steven", "09039103901","","Duran","suruchimam@unemi.edu.ec")
            modulo = Modulo(administrador)
            modulo.agregarDetalle("0905","Pago tarjeta credito","Pagado","$20","[+]$250[-]","")
            modulo.mostrarModuloAdministrativo(empresa.nombre,empresa.ruc)
            opc5=input("Seleccione cualquier tecla para regresar al menu principal: ")
            if opc5 ==opc5:
                os.system("cls")
                
            else:
                os.system("cls")
                print("Opcion no valida... inserte una opcion valida")
        elif opc4 =='2':
            os.system("cls")
            empresa = Empresa("0907067890","Banco Pichincha", "0835363232", "Milagro", "josd@hotmail.com") 
            administrador = Administrador("Steven", "09039103901","","Duran","suruchimam@unemi.edu.ec")
            modulo = Modulo(administrador)
            modulo.agregarDetalle("0905","Proximo pago","Pendiente","$20","19/07/2022","")
            modulo.modificarFechaPago(empresa.nombre,empresa.ruc)
            opc7=input("Seleccione cualquier tecla para regresar al menu principal: ")
            if opc7 ==opc7:
                os.system("cls")
            else:
                os.system("cls")
                print("Opcion no valida... inserte una opcion valida")
        elif opc4=='3':
              os.system("cls")
              empresa = Empresa("0907067890","Banco Pichincha", "0835363232", "Milagro", "josd@hotmail.com") 
              administrador = Administrador("Steven", "09039103901","","Duran","suruchimam@unemi.edu.ec")
              modulo = Modulo(administrador)
              modulo.agregarDetalle("0905","Proximo pago","Pendiente","$20","","[+]Crear")
              modulo.crearFactura(empresa.nombre,empresa.ruc)
              opc7=input("Seleccione cualquier tecla para regresar al menu principal: ")
              if opc7 ==opc7:
                  os.system("cls")
              else:
                  os.system("cls")
                  print("Opcion no valida... inserte una opcion valida")
        elif opc4=='4':
              os.system("cls")
        elif opc4==opc4:
            os.system("cls")
            print("Gracias por utilizar nuestro servicio")
            break
        else:
            os.system("cls")
            print("Opcion no valida... favor ingrese una opcion valida")
    elif opc =='3':
        os.system("cls")
        print("Gracias por utilizar nuestro servicio")
        break
    else:
        os.system("cls")
        print("Opcion invalida... por favor digite una opcion correcta")
