class Kund:
    def __init__(self, namn = "", pNum = 0, idKund = 0):
        self.namn = namn
        self.pNum = pNum
        self.idKund = idKund
   
class Konto:
    def __init__(self, idKonto = 0, saldo = 0, senTra = ""):
        self.idKonto = idKonto
        self.saldo = saldo
        self.senTra = senTra
    
    def KopplaKonto(self, idNu = 0):
        self.idKonto = idNu
        
    def SaldoÄndra(self, saldoNy = 0):
        self.saldo = saldoNy

"""class Bank:
    def __init__(self, ):
   """     
    
        
    
        
        
    
