class Calculator:

    def add(self, x,y):
        return x+y
    
    def mult(self, x,y):
        return x*y

    def div(self, x,y):
        if y==0 :
            raise ValueError("Cannot divide by 0")
        return x/y
