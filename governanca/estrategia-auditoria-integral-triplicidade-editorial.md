# Estratégia — Auditoria integral da triplicidade editorial

**strategy_id:** `STRAT-CEM-20260918-002`  
**Projeto:** Classe e Massas  
**Data:** 18/09/2026  
**Estado:** EM EXECUÇÃO

## Objetivo

Auditar todos os textos publicados no site Classe e Massas e eliminar as inconsistências com a regra instituída no `AGENTS.md` v2.0:

```text
Markdown (.md) = fonte textual canônica
HTML (.html) = artefato de publicação
JSON (.json) = representação estruturada/interoperável
```

## Critério de escopo

Entram na auditoria todos os HTML públicos que representem conteúdo textual editorial, documental, jurídico, investigativo, metodológico ou de tradução.

Ficam fora, salvo conteúdo editorial próprio:
- páginas de índice e navegação;
- páginas puramente operacionais;
- 404 e confirmações de formulário;
- CSS, JavaScript, logs e arquivos técnicos;
- páginas geradas que não constituam texto autônomo.

## Plano de Fases

### Fase 1 — Inventário e classificação
- enumerar todos os HTML públicos do repositório;
- classificar cada um como TEXTO APLICÁVEL ou EXCLUÍDO;
- registrar a justificativa de exclusão.

**Gate:** inventário integral produzido, sem depender de amostragem.

### Fase 2 — Matriz de conformidade
Para cada texto aplicável:
- localizar o Markdown correspondente;
- localizar o JSON correspondente;
- conferir identidade de slug/título e vínculos;
- registrar ausências e divergências.

**Gate:** matriz integral de conformidade.

### Fase 3 — Saneamento documental
- criar Markdown ausente a partir do conteúdo publicado, preservando o sentido e a estrutura textual;
- criar JSON ausente com metadados e vínculos mínimos;
- corrigir vínculos, nomes e metadados inconsistentes;
- não reescrever conteúdo editorial sem necessidade.

**Gate:** todo texto aplicável possui os três artefatos.

### Fase 4 — Verificação cruzada
- reler os artefatos;
- verificar HTML x Markdown x JSON;
- verificar nomes/caminhos e validade JSON;
- registrar exceções expressas, se houver.

**Gate:** nenhuma inconsistência aberta sem registro explícito.

### Fase 5 — Relatório e fechamento
- criar relatório de auditoria;
- atualizar `PROJECT_STATE.json`;
- concluir estratégia e pedido;
- registrar resultados nos logs.

**Gate:** auditoria persistida, versionada e verificável no remoto.
