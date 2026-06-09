def return_args(*args,**kwargs):
    return args,kwargs


def return_first(*args,default=None):
    if args:
        return args[0]
    else:
        return default
    return_args(1,2,a=3)
    return_first(1,2,3)