# Baseline — Normalização do Menu Global

**Projeto:** PRJ-000001 — Classe e Massas  
**Estratégia:** EA-000001-000019 — Normalização do Menu Global do Site  
**Data:** 19/09/2026  
**Origem:** A-06 da auditoria de Modelos Públicos.

## Escopo confirmado

O inventário permanece em **26 páginas públicas**:

- 10 páginas em `artigos/2026/`;
- 9 páginas em `lai/`;
- 4 páginas em `biblioteca/` e `biblioteca/traducoes/`;
- 2 páginas em `observatorio/documentos/`;
- 1 página em `fale-conosco/`.

## Menu global canônico vigente

A referência verificada em páginas modernas contém, nesta ordem:

1. Início
2. Notícias
3. Artigos
4. Observatório
5. Biblioteca
6. MPT
7. LAI
8. Fale Conosco

Estrutura canônica:

- `class="nav global-nav"`;
- `aria-label="Navegação principal"`;
- `aria-current="page"` no item da seção corrente.

Referências verificadas:

- `noticias/index.html`;
- `noticias/2026/modelo-pedido-posicionamento-assessorias-imprensa-bancos-fiscalizacao-produtividade.html`;
- `mpt/modelo-representacao.html`;
- `biblioteca/index.html`;
- `observatorio/index.html`.

## Diferenças confirmadas no baseline

### Artigos
Páginas históricas examinadas usam menus antigos que omitem pelo menos LAI e Fale Conosco; algumas também não usam `global-nav` ou `aria-current` de modo uniforme.

### LAI
As páginas do Modelo LAI possuem LAI, mas parte delas omite Notícias, Observatório, Biblioteca e Fale Conosco. O caso mais recente ainda omite Fale Conosco e não usa `global-nav`.

### Biblioteca
As quatro páginas examinadas omitem LAI; algumas já possuem `global-nav`, outras não.

### Observatório / Documentos
As duas páginas possuem navegação reduzida e misturam acesso local a Documentos com o menu global. A remediação deve inserir o menu global completo e preservar o acesso local a Documentos sem classificá-lo como item global.

### Fale Conosco
A página possui sete dos oito itens e omite LAI.

## Regras de caminhos relativos

### Profundidade 1
Para páginas diretamente em uma pasta de seção, usar prefixo `../` para os itens globais.

### Profundidade 2
Para páginas em `artigos/2026/`, `biblioteca/traducoes/` e `observatorio/documentos/`, usar prefixo `../../` para os itens globais.

## Gate da Fase 01

**SATISFEITO.** O inventário de 26 páginas e o padrão canônico estão confirmados.

## Modelo da Fase 02

Cada página deve receber o conjunto completo dos oito itens, `nav global-nav`, `aria-label` e `aria-current` na seção correspondente. O conteúdo do artigo/documento não deve ser alterado. Links locais devem ser preservados separadamente quando existirem.
