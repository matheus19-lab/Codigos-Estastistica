import pandas as pd
import dataframe_image as dfi

# Dados completos dos 50 maiores PIBs
dados = [
    [1, 'São Paulo', 'SP', 1066.83],
    [2, 'Rio de Janeiro', 'RJ', 418.46],
    [3, 'Brasília', 'DF', 365.67],
    [4, 'Maricá', 'RJ', 134.09],
    [5, 'Belo Horizonte', 'MG', 130.20],
    [6, 'Manaus', 'AM', 127.65],
    [7, 'Curitiba', 'PR', 120.07],
    [8, 'Osasco', 'SP', 119.40],
    [9, 'Porto Alegre', 'RS', 104.74],
    [10, 'Guarulhos', 'SP', 97.56],
    [11, 'Campinas', 'SP', 91.97],
    [12, 'Fortaleza', 'CE', 86.94],
    [13, 'Salvador', 'BA', 76.70],
    [14, 'Niterói', 'RJ', 76.27],
    [15, 'Goiânia', 'GO', 75.78],
    [16, 'São Bernardo do Campo', 'SP', 71.97],
    [17, 'Barueri', 'SP', 71.65],
    [18, 'Duque de Caxias', 'RJ', 70.07],
    [19, 'Paulínia', 'SP', 67.07],
    [20, 'Recife', 'PE', 66.35],
    [21, 'Jundiaí', 'SP', 65.42],
    [22, 'Saquarema', 'RJ', 64.70],
    [23, 'São José dos Campos', 'SP', 61.39],
    [24, 'Sorocaba', 'SP', 58.82],
    [25, 'Betim', 'MG', 52.61],
    [26, 'Ribeirão Preto', 'SP', 52.31],
    [27, 'Uberlândia', 'MG', 51.07],
    [28, 'Joinville', 'SC', 49.82],
    [29, 'Itajaí', 'SC', 48.20],
    [30, 'Contagem', 'MG', 45.09],
    [31, 'Piracicaba', 'SP', 44.35],
    [32, 'Campos dos Goytacazes', 'RJ', 42.95],
    [33, 'São Luís', 'MA', 42.39],
    [34, 'Campo Grande', 'MS', 42.27],
    [35, 'Belém', 'PA', 40.54],
    [36, 'Cuiabá', 'MT', 39.05],
    [37, 'Caxias do Sul', 'RS', 37.86],
    [38, 'Serra', 'ES', 37.65],
    [39, 'Santo André', 'SP', 36.93],
    [40, 'Araucária', 'PR', 34.08],
    [41, 'São José dos Pinhais', 'PR', 33.96],
    [42, 'Maceió', 'AL', 33.75],
    [43, 'Florianópolis', 'SC', 31.19],
    [44, 'Natal', 'RN', 31.16],
    [45, 'Santos', 'SP', 30.96],
    [46, 'Teresina', 'PI', 29.45],
    [47, 'Canoas', 'RS', 29.17],
    [48, 'Cajamar', 'SP', 28.99],
    [49, 'João Pessoa', 'PB', 28.44],
    [50, 'Indaiatuba', 'SP', 28.27]
]

# Criar DataFrame
df = pd.DataFrame(dados, columns=['Rank', 'Município', 'UF', 'PIB (R$ bilhões)'])

# Estilizar o DataFrame
df_styled = df.style.set_properties(**{
    'background-color': 'white',
    'color': 'black',
    'border-color': 'black',
    'border-width': '1px',
    'border-style': 'solid',
    'text-align': 'center'
}).set_table_styles([
    {'selector': 'th', 'props': [('background-color', '#4472C4'), 
                                 ('color', 'white'),
                                 ('font-weight', 'bold'),
                                 ('text-align', 'center')]},
    {'selector': 'td', 'props': [('padding', '5px')]}
]).hide(axis='index')

# Salvar como imagem
dfi.export(df_styled, 'top_50_pib_municipais_completo.png')
print("Imagem salva como 'top_50_pib_municipais_completo.png'")