import pandas as pd
import matplotlib.pyplot as plt

# Dados
dados = [
    ['São Paulo', 'SP', 1066.83], ['Rio de Janeiro', 'RJ', 418.46],
    ['Brasília', 'DF', 365.67], ['Maricá', 'RJ', 134.09],
    ['Belo Horizonte', 'MG', 130.20], ['Manaus', 'AM', 127.65],
    ['Curitiba', 'PR', 120.07], ['Osasco', 'SP', 119.40],
    ['Porto Alegre', 'RS', 104.74], ['Guarulhos', 'SP', 97.56],
    ['Campinas', 'SP', 91.97], ['Fortaleza', 'CE', 86.94],
    ['Salvador', 'BA', 76.70], ['Niterói', 'RJ', 76.27],
    ['Goiânia', 'GO', 75.78], ['São Bernardo do Campo', 'SP', 71.97],
    ['Barueri', 'SP', 71.65], ['Duque de Caxias', 'RJ', 70.07],
    ['Paulínia', 'SP', 67.07], ['Recife', 'PE', 66.35],
    ['Jundiaí', 'SP', 65.42], ['Saquarema', 'RJ', 64.70],
    ['São José dos Campos', 'SP', 61.39], ['Sorocaba', 'SP', 58.82],
    ['Betim', 'MG', 52.61], ['Ribeirão Preto', 'SP', 52.31],
    ['Uberlândia', 'MG', 51.07], ['Joinville', 'SC', 49.82],
    ['Itajaí', 'SC', 48.20], ['Contagem', 'MG', 45.09],
    ['Piracicaba', 'SP', 44.35], ['Campos dos Goytacazes', 'RJ', 42.95],
    ['São Luís', 'MA', 42.39], ['Campo Grande', 'MS', 42.27],
    ['Belém', 'PA', 40.54], ['Cuiabá', 'MT', 39.05],
    ['Caxias do Sul', 'RS', 37.86], ['Serra', 'ES', 37.65],
    ['Santo André', 'SP', 36.93], ['Araucária', 'PR', 34.08],
    ['São José dos Pinhais', 'PR', 33.96], ['Maceió', 'AL', 33.75],
    ['Florianópolis', 'SC', 31.19], ['Natal', 'RN', 31.16],
    ['Santos', 'SP', 30.96], ['Teresina', 'PI', 29.45],
    ['Canoas', 'RS', 29.17], ['Cajamar', 'SP', 28.99],
    ['João Pessoa', 'PB', 28.44], ['Indaiatuba', 'SP', 28.27]
]

df = pd.DataFrame(dados, columns=['Município', 'UF', 'PIB'])

# Estatísticas
q1 = df['PIB'].quantile(0.25)
q3 = df['PIB'].quantile(0.75)
mediana = df['PIB'].median()
media = df['PIB'].mean()

# Figura
fig, ax = plt.subplots(figsize=(12, 6))

# Boxplot
box = ax.boxplot(df['PIB'], vert=False, patch_artist=True, showmeans=True)

# Cores
box['boxes'][0].set(facecolor='#4C72B0', alpha=0.7)
box['medians'][0].set(color='orange', linewidth=3)
box['means'][0].set(color='green', linewidth=2)

# Linhas
ax.axvline(q1, linestyle='--', linewidth=1)
ax.axvline(mediana, linestyle='-', linewidth=2)
ax.axvline(q3, linestyle='--', linewidth=1)
ax.axvline(media, linestyle=':', linewidth=2)

# Configuração
ax.set_xlim(0, 500)
ax.set_yticks([])
ax.set_title('Distribuição do PIB dos 50 Maiores Municípios Brasileiros', fontsize=14, weight='bold')
ax.set_xlabel('PIB (R$ bilhões)')

# Outlier
ax.annotate(
    'São Paulo (outlier)',
    xy=(1066, 1),
    xytext=(330, 1.15),
    arrowprops=dict(arrowstyle='->'),
    fontsize=10
)

# 🔥 INTERPRETAÇÃO (AGORA MAIS PRÓXIMA)
interpretacao = (
    "INTERPRETAÇÃO\n\n"
    f"Q1: {q1:.1f}\n"
    f"Mediana: {mediana:.1f}\n"
    f"Q3: {q3:.1f}\n"
    f"Média: {media:.1f}\n\n"
    "• 50% entre Q1 e Q3\n"
    "• Assimetria à direita\n"
    "• SP = outlier"
)

fig.text(
    0.3, 0.5, interpretacao,   # 👈 puxado mais pra perto
    fontsize=10,
    va='center',
    bbox=dict(boxstyle='round', facecolor='white', alpha=0.95)
)

# Ajuste fino do layout
plt.tight_layout(rect=[0, 0, 0.78, 1])

# ✅ AGORA SALVA CERTO
plt.savefig('boxplot_final.png', dpi=300, bbox_inches='tight')

plt.show()