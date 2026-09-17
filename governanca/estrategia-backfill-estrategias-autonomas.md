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

**Gate:** `REQ-20260917-016` persistido; `STRAT-CEM-20260917-003` criado no `STRATEGY_LOG.jsonl`; este Plano de Fases persistido.

## FASE 2 — Inventário de candidatas

**Estado:** EM EXECUÇÃO

**Objetivo:** levantar frentes com indícios de autonomia estratégica em `PROJECT_STATE.json`, arquivos de planejamento, roadmaps, dossiês, commits e demais fontes persistentes.

Cada candidata receberá uma classificação provisória:

- `COMPROVADA` — há evidência suficiente para backfill;
- `PARCIALMENTE_COMPROVADA` — há indícios fortes, mas falta evidência para afirmar algum elemento essencial;
- `NÃO COMPROVADA` — não há base suficiente para evento `BACKFILLED`.

**Gate:** inventário inicial persistido com fonte de evidência para cada candidata.

## FASE 3 — Validação documental

**Estado:** NÃO INICIADA

**Objetivo:** verificar, para cada candidata, se é possível comprovar ao menos:

- existência da frente como unidade de trabalho autônoma;
- objetivo próprio;
- documento ou artefato canônico;
- estado histórico minimamente determinável;
- relação com outras estratégias, quando aplicável.

Quando a data exata de criação não puder ser comprovada, não será inventada. O evento `BACKFILLED` registrará a data do backfill e indicará separadamente a evidência histórica disponível.

**Gate:** conjunto de estratégias aptas a backfill definido sem inferência não documentada.

## FASE 4 — Backfill progressivo

**Estado:** NÃO INICIADA

**Objetivo:** adicionar eventos `BACKFILLED` ao `STRATEGY_LOG.jsonl`, preservando os arquivos originais como fonte de evidência.

Cada evento deverá conter:

```text
strategy_id
event_type = BACKFILLED
historical_status, quando comprovável
name
objective
scope
parent_strategy_id, quando comprovável
plan_ref ou canonical_refs
evidence_refs
notes sobre limites da reconstrução
```

**Gate:** eventos salvos, versionados e verificados no remoto.

## FASE 5 — Reconciliação do estado corrente

**Estado:** NÃO INICIADA

**Objetivo:** reconciliar `PROJECT_STATE.json` com o `STRATEGY_LOG.jsonl` sem alterar o estado material de frentes editoriais, jurídicas, documentais ou de tradução.

O estado corrente do objeto continua sendo determinado pelos seus arquivos canônicos específicos. O backfill histórico não autoriza rebaixar, reabrir ou encerrar uma frente sem evidência.

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
