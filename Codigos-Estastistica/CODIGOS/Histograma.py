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

# Configurar estilo
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams['axes.edgecolor'] = '#333333'

# Criar figura (tamanho otimizado para histograma)
fig, ax = plt.subplots(figsize=(14, 8))

# Definir bins para melhor visualização
bins = [0, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 170, 200, 250, 300, 350, 400, 450]

# Criar histograma
counts, bins, patches = ax.hist(df['PIB (R$ bilhões)'], bins=bins, 
                                 color='#2E75B6', edgecolor='white', linewidth=2,
                                 alpha=0.9, rwidth=0.85)

# Adicionar valores no topo de cada barra
for i, (count, bin_start) in enumerate(zip(counts, bins[:-1])):
    if count > 0:
        bin_center = bin_start + (bins[i+1] - bin_start) / 2
        ax.text(bin_center, count + 0.15, f'{int(count)}', 
                ha='center', va='bottom', fontsize=12, fontweight='bold',
                color='#1E4E79')

# Configurar eixos
ax.set_xlim(0, 460)
ax.set_ylim(0, 10)
ax.set_xlabel('PIB (R$ bilhões)', fontsize=14, fontweight='bold', labelpad=10)
ax.set_ylabel('Número de Municípios', fontsize=14, fontweight='bold', labelpad=10)
ax.set_title('Distribuição do PIB dos 50 Maiores Municípios do Brasil - 2023', 
             fontsize=18, fontweight='bold', pad=20, color='#1E4E79')

# Configurar ticks do eixo X
xticks = [0, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 170, 200, 250, 300, 350, 400, 450]
xtick_labels = ['0', '30', '40', '50', '60', '70', '80', '90', '100', '120', '140', '170', '200', '250', '300', '350', '400', '450']
ax.set_xticks(xticks)
ax.set_xticklabels(xtick_labels, rotation=45, ha='right', fontsize=11)

# Configurar ticks do eixo Y
ax.set_yticks(range(0, 11))
ax.set_yticklabels(range(0, 11), fontsize=11)

# Adicionar grid suave
ax.grid(True, axis='y', alpha=0.2, linestyle='--', color='gray')
ax.grid(True, axis='x', alpha=0.1, linestyle='--', color='gray')
ax.set_axisbelow(True)

# Calcular estatísticas para as linhas
media = df['PIB (R$ bilhões)'].mean()
mediana = df['PIB (R$ bilhões)'].median()

# Adicionar linhas de média e mediana
ax.axvline(media, color='red', linestyle='--', linewidth=2.5, alpha=0.8, 
           label=f'Média: {media:.1f} bi')
ax.axvline(mediana, color='green', linestyle='--', linewidth=2.5, alpha=0.8, 
           label=f'Mediana: {mediana:.1f} bi')
ax.legend(loc='upper right', fontsize=11, framealpha=0.9)

# Destacar São Paulo como outlier
ax.annotate('São Paulo: 1066.8 bi', 
            xy=(1066, 1), xytext=(500, 8),
            arrowprops=dict(arrowstyle='->', color='darkred', linewidth=2),
            fontsize=11, fontweight='bold', color='darkred',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))

# Ajustar layout
plt.tight_layout()

# Salvar imagem
plt.savefig('histograma_pib_50_municipios.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')

print("✅ Histograma salvo como 'histograma_pib_50_municipios.png'")

# Mostrar o gráfico
plt.show()