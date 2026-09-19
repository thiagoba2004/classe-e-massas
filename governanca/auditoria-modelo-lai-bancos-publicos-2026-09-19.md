# Auditoria — Modelo LAI para posicionamento dos bancos públicos

**Projeto:** PRJ-000001 — Classe e Massas  
**Estratégia:** EA-000001-000020 — Modelo LAI para posicionamento dos bancos públicos  
**Data:** 19/09/2026

## Resultado

O Modelo foi criado e publicado no repositório com os três artefatos canônicos:

- `lai/bancos-publicos-produtividade-clientes.md`;
- `lai/bancos-publicos-produtividade-clientes.html`;
- `lai/bancos-publicos-produtividade-clientes.json`.

A Central LAI foi atualizada em `lai/index.html`.

## Auditoria jurídica

O texto foi estruturado para solicitar:

- normas, políticas, manuais e protocolos preexistentes;
- registros e sistemas já existentes;
- pareceres, notas técnicas e manifestações institucionais já produzidas;
- dados agregados quando já consolidados;
- eventual posição institucional formal já documentada.

O Modelo declara expressamente que não solicita:

- parecer jurídico novo;
- opinião abstrata;
- interpretação inédita;
- estudo específico;
- criação de política para responder ao requerimento;
- identificação pessoal de empregados ou clientes.

Essa estrutura preserva a natureza da LAI como instrumento de acesso a informação e documentação preexistentes.

## Bancos e canais

Foram incluídas **13 instituições principais**:

- União: 5;
- Estados/regionais: 7;
- Distrito Federal: 1.

O universo foi formado a partir dos segmentos oficiais do Banco Central e da confirmação de controle público em fontes institucionais.

Os bancos federais apontam para o **Informa.BR**, plataforma federal vigente para pedidos de LAI desde 30/06/2026.

Nos Estados e Distrito Federal foram usados e-SICs, sistemas estaduais de acesso à informação ou, quando a própria instituição adota outro mecanismo oficial, o canal eletrônico institucional correspondente.

Para o BRDE, a pesquisa oficial não localizou e-SIC próprio. Foi utilizado o Portal da Transparência oficial, que orienta o cidadão sobre solicitação de informação adicional.

## Auditoria técnica

Verificações executadas no HTML publicado:

- menu global: 8/8 itens canônicos;
- seção LAI marcada com `aria-current="page"`;
- botão **COPIAR MODELO** imediatamente acima do bloco copiável;
- alvo de cópia limitado ao corpo do Modelo;
- 13 cards de bancos/canais;
- nenhum ID HTML duplicado detectado;
- fechamento `</html>` presente;
- nenhum portão para edição anterior;
- link do novo Modelo presente em `lai/index.html`;
- `publication.html_blob_sha` do JSON coincide com o blob vigente do HTML.

## Verificação pública

Foi tentado o acesso direto à URL do GitHub Pages pela ferramenta web. O domínio `thiagoba2004.github.io` não ficou acessível por essa ferramenta nesta sessão. Essa limitação foi registrada como limitação de verificação externa e não como falha do site.

O estado persistido no repositório GitHub foi verificado diretamente.

## Gate final

**SATISFEITO NO REPOSITÓRIO — zero inconsistências abertas no escopo.**
