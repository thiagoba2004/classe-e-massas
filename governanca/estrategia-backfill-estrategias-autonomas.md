# Estratégia — Inventário e backfill progressivo das Estratégias Autônomas históricas do Classe e Massas

**strategy_id:** `STRAT-CEM-20260917-003`  
**parent_strategy_id:** `STRAT-CEM-20260917-001`  
**status:** EM EXECUÇÃO  
**data:** 17/09/2026

## Objetivo

Reconstruir progressivamente o mapa histórico das Estratégias Autônomas do projeto Classe e Massas que já existiam antes da implantação completa do `STRATEGY_LOG.jsonl` ou que, embora comprovadas em arquivos canônicos, ainda não tenham evento próprio no log.

O princípio de segurança é:

> **BACKFILL SOMENTE COM EVIDÊNCIA PERSISTENTE SUFICIENTE.**

Nenhuma estratégia será criada retroativamente como fato apenas porque parece provável, foi lembrada no chat ou pode ser inferida do tema do projeto.

## FASE 1 — Registro e delimitação

**Estado:** CONCLUÍDA

**Objetivo:** registrar o pedido, criar a Estratégia Autônoma de backfill e delimitar seu método.

**Gate satisfeito:** `REQ-20260917-016` persistido; `STRAT-CEM-20260917-003` criado no `STRATEGY_LOG.jsonl`; este Plano de Fases persistido.

## FASE 2 — Inventário de candidatas

**Estado:** CONCLUÍDA — LOTE INICIAL

**Objetivo:** levantar frentes com indícios de autonomia estratégica em `PROJECT_STATE.json`, arquivos de planejamento, roadmaps, dossiês, commits e demais fontes persistentes.

Cada candidata recebe classificação:

- `COMPROVADA` — há evidência suficiente para backfill;
- `PARCIALMENTE_COMPROVADA` — há indícios fortes, mas falta evidência para afirmar algum elemento essencial;
- `NÃO COMPROVADA` — não há base suficiente para evento `BACKFILLED`.

**Gate satisfeito:** inventário inicial persistido em `governanca/inventario-backfill-estrategias-autonomas-2026-09-17.md`.

### Resultado do lote inicial

Candidatas comprovadas:

1. `TCM-001 — História da Crise Mundial`;
2. `DOS-PLR-BB-2026 — PLR do Banco do Brasil`;
3. `WHATSAPP-ACT-BB-18-BASES-2026`;
4. `Refundação e implantação do Observatório Classe e Massas`.

Conjuntos deixados para lote posterior por exigirem classificação adicional: MPT, LAI, artigos individuais, diretriz editorial, documentos bancários históricos e ferramentas/automações.

## FASE 3 — Validação documental

**Estado:** CONCLUÍDA — LOTE INICIAL

**Objetivo:** verificar, para cada candidata, se é possível comprovar ao menos:

- existência da frente como unidade de trabalho autônoma;
- objetivo próprio;
- documento ou artefato canônico;
- estado histórico minimamente determinável;
- relação com outras estratégias, quando aplicável.

**Gate satisfeito:** as quatro candidatas do lote inicial possuem fontes canônicas suficientes; datas não comprovadas não foram inventadas.

## FASE 4 — Backfill progressivo

**Estado:** CONCLUÍDA — LOTE INICIAL

**Objetivo:** adicionar eventos `BACKFILLED` ao `STRATEGY_LOG.jsonl`, preservando os arquivos originais como fonte de evidência.

### Eventos registrados

- `STEV-CEM-20260917-009` → `STRAT-CEM-20260917-004` — TCM-001;
- `STEV-CEM-20260917-010` → `STRAT-CEM-20260917-005` — DOS-PLR-BB-2026;
- `STEV-CEM-20260917-011` → `STRAT-CEM-20260917-006` — WhatsApp 18 bases;
- `STEV-CEM-20260917-012` → `STRAT-CEM-20260917-007` — Refundação e implantação do Observatório.

**Gate satisfeito:** eventos salvos, versionados e persistidos no remoto.

## FASE 5 — Reconciliação do estado corrente

**Estado:** EM EXECUÇÃO

**Objetivo:** reconciliar o mapa corrente com o `STRATEGY_LOG.jsonl` sem alterar o estado material de frentes editoriais, jurídicas, documentais ou de tradução.

A reconciliação inclui:

- vincular os IDs backfillados aos objetos correntes sem reabrir frentes concluídas;
- manter `TCM-001` e `DOS-PLR-BB-2026` nos estados materiais já comprovados;
- manter `WHATSAPP-ACT-BB-18-BASES-2026` concluída;
- refletir no Gerador de Agents os strategy_ids já comprovados localmente;
- separar claramente o próximo lote pendente de evidência.

**Gate:** mapa corrente e histórico sem contradição material conhecida.

## FASE FINAL — Fechamento do ciclo inicial

**Estado:** NÃO INICIADA

**Objetivo:** registrar quantas estratégias foram backfilladas, quais permaneceram pendentes de evidência e qual é o próximo lote de investigação, se houver.

Esta estratégia pode ser encerrada quando o inventário razoável do acervo atual tiver sido concluído, ainda que permaneçam lacunas históricas explicitamente marcadas como não comprovadas.

## Regras metodológicas

1. `PROJECT_STATE.json` é fonte de candidatas, não prova automática de origem histórica.
2. Arquivo com nome `estrategia-*`, `roadmap`, `plano` ou equivalente é evidência forte, mas deve ser lido antes do backfill.
3. Commits podem comprovar existência, evolução e estado, mas não devem receber significado não sustentado pelo conteúdo.
4. Uma frente concluída pode ser backfillada sem ser reaberta.
5. Uma estratégia-mãe e uma estratégia derivada devem permanecer distintas quando os documentos comprovarem autonomia real.
6. É permitido registrar incerteza. É proibido preencher lacunas com memória não verificável.
7. O `STRATEGY_REGISTRY.jsonl` do Gerador de Agents só será atualizado depois de o evento existir no log local do Classe e Massas.
