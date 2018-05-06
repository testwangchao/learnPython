def singleton(o,*args,**kwargs):
    instances = {}
    def set():
        if o not in instances:
            instances[o] = o(*args,**kwargs)
        return instances[o]
    return set

@singleton
class Demo():
    pass


if __name__ == '__main__':
    demo1 = Demo()
    demo2 = Demo()
    print(demo1==demo2)
