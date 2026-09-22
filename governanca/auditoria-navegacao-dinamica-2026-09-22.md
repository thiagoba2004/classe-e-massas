# Auditoria — navegação dinâmica responsiva

**Estratégia:** EA-000001-000023  
**Data:** 22/09/2026

## Problema de origem
A navegação anterior havia deixado de rolar horizontalmente, mas todos os itens permaneciam permanentemente expostos no mobile. A captura do usuário comprovou que o menu apenas se reorganizava em duas linhas; não havia comportamento dinâmico.

## Implementação auditada

### Mobile
- marca e botão **MENU** no cabeçalho;
- com JavaScript, navegação recolhida por padrão;
- botão MENU controla o menu por `aria-controls` e `aria-expanded`;
- **Publicações** é disclosure expansível;
- submenu: Visão geral, Notícias, Artigos, Vídeos e Observatório;
- menu em coluna quando aberto;
- zero dependência de rolagem horizontal;
- tecla Escape fecha submenu e menu;
- clique em link fecha o menu;
- clique fora fecha o menu/submenu.

### Desktop
- navegação principal permanece visível;
- Publicações ocupa uma única posição de primeiro nível;
- submenu abre por acionamento do botão Publicações;
- o botão é operável por teclado;
- clique externo e Escape fecham o disclosure.

### Progressive enhancement
A regra de recolhimento móvel está condicionada à classe `.js`. Sem JavaScript, a navegação HTML permanece visível e funcional.

## Verificações de código
- `.js .global-nav{display:none}` apenas no breakpoint móvel;
- `.js .global-nav.is-open{display:flex}`;
- `.menu-toggle` oculto no desktop e visível no mobile;
- `.nav-submenu` posicionado como dropdown no desktop e fluxo normal no mobile;
- não há mais quatro áreas editoriais como itens globais independentes no JS;
- `AGENTS.md` v2.7 registra a navegação dinâmica como padrão.

## Ajuste regressivo durante a auditoria
Foi removida a abertura implícita por `:focus-within` no desktop para evitar submenu visualmente persistente quando o estado `is-open` já estivesse fechado. A abertura passa a depender de estado explícito controlado pelo disclosure, mantendo previsibilidade entre mouse e teclado.

## Deploy intermediário
Commit `e2a77a573da7ace59225aeb341978d3b76fb3384`: GitHub Pages run **35780018397**, completed/success.

## Gate
Aprovado estruturalmente. O fechamento definitivo depende do deploy do commit final que inclui este ajuste e os registros de conclusão.
