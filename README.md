# Concatenação de Arquivos

Esse repositório traz algumas maneiras de concatenar dataframes ou pastas com arquivos CSV. Qualquer dúvida, sinta-se à vontade para me chamar no [linkedin](https://www.linkedin.com/in/paulo-oliveira-a6650121a/).

## Descrição sobre cada file
- ConcatDataFrame - Este código apenas faz a concatenação entre dois DataFrames, caso as colunas possuam os mesmos nomes as colunas serão mescladas, caso não, ela será uma coluna a parte no DataFrame, podendo ser contornado dando Drop na coluna ou Renomeando ela.
- ConcatFile - Neste arquivo será mostrado a seleção de uma pasta aonde o Glob estará fazendo a concatenação de todos os arquivos CSV, abaixo você pode estar vendo alguns filtros que podem ser usados na seleção de arquivos.

##  Seleção de Arquivos do Glob
#### - Seleção de Arquivo por uma Palavra no Nome
~~~
files = [f for f in glob.glob("path/file/*.csv") if "exemplo" in f]
# Ele vai pegar qualquer arquivo que tenha a palavra exemplo em seu nome dentro da pasta, ou seja, ele vai pegar arquivos que estejam como janeiro_exemplo, exemplo_ganhos etc.
~~~

#### - Por Data do Arquivo
~~~
import os
import datetime

ano = 2023

file = glob.glob("path/file/*.csv")

arquivos_ano_x = [
    f for f in file 
    if datetime.datetime.fromtimestamp(os.path.getmtime(f)).year == ano
]
arquivos_ano_x
~~~

#### - Por nome do Arquivo
~~~
file = glob.glob("path/file/exemplo_*.csv")
#Ele vai pegar qualquer arquivo que siga o padrão, ex: exemplo_2023, exemplo_janeiro, exemplo_vendas.
~~~
