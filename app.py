

class App:
    pass

def create_app():
    app = App()
    return app

def app(a,b):
    print(f"{a},{b}")
    return bin(f"hi => a:{a};b:{b}")