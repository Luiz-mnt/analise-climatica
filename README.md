# Analise Climatica Interativa

Ferramenta em Python para explorar um conjunto historico de dados climaticos no terminal. O script carrega um arquivo CSV com registros diarios, permite aplicar filtros por periodo, calcula estatisticas de precipitacao e temperatura e gera um grafico de barras em modo texto para acompanhar a evolucao das temperaturas minimas ao longo dos anos.

## Funcionalidades
- Leitura de dados meteorologicos (data, precipitacao, temp. maxima, temp. minima, umidade, vento).
- Visualizacao de intervalos por mes e ano, com selecao de colunas de interesse.
- Identificacao do mes/ano com maior acumulado de chuva.
- Calculo de medias das temperaturas minimas para um mes entre 2006 e 2016.
- Grafico textual das medias anuais da temperatura minima.

## Requisitos
- Python 3.8 ou superior.
- Arquivo `dados_climaticos_historicos.csv` na mesma pasta do script, codificado em UTF-8 e com cabecalho no formato:

  ```
  data,precipitacao,temp_max,temp_min,umidade,vento
  2006-01-01,5.2,29.0,20.3,81.0,12.1
  ```

## Como executar
```bash
python analise_climatica_interativa.py
```

Siga os passos apresentados no terminal: informe o periodo desejado, escolha os dados que deseja visualizar, selecione um mes por extenso para a analise de temperatura minima e avalie o grafico textual gerado.

## Estrutura
- `analise_climatica_interativa.py`: script principal com toda a logica de analise.
- `dados_climaticos_historicos.csv`: arquivo esperado com os dados brutos (nao incluido neste repositorio).

## Licenca
Projeto educacional sem licenca especifica definida. Ajuste conforme necessario para seu uso.
