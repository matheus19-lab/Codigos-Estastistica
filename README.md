# Projeto Gráficos de Estatística

Este repositório contém scripts Python para processamento de dados estatísticos (PIB municipal) e geração de gráficos/tabulações.

## Estrutura

- `BD/` - Dados brutos (não versionados ou não incluídos).
- `Codigos-Estastistica/`
  - `1.py` - Consolida arquivos Excel (`.xlsx`) de PIB, seleciona top 50 e exporta resultados.
  - `boxplot.py` - Script para gerar boxplot (não detalhado no README atual).
  - `Grafico_Barras.py` - Script para gerar gráfico de barras.
  - `Histograma.py` - Script para gerar histórico.
  - `Tabela_simples.py` - Script para tabela simples.

## Requisitos

- Python 3.8+ (recomendado)
- pandas
- openpyxl (para leitura ou escrita do Excel)

Instalar dependências:

```bash
pip install pandas openpyxl
```

## Uso principal (`1.py`)

1. Coloque os arquivos `.xlsx` no diretório configurado em `caminho_pasta` (por padrão, `...\XLSX`).
2. Execute:

```bash
python Codigos-Estastistica\1.py
```

3. Escolha a opção:
   - 1: Top 50 por PIB (ano mais recente de cada município)
   - 2: Top 50 considerando todos os anos (com repetições)
   - 3: Top 50 para um ano específico

4. Resultado: arquivo de saída `top_50_*_combinado.xlsx` será gerado no mesmo diretório de entrada.

## Observações

- O script detecta automaticamente colunas de PIB e PIB per capita se existirem.
- Se a coluna `Ano` estiver ausente, a opção 1/3 cairá no modo de análise sem ano.
- Ajuste os nomes de colunas se o formato de dados do seu Excel for diferente.
