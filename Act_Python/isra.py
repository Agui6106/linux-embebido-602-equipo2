###################### Primera función ###################################
def my_function(x,y) -> int:
    #print(f"\n{x = }     {y = }")
    print("x = {}".format(x))
    print(f"{y = }")
    return x + y

################### Función usando args
def my_second(*args,**kwargs)->int:
    print(args[0])
    print(kwargs.get('power'))
    x = args[0]
    y = kwargs.get('power')
    return x**y

####################### Main ############################################
if __name__ == "__main__":
    print(my_function(3,4))

    print(my_function(y = 9, x = 3))    # Estamos declarando directo qué es cada valor, en vez de posicional, respetando keyword
    print('\nSecond function')
    #variables = (2,3,4)
    #print(my_function_2(*variables))
    #variable_list = [1, 2, 3]
    #variable_dict = {
    #   'var1' : 1,
    #   'var2' : 2,
    #   3      : 3,
    #}
    
    print(my_second(2,3))