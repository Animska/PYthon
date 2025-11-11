class Mates:
    @staticmethod
    def mayor(num1,num2):
        return max(num1,num2)
    
    @staticmethod
    def producto(num1,num2,num3):
        return num1*num2*num3
    
    @staticmethod
    def potencia(num1,exponente):
        return num1**exponente

print(Mates.mayor(5,6))
print(Mates.producto(5,6,2))
print(Mates.potencia(2,3))