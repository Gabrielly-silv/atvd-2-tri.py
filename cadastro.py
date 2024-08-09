class Cadastro:
    def __init__(self,nome,idade,sexo,email,telefone,endereco):
        self.nome = nome 
        self.idade = idade
        self.sexo = sexo
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def __str__(self):
     return f'Seu nome:{self.nome}  Sua idade:{self.idade}  Seu sexo:{self.sexo}  Seu email:{self.email}  Seu telefone:{self.telefone}   Seu endereco:{self.endereco}'
 
cad1 = Cadastro ('Gabrielly',16,'fem','gaby0812silva@gmail.com','41 4922 0922','rua 16')

print (cad1)