#Relatório 1 - Introdução ao Python

class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrarAula(self, assunto):
        print(f'O professor {self.nome} esta ministrando uma aula sobre {assunto}')


class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        print(f'O aluno {self.nome} esta presente')


class Aula:
    def __init__(self, assunto, professor):
        self.assunto = assunto
        self.professor = professor
        self.alunos = []

    def adicionarAluno(self, aluno):
        self.alunos.insert(aluno)

    def listarPresenca(self):
        print(f'Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor}:')
        for aluno in self.alunos:
            print(f'O aluno {aluno} está presente')