# EA-000001-000023 — Navegação dinâmica responsiva do Site Classe e Massas

**Status:** EM EXECUÇÃO  
**Origem:** REQ-20260922-003.

## Objetivo
Substituir o menu responsivo estático e quebrado em múltiplas linhas por navegação dinâmica, compacta e acessível, preservando o hub Publicações e as URLs editoriais existentes.

## Plano de Fases
1. **FASE 01/04 [F-000001-000023-001] — Diagnóstico da regressão visual** — CONCLUÍDA.
2. **FASE 02/04 [F-000001-000023-002] — Especificação do comportamento dinâmico** — CONCLUÍDA.
3. **FASE 03/04 [F-000001-000023-003] — Implementação do menu e submenu** — EM EXECUÇÃO.
4. **FASE 04/04 [F-000001-000023-004] — Auditoria de acessibilidade, responsividade e deploy** — AGUARDA implementação.

## Diagnóstico
A EA-000001-000022 removeu a rolagem horizontal, porém tornou todos os itens de primeiro nível permanentemente visíveis no mobile. O resultado é responsivo, mas não dinâmico: a barra ocupa duas linhas e não oferece expansão/recolhimento.

## Especificação
### Mobile
- cabeçalho compacto com marca e botão **MENU**;
- menu principal fechado por padrão quando JavaScript estiver disponível;
- abertura/fechamento por botão com `aria-expanded`;
- fechamento por tecla Escape;
- **Publicações** como disclosure expansível;
- submenu: Visão geral, Notícias, Artigos, Vídeos e Observatório;
- sem rolagem horizontal.

### Desktop
- menu principal permanece visível;
- **Publicações** funciona como disclosure/dropdown;
- submenu acessível por clique, teclado e foco;
- demais itens permanecem de primeiro nível.

### Progressive enhancement
Sem JavaScript, a navegação HTML continua visível; o comportamento recolhível é ativado apenas sob a classe `.js`.
