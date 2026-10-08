# EA-000001-000036 — Piloto local de recuperação lexical auditável

**Projeto:** PRJ-000001 — Classe e Massas  
**Alias:** CEM  
**Status:** IN_PROGRESS  
**Criada em:** 2026-10-07T21:38:31-03:00  
**Origem:** REQ-20261007-001  
**Predecessora global:** EA-000000-000022 — Arquitetura Universal de Recuperação, Indexação e RAG Auditável para IA  
**Classificação:** S0_PUBLICO; somente fontes já públicas do próprio repositório entram no corpus  
**Executor:** Codex  
**Persistência canônica:** thiagoba2004/classe-e-massas, branch main

## Objetivo

Validar, em Projeto real e de baixo risco, a aplicação do contrato e do padrão lexical da EA-000000-000022: documentos e unidades rastreáveis, identificadores exatos, índice exact-first + BM25, consultas ouro, métricas e rebuild determinístico.

O piloto não instala embeddings, fusão híbrida ou RAG generativo. Ele não indexa pautas internas, logs de governança, dados pessoais, segredos nem fontes classificadas acima de S0.

## Escopo inicial

Corpus elegível:

- Markdown editorial já publicado;
- HTML público correspondente;
- títulos, caminhos, seções e identificadores públicos.

Corpus excluído:

- governança interna;
- `REQUEST_LOG.jsonl`, `STRATEGY_LOG.jsonl` e `PROJECT_STATE.json`;
- pauta editorial;
- dados de formulários, credenciais e configurações;
- conteúdo não publicado ou com classificação S1+;
- duplicação integral de Markdown e HTML quando ambos representam a mesma obra.

## Plano de Fases

### FASE 01/06 [F-000001-000036-001] — Registro, classificação e baseline

**Estado:** IN_PROGRESS.

Registrar a Estratégia, confirmar o perfil `LEXICAL`, inventariar mecanismos existentes e delimitar corpus público elegível.

**Gate:** estratégia, classificação, escopo, exclusões e baseline persistidos.

### FASE 02/06 [F-000001-000036-002] — Contrato de documentos e unidades

**Estado:** NOT_STARTED.

Materializar documentos e unidades segundo os contratos universais, preservando path, hash, título, seção e provenance.

**Gate:** dataset validado, sem IDs duplicados, órfãos ou conteúdo acima de S0.

### FASE 03/06 [F-000001-000036-003] — Índice lexical determinístico

**Estado:** NOT_STARTED.

Construir índice exact-first + BM25 com normalização Unicode NFD, accent folding e identificadores pontuados.

**Gate:** builder reproduzível e índice reconstruído byte a byte.

### FASE 04/06 [F-000001-000036-004] — Goldset e testes

**Estado:** NOT_STARTED.

Criar consultas positivas, negativas, por título, path e termos raros, com evidências esperadas.

**Gate:** testes de recuperação e integridade sem falhas.

### FASE 05/06 [F-000001-000036-005] — Benchmark e decisão de adoção

**Estado:** NOT_STARTED.

Medir Recall@k, Mean Reciprocal Rank (MRR), Normalized Discounted Cumulative Gain (nDCG) e evidence hit rate; registrar limitações.

**Gate:** thresholds explícitos atendidos ou resultado negativo preservado sem promoção indevida.

### FASE 06/06 [F-000001-000036-006] — Auditoria, readback e fechamento

**Estado:** NOT_STARTED.

Verificar classificação, ausência de regressão, rebuild, documentação, estado e remoto.

**Gate terminal:** `PRJ000001_LEXICAL_RETRIEVAL_PILOT_VERIFIED` ou encerramento fundamentado com limitações.

## Artefatos previstos

- `governanca/retrieval/RETRIEVAL_DOCUMENTS.jsonl`;
- `governanca/retrieval/RETRIEVAL_UNITS.jsonl`;
- `governanca/retrieval/LEXICAL_INDEX.json`;
- `governanca/retrieval/LEXICAL_TEST_CASES.jsonl`;
- `governanca/retrieval/LEXICAL_BENCHMARK_RESULT.json`;
- `tools/build_lexical_retrieval.py`;
- `tools/test_lexical_retrieval.py`;
- `governanca/auditoria-piloto-retrieval-lexical-2026-10-07.md`;
- `governanca/EA-000001-000036_STATE.json`.

JSON/JSONL é justificado porque os arquivos são datasets, índice, casos de teste e estado consumidos por scripts.

## Sucessão e condições de parada

Aplicar continuidade autônoma entre fases. Parar somente diante de blocker material, necessidade real de decisão adicional, risco de classificação ou estado terminal. Não publicar página nova nem alterar conteúdo editorial durante o piloto.
