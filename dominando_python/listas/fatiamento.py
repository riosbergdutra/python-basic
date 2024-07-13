lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # t, h, 0, n. Isso significa que você está pegando todos os elementos da lista a partir do índice 2 até o final.

lista[:2] # p, y. Isso significa que você está pegando todos os elementos da lista do início até o índice 2 (exclusivo).
 
lista[1:3] # y, t Aqui você está pegando os elementos da lista do índice 1 até o índice 3 (exclusivo).

lista[0:3:2] # p, t Isso indica que você está pegando os elementos da lista do índice 0 até o índice 3 (exclusivo), pulando de 2 em 2.

lista[::] # p, y, t, h, o, n Esse formato (lista[::]) pega todos os elementos da lista.

lista[::-1] # n, o, h, t, y, pAqui, [::-1] indica que você está pegando todos os elementos da lista, mas de trás para frente, ou seja, invertendo a ordem.