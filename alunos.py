from datetime import datetime


class Aluno:
    def __init__(self, nome, nascimento, faixa) -> None:
        self.nome = nome
        self.nascimento = nascimento
        self.faixa = faixa

    def idade(self):
        hoje = datetime.now()
        ano = hoje.year

        idade = ano - self.nascimento
        return idade

alunos = []