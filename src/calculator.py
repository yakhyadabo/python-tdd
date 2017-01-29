class Calculator:

    def add(self, x,y):
        return x+y
    
    def mult(self, x,y):
        return x*y

    def div(self, x,y):
        if y==0 :
            raise ValueError("Cannot divide by 0")
        return x/y

    def fact(self, n):
        if n==0:
            return 1
        else:
            return n * self.fact(n-1)


if __name__ == '__main__':
    print "Calculator.main()"
