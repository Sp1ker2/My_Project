def greet2(name):
    print('how are you? '+name)
    greet2(name)
    def bye():
        print('bye')
def greet(name):
    print('hello '+name)
    greet2(name)
    print('bye')
    # bye()
greet('ss')