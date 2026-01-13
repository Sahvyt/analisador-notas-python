import os

def ler_notas(nome_arquivo):
    alunos = []

    # Garante que o CSV seja lido a partir da mesma pasta do script
    pasta_atual = os.path.dirname(__file__) 
    caminho_arquivo = os.path.join(pasta_atual, nome_arquivo)

    with open(caminho_arquivo, 'r') as arquivo: #abre o arquivo com segurança
        linhas = arquivo.readlines()

    for linha in linhas[1:]: #pula o cabeçalho
        partes = linha.strip().split(',')
        nome = partes[0]
        nota = float(partes[1])
        alunos.append((nome, nota))
        
    return alunos

def analisar_notas(alunos):
    notas = []
    aprovados = []

    for nome, nota in alunos:
        notas.append(nota)
        if nota >= 6.0:
            aprovados.append(nome)

    if len(notas) == 0:
        return 0, 0, 0, []

    media = sum(notas) / len(notas)
    maior = max(notas)
    menor = min(notas)

    return media, maior, menor, aprovados


def main():
    arquivo = input("Digite o nome do arquivo CSV: ")
    alunos = ler_notas(arquivo)

    media, maior, menor, aprovados = analisar_notas(alunos)

    print(f"Média da turma: {media:.2f}")
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")
    print("Alunos aprovados:")
    if len(aprovados) == 0:
        print("Nenhum aluno aprovado.")
    else:
        for nome in aprovados:
            print(f"- {nome}")

if __name__ == '__main__':
    main()
