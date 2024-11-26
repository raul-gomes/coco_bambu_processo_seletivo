### Desafio 2

1. Por que armazenar as respostas das APIs?

Armazenar as respostas das APIs oferece várias vantagens:

- <b>Persistência de dados:</b> Permite manter um histórico das informações fornecidas, essencial para análises futuras.
- <b>Auditoria e conformidade:</b> Garante rastreabilidade em caso de inconsistências ou revisões de relatórios.
- <b>Evita dependência em tempo real:</b> Caso a API esteja indisponível, os dados armazenados ainda podem ser usados.
- <b>Desempenho otimizado:</b> Reduz a necessidade de requisições repetidas para APIs, economizando tempo e recursos.
- <b>Flexibilidade analítica:</b> Facilita o uso dos dados em pipelines de ETL, análises preditivas ou relatórios de BI.

2. Como você armazenaria os dados?

Para armazenar os dados no data lake, utilizaria uma estrutura de pastas organizada por critérios que otimizem buscas e mantenham a escalabilidade. Uma possível estrutura seria:

```shell
$tree
/data-lake/
  └── restaurant-chain/
      ├── fiscal-invoice/
      │   └── year=2024/
      │       └── month=05/
      │           └── day=05/
      │               └── storeId=001/
      │                   └── data.json
      ├── guest-checks/
      │   └── year=2024/
      │       └── month=05/
      │           └── day=05/
      │               └── storeId=001/
      │                   └── data.json
      ├── charge-back/
      │   └── year=2024/
      │       └── month=05/
      │           └── day=05/
      │               └── storeId=001/
      │                   └── data.json
      ├── transactions/
      │   └── year=2024/
      │       └── month=05/
      │           └── day=05/
      │               └── storeId=001/
      │                   └── data.json
      └── cash-menanagemt/
          └── year=2024/
              └── month=05/
                  └── day=05/
                      └── storeId=001/
                          └── data.json
```
Justificativa:

- A organização hierárquica por endpoint, ano, mês, dia e storeId facilita a recuperação e processamento seletivo dos dados.
- Usar partições (por exemplo, year, month, day) melhora o desempenho de consultas em ferramentas como Spark ou Hive.
- O uso de JSON mantém o formato original da resposta da API, preservando flexibilidade para transformações futuras.

3. Impacto de mudanças na estrutura da resposta da API

A alteração de guestChecks.taxes para guestChecks.taxation tem os seguintes impactos:

<b>Implicações Técnicas:</b>

- ETL/Data Pipeline: Se o pipeline atual espera guestChecks.taxes, ele falhará ao processar guestChecks.taxation devido à mudança de nomenclatura.
- Scripts de Análise: Consultas ou transformações que dependem da chave taxes precisarão ser ajustadas.
- Documentação: A mudança exige atualização nas definições e contratos da API.
- Inconsistência Temporal: Dados antigos no data lake utilizariam taxes, enquanto dados novos teriam taxation.

<b>Soluções:</b>

- Criação de uma camada de pré-processamento: 
  - Detectar e renomear automaticamente taxation para taxes ao inserir os dados no data lake.
  - Garante consistência entre dados históricos e novos.
- Versão dos Dados:
  - Adicionar metadados para indicar a versão do schema no momento da ingestão.
  - Permite rastrear mudanças no formato da API ao longo do tempo.
- Documentação:
  - Atualizar a definição do contrato da API e informar a equipe responsável pelas pipelines para evitar interrupções.