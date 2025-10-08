import os

# Dicionário para conversão do nome do mês para número
MESES = {
    "janeiro": 1, "fevereiro": 2, "março": 3, "abril": 4,
    "maio": 5, "junho": 6, "julho": 7, "agosto": 8,
    "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12
}

def parse_date(data_str):
    """
    Converte a string de data em uma tupla (ano, mês, dia).
    Tenta o formato dd/mm/aaaa e, se falhar, tenta o formato aaaa-mm-dd.
    """
    try:
        dia, mes, ano = map(int, data_str.split('/'))
        return ano, mes, dia
    except Exception:
        try:
            ano, mes, dia = map(int, data_str.split('-'))
            return ano, mes, dia
        except Exception:
            raise ValueError("Formato de data desconhecido: " + data_str)

def carregar_dados():
    """
    Lê os dados do arquivo CSV (deve estar na mesma pasta do programa).
    Espera que o arquivo contenha um cabeçalho e os campos:
    data, precipitação, temperatura máxima, temperatura mínima, umidade e vento.
    Registros com número insuficiente de campos ou erro na conversão são ignorados.
    """
    dados = []
    # Nome do arquivo contendo os dados brutos.
    nome_arquivo = 'dados_climaticos_historicos.csv'
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            # Supõe que a primeira linha é o cabeçalho
            for linha in linhas[1:]:
                partes = linha.strip().split(',')
                if len(partes) < 6:
                    continue  # descarta linhas incompletas
                try:
                    registro = {
                        "data": partes[0],
                        "precipitacao": float(partes[1]),
                        "temp_max": float(partes[2]),
                        "temp_min": float(partes[3]),
                        "umidade": float(partes[4]),
                        "vento": float(partes[5])
                    }
                    dados.append(registro)
                except ValueError:
                    # Caso ocorra erro na conversão numérica, ignora o registro
                    continue
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado. Certifique-se de que ele está na mesma pasta do programa.")
    return dados

def visualizar_intervalo(dados):
    """
    Permite que o usuário visualize um intervalo de dados.
    O usuário informa o mês/ano de início e fim e escolhe entre:
      1) Todos os dados;
      2) Apenas precipitação;
      3) Apenas temperaturas (máxima e mínima);
      4) Apenas umidade e vento.
    Os dados são filtrados com base no período informado.
    """
    print("\n=== Visualização de Intervalo de Dados ===")
    try:
        mes_inicio = int(input("Informe o mês inicial (1-12): "))
        ano_inicio = int(input("Informe o ano inicial: "))
        mes_fim = int(input("Informe o mês final (1-12): "))
        ano_fim = int(input("Informe o ano final: "))
        if not (1 <= mes_inicio <= 12 and 1 <= mes_fim <= 12):
            print("Mês inválido!")
            return
    except ValueError:
        print("Entrada inválida. Certifique-se de informar números inteiros.")
        return

    print("\nSelecione os dados a serem visualizados:")
    print("1) Todos os dados")
    print("2) Apenas precipitação")
    print("3) Apenas temperaturas (máxima e mínima)")
    print("4) Apenas umidade e vento")
    opcao = input("Opção: ")

    registros_filtrados = []
    # Converte os períodos para um formato inteiro (aaaaMM) para facilitar a comparação
    inicio = ano_inicio * 100 + mes_inicio
    fim = ano_fim * 100 + mes_fim

    for registro in dados:
        try:
            ano, mes, _ = parse_date(registro["data"])
        except ValueError:
            continue
        data_int = ano * 100 + mes
        if inicio <= data_int <= fim:
            registros_filtrados.append(registro)

    print("\n--- Dados Selecionados ---")
    if opcao == "1":
        print("Data\t\tPrecipitação\tTemp Máx\tTemp Mín\tUmidade\tVento")
        for r in registros_filtrados:
            print(f"{r['data']}\t{r['precipitacao']}\t\t{r['temp_max']}\t\t{r['temp_min']}\t\t{r['umidade']}\t{r['vento']}")
    elif opcao == "2":
        print("Data\t\tPrecipitação")
        for r in registros_filtrados:
            print(f"{r['data']}\t{r['precipitacao']}")
    elif opcao == "3":
        print("Data\t\tTemp Máx\tTemp Mín")
        for r in registros_filtrados:
            print(f"{r['data']}\t{r['temp_max']}\t\t{r['temp_min']}")
    elif opcao == "4":
        print("Data\t\tUmidade\tVento")
        for r in registros_filtrados:
            print(f"{r['data']}\t{r['umidade']}\t{r['vento']}")
    else:
        print("Opção inválida!")

def mes_mais_chuvoso(dados):
    """
    Calcula qual mês/ano acumulou a maior precipitação.
    Para isso, soma os valores diários de precipitação para cada mês/ano,
    armazenando os resultados em um dicionário, e depois identifica o maior.
    """
    precip_por_mes = {}
    for registro in dados:
        try:
            ano, mes, _ = parse_date(registro["data"])
        except ValueError:
            continue
        chave = f"{mes:02d}/{ano}"
        precip_por_mes[chave] = precip_por_mes.get(chave, 0) + registro["precipitacao"]

    if precip_por_mes:
        mes_chuvoso = max(precip_por_mes, key=precip_por_mes.get)
        print(f"\nMês mais chuvoso: {mes_chuvoso} com um total de {precip_por_mes[mes_chuvoso]:.2f} mm de precipitação")
    else:
        print("Nenhum dado disponível para análise de precipitação.")

def calcular_media_temp_min_mes(dados, mes_num, mes_nome):
    """
    Para cada ano de 2006 a 2016, calcula a média da temperatura mínima
    do mês especificado. Os resultados são armazenados em um dicionário cuja
    chave é o nome do mês concatenado com o ano (ex: 'agosto2006') e o valor é a média.
    """
    media_dict = {}
    for ano in range(2006, 2017):
        registros = []
        for r in dados:
            try:
                ano_r, mes_r, _ = parse_date(r["data"])
            except ValueError:
                continue
            if ano_r == ano and mes_r == mes_num:
                registros.append(r)
        if registros:
            media = sum(r["temp_min"] for r in registros) / len(registros)
            chave = f"{mes_nome}{ano}"
            media_dict[chave] = media
        else:
            print(f"Aviso: Sem dados para {mes_nome} de {ano}.")
    return media_dict

def plot_media_temp_min_texto(media_dict, mes_nome):
    """
    Gera um "gráfico de barras" em modo texto para as médias da temperatura mínima
    do mês informado, ao longo dos anos (2006 a 2016). Cada linha exibe o ano, o valor
    médio e uma barra composta de caracteres, proporcional ao valor.
    """
    print(f"\nGráfico de barras para a média da temperatura mínima de {mes_nome.capitalize()} (2006-2016):")
    
    # Extrai anos e médias a partir do dicionário (chaves no formato 'mesAno', ex.: 'agosto2006')
    dados_plot = []
    for chave, media in media_dict.items():
        try:
            ano = int(chave.replace(mes_nome, ""))
            dados_plot.append((ano, media))
        except Exception:
            continue

    if not dados_plot:
        print("Não há dados suficientes para gerar o gráfico.")
        return

    # Ordena os dados por ano
    dados_plot.sort(key=lambda x: x[0])
    
    # Define um fator de escala para o comprimento das barras.
    # Aqui, multiplicamos a média por 5 para gerar uma barra com tamanho perceptível.
    scale = 5

    for ano, media in dados_plot:
        # Se a média for negativa, usa '-' para representar; caso contrário, usa '*'
        length = int(abs(media) * scale)
        bar = ("*" * length) if media >= 0 else ("-" * length)
        print(f"{ano}: {media:.2f}°C | {bar}")

def main():
    # Carrega os dados do arquivo CSV
    dados = carregar_dados()
    if not dados:
        return

    # a) Visualização de intervalo de dados
    visualizar_intervalo(dados)

    # b) Mês mais chuvoso (acumulado de precipitação)
    mes_mais_chuvoso(dados)

    # c) Média da temperatura mínima de um determinado mês (2006-2016)
    mes_input = input("\nInforme o mês (por extenso, ex: 'agosto'): ").strip().lower()
    if mes_input not in MESES:
        print("Mês inválido!")
        return
    mes_num = MESES[mes_input]
    media_dict = calcular_media_temp_min_mes(dados, mes_num, mes_input)

    # d) Geração do "gráfico" de barras em modo texto com as médias calculadas
    plot_media_temp_min_texto(media_dict, mes_input)

    # e) Média geral da temperatura mínima para o mês (2006-2016)
    if media_dict:
        media_geral = sum(media_dict.values()) / len(media_dict)
        print(f"\nMédia geral da temperatura mínima para {mes_input} (2006-2016): {media_geral:.2f}°C")
    else:
        print("Não foi possível calcular a média geral devido à falta de dados.")

if __name__ == "__main__":
    main()
