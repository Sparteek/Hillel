def print_arg(*args):
    print(type(args))  # tuple()
    list_elements = list(args)
    list_str_elements = []

    for arg in list_elements:
        if isinstance(arg, str):
            list_str_elements.append(arg)
            print(arg)

    return list_str_elements


print(print_arg('123','test',1,2,3,4,5,6,7,8,8,8,8))


def print_kwargs(**kwargs):
    print(type(kwargs))  # tuple()
    print(kwargs)

print_kwargs(name="Bob", age=12, list_values =[1,23,54433,34535,433], dict_values={1: 2})
