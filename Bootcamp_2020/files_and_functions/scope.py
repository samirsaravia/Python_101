var_3 = 5
var_4 = 6


# not recommended to add global variables inside a func, just a few cases to do that.
def add_1(var_3, var_4):
    var_3 = var_3 + 1
    var_4 = var_4 + 1
    print(f'Inside the function var_3={var_3} and var_4={var_4}')
    return var_3, var_4


add_1(18, 19)
print(f'Outside the function var_3 ={var_3} and var_4={var_4}')
