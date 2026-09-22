# EA-000001-000024 — Convergência visual e navegacional do Classe e Massas ao padrão AJ/PF

**Status:** CONCLUÍDA  
**Origem:** REQ-20260922-004 e REQ-20260922-005.

## Objetivo

Corrigir dois desvios comprovados na interface pública do Site Classe e Massas:

1. cards que dependem de botões pretos internos para sinalizar navegação, em vez de comunicar visualmente o hiperlink pelo próprio card;
2. menu móvel recolhível por botão **MENU**, divergente do padrão horizontal deslizante já adotado nos Sites Ações Judiciais e Planejamento Financeiro.

## Referência comparativa comprovada

- Ações Judiciais: navegação móvel horizontal rolável por `.global-nav{overflow-x:auto;flex-wrap:nowrap}`; cards-link usam superfície cromaticamente distinta de cards não clicáveis.
- Planejamento Financeiro: navegação móvel horizontal rolável com o mesmo paradigma estrutural.
- Classe e Massas: estado anterior usa botão MENU, disclosure de Publicações e cards MPT com botões pretos internos.

## Plano de Fases

1. **FASE 01/04 [F-000001-000024-001] — Diagnóstico comparativo AJ/PF/CEM** — CONCLUÍDA.
2. **FASE 02/04 [F-000001-000024-002] — Especificação do padrão convergente** — CONCLUÍDA.
3. **FASE 03/04 [F-000001-000024-003] — Implementação de cards-link e menu deslizante** — CONCLUÍDA.
4. **FASE 04/04 [F-000001-000024-004] — Auditoria responsiva, semântica e deploy** — CONCLUÍDA.

## Especificação aprovada

### Menu
- manter a barra de navegação sempre visível no mobile;
- usar rolagem horizontal controlada no componente de navegação, sem overflow geral da página;
- item atual permanece destacado;
- **Publicações** permanece como item único do primeiro nível e aponta para o hub editorial;
- Notícias, Artigos, Vídeos e Observatório permanecem agrupados dentro do hub Publicações, sem necessidade de dropdown no menu global;
- remover a dependência do botão MENU no Classe e Massas.

### Cards-link
- quando um card inteiro representar um único destino, o elemento deve ser um hiperlink de bloco inteiro;
- card clicável deve possuir superfície/borda visualmente distinta de card informativo não clicável;
- é vedado depender de botão preto interno como única pista de navegação;
- hover e foco devem reforçar a affordance sem alterar a identidade editorial;
- cards com múltiplas ações reais não devem virar um único link; nesses casos, preservar links secundários claros sem transformar toda a área em botão.

## Gate

A estratégia só fecha após:
- menu horizontal deslizante confirmado em largura móvel;
- ausência do botão MENU;
- Publicações preservado como hub;
- cards MPT de destino único convertidos em cards-link;
- botões pretos de navegação removidos desses cards;
- atualização normativa local e transversal;
- GitHub Pages concluído com sucesso.

## Fechamento

Implementação concluída e auditada. O menu móvel do Classe e Massas passou ao padrão horizontal deslizante já utilizado em Ações Judiciais e Planejamento Financeiro; **Publicações** permanece como hub de primeiro nível; os três cards MPT de destino único tornaram-se hiperlinks integrais com diferenciação cromática e os botões pretos redundantes foram removidos. GitHub Pages run **35784291957** concluído com **success** para o commit `a8964898f0c3365a08f0771c934a685112f4420f`.
