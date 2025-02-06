import coverage 
import unittest

class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

class SistemaCadastro:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, nome, idade, matricula):
        aluno = Aluno(nome, idade, matricula)
        self.alunos.append(aluno)
        print(f"Aluno {nome} adicionado com sucesso!")
        
    def adicionar_aluno(self, nome, idade, matricula):
        aluno = Aluno(nome, idade, matricula)
        self.alunos.append(aluno)
        print(f"Aluno {nome} adicionado com sucesso!")

    def listar_alunos(self):
        for aluno in self.alunos:
            print(f"Nome: {aluno.nome}, Idade: {aluno.idade}, Matrícula: {aluno.matricula}")

    def atualizar_aluno(self, matricula, nome=None, idade=None):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                if nome:
                    aluno.nome = nome
                if idade:
                    aluno.idade = idade
                print(f"Aluno com matrícula {matricula} atualizado com sucesso!")
                return
        print(f"Aluno com matrícula {matricula} não encontrado.")

    def remover_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                self.alunos.remove(aluno)
                print(f"Aluno com matrícula {matricula} removido com sucesso!")
                return
        print(f"Aluno com matrícula {matricula} não encontrado.")

    def menu(self):
        while True:
            print("\nSistema de Cadastro de Alunos")
            print("1. Adicionar Aluno")
            print("2. Listar Alunos")
            print("3. Atualizar Aluno")
            print("4. Remover Aluno")
            print("5. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                nome = input("Nome do Aluno: ")
                idade = input("Idade do Aluno: ")
                matricula = input("Matrícula do Aluno: ")
                self.adicionar_aluno(nome, idade, matricula)
            
            elif opcao == '2':
                self.listar_alunos()
            
            elif opcao == '3':
                matricula = input("Matrícula do Aluno a ser atualizado: ")
                nome = input("Novo Nome (deixe em branco para não alterar): ")
                idade = input("Nova Idade (deixe em branco para não alterar): ")
                self.atualizar_aluno(matricula, nome, idade)
            
            elif opcao == '4':
                matricula = input("Matrícula do Aluno a ser removido: ")
                self.remover_aluno(matricula)
            
            elif opcao == '5':
                break
            
            else:
                print("Opção inválida! Tente novamente.")
                
                

def main():
    sistema = SistemaCadastro()
    sistema.menu()

if __name__ == "__main__":
    main()
    
    
class TestCRUD(unittest.TestCase):

    def setUp(self):
        self.sistema = SistemaCadastro()

    def test_adicionar_aluno(self):
        self.sistema.adicionar_aluno("João", 20, "123")
        self.assertEqual(len(self.sistema.alunos), 1)
        self.assertEqual(self.sistema.alunos[0].nome, "João")
        self.assertEqual(self.sistema.alunos[0].idade, 20)
        self.assertEqual(self.sistema.alunos[0].matricula, "123")

    def test_listar_alunos(self):
        self.sistema.adicionar_aluno("João", 20, "123")
        self.sistema.adicionar_aluno("Maria", 22, "456")
        self.sistema.listar_alunos()

    def test_atualizar_aluno(self):
        self.sistema.adicionar_aluno("João", 20, "123")
        self.sistema.atualizar_aluno("123", nome="João Silva", idade=21)
        self.assertEqual(self.sistema.alunos[0].nome, "João Silva")
        self.assertEqual(self.sistema.alunos[0].idade, 21)

    def test_remover_aluno(self):
        self.sistema.adicionar_aluno("João", 20, "123")
        self.sistema.remover_aluno("123")
        self.assertEqual(len(self.sistema.alunos), 0)

if __name__ == "__main__":
    unittest.main()


# Comentários sobre os erros intencionais no código:
# 1. Duplicidade de código: As funções `adicionar_aluno`, `atualizar_aluno` e `remover_aluno` possuem trechos de código semelhantes que poderiam ser refatorados.
# 2. Falta de tratamento de exceções: O código não trata possíveis exceções que podem ocorrer durante a execução, como entradas inválidas.
# 3. Variáveis não utilizadas: A variável `alunos` é passada como argumento em várias funções, mas poderia ser uma variável global.
# 4. Código desnecessário: A função `listar_alunos` poderia ser simplificada utilizando list comprehensions.
