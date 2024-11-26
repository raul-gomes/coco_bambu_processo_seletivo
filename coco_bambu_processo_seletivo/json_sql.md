## Estrutura Relacional do JSON

### Tabela: guest_checks
Armazena informações sobre cada pedido realizado no restaurante.

| Coluna            | Tipo       | Descrição                                  |
|--------------------|------------|--------------------------------------------|
| guest_check_id     | INTEGER    | ID único do pedido (PK).                   |
| chk_num            | INTEGER    | Número do pedido.                          |
| opn_bus_dt         | DATE       | Data de abertura do pedido.                |
| opn_utc            | DATETIME   | Hora de abertura (UTC).                    |
| opn_lcl            | DATETIME   | Hora de abertura (local).                  |
| clsd_bus_dt        | DATE       | Data de fechamento do pedido.              |
| clsd_utc           | DATETIME   | Hora de fechamento (UTC).                  |
| clsd_lcl           | DATETIME   | Hora de fechamento (local).                |
| last_trans_utc     | DATETIME   | Última transação (UTC).                    |
| last_trans_lcl     | DATETIME   | Última transação (local).                  |
| last_updated_utc   | DATETIME   | Última atualização (UTC).                  |
| last_updated_lcl   | DATETIME   | Última atualização (local).                |
| clsd_flag          | BOOLEAN    | Indicador de pedido fechado.               |
| gst_cnt            | INTEGER    | Número de convidados.                      |
| sub_ttl            | FLOAT      | Subtotal do pedido.                        |
| non_txbl_sls_ttl   | FLOAT      | Valor não tributável (nulo se não existir).|
| chk_ttl            | FLOAT      | Total do pedido.                           |
| dsc_ttl            | FLOAT      | Total de descontos.                        |
| pay_ttl            | FLOAT      | Total pago.                                |
| bal_due_ttl        | FLOAT      | Saldo devedor (nulo se quitado).           |
| rvc_num            | INTEGER    | Número do recibo vinculado.                |
| ot_num             | INTEGER    | Número da ordem do ticket.                 |
| oc_num             | INTEGER    | Código do operador (nulo se não aplicável).|
| tbl_num            | INTEGER    | Número da mesa.                            |
| tbl_name           | TEXT       | Nome ou código da mesa.                    |
| emp_num            | INTEGER    | Número do funcionário responsável.         |
| num_srvc_rd        | INTEGER    | Número de rodadas de serviço.              |
| num_chk_prntd      | INTEGER    | Número de vezes que o pedido foi impresso. |


```sql
CREATE TABLE guest_checks (
    guest_check_id INTEGER PRIMARY KEY,
    chk_num INTEGER,
    opn_bus_dt DATE,
    opn_utc DATETIME,
    opn_lcl DATETIME,
    clsd_bus_dt DATE,
    clsd_utc DATETIME,
    clsd_lcl DATETIME,
    last_trans_utc DATETIME,
    last_trans_lcl DATETIME,
    last_updated_utc DATETIME,
    last_updated_lcl DATETIME,
    clsd_flag BOOLEAN,
    gst_cnt INTEGER,
    sub_ttl FLOAT,
    non_txbl_sls_ttl FLOAT,
    chk_ttl FLOAT,
    dsc_ttl FLOAT,
    pay_ttl FLOAT,
    bal_due_ttl FLOAT,
    rvc_num INTEGER,
    ot_num INTEGER,
    oc_num INTEGER,
    tbl_num INTEGER,
    tbl_name TEXT,
    emp_num INTEGER,
    num_srvc_rd INTEGER,
    num_chk_prntd INTEGER
);

```
---

### Tabela: taxes
Armazena informações sobre taxas aplicadas no pedido.

| Coluna            | Tipo       | Descrição                                  |
|--------------------|------------|--------------------------------------------|
| tax_id            | INTEGER    | ID único da taxa (PK).                     |
| tax_num           | INTEGER    | Número de identificação da taxa.           |
| txbl_sls_ttl      | FLOAT      | Total de vendas tributáveis.               |
| tax_coll_ttl      | FLOAT      | Total de imposto coletado.                 |
| tax_rate          | FLOAT      | Taxa de imposto aplicada (%).              |
| type              | INTEGER    | Tipo de imposto.                           |
| guest_check_id    | INTEGER    | ID do pedido (FK para guest_checks).       |


```sql
CREATE TABLE taxes (
    tax_id INTEGER PRIMARY KEY,
    tax_num INTEGER,
    txbl_sls_ttl FLOAT,
    tax_coll_ttl FLOAT,
    tax_rate FLOAT,
    type INTEGER,
    guest_check_id INTEGER,
    FOREIGN KEY (guest_check_id) REFERENCES guest_checks (guest_check_id)
);
```
---

### Tabela: detail_lines
Armazena os itens detalhados do pedido.


| Coluna            | Tipo       | Descrição                                  |
|--------------------|------------|--------------------------------------------|
| detail_line_id    | INTEGER    | ID único do item detalhado (PK).           |
| rvc_num           | INTEGER    | Número do recibo vinculado.                |
| dtl_ot_num        | INTEGER    | Número da ordem do ticket para o item.     |
| dtl_oc_num        | INTEGER    | Código do operador vinculado ao item.      |
| line_num          | INTEGER    | Número da linha no pedido.                 |
| dtl_id            | INTEGER    | ID único do detalhe.                       |
| detail_utc        | DATETIME   | Hora do detalhe (UTC).                     |
| detail_lcl        | DATETIME   | Hora do detalhe (local).                   |
| last_update_utc   | DATETIME   | Última atualização do item (UTC).          |
| last_update_lcl   | DATETIME   | Última atualização do item (local).        |
| bus_dt            | DATE       | Data do detalhe.                           |
| ws_num            | INTEGER    | Número da estação de trabalho vinculada.   |
| dsp_ttl           | FLOAT      | Total exibido para o item.                 |
| dsp_qty           | INTEGER    | Quantidade exibida para o item.            |
| agg_ttl           | FLOAT      | Total agregado para o item.                |
| agg_qty           | INTEGER    | Quantidade agregada para o item.           |
| chk_emp_id        | INTEGER    | ID do funcionário responsável pelo item.   |
| chk_emp_num       | INTEGER    | Número do funcionário responsável.         |
| svc_rnd_num       | INTEGER    | Número da rodada de serviço.               |
| seat_num          | INTEGER    | Número do assento vinculado.               |
| guest_check_id    | INTEGER    | ID do pedido (FK para guest_checks).       |


```sql
CREATE TABLE detail_lines (
    detail_line_id INTEGER PRIMARY KEY,
    rvc_num INTEGER,
    dtl_ot_num INTEGER,
    dtl_oc_num INTEGER,
    line_num INTEGER,
    dtl_id INTEGER,
    detail_utc DATETIME,
    detail_lcl DATETIME,
    last_update_utc DATETIME,
    last_update_lcl DATETIME,
    bus_dt DATE,
    ws_num INTEGER,
    dsp_ttl FLOAT,
    dsp_qty INTEGER,
    agg_ttl FLOAT,
    agg_qty INTEGER,
    chk_emp_id INTEGER,
    chk_emp_num INTEGER,
    svc_rnd_num INTEGER,
    seat_num INTEGER,
    guest_check_id INTEGER,
    FOREIGN KEY (guest_check_id) REFERENCES guest_checks (guest_check_id)
);
```
---

### Tabela: menu_items
Armazena informações específicas sobre itens do menu.


| Coluna            | Tipo       | Descrição                                  |
|--------------------|------------|--------------------------------------------|
| menu_item_id      | INTEGER    | ID único do item do menu (PK).             |
| mi_num            | INTEGER    | Número de identificação do item no menu.   |
| mod_flag          | BOOLEAN    | Indicador de modificação no item.          |
| incl_tax          | FLOAT      | Valor total de impostos incluídos.         |
| active_taxes      | TEXT       | Lista de IDs de taxas aplicadas (separados).|
| prc_lvl           | INTEGER    | Nível de preço aplicado ao item.           |
| detail_line_id    | INTEGER    | ID do item detalhado (FK para detail_lines).|

```sql
CREATE TABLE menu_items (
    menu_item_id INTEGER PRIMARY KEY,
    mi_num INTEGER,
    mod_flag BOOLEAN,
    incl_tax FLOAT,
    active_taxes TEXT,
    prc_lvl INTEGER,
    detail_line_id INTEGER,
    FOREIGN KEY (detail_line_id) REFERENCES detail_lines (detail_line_id)
);
```
---
### Relacionamentos
- <b>guest_checks ↔ taxes:</b> Um pedido pode ter várias taxas associadas.
- <b>guest_checks ↔ detail_lines:</b> Um pedido pode conter vários itens detalhados.
- <b>detail_lines ↔ menu_items:</b> Cada item detalhado pode conter um item do menu.