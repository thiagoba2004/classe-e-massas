# Estratégia — Inventário e backfill progressivo das Estratégias Autônomas históricas do Classe e Massas

**strategy_id:** `STRAT-CEM-20260917-003`  
**parent_strategy_id:** `STRAT-CEM-20260917-001`  
**status:** CONCLUÍDA — CICLO INICIAL  
**data:** 17/09/2026

## Objetivo

Reconstruir progressivamente o mapa histórico das Estratégias Autônomas do projeto Classe e Massas que já existiam antes da implantação completa do `STRATEGY_LOG.jsonl` ou que, embora comprovadas em arquivos canônicos, ainda não tenham evento próprio no log.

O princípio de segurança é:

> **BACKFILL SOMENTE COM EVIDÊNCIA PERSISTENTE SUFICIENTE.**

Nenhuma estratégia será criada retroativamente como fato apenas porque parece provável, foi lembrada no chat ou pode ser inferida do tema do projeto.

## FASE 1 — Registro e delimitação

**Estado:** CONCLUÍDA

**Gate satisfeito:** `REQ-20260917-016` persistido; `STRAT-CEM-20260917-003` criado no `STRATEGY_LOG.jsonl`; este Plano de Fases persistido.

## FASE 2 — Inventário de candidatas

**Estado:** CONCLUÍDA — LOTE INICIAL

**Gate satisfeito:** inventário persistido em `governanca/inventario-backfill-estrategias-autonomas-2026-09-17.md` após leitura do `PROJECT_STATE.json`, árvore completa do repositório e arquivos canônicos das candidatas principais.

### Resultado

Candidatas comprovadas:

1. `TCM-001 — História da Crise Mundial`;
2. `DOS-PLR-BB-2026 — PLR do Banco do Brasil`;
3. `WHATSAPP-ACT-BB-18-BASES-2026`;
4. `Refundação e implantação do Observatório Classe e Massas`.

Conjuntos não transformados em estratégias por falta de classificação documental suficiente neste ciclo: MPT, LAI, artigos individuais, diretriz editorial, documentos bancários históricos e ferramentas/automações.

## FASE 3 — Validação documental

**Estado:** CONCLUÍDA — LOTE INICIAL

**Gate satisfeito:** as quatro candidatas possuem unidade autônoma de trabalho, objetivo próprio, documentos canônicos, estado histórico determinável e referências suficientes. Datas não comprovadas não foram inventadas.

## FASE 4 — Backfill progressivo

**Estado:** CONCLUÍDA — LOTE INICIAL

### Eventos registrados

- `STEV-CEM-20260917-009` → `STRAT-CEM-20260917-004` — TCM-001;
- `STEV-CEM-20260917-010` → `STRAT-CEM-20260917-005` — DOS-PLR-BB-2026;
- `STEV-CEM-20260917-011` → `STRAT-CEM-20260917-006` — WhatsApp 18 bases;
- `STEV-CEM-20260917-012` → `STRAT-CEM-20260917-007` — Refundação e implantação do Observatório.

**Gate satisfeito:** eventos persistidos e versionados no `STRATEGY_LOG.jsonl` sem reabrir estratégias concluídas.

## FASE 5 — Reconciliação do estado corrente

**Estado:** CONCLUÍDA

**Resultado:** criado `governanca/STRATEGY_MAP.json` como mapa corrente reconstruível derivado do log histórico. O mapa preserva os estados materiais já comprovados:

- `STRAT-CEM-20260917-004` / TCM-001 — EM EXECUÇÃO, revisão humana;
- `STRAT-CEM-20260917-005` / DOS-PLR-BB-2026 — EM EXECUÇÃO, revisão editorial/direito de resposta;
- `STRAT-CEM-20260917-006` / WhatsApp 18 bases — CONCLUÍDO;
- `STRAT-CEM-20260917-007` / Observatório Classe e Massas — EM EXECUÇÃO conforme roadmap canônico.

O `STRATEGY_REGISTRY.jsonl` do Gerador de Agents e o perfil `profiles/classe-e-massas.json` foram sincronizados com os IDs comprovados.

**Gate satisfeito:** mapa corrente e histórico reconciliados sem alterar o estado material de qualquer frente.

## FASE FINAL — Fechamento do ciclo inicial

**Estado:** CONCLUÍDA

**Resultado:** `STEV-CEM-20260917-013` registra `STRAT-CEM-20260917-003` como `CONCLUDED`.

### Balanço do ciclo

- estratégias backfilladas: **4**;
- estratégias reabertas indevidamente: **0**;
- grupos mantidos pendentes por ausência de evidência/classificação suficiente: **6**;
- inferências convertidas em fato: **0**.

### Grupos pendentes de evidência/classificação

- MPT;
- LAI;
- artigos individuais de 2026;
- diretriz editorial de notícias;
- documentos bancários históricos anteriores à refundação;
- ferramentas e automações.

Esses grupos não constituem, por ora, estratégias retroativas reconhecidas. Nova leitura poderá produzir `BACKFILLED` futuro se houver evidência persistente suficiente.

## Regras metodológicas preservadas

1. `PROJECT_STATE.json` é fonte de candidatas, não prova automática de origem histórica.
2. Arquivo com nome `estrategia-*`, `roadmap`, `plano` ou equivalente é evidência forte, mas deve ser lido antes do backfill.
3. Commits podem comprovar existência, evolução e estado, mas não devem receber significado não sustentado pelo conteúdo.
4. Uma frente concluída pode ser backfillada sem ser reaberta.
5. Uma estratégia-mãe e uma estratégia derivada devem permanecer distintas quando os documentos comprovarem autonomia real.
6. É permitido registrar incerteza. É proibido preencher lacunas com memória não verificável.
7. O `STRATEGY_REGISTRY.jsonl` agregado só reconhece estratégias depois de comprovação no log local do projeto de origem.

## Próximo passo lógico

Nenhuma estratégia adicional deve ser criada apenas para esgotar a lista de grupos pendentes. Quando um desses conjuntos voltar a ser objeto de trabalho ou surgir evidência persistente nova, realizar classificação documental antes de eventual novo `BACKFILLED`.
