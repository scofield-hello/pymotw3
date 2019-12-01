class ContextImpl:
    def __init__(self, handle_error: bool = True):
        print('__init__()')
        self.handle_error = handle_error

    def __enter__(self):
        print('__enter__()')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__()')
        print(' exc_type =', exc_type)
        print(' exc_val =', exc_val)
        print(' exc_tb =', exc_tb)
        # 如果 返回 True 则异常不再传播，如果返回 False,则在__exit__()之后继续抛出
        return self.handle_error

    def say_hello(self):
        print('ContextImpl hello...')


if __name__ == "__main__":
    with ContextImpl(handle_error=False) as contextImpl:
        print(contextImpl.say_hello())
        raise ValueError("ContextImpl value error.")
