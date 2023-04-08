from models.Passageiro import Passageiro
from models.Motorista import Motorista
from models.Corrida import Corrida
from MotoristaDAO import MotoristaDAO


class MotoristaCLI:
    def __init__(self):
        pass

    def menu(self):
        opcao = input("Escreva a opção que deseja: "
                      "[1] - Create \n[2] - Read\n[3] - Update\n[4] - Delete")
        if opcao == 1:
            MotoristaCLI.createMotorista()
        elif opcao == 2:
            MotoristaCLI.readMotorista()
        elif opcao == 3:
            MotoristaCLI.updateMotorista()
        elif opcao == 4:
            MotoristaCLI.deleteMotorista()

    def createMotorista(self):
        nome = input("Nome: ")
        documento = input("Documento: ")
        passageiro = Passageiro(documento, nome)
        op = 1
        corridas = []
        while (op):
            nota = input("Nota: ")
            distancia = input("Distancia: ")
            valor = input("Valor: ")
            corrida = Corrida(nota, distancia, valor, passageiro)
            corridas.insert(corrida)
            op = input("Deseja continuar? [1] sim [0] não")
        nota = input("Nota: ")
        motorista = Motorista(nota, corridas)
        MotoristaDAO.create_motorista(motorista)

    def readmotorista(self):
        id = input("_id: ")
        motorista = MotoristaDAO.read_motorista_by_id(id)
        print(motorista)

    def updatemotorista(self):
        id = input("_id: ")
        nome = input("Nome: ")
        documento = input("Documento: ")
        passageiro = Passageiro(documento, nome)
        op = True
        corridas = []
        while (op):
            nota = input("Nota: ")
            distancia = input("Distancia: ")
            valor = input("Valor: ")
            corrida = Corrida(nota, distancia, valor, passageiro)
            corridas.insert(corrida)
        nota = input("Nota: ")
        motorista = Motorista(nota, corridas)
        motorista = MotoristaDAO.update_motorista(id, motorista)

    def deletemotorista(self):
        id = input("_id: ")
        motorista = MotoristaDAO.delete_motorista(id)
