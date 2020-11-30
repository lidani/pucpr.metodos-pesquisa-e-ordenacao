
class No():
    dado: str = '' # este campo será usado para armazenar o nome de um arquivo
    frequencia: int = 0 # este campo será usado para armazenar um número inteiro que corresponda à quantidade de vezes que um termo aparece dentro do arquivo
    proximo: 'No' = None

    # constructor
    def __init__(self, dado: str, frequencia: int):
        self.dado = dado
        self.frequencia = frequencia

class ListaArquivos():

    primeiro: No = None
    ultimo: No = None
    tamanho = 0

    def inicio(self, no: No):
        if not self.primeiro:
            self.primeiro = no
            self.ultimo = no

        else:
            no.proximo = self.primeiro
            self.primeiro = no

        self.tamanho += 1

    def depois(self, no: No, novo_no: No):
        novo_no.proximo = no.proximo
        no.proximo = novo_no 
        return novo_no

    def final(self, no: No):
        if not self.primeiro:
            self.inicio(no)

        else:
            self.ultimo = self.depois(self.ultimo, no)

        self.tamanho += 1

    def imprimir(self):
        no = self.primeiro

        while (no != None):
            print("'{}' ({})".format(no.dado, no.frequencia))
            no = no.proximo

    def vazio(self):
        return self.primeiro == None

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
