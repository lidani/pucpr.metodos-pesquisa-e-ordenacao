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

def sortByLen(e):
    return len(e)

def main():
    arvore = ArvoreBinaria()

    arvore.insere("bola", "arq1.txt")
    arvore.insere("casa", "arq1.txt")
    arvore.insere("dado", "arq1.txt")
    arvore.insere("bola", "arq1.txt")
    arvore.insere("casa", "arq1.txt")
    arvore.insere("dado", "arq2.txt")
    arvore.insere("bola", "arq2.txt")
    arvore.insere("arvore", "arq2.txt")

    # imprime a árvore
    # arvore.imprimir()

    busca_termo = "bola"

    print("\n== Resultado da busca por {} ==".format(busca_termo))
    for resultado in arvore.buscar_recursivo(busca_termo):
        print("{} - {}".format(resultado.termo, resultado.nome_do_arquivo))
    print("===================")

    print("\n== Buscando por... ==")
    busca_termos = ['arvore', 'dado']
    print(busca_termos)

    resultados = arvore.buscar_termos(busca_termos)
    resultados.sort(reverse=True, key=sortByLen)

    for index, resultados in enumerate(resultados, start=0):
        print("\nResultados da busca por: {}".format(busca_termos[index]))
        for resultado in resultados:
            print("{} - {}".format(resultado.termo, resultado.nome_do_arquivo))

if __name__ == '__main__':
    main()