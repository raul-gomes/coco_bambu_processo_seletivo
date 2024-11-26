# Estratégia de Modelagem e Implementação

## 1. Esboço e Planejamento

Antes de começar, analisei o arquivo JSON para identificar os objetos e as relações entre eles. A estrutura principal do JSON se organiza em torno de um pedido (`guestCheck`) contendo informações gerais, itens detalhados (`detailLines`), taxas (`taxes`) e um item de menu associado (`menuItem`). O desafio também introduziu outros possíveis detalhes nos itens, como:

- Descontos (`discount`)
- Cobranças de serviço (`serviceCharge`)
- Meios de pagamento (`tenderMedia`)
- Códigos de erro (`errorCode`)

Meu objetivo foi criar uma estrutura de banco de dados relacional que fosse eficiente e escalável, considerando a necessidade de manipulação, consultas rápidas e manutenção para toda a cadeia de restaurantes.

---

## 2. Processo de Pensamento

### 2.1 Identificação de Entidades

A análise do JSON levou à definição das seguintes entidades:

- **GuestChecks**: Representa um pedido realizado em um restaurante.
- **Taxes**: Contém informações sobre as taxas associadas ao pedido.
- **DetailLines**: Detalha os itens associados a um pedido.
- **MenuItems**: Representa informações específicas sobre um item do menu.
- **Discounts, ServiceCharges, TenderMedia, ErrorCodes**: Possíveis extensões para os itens detalhados.

### 2.2 Estrutura Relacional

A modelagem seguiu o paradigma relacional:

- Cada entidade foi mapeada para uma tabela.
- Relacionamentos foram definidos com chaves estrangeiras, respeitando a hierarquia do JSON.
- Estruturas normalizadas para evitar redundância e facilitar a manutenção.

### 2.3 Decisões Técnicas

- **Tipos de Dados**: Escolhidos para otimizar espaço e precisão (e.g., `FLOAT` para valores monetários, `DATETIME` para timestamps).
- **Normalização**: Separação de entidades em tabelas distintas, promovendo modularidade e permitindo futuras alterações (e.g., novos tipos de instâncias em `detailLines`).
- **Manutenção e Escalabilidade**: O design considera a possibilidade de novos atributos ou entidades.

---

## 3. Preocupações

### 3.1 Escalabilidade

Considerando a cadeia de restaurantes, o volume de dados pode crescer rapidamente. A estrutura criada suporta consultas eficientes por meio de índices e organização lógica.

### 3.2 Integração com APIs

Os dados provenientes das APIs são complexos, e mudanças nos endpoints, como a renomeação de atributos (e.g., `taxes` para `taxation`), podem impactar as operações. Foi considerado o uso de camadas intermediárias (ETL) para tratar essas alterações antes de salvar os dados no banco.

### 3.3 Manutenção

O design modular facilita a adaptação a mudanças. Por exemplo, se um novo tipo de detalhe for adicionado, pode-se criar uma nova tabela e relacioná-la sem alterações disruptivas.

---

## 4. Consequências

### Vantagens

- Estrutura robusta e pronta para operações de leitura intensiva (BI e dashboards).
- Facilidade de extensão para novos atributos ou tipos de dados.
- Clareza nas relações, facilitando consultas e análises.

### Desafios

- Inserção inicial mais complexa devido à normalização.
- Dependência de ETL para mitigar mudanças nos dados de entrada.

---

## 5. Justificativa

Essa abordagem equilibra eficiência operacional e flexibilidade. A normalização mantém o banco escalável e evita redundância, enquanto os relacionamentos definidos facilitam a consulta e a análise dos dados.

O código apresentado está otimizado para produção e permite fácil integração com sistemas de BI ou pipelines de dados. Além disso, a modularidade suporta o crescimento do negócio e a evolução tecnológica da cadeia de restaurantes.
