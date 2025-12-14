from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor: float  = valor
        self.descricao: str  = descricao
        
    def resumo(self)-> str:
            return f"Pagamento de R${self.valor}: {self.descricao}"
    
    def validar_valor(self) -> None:
        if self.valor <= 0:
            raise ValueError("falhou: valor inválido")
    
    @abstractmethod
    def processar(self):
        pass

class CartaoCredito(Pagamento):
    def __init__(self, valor: float, descricao: str, num: str, nome_titular: str, limite: float):
        super().__init__(valor, descricao)
        self.num: str = num
        self.nome_titular: str = nome_titular
        self.limite: float = limite

    def processar(self) -> None:
        if self.valor > self.limite:
            raise RuntimeError(f"Erro: Limite insuficiente no cartão {self.num}")
        

        self.limite -= self.valor
        print(f"Pagamento aprovado no cartão {self.nome_titular}. Limite restante: {self.limite:.2f}")
       
class Pix(Pagamento):
    def __init__(self, valor: float, descricao: str, chave: str, banco: str):
        super().__init__(valor, descricao)
        self.chave: str = chave
        self.banco: str = banco
    
    def processar(self) -> None:
        print(f"PIX enviado via {self.banco} usando chave {self.chave}")

class Boleto(Pagamento):
    def __init__(self, valor: float, descricao: str, codigo_barras: str, vencimento: str):
        super().__init__(valor, descricao)
        self.codigo_barras: str = codigo_barras
        self.vencimento: str = vencimento
    
    def processar(self) -> None:
        print("Boleto gerado. Aguardando pagamento...")

def processar_pagamento(pagamento: Pagamento) -> None:
    try:
        pagamento.validar_valor()
        pagamento.resumo()
        pagamento.processar()
        
    except (ValueError, RuntimeError) as e:
        print(f"{e}")
    finally:
        print("-" * 4)


pagamentos: list[Pagamento] = [
    Pix(150.00, "Camisa esportiva", "email@ex.com", "Banco XPTO"),

    CartaoCredito(400.00, "Tênis esportivo", "1234 5678 9123 4567", "Cliente X", 500.00),
  
    Boleto(89.90, "Livro de Python", "123456789000", "2025-01-10"),
    
    CartaoCredito(800.00, "Notebook", "9999 8888 7777 6666", "Cliente Y", 700.00), 
    
    Pix(0, "Item Gratuito", "test@fail.com", "Banco Teste"),
]

print("--- Início do Processamento de Pagamentos ---")

for pagamento in pagamentos:
    processar_pagamento(pagamento)

print("--- Fim do Processamento ---")