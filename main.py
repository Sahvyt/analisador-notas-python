def ler_notas(nome_arquivo):
    notas = []
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas[1:]:  # pula o cabeçalho
        partes = linha.strip().split(',')
        nome = partes[0]
        nota = float(partes[1])
        notas.append(nota)

    return notas


def analisar_notas(notas):
    media = sum(notas) / len(notas)
    maior = max(notas)
    menor = min(notas)

    aprovados = 0
    for nota in notas:
        if nota >= 6.0:
            aprovados += 1

    return media, maior, menor, aprovados


def main():
    notas = ler_notas('notas.csv')
    media, maior, menor, aprovados = analisar_notas(notas)

    print(f"Média da turma: {media:.2f}")
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")
    print(f"Aprovados: {aprovados}")


main()
