class Email:
    def __init__(self,n1):
        self.emailName(n1)
        self.emailDominion(n1)
    def emailName(n1:str) -> str:
        arroba = n1.find('@')
        varLocal_1 = n1.strip()
        varPosition = varLocal_1[0:arroba]
        return varPosition
    def emailDominion(n1:str) -> str:
        arroba = n1.find('@')
        varLocal_1 = n1.strip()
        varLocal_2 = varLocal_1.lower()
        varPosition = varLocal_2[arroba: ]
        return varPosition
    
if __name__ == '__main__':
    var = 'PietroEzioSouzaSuzao@yahoo.com'
    print(Email.emailDominion(var))