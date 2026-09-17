# Protocolo canônico — Registro obrigatório de todos os pedidos

**Projeto:** Classe e Massas  
**Status:** CANÔNICO — EMENDA DE GOVERNANÇA PENDENTE DE INCORPORAÇÃO AO `AGENTS.md`  
**Data:** 17/09/2026  
**Pedido de origem:** `REQ-20260917-001`

## 1. Regra fundamental

Todo pedido do usuário relativo ao projeto Classe e Massas, sem exceção por tamanho, simplicidade, urgência ou natureza, deve ser registrado de modo cronológico e persistente no arquivo canônico `REQUEST_LOG.jsonl` antes ou no início de seu processamento.

> **PEDIDO RECEBIDO → REGISTRO PERSISTENTE → VERIFICAÇÃO DO REGISTRO → VINCULAÇÃO ESTRATÉGICA → EXECUÇÃO.**

O registro de um pedido é uma ação preparatória de governança e deve anteceder qualquer processamento substantivo decorrente dele.

## 2. Objetivo

O log deve permitir que qualquer modelo, em qualquer conversa futura, possa determinar documentalmente:

- qual foi o último pedido do usuário;
- quais pedidos o antecederam;
- qual pedido está em execução;
- quais pedidos foram concluídos, bloqueados, cancelados ou substituídos;
- a qual estratégia cada pedido pertence;
- quais arquivos, commits, publicações ou demais resultados decorreram de cada pedido.

Memória do modelo, resumo de conversa e inferência não substituem o registro persistente.

## 3. Arquivo canônico

O arquivo canônico é:

`REQUEST_LOG.jsonl`

Cada pedido deve ocupar uma entrada própria. É proibido acumular vários pedidos e registrá-los apenas ao final de uma sessão.

Quando uma mensagem contiver ações materialmente independentes, poderão ser registrados subpedidos ou entradas vinculadas, desde que a ordem original permaneça recuperável.

Correções, alterações de escopo, ordens de publicar, ordens de interromper, aprovações que autorizem nova etapa e pedidos de retomada também devem ser registrados quando produzirem efeito operacional.

## 4. Campos mínimos

Cada entrada deve conter, quando tecnicamente disponível:

```text
request_id
timestamp
source
text
scope
strategy ou strategy_id
status
requested_action
result_refs
```

O campo `text` deve preservar o pedido com fidelidade suficiente para recuperação da formulação original. Informações que não devam ser expostas em repositório aberto devem ser redigidas, com indicação explícita de que houve redação, preservando-se o significado operacional necessário à continuidade.

## 5. Estados

Usar estados inequívocos, como:

```text
RECEBIDO
EM_EXECUCAO
CONCLUIDO
BLOQUEADO
CANCELADO
SUBSTITUIDO
```

O estado deve ser atualizado quando houver mudança material. Na conclusão, registrar referências aos arquivos, commits, páginas ou outros resultados produzidos.

## 6. Perguntas de continuidade

Quando o usuário perguntar “qual foi meu último pedido?”, “onde paramos?”, “o que eu pedi por último?” ou equivalente, a ordem obrigatória de consulta será:

```text
REQUEST_LOG.jsonl
        ↓
ARQUIVOS CANÔNICOS / PROJECT_STATE.json
        ↓
HISTÓRICO GIT E COMMITS
        ↓
CONTEXTO DE CONVERSA, APENAS COMO APOIO
```

É proibido responder a essas perguntas apenas a partir da memória do modelo.

Se o log estiver incompleto, deve-se declarar a lacuna documental e reconstruí-la a partir das fontes disponíveis antes de afirmar com segurança qual foi o último pedido.

## 7. Natureza de auditoria

O `REQUEST_LOG.jsonl` é cronológico e auditável. Entradas anteriores não devem ser apagadas ou reescritas silenciosamente para acomodar estados posteriores.

Se um novo pedido chegar durante a execução de outro, o novo pedido deve ser registrado antes de qualquer processamento substantivo decorrente dele, sem apagar ou tornar ambíguo o estado do pedido anterior.

A incapacidade de responder documentalmente qual foi o último pedido deve ser tratada como falha de continuidade documental, e não como simples falha de memória.

## 8. Alterações requeridas no AGENTS.md

Na próxima gravação autorizada do `AGENTS.md`, esta emenda deverá ser incorporada à versão seguinte, no mínimo com:

1. inclusão do `REQUEST_LOG.jsonl` entre as fontes canônicas de continuidade;
2. inclusão de “registrar o pedido” como primeira etapa do protocolo operacional;
3. autorização expressa do registro do pedido como ação preparatória anterior à vinculação estratégica;
4. regra específica para consulta ao log em perguntas sobre o último pedido e a retomada do trabalho;
5. obrigação de atualizar o estado e os resultados do pedido no fechamento;
6. registro da mudança no histórico de versões do `AGENTS.md`.

Esta emenda existe porque a tentativa de atualizar diretamente o `AGENTS.md` em 17/09/2026 foi bloqueada pela camada de segurança da ferramenta disponível; a pendência deve permanecer explícita até a incorporação efetiva.
