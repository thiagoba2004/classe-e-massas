# Estratégia — Migração do AGENTS.md do Classe e Massas para o kernel 1.2

**strategy_id:** `STRAT-CEM-20260917-002`  
**parent_strategy_id:** `STRAT-CEM-20260917-001`  
**status:** EM EXECUÇÃO  
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

**Objetivo:** registrar pedido, estratégia, vínculo com a governança geral e Plano de Fases.

**Gate:** `REQ-20260917-015` persistido; `STRAT-CEM-20260917-002` criado no `STRATEGY_LOG.jsonl`; este plano persistido.

## FASE 2 — Preservação e comparação

**Estado:** EM EXECUÇÃO

**Objetivo:** comparar o `AGENTS.md` v1.8 com o kernel 1.2 e a auditoria produzida pelo Gerador, localizar todas as regras afetadas pela mudança de ordem operacional e confirmar quais regras locais devem permanecer intocadas.

**Gate:** mapa de alterações fechado; nenhuma modificação destrutiva ou simplificadora proposta; versão anterior recuperável pelo Git confirmada.

## FASE 3 — Migração controlada

**Estado:** NÃO INICIADA

**Objetivo:** produzir a nova versão do `AGENTS.md`, incorporando:

- `generated_from_kernel: 1.2`;
- nova versão documental do Classe e Massas;
- ordem obrigatória vigente: registrar → confirmar tecnicamente → informar “Pedido registrado.” → informar leitura/análise/providências → executar;
- atualização coerente dos itens 23, 24.14, 24.15 e de quaisquer referências cruzadas conflitantes;
- registro da alteração no histórico de versões.

**Gate:** arquivo salvo e versionado sem perda das regras locais válidas.

## FASE 4 — Verificação de não regressão

**Estado:** NÃO INICIADA

**Objetivo:** reler a versão migrada, pesquisar contradições residuais, confirmar preservação das regras específicas e comparar as passagens críticas com o kernel 1.2 e com a versão anterior.

**Gate:** nenhuma contradição material conhecida; regras locais mais rigorosas preservadas; remoto confirmado.

## FASE FINAL — Fechamento

**Estado:** NÃO INICIADA

**Objetivo:** atualizar `PROJECT_STATE.json`, `STRATEGY_LOG.jsonl` e `REQUEST_LOG.jsonl`, registrar o resultado e encerrar `STRAT-CEM-20260917-002` se todos os gates estiverem satisfeitos.

**Gate:** estado reconstruível sem depender do chat e próximo passo lógico registrado.

## Regras de segurança da migração

1. A versão v1.8 deve permanecer recuperável pelo histórico Git.
2. Nenhuma regra local mais rigorosa pode ser removida apenas por não constar do kernel universal.
3. A migração não autoriza o backfill geral das demais estratégias do projeto.
4. Alterações devem ser cirúrgicas e rastreáveis.
5. “Auditado”, “salvo”, “versionado”, “enviado ao remoto” e “concluído” permanecem estados distintos.
