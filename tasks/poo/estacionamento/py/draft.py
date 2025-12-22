from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id_veiculo: str, tipo: str):
        self.id = id_veiculo
        self.tipo = tipo
        self.horaEntrada: int = 0
        self.horaSaida: int = 0

    def getid(self) -> str:
        return self.id
    
    def getTipo(self) -> str:
        return self.tipo
    
    def setEntrada(self, horaEntrada: int) -> None:
        self.horaEntrada = horaEntrada

    def setSaida(self, horaSaida: int) -> None:
        self.horaSaida = horaSaida

    @abstractmethod
    def calcularValor(self, horaSaida: int) -> float:
        pass
    
    def __str__(self) -> str:
        tipo_preenchido = self.tipo.rjust(10, '_')
        id_preenchido = self.id.rjust(10, '_')
        return f"{tipo_preenchido} : {id_preenchido} : {self.horaEntrada}"


class Bike(Veiculo):
    def __init__(self, id_veiculo: str):
        super().__init__(id_veiculo, "Bike")

    def calcularValor(self, horaSaida: int) -> float:
        return 3.00

class Moto(Veiculo):
    def __init__(self, id_veiculo: str):
        super().__init__(id_veiculo, "Moto")

    def calcularValor(self, horaSaida: int) -> float:
        tempo_minutos = horaSaida - self.horaEntrada
        return max(0.0, tempo_minutos / 20.0)

class Carro(Veiculo):
    def __init__(self, id_veiculo: str):
        super().__init__(id_veiculo, "Carro")

    def calcularValor(self, horaSaida: int) -> float:
        tempo_minutos = horaSaida - self.horaEntrada
        valor_calculado = tempo_minutos / 10.0
        return max(valor_calculado, 5.00)

class Estacionamento:
    def __init__(self):
        self.veiculos: dict[str, Veiculo] = {}
        self.horaAtual: int = 0

    def procurarVeiculo(self, id_veiculo: str) -> bool:
        return id_veiculo in self.veiculos

    def estacionarVeiculo(self, id_veiculo: str, tipo_veiculo: str) -> None:
        if self.procurarVeiculo(id_veiculo):
            return

        tipo = tipo_veiculo.lower()
        if tipo == "bike":
            veiculo = Bike(id_veiculo)
        elif tipo == "moto":
            veiculo = Moto(id_veiculo)
        elif tipo == "carro":
            veiculo = Carro(id_veiculo)
        else:
            return

        veiculo.setEntrada(self.horaAtual)
        self.veiculos[id_veiculo] = veiculo

    def sair(self, id_veiculo: str) -> None:
        if not self.procurarVeiculo(id_veiculo):
            return

        veiculo = self.veiculos.pop(id_veiculo)
        veiculo.setSaida(self.horaAtual)
        valor = veiculo.calcularValor(self.horaAtual)
        
        print(f"{veiculo.getTipo()} chegou {veiculo.horaEntrada} saiu {veiculo.horaSaida}. Pagar R$ {valor:.2f}")

    def passarTempo(self, tempo: int) -> None:
        if tempo >= 0:
            self.horaAtual += tempo

    def __str__(self) -> str:
        resumo = ""
        for veiculo in self.veiculos.values():
             resumo += f"{veiculo}\n"
        
        resumo += f"Hora atual: {self.horaAtual}"
        return resumo.strip()


def main():
    estacionamento = Estacionamento()
    
    while True:
        try:
            line = input()
        except EOFError:
            break
        except Exception:
            break
        
        if not line:
            continue

        print("$" + line)
        args = line.split(" ")
        
        
        if args[0].upper() == "END":
            break
        elif args[0].upper() == "SHOW":
            print(estacionamento)
        elif args[0].upper() == "TEMPO": 
            if len(args) > 1:
                estacionamento.passarTempo(int(args[1]))
        elif args[0].upper() == "ESTACIONAR": 
            if len(args) >= 3:
                estacionamento.estacionarVeiculo(args[2], args[1])
        elif args[0].upper() == "PAGAR": 
            if len(args) > 1:
                estacionamento.sair(args[1])


main()