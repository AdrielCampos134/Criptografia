"""Quatro cifras clássicas em Python."""

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def mover_letra(letra, passo):
    """Move uma letra no alfabeto e mantém letras maiúsculas/minúsculas."""
    maiuscula = letra.upper()
    if maiuscula not in ALFABETO:
        return letra
    nova = ALFABETO[(ALFABETO.index(maiuscula) + passo) % 26]
    return nova.lower() if letra.islower() else nova


def cesar(texto, chave, descriptografar=False):
    passo = int(chave) * (-1 if descriptografar else 1)
    return "".join(mover_letra(letra, passo) for letra in texto)


def vigenere(texto, chave, descriptografar=False):
    chave = "".join(letra for letra in chave.upper() if letra in ALFABETO)
    if not chave:
        raise ValueError("A chave deve possuir pelo menos uma letra de A a Z.")

    resultado = ""
    posicao = 0
    for letra in texto:
        if letra.upper() in ALFABETO:
            passo = ALFABETO.index(chave[posicao % len(chave)])
            if descriptografar:
                passo = -passo
            resultado += mover_letra(letra, passo)
            posicao += 1
        else:
            resultado += letra
    return resultado


def substituicao(texto, chave, descriptografar=False):
    chave = chave.upper()
    if len(chave) != 26 or any(letra not in ALFABETO for letra in chave):
        raise ValueError("A chave deve ter 26 letras de A a Z.")
    if len(set(chave)) != 26:
        raise ValueError("A chave não pode repetir letras.")

    origem, destino = (chave, ALFABETO) if descriptografar else (ALFABETO, chave)
    resultado = ""
    for letra in texto:
        maiuscula = letra.upper()
        if maiuscula not in origem:
            resultado += letra
            continue
        nova = destino[origem.index(maiuscula)]
        resultado += nova.lower() if letra.islower() else nova
    return resultado


def trilho(posicao, quantidade):
    ciclo = 2 * quantidade - 2
    resto = posicao % ciclo
    return resto if resto < quantidade else ciclo - resto


def transposicao(texto, chave, descriptografar=False):
    quantidade = int(chave)
    if quantidade < 2:
        raise ValueError("A chave deve ser um número maior ou igual a 2.")
    if len(texto) <= 1:
        return texto

    trilhos = [trilho(i, quantidade) for i in range(len(texto))]
    if not descriptografar:
        return "".join(texto[i] for trilho_atual in range(quantidade)
                        for i in range(len(texto)) if trilhos[i] == trilho_atual)

    resultado = [""] * len(texto)
    inicio = 0
    for trilho_atual in range(quantidade):
        posicoes = [i for i in range(len(texto)) if trilhos[i] == trilho_atual]
        for posicao, letra in zip(posicoes, texto[inicio:inicio + len(posicoes)]):
            resultado[posicao] = letra
        inicio += len(posicoes)
    return "".join(resultado)


def main():
    cifras = {
        "1": ("Cifra de César", cesar, "Chave numérica: "),
        "2": ("Cifra de Vigenère", vigenere, "Palavra-chave: "),
        "3": ("Substituição Monoalfabética", substituicao, "Chave com 26 letras: "),
        "4": ("Transposição Rail Fence", transposicao, "Número de trilhos: "),
    }

    while True:
        print("\n=== CRIPTOGRAFIA CLÁSSICA ===")
        print("1 - César | 2 - Vigenère | 3 - Substituição | 4 - Rail Fence | 0 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "0":
            print("Programa encerrado.")
            break
        if opcao not in cifras:
            print("Opção inválida.")
            continue

        operacao = input("1 - Criptografar | 2 - Descriptografar: ")
        if operacao not in ("1", "2"):
            print("Operação inválida.")
            continue

        texto = input("Mensagem: ")
        chave = input(cifras[opcao][2])
        try:
            resultado = cifras[opcao][1](texto, chave, operacao == "2")
            print("Resultado:", resultado)
        except ValueError as erro:
            print("Erro:", erro)


if __name__ == "__main__":
    main()
