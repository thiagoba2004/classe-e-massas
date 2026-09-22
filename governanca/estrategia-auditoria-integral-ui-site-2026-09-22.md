# EA-000001-000025 — Auditoria integral de interface e coerência visual do Site Classe e Massas

**Status:** EM EXECUÇÃO  
**Origem:** REQ-20260922-006.

## Objetivo

Auditar o Site Classe e Massas inteiro, sem presumir que a correção anterior tenha resolvido as inconsistências globais, comparando todas as páginas públicas com:

- o padrão real dos Sites Ações Judiciais e Planejamento Financeiro;
- o AGENTS.md vigente do Classe e Massas;
- o módulo `web-site` do Gerador de Agents;
- a captura móvel fornecida pelo usuário.

A auditoria deve localizar inconsistências de tipografia, navegação, cards, hiperlinks, botões/CTAs, cores, espaçamento, páginas legadas, CSS embutido, semântica de componentes e responsividade.

## Plano de Fases

1. **FASE 01/05 [F-000001-000025-001] — Inventário completo do Site e padrões de referência** — EM EXECUÇÃO.
2. **FASE 02/05 [F-000001-000025-002] — Auditoria automatizada de todas as páginas públicas** — AGUARDA.
3. **FASE 03/05 [F-000001-000025-003] — Auditoria visual e semântica por famílias de páginas** — AGUARDA.
4. **FASE 04/05 [F-000001-000025-004] — Relatório consolidado, severidade e causa-raiz** — AGUARDA.
5. **FASE 05/05 [F-000001-000025-005] — Gate e definição do plano corretivo** — AGUARDA.

## Regra desta estratégia

Esta estratégia é de **auditoria**. Não executar refatoração pública em massa antes do relatório consolidado, salvo correção indispensável para tornar a própria auditoria possível.

## Hipótese inicial a testar

A correção EA-000001-000024 foi localizada e insuficiente: ela alterou componentes específicos, mas o Site ainda contém páginas e componentes legados com estilos diferentes. A introdução de azul nos cards MPT pode ter criado uma divergência adicional em relação ao princípio de usar a própria paleta do Site em variações de luminosidade.
