# Relatório - Criptografia Clássica

**Disciplina:** Segurança da Informação  
**Modalidade:** Trabalho em grupo  
**Integrantes:** preencher com os nomes do grupo

## 1. Contextualização

Antes dos algoritmos modernos, mensagens eram protegidas por métodos baseados em deslocamento, substituição e mudança de posição das letras. O estudo dessas técnicas ajuda a entender o uso de chaves e a necessidade de algoritmos mais fortes.

## 2. Objetivo

Criar um programa autoral que permita criptografar e descriptografar mensagens usando quatro cifras clássicas:

- César;
- Vigenère;
- substituição monoalfabética;
- transposição Rail Fence.

## 3. Desenvolvimento

O programa foi escrito em Python, sem bibliotecas externas e com estruturas básicas. Cada cifra possui uma função de criptografia e uma função de descriptografia, controlada pelo parâmetro `descriptografar`.

### 3.1 Cifra de César

Recebe uma chave numérica. A posição de cada letra é somada ao deslocamento. Na descriptografia, o deslocamento é subtraído.

### 3.2 Cifra de Vigenère

Recebe uma palavra-chave. Cada letra da chave representa um deslocamento e a palavra é repetida até o final da mensagem.

### 3.3 Substituição monoalfabética

Recebe um alfabeto embaralhado com 26 letras sem repetição. A descriptografia usa a associação inversa para descobrir a letra original.

### 3.4 Transposição Rail Fence

Recebe a quantidade de trilhos. A mensagem é escrita em zigue-zague e lida por trilho na criptografia; na descriptografia, o zigue-zague é reconstruído.

## 4. Demonstração de funcionamento

Foi utilizada a mensagem `Ataque ao amanhecer!`. No menu do programa, a mensagem pode ser criptografada e depois descriptografada usando a mesma cifra e a mesma chave. O resultado deve ser a recuperação do texto original.

## 5. Conclusão

O trabalho mostra, de forma prática, como uma chave pode alterar uma mensagem e como a operação inversa recupera o conteúdo. Também mostra que cifras históricas são úteis para aprendizado, mas não oferecem proteção suficiente para informações atuais.

## 6. Limitações

O programa usa apenas as letras A a Z nas operações. Espaços, números, pontuação e caracteres acentuados são preservados. As cifras são educacionais e não devem proteger dados reais.
