# Atividade de Criptografia Clássica

**Disciplina:** Segurança da Informação  
**Linguagem:** Python 3  
**Nível:** implementação simples para trabalho acadêmico

## Objetivo

Este trabalho implementa quatro algoritmos históricos de criptografia. Todos possuem as duas funções solicitadas:

- receber uma mensagem em texto claro e uma chave e gerar o texto cifrado;
- receber o texto cifrado e a mesma chave e recuperar o texto claro.

## Cifras implementadas

1. **Cifra de César:** cada letra é deslocada uma quantidade definida por uma chave numérica.
2. **Cifra de Vigenère:** cada letra é deslocada de acordo com as letras repetidas de uma palavra-chave.
3. **Substituição monoalfabética:** cada letra do alfabeto é trocada por outra letra conforme uma chave de 26 letras.
4. **Transposição Rail Fence:** a mensagem é escrita em zigue-zague em trilhos e depois lida por linhas.

O programa trabalha com o alfabeto de A a Z. Espaços, números, pontuação e acentos são mantidos no mesmo lugar. Assim, uma mensagem com acento pode ser usada, mas o acento não é transformado.

## Arquivos

- `criptografia_classica.py`: programa principal com menu, criptografia e descriptografia.
- `README.md`: explicação e instruções deste trabalho.
- `roteiro_apresentacao.md`: roteiro curto para explicar o trabalho em sala.

## Como executar

1. Instale o Python 3, caso ainda não esteja instalado.
2. Abra o terminal nesta pasta.
3. Execute:

```text
python criptografia_classica.py
```

Escolha a cifra, escolha entre criptografar e descriptografar, informe a mensagem e informe a chave.

## Exemplos de chaves

- César: `3`
- Vigenère: `CHAVE`
- Substituição: `QWERTYUIOPASDFGHJKLZXCVBNM`
- Rail Fence: `3` trilhos

## Observação de segurança

Essas cifras são importantes para estudar a história e os conceitos de criptografia, mas não devem ser usadas para proteger dados reais. Elas podem ser quebradas com técnicas simples e não substituem algoritmos atuais, como AES e RSA.
