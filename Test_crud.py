import unittest
from Crud_escola import SistemaCadastro 
# Classe de testes para o sistema de cadastro CRUD de alunos
# test_aluno_crud.py

import unittest
from Crud_escola import SistemaCadastro

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