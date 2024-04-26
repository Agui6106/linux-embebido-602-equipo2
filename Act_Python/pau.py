    # En esta función podemos decir que tipo de dato es o no, sirve como ayuda para saber que recibe y que regresa
    # (x:int, y:int)
def my_function(x:int, y:int)->int:
    # Darle formato
    print("x={}".format(x))
    # (f"{}") => fstring te permite darle formato a lo que se encuentra entre las llaves
    print(f"{y=}")  # Tambien se puede poner como print(f"y={y}")
    return x+y

    #Funcion que va a tener parametros genéricos (argumentos posicionales, argumentos de llaves)
def my_function_2(*args, **kwargs)->int:
    #Tomar el primer argumento posicional que mandes
    print(args[0])
    #Toma kwargs como un diccionario y va a buscar a power
    print(kwargs.get('power'))
    x = args[0]
    y = kwargs.get('power')
    return x**y

#ORIENTADO A OBJETOS
    #Clase Padre
class Point:
    name:str = "Clase punto"
    
    def __init__(self, x:int, y:int)->None:
        self.x = x
        self.y = y

    #Clase Hija
class Point3D(Point):
     def __init__(self,x:int ,y:int ,z:int):
         self.z = z
         # 
         super().__init__(x,y)
         
    
if __name__ =='__main__':
    # Se manda los argumentos de manera posicional es decir (x, y)
    print(my_function(3,4))
    # Uso los keywords, le digo explicitamente que valor es de que variable
    print(my_function(y=9, x=3))
    
    print('second function')
    
    # Solo va a tomar el primer argumento posicional (2) que aparece(2,6,7,8,9,0), los demas los ignora
    # Solo toma el valor de llave que queremos, en este caso solo toma power
    # Debido a que especificamo que primero van los valores posicionales y despues lo de llave
    print(my_function_2(2,6,7,8,9,0,power=3,var=3))
    
    # Asi se ven algunos de los tipos de datos
    variables = (2,3,4) #This is a tuple
    variable_list = [1,2,3,4,5]
    # Las llaves tienen que llamarse como objetos inmutables
    variable_dict = {
        'var1': 1,
        'var2': 2,
        3 : 3,
    }
    xor_dist = {
        (0,0):0,
        (0,1):1,
        (1,0):1,
        (1,1):0,
    }
    print(my_function_2(*variables, power=3, var=3))
    
    # Imprime todo nuestro diccionario
    print(variable_dict)
    print("XOR(1,0)->", xor_dist[(1,0)])
    
    point1 = Point(5, 6)
    
    point2 = Point3D(4,5,6)
    
    print(point2.name)