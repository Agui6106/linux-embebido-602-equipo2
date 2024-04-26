
def my_func(x:int,y:int)->int:
    print("x = {}".format(x))
    print(f"y = {y}")

def my_2nd_func(*args,**kwargs)->int:
    print(args[0])
    print(kwargs.get('power'))
    x = args[0]
    y = kwargs.get('power')

    return x**y

# Downder var
if __name__ == '__main__':
    # Argumentos de manera posicional
    print(my_func(3,4))

    # Utilizando los keywords (Digo explictamante etse es y and this is x)
    print(my_func(y=3,x=4))

    # Variables Para la funcion 2
    variables = (2,3,4)
    var_list = [1,2,3,4,5]
    var_dict = {
        'var1' : 1,
        'var2' : 2,
        3:3,
    }
    # Las llaves de un diccionario no puedne ser cambiadas

    # XOR Dicccionario
    xor_dict = {
        (0,0) : 0,
        (0,1) : 1,
        (1,0) : 1,
        (1,1) : 0,
    }

    print('Second Function')

    print(my_2nd_func(*variables,power=3,var=3))

    print(var_dict)



