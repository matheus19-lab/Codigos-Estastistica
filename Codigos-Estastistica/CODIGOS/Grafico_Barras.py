import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Dados dos 50 maiores PIBs
dados = [
    ['São Paulo', 'SP', 1066.83],
    ['Rio de Janeiro', 'RJ', 418.46],
    ['Brasília', 'DF', 365.67],
    ['Maricá', 'RJ', 134.09],
    ['Belo Horizonte', 'MG', 130.20],
    ['Manaus', 'AM', 127.65],
    ['Curitiba', 'PR', 120.07],
    ['Osasco', 'SP', 119.40],
    ['Porto Alegre', 'RS', 104.74],
    ['Guarulhos', 'SP', 97.56],
    ['Campinas', 'SP', 91.97],
    ['Fortaleza', 'CE', 86.94],
    ['Salvador', 'BA', 76.70],
    ['Niterói', 'RJ', 76.27],
    ['Goiânia', 'GO', 75.78],
    ['São Bernardo do Campo', 'SP', 71.97],
    ['Barueri', 'SP', 71.65],
    ['Duque de Caxias', 'RJ', 70.07],
    ['Paulínia', 'SP', 67.07],
    ['Recife', 'PE', 66.35],
    ['Jundiaí', 'SP', 65.42],
    ['Saquarema', 'RJ', 64.70],
    ['São José dos Campos', 'SP', 61.39],
    ['Sorocaba', 'SP', 58.82],
    ['Betim', 'MG', 52.61],
    ['Ribeirão Preto', 'SP', 52.31],
    ['Uberlândia', 'MG', 51.07],
    ['Joinville', 'SC', 49.82],
    ['Itajaí', 'SC', 48.20],
    ['Contagem', 'MG', 45.09],
    ['Piracicaba', 'SP', 44.35],
    ['Campos dos Goytacazes', 'RJ', 42.95],
    ['São Luís', 'MA', 42.39],
    ['Campo Grande', 'MS', 42.27],
    ['Belém', 'PA', 40.54],
    ['Cuiabá', 'MT', 39.05],
    ['Caxias do Sul', 'RS', 37.86],
    ['Serra', 'ES', 37.65],
    ['Santo André', 'SP', 36.93],
    ['Araucária', 'PR', 34.08],
    ['São José dos Pinhais', 'PR', 33.96],
    ['Maceió', 'AL', 33.75],
    ['Florianópolis', 'SC', 31.19],
    ['Natal', 'RN', 31.16],
    ['Santos', 'SP', 30.96],
    ['Teresina', 'PI', 29.45],
    ['Canoas', 'RS', 29.17],
    ['Cajamar', 'SP', 28.99],
    ['João Pessoa', 'PB', 28.44],
    ['Indaiatuba', 'SP', 28.27]
]

# Criar DataFrame
df = pd.DataFrame(dados, columns=['Município', 'UF', 'PIB (R$ bilhões)'])

# Criar rótulos mais curtos para melhor visualização
df['rotulo'] = df['Município'].apply(lambda x: x[:15] + '...' if len(x) > 15 else x) + ' - ' + df['UF']

# Configurar o estilo
plt.style.use('seaborn-v0_8-darkgrid')

# Criar figura com tamanho adequado para 50 barras
fig, ax = plt.subplots(figsize=(14, 16))

# Criar cores (azul padrão, com destaque para os 3 primeiros)
cores = ['#4472C4'] * 50
cores[0] = '#FF6B6B'  # 1º lugar - vermelho
cores[1] = '#4ECDC4'  # 2º lugar - verde água
cores[2] = '#FFD166'  # 3º lugar - amarelo

# Gráfico de barras horizontais (melhor para muitos itens)
bars = ax.barh(df['rotulo'], df['PIB (R$ bilhões)'], 
               color=cores, alpha=0.8, edgecolor='white', linewidth=1)

# Configurar eixos
ax.set_xlabel('PIB (R$ bilhões)', fontsize=14, fontweight='bold', labelpad=10)
ax.set_ylabel('Municípios', fontsize=14, fontweight='bold', labelpad=10)
ax.set_title('50 Maiores PIBs Municipais do Brasil - 2023', 
             fontsize=18, fontweight='bold', pad=20)

# Inverter eixo Y para mostrar o maior no topo
ax.invert_yaxis()

# Ajustar espaçamento das linhas do eixo Y
ax.tick_params(axis='y', labelsize=10)
ax.yaxis.set_tick_params(pad=2)

# Grid apenas no eixo X para não poluir
ax.grid(True, axis='x', alpha=0.3, linestyle='--')

# Adicionar valores nas barras (com ajuste de posição)
for i, (bar, valor) in enumerate(zip(bars, df['PIB (R$ bilhões)'])):
    # Posicionar o texto no final de cada barra
    ax.text(valor + 3, bar.get_y() + bar.get_height()/2, 
            f'R$ {valor:.1f} bi', 
            va='center', ha='left', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7, edgecolor='none'))

# Ajustar limites do eixo X para dar espaço aos rótulos
ax.set_xlim(0, df['PIB (R$ bilhões)'].max() * 1.15)

# Adicionar uma linha vertical para destacar a média
media = df['PIB (R$ bilhões)'].mean()
ax.axvline(x=media, color='#FF6B6B', linestyle='--', linewidth=2, alpha=0.7, label=f'Média: R$ {media:.1f} bi')

# Adicionar legenda para as cores
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#FF6B6B', alpha=0.8, label='1º Lugar (São Paulo)'),
    Patch(facecolor='#4ECDC4', alpha=0.8, label='2º Lugar (Rio de Janeiro)'),
    Patch(facecolor='#FFD166', alpha=0.8, label='3º Lugar (Brasília)'),
    Patch(facecolor='#4472C4', alpha=0.8, label='Demais municípios'),
    Patch(facecolor='none', edgecolor='#FF6B6B', linestyle='--', label=f'Média: R$ {media:.1f} bi')
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=10, framealpha=0.9)

# Ajustar layout para garantir que nada seja cortado
plt.tight_layout()

# Salvar imagem em PNG com alta qualidade
plt.savefig('top_50_pib_grafico_barras.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none', pad_inches=0.5)

print("Gráfico salvo como 'top_50_pib_grafico_barras.png'")
print(f"Dimensões: 14x16 polegadas, 300 DPI")
print("\nInformações do gráfico:")
print(f"- Total de municípios: 50")
print(f"- PIB total: R$ {df['PIB (R$ bilhões)'].sum():.2f} bilhões")
print(f"- Média: R$ {media:.2f} bilhões")
print(f"- Mediana: R$ {df['PIB (R$ bilhões)'].median():.2f} bilhões")
print(f"- Maior: {df.loc[0, 'Município']} - R$ {df.loc[0, 'PIB (R$ bilhões)']:.2f} bi")
print(f"- Menor: {df.loc[49, 'Município']} - R$ {df.loc[49, 'PIB (R$ bilhões)']:.2f} bi")

# Mostrar o gráfico
plt.show()