# Função para adicionar um aluno
def adicionar_aluno(alunos, nome, idade, matricula):
    aluno = {
        'nome': nome,
        'idade': idade,
        'matricula': matricula
    }
    alunos.append(aluno)
    print(f"Aluno {nome} adicionado com sucesso!")

# Função para listar todos os alunos
def listar_alunos(alunos):
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Matrícula: {aluno['matricula']}")

# Função para atualizar os dados de um aluno
def atualizar_aluno(alunos, matricula, nome=None, idade=None):
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            if nome:
                aluno['nome'] = nome
            if idade:
                aluno['idade'] = idade
            print(f"Aluno com matrícula {matricula} atualizado com sucesso!")
            return
    print(f"Aluno com matrícula {matricula} não encontrado.")

# Função para remover um aluno
def remover_aluno(alunos, matricula):
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            alunos.remove(aluno)
            print(f"Aluno com matrícula {matricula} removido com sucesso!")
            return
    print(f"Aluno com matrícula {matricula} não encontrado.")

# Função principal do sistema
def main():
    alunos = []
    
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
            adicionar_aluno(alunos, nome, idade, matricula)
        
        elif opcao == '2':
            listar_alunos(alunos)
        
        elif opcao == '3':
            matricula = input("Matrícula do Aluno a ser atualizado: ")
            nome = input("Novo Nome (deixe em branco para não alterar): ")
            idade = input("Nova Idade (deixe em branco para não alterar): ")
            atualizar_aluno(alunos, matricula, nome, idade)
        
        elif opcao == '4':
            matricula = input("Matrícula do Aluno a ser removido: ")
            remover_aluno(alunos, matricula)
        
        elif opcao == '5':
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

# Comentários sobre os erros intencionais no código:
# 1. Duplicidade de código: As funções `adicionar_aluno`, `atualizar_aluno` e `remover_aluno` possuem trechos de código semelhantes que poderiam ser refatorados.
# 2. Falta de tratamento de exceções: O código não trata possíveis exceções que podem ocorrer durante a execução, como entradas inválidas.
# 3. Variáveis não utilizadas: A variável `alunos` é passada como argumento em várias funções, mas poderia ser uma variável global.
# 4. Código desnecessário: A função `listar_alunos` poderia ser simplificada utilizando list comprehensions.