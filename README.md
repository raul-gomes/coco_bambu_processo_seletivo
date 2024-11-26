### DESAFIO 1
#### Contexto:
A resposta de um determinado endpoint de API de ERP para uma loja de um restaurante está no arquivo [ERP.json](https://drive.google.com/file/d/1IFoFg_2B1A7gHukyaP92QX6EAt2FTZNs/view).
Este exemplo corresponde a um determinado pedido <i>(guestCheckId)</i> com um único item <i>(guestCheckLineItemId)</i>, referente a um único item de menu <i>(menuItem)</i> .

1. Descreva o esquema JSON correspondente ao exemplo acima.
<br>
2. Contexto

    No exemplo fornecido, o objeto detailLines contém um menuItem. Ele também pode conter instâncias de:
    - discount
    - serviceCharge
    - tenderMedia
    - errorCode

    Transcreva o JSON para tabelas SQL. A implementação deve fazer sentido para operações de restaurante.
<br>
3. Descreva a abordagem escolhida em detalhes. Justifique a escolha. Recomendações:
    - Faça um esboço antes de começar.
    - Considere que esta tarefa abrange toda a cadeia de restaurantes.
    - Descreva seu processo de pensamento, preocupações e as consequências detalhadamente.
    - Certifique-se de incluir pelo menos uma linha por ativo (asset).
    - Esperamos ver um código que você estaria confortável em colocar em produção.
    - Não hesite em pedir esclarecimentos ou, se preferir, faça uma suposição e siga com ela.


### DESAFIO 2
#### Contexto:
Nossa equipe de inteligência de negócios precisa analisar a receita de todas as lojas de uma rede de restaurantes. Essas informações podem ser obtidas por meio de 5 endpoints de API.

<b>Tarefa:</b> Esta é uma continuação do primeiro desafio. Você deve armazenar os dados das respostas das APIs (JSON) no nosso data lake.
1. Por que armazenar as respostas das APIs?
<br>
2. Como você armazenaria os dados? Crie uma estrutura de pastas capaz de armazenar as respostas da API. Ela deve permitir manipulaçõe, verificações, buscas e pesquisas rápidas.
<br>
3. Considere que a resposta do endpoint getGuestChecks foi alterada, por exemplo, <i>guestChecks</i>.taxes foi renomeado para guestChecks.taxation. O que isso implicaria?

<b>Recomendações:</b>
- Faça um esboço antes de começar.
- Considere que esta tarefa abrange toda a cadeia de restaurantes.
- Descreva seu processo de pensamento, preocupações e as consequências detalhadamente.
- Certifique-se de incluir pelo menos uma linha por ativo (asset).
- Esperamos ver um código que você estaria confortável em colocar em produção.
- Não hesite em pedir esclarecimentos ou, se preferir, faça uma suposição e siga com ela.

Você tem até 7 (sete) dias para completar esse desafio, a partir da data de recebimento. Cada
arquivo produzido na solução deve estar em um repositório Git, tais quais o código do
projeto, README.md, e o documento Kanban. Envie um email para
talentos.ti@cocobambu.com com o assunto Desafio Engenharia Dados Coco Bambu
2024. O corpo do email deve conter o link para o repositório Git. Com esse repositório,
devemos ser capazes de acessar o código, executar o projeto e possíveis testes.
Preparado?
Estamos ansiosos para receber sua solução. Boa sorte!