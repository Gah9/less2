my_list = [12, None, -50, 'True', True, 8.5]
def my_type(el) :
    for el in range(len(my_list)) :
        print(type(my_list[el]))
        return
    my_type(my_list)