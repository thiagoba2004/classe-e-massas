# Estratégia Autônoma — Governança numérica de Projetos, Estratégias Autônomas e Fases

**Projeto:** `CEM — Classe e Massas`  
**Estratégia:** `STRAT-CEM-20260919-001 — Governança numérica de Projetos, Estratégias Autônomas e Fases`  
**Status:** CONCLUÍDA

## Plano de Fases

### FASE 01 — Registro e delimitação
**Objetivo:** registrar o pedido, criar a Estratégia Autônoma e fixar o escopo normativo.  
**Gate:** pedido e estratégia persistidos com código, denominação e fase numerada.

### FASE 02 — Modelagem normativa universal
**Objetivo:** definir os campos, formatos, invariantes e padrão determinístico de resposta.  
**Gate:** convenção completa definida sem ambiguidade.

### FASE 03 — Implementação no Gerador de Agents
**Objetivo:** incorporar a regra no kernel universal, AGENTS do Gerador e template de novos AGENTS.  
**Gate:** novos projetos passam a herdar obrigatoriamente o padrão.

### FASE 04 — Implementação no Classe e Massas
**Objetivo:** atualizar o AGENTS.md e o estado corrente do Classe e Massas, preservando compatibilidade histórica.  
**Gate:** CEM passa a expor código do projeto, código e denominação da estratégia e fase numerada.

### FASE 05 — Verificação e fechamento
**Objetivo:** verificar persistência, consistência entre os dois repositórios e registrar o estado final.  
**Gate:** regra comprovadamente presente nas fontes canônicas e padrão de resposta apto para uso imediato.

## Padrão-alvo de resposta de continuidade

Quando o usuário perguntar “Onde paramos? Qual a Estratégia Autônoma em curso? Qual a Fase dessa Estratégia Autônoma? E qual o Projeto?” ou equivalente, a resposta deverá conter obrigatoriamente:

1. **Projeto:** código + denominação;
2. **Estratégia Autônoma:** código + denominação;
3. **Fase:** número/código + denominação;
4. **Estado da fase/estratégia;**
5. **Onde paramos:** ponto exato comprovado;
6. **Próximo passo lógico.**

Nenhuma dessas informações poderá ser inferida apenas da memória quando houver fonte persistente disponível.

## Fechamento

Estratégia concluída em 19/09/2026 após verificação remota do AGENTS v2.1, estado estruturado, mapa de estratégias e integração com o Gerador de Agents 1.5 / kernel 1.3.
