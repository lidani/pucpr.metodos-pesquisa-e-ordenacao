"""
Author: Gustavo Lidani

Classe que representa um nó da lista de arquivos
"""
class No():
    dado: str = ''
    frequencia: int = 0
    proximo: 'No' = None

    # constructor
    def __init__(self, dado: str, frequencia: int):
        self.dado = dado
        self.frequencia = frequencia

"""
Author: Gustavo Lidani

Classe que representa uma lista de arquivos
"""
class ListaArquivos():

    primeiro: No = None
    ultimo: No = None
    tamanho = 0

    """
    Função que insere um nó no início da lista
    """
    def inicio(self, no: No):
        if not self.primeiro:
            self.primeiro = no
            self.ultimo = no

        else:
            no.proximo = self.primeiro
            self.primeiro = no

        self.tamanho += 1

    """
    Função que insere um nó depois do nó referenciado (passado por parametro)
    """
    def depois(self, no: No, novo_no: No):
        novo_no.proximo = no.proximo
        no.proximo = novo_no 
        return novo_no

    """
    Função que insere um nó no final da lista
    """
    def final(self, no: No):
        if not self.primeiro:
            self.inicio(no)

        else:
            self.ultimo = self.depois(self.ultimo, no)

        self.tamanho += 1

    """
    Função que anda pelos nós imprimindo cada um deles
    """
    def imprimir(self):
        no = self.primeiro

        while (no != None):
            print("'{}' ({})".format(no.dado, no.frequencia))
            no = no.proximo

    """
    Função que determina se a lista está vazia
    """
    def vazio(self):
        return self.primeiro == None

    """
    Função que insere um nó de forma ordenada, usando como base a frequência do arquivo
    """
    def ordenado(self, no: No):
        if self.vazio() or no.frequencia >= self.primeiro.frequencia:
            self.inicio(no)
            
        elif no.frequencia <= self.ultimo.frequencia:
            self.final(no)
        
        else:
            a = self.primeiro
            b = None

            while(a.frequencia > no.frequencia):
                b = a
                a = a.proximo

            self.depois(b, no)
    
    """
    Função que faz a busca de um arquivo e retorna a frequência do mesmo
    """
    def buscar(self, dado: str):
        no = self.primeiro
        while (no != None):
            if no.dado == dado:
                return no.frequencia
            no = no.proximo
        return 0

def main():
    # inicializa a classe
    lista = ListaArquivos()

    # Adiciona as informacoes
    lista.ordenado(No('Arquivo 12.txt', 14))
    lista.ordenado(No('Arquivo 55.txt', 23))
    lista.ordenado(No('Arquivo 78.txt', 5))
    lista.ordenado(No('Arquivo 65.txt', 8))

    # Ao imprimir
    lista.imprimir()
    """ Obtemos o seguinte resultado:
    'Arquivo 55.txt' (23)
    'Arquivo 12.txt' (14)
    'Arquivo 65.txt' (8)
    'Arquivo 78.txt' (5)
    """
    
    parametro_de_busca = 'Arquivo 12.txt'
    # Ao buscar por 'Arquivo 12.txt'
    print("O valor retornado para '{}' é {}.".format(parametro_de_busca, lista.buscar(parametro_de_busca))) # 14

# Iniciar a execucao
if __name__ == '__main__': 
    main()
