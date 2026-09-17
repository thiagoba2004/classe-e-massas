# Estratégia — Migração do AGENTS.md do Classe e Massas para o kernel 1.2

**strategy_id:** `STRAT-CEM-20260917-002`  
**parent_strategy_id:** `STRAT-CEM-20260917-001`  
**status:** EM FECHAMENTO  
**data:** 17/09/2026

## Objetivo

Migrar de forma controlada o `AGENTS.md` do projeto Classe e Massas para a ordem operacional vigente do `AGENTS_KERNEL.md` 1.2 do Gerador de Agents, preservando integralmente as regras locais mais rigorosas e específicas válidas e registrando a origem do kernel sem descaracterizar a autonomia documental do projeto.

## Escopo

Esta estratégia abrange exclusivamente a migração de governança do `AGENTS.md` e a sincronização mínima dos registros de estado necessários para comprovar a migração.

Ficam fora do escopo:

- inventário/backfill geral das demais Estratégias Autônomas do Classe e Massas;
- alteração de conteúdo editorial, jurídico, sindical ou de tradução;
- reestruturação de roadmaps setoriais;
- remoção de regras locais mais rigorosas.

## FASE 1 — Registro e delimitação

**Estado:** CONCLUÍDA

**Gate atingido:** `REQ-20260917-015` persistido; `STRAT-CEM-20260917-002` criado no `STRATEGY_LOG.jsonl`; Plano de Fases persistido.

## FASE 2 — Preservação e comparação

**Estado:** CONCLUÍDA

**Gate atingido:** conflito material localizado nos antigos itens 23, 24.14 e 24.15; regras locais mais rigorosas identificadas para preservação; versão v1.8 recuperável pelo blob Git `0c0fc7bd17de1084728ed1f1f2c4aa61405d1a86`.

## FASE 3 — Migração controlada

**Estado:** CONCLUÍDA

**Gate atingido:** `AGENTS.md` migrado para v1.9, com `generated_from_kernel: 1.2`, ordem registro → verificação → “Pedido registrado” → leitura/análise/providências → execução e incorporação por referência das regras locais válidas da v1.8.

**Commit da migração:** `3fb8a9ed721b5e614301d4528c0bad54eded62f9`.

## FASE 4 — Verificação de não regressão

**Estado:** CONCLUÍDA

**Gate atingido:** v1.9 relida diretamente do remoto; metadado do kernel confirmado; ordem operacional confirmada; regras específicas de tradução, formatos, siglas, cadeia sindical, checkpoints, persistência, recuperação e não regressão preservadas expressamente; v1.8 mantida recuperável pelo Git.

## FASE FINAL — Fechamento

**Estado:** EM EXECUÇÃO

**Objetivo:** atualizar `PROJECT_STATE.json`, `STRATEGY_LOG.jsonl` e `REQUEST_LOG.jsonl`, registrar o resultado e encerrar `STRAT-CEM-20260917-002`.

**Gate:** estado reconstruível sem depender do chat e próximo passo lógico registrado.

## Resultado material já alcançado

- `AGENTS.md` vigente: **v1.9**;
- kernel de origem: **1.2**;
- versão anterior: preservada no histórico Git;
- alteração do projeto-alvo: realizada e verificada remotamente;
- backfill geral de outras estratégias: **não executado**, por estar fora do escopo.

## Regras de segurança da migração

1. A versão v1.8 permanece recuperável pelo histórico Git.
2. Nenhuma regra local mais rigorosa foi declarada revogada apenas por não constar do kernel universal.
3. A migração não autoriza o backfill geral das demais estratégias do projeto.
4. Alterações foram registradas e verificadas no remoto.
5. “Auditado”, “salvo”, “versionado”, “enviado ao remoto” e “concluído” permanecem estados distintos.
