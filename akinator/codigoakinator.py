import pandas as pd

dados = pd.read_csv('perguntas.csv')
pessoa = None

while not pessoa:
    
    perguntas = list(dados.columns[1:].values)
    respostas = []
    for perguntas in perguntas:
        respostas.append(dados[perguntas].sum())
    pergunta_rodada = perguntas[respostas.index(max(respostas))]
    resposta_rodada = input(f'{pergunta_rodada}(S: SIM / N: NAO / NS: NAO SEI)')

    if resposta_rodada == 'S':
        dados = dados[dados[pergunta_rodada] == 1]
    elif resposta_rodada == 'N':
        dados = dados[dados[pergunta_rodada]==0]
    if len(dados.index) == 1:
        pessoa = dados['pessoa'].values[0]
    elif len(dados.index) == 0:
        print('joga direito  porra')
        dados = pd.read_csv('perguntas.csv')
        
    print(f'A resposta é {pessoa}')