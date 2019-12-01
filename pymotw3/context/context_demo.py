class ContextImpl:
    def __init__(self):
        print('__init__()')

    def __enter__(self):
        print('__enter__()')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__()')

    def say_hello(self):
        print('ContextImpl hello...')


if __name__ == "__main__":
    with ContextImpl() as contextImpl:
        print(contextImpl.say_hello())
