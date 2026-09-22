# Auditoria Residual de Interface e Publicação — Site Classe e Massas

**Projeto:** PRJ-000001 — Classe e Massas  
**Estratégia:** EA-000001-000027 — Saneamento residual de links, botões e separação público/interno  
**Data:** 22/09/2026

## Síntese

A auditoria ampliada posterior ao fechamento da EA-000001-000026 identificou duas lacunas que não integravam os gates anteriores:

1. hiperlinks de navegação simples ainda herdavam aparência de botão preenchido em páginas da Biblioteca, LAI, MPT, Notícias, Vídeos, confirmação de contato e 404;
2. a página pública **Linha Editorial** apontava diretamente para um arquivo de `editorial/documentos/` rotulado como documento canônico interno.

As duas lacunas foram corrigidas sem reabrir o histórico concluído da EA-000001-000026.

## 1. Semântica de links e botões

O CSS global passou a diferenciar o elemento e a função:

- `<button>` e links com atributo `download`: continuam com aparência de ação;
- `a.button:not([download])`, `a.model-button:not([download])`, `a.guide-button` e `a.note-button`: passam a renderizar como links contextuais, sem fundo preto, sem caixa preenchida e sem largura total artificial no mobile.

O HTML permanece semanticamente correto: navegação usa `<a>`; ações reais usam `<button>` ou download explícito.

## 2. Linha Editorial pública

Foi criada:

`noticias/linha-editorial.html`

A página preserva os princípios públicos da Linha Editorial, mas remove linguagem de governança como **DOCUMENTO CANÔNICO**, versão interna, estado **APROVADO** e histórico técnico de versões.

`noticias/index.html` passou a apontar para a nova página pública.

O diretório:

`editorial/documentos/`

foi acrescentado às exclusões de `_config.yml`, impedindo sua publicação pelo GitHub Pages.

## 3. Limpeza de linguagem interna

Foram removidas da superfície pública de Traduções as expressões:

- `DOCUMENTO CANÔNICO • POLÍTICA EDITORIAL`;
- `DOCUMENTO CANÔNICO • VERSÃO 1.0 • 13/09/2026`.

A política editorial continua pública, mas sem expor classificação interna de governança.

## 4. Auditoria das páginas publicáveis

Superfície resultante: **47 arquivos HTML publicáveis**.

Verificados em todas as famílias públicas:

- exatamente um `<h1>`;
- `meta viewport`;
- menu global canônico;
- ausência de Notícias, Artigos, Vídeos e Observatório como itens autônomos do menu global;
- ausência de `<style>` e atributos `style=`;
- ausência do menu antigo (`menu-toggle`, dropdown/disclosure e `aria-expanded`);
- Mapa do Site no rodapé;
- Fale Conosco no rodapé;
- carregamento de `js/main.js`;
- ausência de referências públicas a `editorial/documentos`, `DOCUMENTO CANÔNICO`, `PROJECT_STATE`, `STRATEGY_LOG`, `REQUEST_LOG` e `AGENTS.md`.

**Resultado após as correções: 47/47 sem anomalias nesses gates.**

## 5. CSS e responsividade

Verificação estática final:

- chaves CSS balanceadas: **0**;
- paleta azul anterior ausente: **sim**;
- regra de menu horizontal rolável até 880 px: **presente**;
- `.section-nav` horizontal rolável até 700 px: **presente**;
- regra residual de semântica de links da EA-000001-000027: **presente**.

A escala canônica continua prevalecendo sobre regras legadas específicas de MPT/guia por seletores posteriores com `!important`, limitando H1 interno a `clamp(1.5rem, 2.7vw, 1.9rem)` e H1 da Home a `clamp(1.8rem, 3.5vw, 2.2rem)`, com 1.8rem no mobile.

## Gate da Fase 04/05

**APROVADO.**

Nenhuma não conformidade crítica ou alta permanece aberta no código após a auditoria residual.

A verificação gráfica em dispositivo real permanece evidência complementar; o gate atual é estrutural, semântico, responsivo por CSS e posteriormente de build/deploy.
