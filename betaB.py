class fuzzyNumber:
    value = [] #Trapezoidal o Triangular

    def __init__(self, m, a, b, d):
        #Caso Triangular
        if d == None:
            self.value = [m,a,b]
        else: #Caso Trapezoidal
            self.value = [m,a,b,d]

    #De momento solo estan los casos en los que ambos son triangulares o ambos son trapezoidales
    def op_suma(self, num):
        if len(self.value) == 3 and len(num.value) == 3:
            return [self.value[0] + num.value[0], self.value[1] + num.value[1], self.value[2] + num.value[2]]
        else:
            return [self.value[0] + num.value[0], self.value[1] + num.value[1], self.value[2] + num.value[2], self.value[3] + num.value[3]]

    def op_resta(self, num):
        if(len(num.value) == 3 and len(self.value) == 3):
            return self.op_suma(fuzzyNumber(-num.value[0], -num.value[1], -num.value[2], d=None))
        else:
            return self.op_suma(fuzzyNumber(-num.value[0],-num.value[1],-num.value[2],-num.value[3]))

    def op_opuesto(self):
        if len(self.value) == 3:
            return [-self.value[0], self.value[2], self.value[1]]
        else:
            return [-self.value[0], self.value[2], self.value[1], -self.value[3]] 
    
    def op_mult(self, num):
        if len(self.value) == 3 and len(num.value) == 3:
            return [self.value[0]*num.value[0],self.value[1]*num.value[1],self.value[2]*num.value[2]]
        else:
            return [self.value[0]*num.value[0],self.value[1]*num.value[1],self.value[2]*num.value[2],self.value[3]*num.value[3]]

    def op_div(self, num):
        if(len(num.value) == 3 and len(self.value) == 3):
            return [self.value[0]/num.value[0], (num.value[1]*self.value[0] + self.value[1]*num.value[0])/num.value[0]**2, (num.value[2]*self.value[0] + self.value[2]*num.value[0])/num.value[0]**2]
        else:
            return [self.value[0]/num.value[0], (num.value[1]*self.value[0] + self.value[1]*num.value[0])/num.value[0]**2, (num.value[2]*self.value[0] + self.value[2]*num.value[0])/num.value[0]**2, (num.value[3]*self.value[0] + self.value[3]*num.value[0])/num.value[0]**2]

b1 = fuzzyNumber(m=0, a=1, b=2, d=3)
b2 = fuzzyNumber(m=1, a=2, b=0, d=3)
bSuma = b1.op_suma(b2)
bResta = b1.op_div(b2)
print(bResta)