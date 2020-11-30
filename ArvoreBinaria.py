class No():
    termo: str = ''
    nome_do_arquivo: str = '' # este campo será usado para armazenar um termo que poderá ser utilizado em buscas
    esquerda: 'No'
    direita: 'No'

    def __init__(self, termo: str, nome_do_arquivo: str):
        self.termo = termo
        self.nome_do_arquivo = nome_do_arquivo

class ArvoreBinaria():
    raiz: No = None

    def vazia(self):
        return self.raiz == None

    def insere(self, termo: str, nome_do_arquivo: str):
        no = No(termo, nome_do_arquivo)
        no.direita = None
        no.esquerda = None

        if self.vazia():
            self.raiz = no
            return

        atual: No = self.raiz
        anterior: No
        
        while (True):
            anterior = atual
            if termo <= atual.termo:
                atual = atual.esquerda
                if not atual:
                    anterior.esquerda = no
                    return
            else:
                atual = atual.direita
                if not atual:
                    anterior.direita = no
                    return
    
    def buscar(self, no: No, termo: str) -> No:
        if self.vazia(): return

        if no is None:
            # termo não encontrado
            return

        if termo == no.termo:
            # termo encontrado
            return no
        elif termo < no.termo:
            # busca na subárvore esquerda
            return self.buscar(no.esquerda, termo)
        elif termo > no.termo:
            # busca na subárvore direita
            return self.buscar(no.direita, termo)

    def buscar_recursivo(self, termo: str) -> [No]:
        resultados = []
        # Pesquisar por bola
        resultado = self.buscar(self.raiz, termo)

        if not resultado: return resultados

        while (resultado != None):
            resultados.append(resultado)

            if resultado.esquerda != None:
                resultado = self.buscar(resultado.esquerda, termo)
            else:
                resultado = self.buscar(resultado.direita, termo)

        return resultados

    def buscar_termos(self, termos: [str]) -> [[No]]:
        resultados = []
        for termo in termos:
            resultados.append(self.buscar_recursivo(termo))

        return resultados

    def buscar_termos_recursivo(self, termos: [str]) -> [No]:
        # Faz a busca dos termos
        resultados = self.buscar_termos(termos)
        # Ordena a lista para mostrar os termos com mais resultados por primeiro
        resultados.sort(reverse=True, key=sortByLen)

        # Para cada lista de nós de cada termo
        for index, resultados in enumerate(resultados, start=0):
            # Imprime os resultados do termo [index]
            print("\nResultados da busca por: {}".format(termos[index]))
            # Para cada resultado no termo [index]
            for resultado in resultados:
                # Imprime o nó do resultado
                print("{} - {}".format(resultado.termo, resultado.nome_do_arquivo))

    def imprimir(self):
        print("\nExibindo preOrder: \n")
        self._pre(self.raiz)
        
        print("Exibindo inOrder: \n")
        self._in(self.raiz)
        
        print("\nExibindo posOrder: \n")
        self._pos(self.raiz)


    def _in(self, no: No):
        if not no: return

        self._in(no.esquerda)
        print("-{} - {}".format(no.termo, no.nome_do_arquivo))
        self._in(no.direita)

    def _pre(self, no: No):
        if not no: return

        print("{} ".format(no.termo))
        self._pre(no.esquerda)
        self._pre(no.direita)

    def _pos(self, no: No):
        if not no: return

        self._pos(no.esquerda)
        self._pos(no.direita)
        print("{} ".format(no.termo))

    # Função que pergunta ações para o usuário
    def ask(self):
        try:
            # Captura a operação
            operacao = input('\nOperação 1 = pesquisa\nDigite qualquer tecla e pressione enter para sair\n\nDigite a operação: ')

            # Lista das operações
            operacoes_disponiveis = ('1')

            # Se a operação for de pesquisa
            if operacao == '1':
                # Captura os termos
                termos = input('\nDigite os termos da busca (separando por espaços): ')
                # Busca na árvore pelos termos
                self.buscar_termos_recursivo(termos.split(' '))
                # Faz a pergunta novamente
                self.ask()

            # Caso contrário, finaliza
            else: return print('\nTchau!')
        except:
            # Caso haja exceções, finaliza
            return print('\n\nTchau!')

# Função usada no sort por tamanho de lista
def sortByLen(e):
    # Retorna o tamanho do elemento
    return len(e)

# Função principal
def main():
    arvore = ArvoreBinaria()

    # Popula a árvore
    arvore.insere("bola", "arq1.txt")
    arvore.insere("casa", "arq1.txt")
    arvore.insere("dado", "arq1.txt")
    arvore.insere("bola", "arq1.txt")
    arvore.insere("casa", "arq1.txt")
    arvore.insere("dado", "arq2.txt")
    arvore.insere("bola", "arq2.txt")
    arvore.insere("arvore", "arq2.txt")

    # imprime a árvore
    arvore.imprimir()

    # Define o termpo de busca recursiva
    busca_termo = "bola"

    # Imprime o label
    print("\n== Resultado da busca por {} ==".format(busca_termo))
    # Para cada resultado na busca recursiva
    for resultado in arvore.buscar_recursivo(busca_termo):
        # Imprime o nó formatado
        print("{} - {}".format(resultado.termo, resultado.nome_do_arquivo))

    # Busca por termos múltiplos
    print("\n== Buscando por... ==")
    # Define os termos
    busca_termos = ['arvore', 'dado']
    print(busca_termos)

    # Busca recursivamente múltiplos termos, definidos acima
    arvore.buscar_termos_recursivo(busca_termos)
    
    # Pergunta por ações para o usuário
    arvore.ask()

# Início da aplicação
if __name__ == '__main__':
    main()