from tkinter import *
from pacoteFormatacao.formatos import Email,Nome
from pacoteConnectMySQL.DataRedePacote import DataRede as Dr

class formulario:
    def __init__(self):
        # variables datas
        self.varName = None
        self.varEmail = None
        self.varMenssage = None

        # variables general
        self.frame_1 = None
        self.frame_2 = None
        self.frame_3 = None

        # variables frame_1 internal 
        self.frame_1Inter_2 = None
        self.frame_1Inter_1 = None

        #  variables inputs
        self.frameInput_1 = None
        self.frameInput_2 = None
        self.frameInput_3 = None

        # variable frameInput_3 internal
        self.frameInput_3Inter = None

        # buttonCode
        self.buttonCode = None

        # colors defalt

        color_1 = "#E8E8E8"
        color_2 = "#ffffff"
        colorTitle = "#464646"

        # --- CODE PROGRAM
        self.root = Tk()
        self.configWindow()
        self.struForms(color_1,color_2)
        self.textFramer_1(color_1,colorTitle)
        self.textFramer_2(color_2,colorTitle)
        self.root.mainloop()

    def configWindow(self):

        # windon visual default
        self.root.geometry("500x768")
        self.root.minsize(width=500,height=768)
        self.root.maxsize(width=1366,height=768)
        self.root.config(bg="red")

        # user config
        self.root.title('Plus Formulário')
        self.root.iconbitmap("") #MUDAR IMAGEM
    
    def struForms(self,nColor1:str,nColor2:str) -> None:

        self.frame_1 = Frame(self.root,bg=nColor1)
        self.frame_1.place(relx=0,rely=0,relwidth=10,relheight=0.30)

        self.frame_2 = Frame(self.root,bg=nColor2)
        self.frame_2.place(relx=0,rely=0.30,relwidth=10,relheight=0.70)
        
        self.frame_3 = Frame(self.frame_2,bg='green')
        self.frame_3.place(x=50,y=5,relwidth=0.080,relheight=0.96)

    def textFramer_1(self,nColor1:str,nColor2:str) -> None:

        self.frame_1Inter_1 = Frame(self.frame_1,bg=nColor1)
        self.frame_1Inter_1.place(relx=0,rely=0,relwidth=10,relheight=50)

        # title one
        textTitle_1 = Label(self.frame_1Inter_1,
                        bg=nColor1, # cor alterada para teste
                        text='Fale Com a Gente!',
                        font='Ariel 30 bold',
                        fg=nColor2)
        textTitle_1.place(x=0,y=40,width=400,height=100)
        
        self.frame_1Inter_2 = Frame(self.frame_1,bg=nColor1)
        self.frame_1Inter_2.place(relx=0,rely=0.50,relwidth=10,relheight=50)

        # title two
        textTitle_2 = Label(self.frame_1Inter_2,
                            bg=nColor1,
                            text='Por favor nos informe algumas coisas sobre você',
                            font='Ariel 15',
                            fg=nColor2,
                            anchor='sw')
        textTitle_2.place(x=21,y=-20,width=450,height=50)

    def textFramer_2(self,nColor_1:str,nColor_2:str) -> None:
        # frameInputs one
        self.frameInput_1 = Frame(self.frame_3,bg='yellow')
        self.frameInput_1.place(relx=0,rely=0,relwidth=10,relheight=0.20)

        # name box
        textName = Label(self.frameInput_1,
                        bg=nColor_1,
                        text='Nome Completo',
                        font='Ariel 13 bold',
                        fg=nColor_2,
                        anchor='sw')
        textName.place(relx=0,rely=0,relwidth=10,relheight=0.50)

        # inputName box
        inputName = Entry(self.frameInput_1,bg=nColor_1
                        ,font='Ariel 10',relief='groove',bd=1)
        inputName.place(relx=0,rely=0.50,relwidth=10,relheight=0.50)
        self.varName = inputName

        # frameInputs two
        self.frameInput_2 = Frame(self.frame_3,bg='red')
        self.frameInput_2.place(relx=0,rely=0.20,relwidth=10,relheight=0.20)

        # Email box
        textEmail = Label(self.frameInput_2,
                        bg=nColor_1,
                        text='E-mail',
                        font='Ariel 13 bold',
                        fg=nColor_2,
                        anchor='sw')
        textEmail.place(relx=0,rely=0,relwidth=10,relheight=0.50)

        # inputName box
        inputEmail = Entry(self.frameInput_2,bg=nColor_1
                        ,font='Ariel 10',relief='groove',bd=1)
        inputEmail.place(relx=0,rely=0.50,relwidth=10,relheight=0.50)
        self.varEmail = inputEmail

        # frameInputs three
        self.frameInput_3 = Frame(self.frame_3,bg='blue')
        self.frameInput_3.place(relx=0,rely=0.40,relwidth=10,relheight=0.60)
        
        # name box
        textName = Label(self.frameInput_3,
                        bg=nColor_1,
                        text='Sobre Você',
                        font='Ariel 13 bold',
                        fg=nColor_2,
                        anchor='sw')
        textName.place(relx=0,rely=0,relwidth=10,relheight=0.20)

        # inputName box
        inputMenssage = Text(self.frameInput_3,bg=nColor_1
                        ,font='Ariel 10',relief='groove',bd=1)
        inputMenssage.place(relx=0,rely=0.20,relwidth=10,relheight=0.30)
        self.varMenssage = inputMenssage

        # frameInternal

        self.frameInput_3Inter = Frame(self.frameInput_3,bg=nColor_1)
        self.frameInput_3Inter.place(relx=0,rely=0.50,relwidth=10,relheight=0.50)
        
        # button
        self.buttonCode = Button(self.frameInput_3Inter,
                                bg=nColor_1,
                                text='ENVIAR',
                                fg=nColor_2,
                                relief='groove',
                                bd=2,
                                command=self.buttonFunction)
        self.buttonCode.place(x=0,y=50,width=150,height=65)
    
    def buttonFunction(self):
        c = ""
        var_NameGet = self.varName.get()
        var_EmailGet = self.varEmail.get()
        var_MessageGet = self.varMenssage.get("1.0", "end-1c") # parametros de primeira linha a final de linha
        
        a = Email.Email.emailName(var_EmailGet)
        b = Email.Email.emailDominion(var_EmailGet)
        totalEmail = a + b

        print(c.ljust(20,'-'))
        print(f'Nome: {Nome.Nome.nome(var_NameGet)}')
        print(c.ljust(20,'-'))
        print(f'Nome do email: {Email.Email.emailName(var_EmailGet)}')
        print(c.ljust(20,'-'))
        print(f'Dominio de email: {Email.Email.emailDominion(var_EmailGet)}')
        print(c.ljust(20,'-'))
        print(f'Mensagem: {var_MessageGet}')

        Dr.staringConection(Nome.Nome.nome(var_NameGet),totalEmail,var_MessageGet)

if __name__ == '__main__':
    formulario()
