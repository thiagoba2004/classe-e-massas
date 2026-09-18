# Estratégia — Trio obrigatório de formatos editoriais

**strategy_id:** `STRAT-CEM-20260918-001`  
**Projeto:** Classe e Massas  
**Data:** 18/09/2026  
**Estado:** EM EXECUÇÃO

## Objetivo

Eliminar a lacuna normativa identificada nos fluxos editoriais do projeto: textos publicáveis não podem existir apenas em HTML ou apenas em Markdown sem o conjunto coordenado de formatos previsto pela arquitetura documental.

## Regra-alvo

Para cada texto editorial/publicável do Classe e Massas, manter três artefatos sincronizados:

1. **Markdown (`.md`)** — fonte textual canônica e humana;
2. **HTML (`.html`)** — artefato de publicação pública;
3. **JSON (`.json`)** — metadados estruturados e representação de interoperabilidade com modelos, automações e auditoria.

Exceções somente podem existir quando forem tecnicamente justificadas, registradas e versionadas.

## Plano de Fases

### Fase 1 — Registro e delimitação
- registrar pedido;
- registrar estratégia;
- definir escopo e relação com o Gerador.

**Gate:** pedido e estratégia persistidos.

### Fase 2 — Norma local
- alterar `AGENTS.md`;
- tornar a triplicidade explícita;
- definir papéis dos três formatos, sincronização e exceções.

**Gate:** regra inequívoca e verificável no documento canônico.

### Fase 3 — Alinhamento com o Gerador
- incorporar regra reutilizável ao módulo `publication`;
- atualizar template de AGENTS para projetos editoriais.

**Gate:** projetos futuros com módulo de publicação podem herdar a regra sem importar regras locais indevidas.

### Fase 4 — Verificação
- reler arquivos alterados;
- confirmar commits;
- registrar conclusão e referências.

**Gate:** regra comprovadamente persistida nos dois repositórios.
