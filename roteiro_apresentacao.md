# Roteiro simples para a apresentação

## 1. Introdução

Criptografia é o processo de transformar uma mensagem para que apenas quem possui a chave consiga entendê-la. Neste trabalho foram implementadas quatro cifras clássicas em Python.

## 2. César

Na Cifra de César, a chave é um número. Com chave 3, A vira D, B vira E e assim por diante. Para descriptografar, fazemos o deslocamento no sentido contrário.

## 3. Vigenère

Na Vigenère, a chave é uma palavra. Cada letra da palavra define um deslocamento diferente. Quando a chave termina, ela começa novamente do início.

## 4. Substituição monoalfabética

Nesta cifra, a chave é um alfabeto embaralhado com 26 letras. A primeira letra da mensagem usa a primeira letra da chave, a segunda usa a segunda e assim por diante. Para descriptografar, fazemos a associação inversa.

## 5. Transposição Rail Fence

Na transposição, as letras não são trocadas. Elas apenas mudam de posição. A mensagem é escrita em zigue-zague usando uma quantidade de trilhos e depois lida linha por linha.

## 6. Demonstração

1. Executar `python criptografia_classica.py`.
2. Escolher uma cifra.
3. Criptografar a mensagem `Ataque ao amanhecer!`.
4. Usar o mesmo resultado, a mesma cifra e a mesma chave para descriptografar.
5. Mostrar que a mensagem original foi recuperada.

## 7. Conclusão

As quatro cifras mostram ideias fundamentais: deslocamento, uso de chave, substituição, transposição e operações repetidas. Elas são didáticas, mas não são seguras para uso atual.
