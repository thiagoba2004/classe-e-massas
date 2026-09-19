# Auditoria regressiva — Normalização do Menu Global

**Projeto:** PRJ-000001 — Classe e Massas  
**Estratégia:** EA-000001-000019 — Normalização do Menu Global do Site  
**Data:** 19/09/2026  
**Escopo:** 26 páginas públicas apontadas no achado A-06.

## Resultado executivo

**26/26 páginas remediadas e aprovadas na auditoria regressiva do repositório.**

O menu global passou a apresentar, em todas as páginas do escopo, os oito itens canônicos, nesta ordem:

1. Início
2. Notícias
3. Artigos
4. Observatório
5. Biblioteca
6. MPT
7. LAI
8. Fale Conosco

Todas as páginas auditadas possuem:

- `nav class="nav global-nav"`;
- `aria-label="Navegação principal"`;
- exatamente um `aria-current="page"`, correspondente à seção corrente;
- fechamento `</html>`;
- nenhum ID HTML duplicado detectado pela auditoria;
- caminhos relativos compatíveis com a profundidade do arquivo.

## Remediação por seção

- **Artigos:** 10/10;
- **LAI:** 9/9;
- **Biblioteca:** 4/4;
- **Observatório:** 2/2;
- **Fale Conosco:** 1/1.

## Variantes históricas tratadas

A remediação não presumiu que todas as páginas possuíam a mesma estrutura antiga.

Foram tratados:

- menus antigos em elemento `<nav>`;
- páginas históricas de Artigos cujo cabeçalho usava apenas `<div class="nav"><a ...>Início</a></div>`;
- páginas LAI com conjuntos reduzidos de quatro ou sete itens;
- páginas da Biblioteca que já possuíam `global-nav`, mas omitiam LAI;
- páginas de `observatorio/documentos/` que misturavam navegação global e acesso local.

Na página `observatorio/documentos/07_Roadmap_do_Observatorio_Classe_e_Massas.html`, o acesso local **Documentos** foi preservado em navegação separada da seção, enquanto o menu global foi normalizado.

## Integridade dos metadados

A mudança do cabeçalho altera o blob do HTML. Para evitar divergência entre publicação e representação estruturada:

- **22 artefatos JSON** que continham `html_blob_sha` tiveram o hash sincronizado com o HTML vigente;
- o artigo `quando-o-cliente-vira-fiscal-do-trabalhador.json` não utiliza `html_blob_sha`, portanto não exigiu alteração;
- páginas operacionais sem JSON correspondente não receberam JSON artificial apenas para satisfazer a auditoria.

## Conteúdo preservado

A remediação foi restrita ao cabeçalho/menu global e, no caso do Roadmap do Observatório, à separação explícita do link local **Documentos**.

Não houve alteração deliberada do corpo editorial dos artigos, Modelos LAI, documentos da Biblioteca ou conteúdo do Observatório.

## Verificação pública

Foi tentada verificação direta de URLs do GitHub Pages por ferramenta externa em páginas representativas de Artigos, LAI, Biblioteca, Observatório e Fale Conosco. A ferramenta externa não conseguiu acessar as URLs do domínio `thiagoba2004.github.io` nesta sessão.

Essa limitação não constitui falha do site e não foi tratada como evidência de indisponibilidade. A verificação do estado persistido foi realizada diretamente no repositório GitHub, incluindo conteúdo e blobs vigentes.

A confirmação de implantação pública será complementada, quando disponível, pela verificação do workflow de GitHub Pages associado ao marco final.

## Gate da Fase 04

**SATISFEITO — zero inconsistências abertas atribuíveis à remediação nas 26 páginas do escopo.**
