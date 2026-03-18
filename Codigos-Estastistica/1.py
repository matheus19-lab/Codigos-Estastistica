import pandas as pd
import os
import glob

# Caminho para a pasta com os arquivos
caminho_pasta = r"C:\Users\Mathe\Documents\Faculdade\5\Estastitica\TRABALHO 1\XLSX"

# Encontra todos os arquivos .xlsx na pasta
arquivos_xlsx = glob.glob(os.path.join(caminho_pasta, "*.xlsx"))

if not arquivos_xlsx:
    print("Nenhum arquivo .xlsx encontrado na pasta especificada.")
else:
    print(f"Encontrados {len(arquivos_xlsx)} arquivos:")
    for i, arquivo in enumerate(arquivos_xlsx):
        print(f"{i+1}. {os.path.basename(arquivo)}")
    
    # Lista para armazenar todos os DataFrames
    dataframes = []
    
    # Lê cada arquivo e adiciona à lista
    for arquivo in arquivos_xlsx:
        nome_arquivo = os.path.basename(arquivo)
        print(f"\nLendo o arquivo: {nome_arquivo}")
        
        try:
            df_temp = pd.read_excel(arquivo)
            print(f"  - Linhas: {len(df_temp)}")
            print(f"  - Colunas: {len(df_temp.columns)}")
            dataframes.append(df_temp)
        except Exception as e:
            print(f"  - Erro ao ler o arquivo: {e}")
    
    if not dataframes:
        print("Nenhum arquivo pôde ser lido com sucesso.")
    else:
        # Combina todos os DataFrames em um único
        df_combinado = pd.concat(dataframes, ignore_index=True)
        
        print(f"\n" + "="*80)
        print("DADOS COMBINADOS")
        print("="*80)
        print(f"Total de registros: {len(df_combinado)}")
        print(f"Total de colunas: {len(df_combinado.columns)}")
        
        # Mostra os anos disponíveis
        if 'Ano' in df_combinado.columns:
            anos_disponiveis = sorted(df_combinado['Ano'].unique())
            print(f"Anos disponíveis: {anos_disponiveis}")
        
        # Identifica a coluna do PIB
        coluna_pib = None
        for col in df_combinado.columns:
            if 'Produto Interno Bruto' in col and 'per capita' not in col:
                coluna_pib = col
                break
        
        if coluna_pib is None:
            print("\nColuna do PIB não encontrada. Colunas disponíveis:")
            print(df_combinado.columns.tolist())
        else:
            print(f"\nColuna do PIB identificada como: '{coluna_pib}'")
            
            # Remove valores nulos
            df_combinado = df_combinado.dropna(subset=[coluna_pib])
            
            # Identifica outras colunas
            coluna_municipio = 'Nome do Município' if 'Nome do Município' in df_combinado.columns else None
            coluna_uf = 'Sigla da Unidade da Federação' if 'Sigla da Unidade da Federação' in df_combinado.columns else None
            coluna_cod_municipio = 'Código do Município' if 'Código do Município' in df_combinado.columns else None
            
            # PIB per capita
            coluna_pib_percapita = None
            for col in df_combinado.columns:
                if 'per capita' in col.lower():
                    coluna_pib_percapita = col
                    break
            
            # Verifica se tem ano
            tem_ano = 'Ano' in df_combinado.columns
            
            print("\n" + "="*80)
            print("OPÇÕES DE ANÁLISE")
            print("="*80)
            print("1. Top 50 municípios (apenas o ano mais recente de cada)")
            print("2. Top 50 considerando todos os anos (com repetições)")
            print("3. Top 50 de um ano específico")
            
            opcao = input("\nEscolha uma opção (1, 2 ou 3): ").strip()
            
            if opcao == "1" and tem_ano:
                # Pega o ano mais recente para cada município
                print("\nAgrupando por município e pegando o ano mais recente...")
                
                # Identificador único do município (código ou nome+UF)
                if coluna_cod_municipio:
                    identificador = coluna_cod_municipio
                    print(f"Usando código do município como identificador: {identificador}")
                else:
                    # Se não tiver código, combina nome e UF
                    df_combinado['municipio_uf'] = df_combinado[coluna_municipio] + ' - ' + df_combinado[coluna_uf]
                    identificador = 'municipio_uf'
                    print("Usando nome + UF como identificador")
                
                # Pega o índice do ano mais recente para cada município
                idx_mais_recente = df_combinado.groupby(identificador)['Ano'].idxmax()
                df_filtrado = df_combinado.loc[idx_mais_recente].copy()
                
                print(f"Total de municípios únicos: {len(df_filtrado)}")
                
            elif opcao == "3" and tem_ano:
                anos_disponiveis = sorted(df_combinado['Ano'].unique())
                print(f"\nAnos disponíveis: {anos_disponiveis}")
                ano_escolhido = int(input("Digite o ano desejado: "))
                if ano_escolhido in anos_disponiveis:
                    df_filtrado = df_combinado[df_combinado['Ano'] == ano_escolhido].copy()
                    print(f"\nAnalisando dados apenas de {ano_escolhido}...")
                    print(f"Registros encontrados: {len(df_filtrado)}")
                else:
                    print("Ano inválido! Usando todos os anos.")
                    df_filtrado = df_combinado.copy()
            else:
                if opcao in ["1", "3"] and not tem_ano:
                    print("Coluna 'Ano' não encontrada! Usando todos os anos.")
                df_filtrado = df_combinado.copy()
                if opcao == "2":
                    print("\nMantendo todos os registros (com repetições por ano)...")
            
            # Filtra os 50 municípios com maior PIB
            top_50 = df_filtrado.nlargest(50, coluna_pib)
            
            # Prepara visualização
            colunas_visualizacao = []
            if coluna_municipio:
                colunas_visualizacao.append(coluna_municipio)
            if coluna_uf:
                colunas_visualizacao.append(coluna_uf)
            colunas_visualizacao.append(coluna_pib)
            if coluna_pib_percapita:
                colunas_visualizacao.append(coluna_pib_percapita)
            if tem_ano and 'Ano' in df_filtrado.columns:
                colunas_visualizacao.append('Ano')
            
            print(f"\n=== 50 MUNICÍPIOS COM MAIOR PIB ===\n")
            
            # Cria uma cópia para visualização
            top_50_display = top_50[colunas_visualizacao].copy()
            
            # Adiciona coluna em bilhões
            top_50_display['PIB (R$ bilhões)'] = top_50_display[coluna_pib] / 1000000
            
            # Formata a visualização
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', None)
            pd.set_option('display.max_colwidth', 30)
            
            # Mostra apenas as colunas mais relevantes
            colunas_mostrar = []
            if coluna_municipio:
                colunas_mostrar.append(coluna_municipio)
            if coluna_uf:
                colunas_mostrar.append(coluna_uf)
            colunas_mostrar.append('PIB (R$ bilhões)')
            if coluna_pib_percapita:
                colunas_mostrar.append(coluna_pib_percapita)
            if tem_ano and 'Ano' in df_filtrado.columns:
                colunas_mostrar.append('Ano')
            
            print(top_50_display[colunas_mostrar].to_string(index=False))
            
            # Salva resultados
            if opcao == "1":
                nome_saida = "top_50_pib_mais_recente_combinado.xlsx"
            elif opcao == "2":
                nome_saida = "top_50_pib_todos_anos_combinado.xlsx"
            else:
                nome_saida = f"top_50_pib_{ano_escolhido}_combinado.xlsx" if opcao == "3" and 'ano_escolhido' in locals() else "top_50_pib_combinado.xlsx"
            
            caminho_saida = os.path.join(caminho_pasta, nome_saida)
            top_50.to_excel(caminho_saida, index=False)
            print(f"\nResultados salvos em: {caminho_saida}")
            
            # Estatísticas
            print(f"\n=== RESUMO ESTATÍSTICO ===")
            print(f"Total de registros analisados: {len(df_filtrado)}")
            print(f"Total de arquivos combinados: {len(arquivos_xlsx)}")
            if tem_ano:
                print(f"Período analisado: {df_filtrado['Ano'].min()} a {df_filtrado['Ano'].max()}")
            
            pib_total_top50 = top_50[coluna_pib].sum()
            pib_medio_top50 = top_50[coluna_pib].mean()
            
            print(f"Soma do PIB dos top 50: R$ {pib_total_top50:,.2f} (mil) = R$ {pib_total_top50/1000000:.2f} bilhões")
            print(f"Média do PIB dos top 50: R$ {pib_medio_top50:,.2f} (mil) = R$ {pib_medio_top50/1000000:.2f} bilhões")
            
            # Mostra os 10 maiores
            print(f"\n=== TOP 10 MUNICÍPIOS ===")
            for idx, row in top_50.head(10).iterrows():
                municipio = row[coluna_municipio] if coluna_municipio else "N/A"
                uf = row[coluna_uf] if coluna_uf else "N/A"
                pib_bilhoes = row[coluna_pib] / 1000000
                ano = row['Ano'] if tem_ano and 'Ano' in row else "N/A"
                print(f"{idx+1}. {municipio}/{uf}: R$ {pib_bilhoes:.2f} bilhões (Ano: {ano})")
