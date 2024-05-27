class Senha:
    def __init__(self,n1):
        self.senha(n1)
    def senha(n1:str) -> str:
        varLocal_1 = n1.strip()
        if (len(varLocal_1) > 6):
            return 'error'
        elif (len(varLocal_1) <= 0):
            return 'error'
        else:
            return varLocal_1
        
if __name__ == '__main__':
    var = '123Fas  '
    print(Senha.senha(Senha,var))