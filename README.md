# Análise Climática Interativa

Ferramenta em Python para explorar um conjunto histórico de dados climáticos no terminal. O script carrega um arquivo CSV com registros diários, permite aplicar filtros por período, calcula estatísticas de precipitação e temperatura e gera um gráfico de barras em modo texto para acompanhar a evolução das temperaturas mínimas ao longo dos anos.

## Funcionalidades
- Leitura de dados meteorológicos (data, precipitação, temp. maxima, temp. minima, umidade, vento).
- Visualização de intervalos por mês e ano, com seleção de colunas de interesse.
- Identificação do mês/ano com maior acumulado de chuva.
- Cálculo de médias das temperaturas mínimas para um mês entre 2006 e 2016.
- Gráfico textual das médias anuais da temperatura mínima.

## Requisitos
- Python 3.8 ou superior.
- Arquivo `dados_climaticos_historicos.csv` na mesma pasta do script e com cabeçalho no formato:

  ```
  data,precipitacao,temp_max,temp_min,umidade,vento
  2006-01-01,5.2,29.0,20.3,81.0,12.1
  ```

## Como executar
```bash
python analise_climatica_interativa.py
```

Siga os passos apresentados no terminal: informe o período desejado, escolha os dados que deseja visualizar, selecione um mês por extenso para a análise de temperatura mánima e avalie o gráfico textual gerado.

## Estrutura
- `analise_climatica_interativa.py`: script principal com toda a lógica de análise.
- `dados_climaticos_historicos.csv`: arquivo esperado com os dados brutos.
