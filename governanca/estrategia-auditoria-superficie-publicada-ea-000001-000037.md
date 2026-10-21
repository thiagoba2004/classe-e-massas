# EA-000001-000037 — Auditoria da superfície efetivamente publicada e decisão de arquitetura GitHub Pages

**Projeto:** PRJ-000001 — Classe e Massas (`thiagoba2004/classe-e-massas`).
**Estratégia:** `EA-000001-000037`.
**Pedido:** `REQ-20261020-001`, determinação humana de 20/10/2026.
**Constituição:** 20/10/2026; `PLANNED`; não iniciada a auditoria técnica.
**Origem e motivação:** a configuração corrente do site utiliza `main/(root)` porque o `index.html`, `_config.yml`, `css/`, `js/` e as seções editoriais existem na raiz. A recomendação de migrar para `/docs` foi feita como hipótese de defesa em profundidade, mas depende de auditoria efetiva e análise comparativa antes de qualquer decisão.
**Plano canônico:** este arquivo. **Matriz por ação:** `governanca/EA-000001-000037-actions.json`.
**Classificação:** S0 de descrição arquitetural; o repositório é público. Não publicar resultados com dados S2+, tokens, dados privados, material editorial inédito ou informação operacional sensível.
**Prioridade:** auditabilidade e segurança do site publicado, preservando funcionalidades e conteúdo editorial existentes.

## 1. Objetivo e pergunta decisória

**Objetivo:** determinar a superfície realmente exposta pelo GitHub Pages, testar se as exclusões vigentes são aplicadas no artefato gerado e identificar arquivos que não deveriam ser publicados. **Somente após essa prova**, comparar objetivamente as alternativas (a) manter `main/(root)` com controles de allowlist/negação, (b) migrar a fonte para `main/docs` ou (c) separar o artefato de deploy em branch/fluxo dedicado, conforme capacidade e custo demonstrados.

**Pergunta de decisão:** qual arquitetura oferece melhor isolamento verificável entre fonte editorial e governança, sem regressões de navegação, URLs, imagens, scripts, formulários, identidade visual, SEO, acessibilidade ou custo?

Esta EA autoriza **planejamento, coleta de evidências públicas, testes read-only autorizados e parecer documental**. Não autoriza publicar, excluir, renomear, migrar ou modificar produção, configuração Pages, arquivos de site, workflows, permissões, segredos ou despesas. Eventual mudança exige nova decisão humana expressa e plano de execução compatível, podendo ser aditamento formal ou outra EA se a finalidade se tornar materialmente distinta. Não alterar o site por mera hipótese de risco.

## 2. Diagnóstico preliminar — hipóteses, não resultados de auditoria

A inspeção documental de constituição encontrou:

- `index.html`, `404.html`, `_config.yml` e `css/`, `js/`, `artigos/`, `biblioteca/`, `noticias/`, `publicacoes/` na raiz.
- `SITE_ARCHITECTURE.md` já exige distinguir camada pública de `AGENTS.md`, `PROJECT_STATE.json`, logs, `governanca/`, planos de fases e rascunhos editoriais.
- `_config.yml` contém `exclude` para arquivos específicos e diretórios, como `governanca`, `tools`, `templates`, logs e rascunhos. Esse controle é **configuração declarada**, ainda não é prova de exclusão nos bytes publicados.
- `ROADMAP.md` e alguns arquivos de governança na raiz não estão individualmente listados no `exclude`; isso é **hipótese de exposição**, não constatação de publicação. Arquivos do repositório GitHub público também são acessíveis pelo GitHub independentemente do Pages: distinguir exposição GitHub da exposição no site.
- Páginas e recursos não devem ser movidos sem inventário de URLs, basepaths e referenciadores.
- Alterações em arquivos Git do branch de publicação podem disparar build; a auditoria evitará efeitos não aprovados e não editará a origem do site.

**Condição de integridade:** usar SHA de HEAD e recibos de build/deploy reais no momento dos testes; não extrapolar do repositório para o site sem evidência HTTP/artefato.

## 3. Plano de Fases (06 fases)

### FASE 01/06 [F-000001-000037-001] — Registro, identidade, escopo e segurança

**Executor:** CHAT com conector GitHub, no contexto de Governança Geral, para registro documental; titular define a finalidade.
**Entregas:** pedido no `REQUEST_LOG.jsonl`, evento `CREATED` no `STRATEGY_LOG.jsonl`, Plano, matriz por ação, `PROJECT_STATE.json` e registro global dual.
**Gate:** `EA037_DUAL_REGISTRATION_VERIFIED` mediante readback de caminhos, IDs, matriz e commits; nenhuma auditoria substantiva presumida.
**Estado na constituição:** IN_PROGRESS_DOCUMENTARY_REGISTRATION.

### FASE 02/06 [F-000001-000037-002] — Inventário da superfície real publicada

**Executor candidato:** CODEX Local no checkout verificado do PRJ-000001; uso limitado a inspeção de fonte, metadados e URLs públicas (sem operações administrativas).
**Entregas:** baseline do branch/configuração/commit/deploy efetivo, mapa de conteúdo pretendido e URLs observadas, inspeção HTTP e distinção entre Git público, build e site Pages. Incluir arquivos raiz, diretórios, resources JS/CSS, `robots.txt`, `404.html`, `_config.yml` e exclusões listadas; não varrer hosts externos ou recursos privados.
**Gate:** `EA037_PUBLICATION_SURFACE_BASELINE_VERIFIED`. HTTP inacessível => `NOT_VERIFIED`, sem resultado inventado.
**Estado:** NOT_STARTED.

### FASE 03/06 [F-000001-000037-003] — Teste de eficácia das exclusões e segurança de publicação

**Executor candidato:** CODEX Local no checkout isolado e ambiente de build compatível, sem modificar o site ativo.
**Entregas:** reproduzir o build do GitHub Pages/Jekyll sob configuração controlada e registrar manifestos/hashes de saída, `exclude`/includes efetivos, caminhos publicados indevidos, diferença entre arquivos publicamente acessíveis na hospedagem e arquivos visíveis apenas no Git público; ensaios negativos limitados a caminhos canônicos conhecidos (sem brute force), verificação de fronteira de diretórios e links simbólicos, prevenção de segredo e regressões de URLs/SEO/recursos.
**Gate:** `EA037_EXCLUSION_CONTROLS_EVALUATED`, com `PASS/FAIL/NOT_VERIFIED` individual e evidência. Um HTTP 404 isolado não prova ausência universal; um teste local não equivale à configuração produtiva.
**Estado:** NOT_STARTED.

### FASE 04/06 [F-000001-000037-004] — Comparação arquitetural e parecer fundamentado

**Executor:** CHAT especializado em análise/arquitetura, com evidências verificadas da F002/F003; não altera código.
**Entregas:** matriz comparativa das alternativas `/(root)+controles`, `/docs` e `artefato de deploy segregado`; critérios: superfície de ataque, privacidade, manutenção, testes negativos, risco operacional, reversibilidade, links existentes, complexidade de build, custo e dependências. Definir recomendação condicional, mitigação mínima, riscos residuais e eventual ADR; citar evidências e limitações.
**Gate:** `EA037_ARCHITECTURE_OPTIONS_GROUNDED`, não equivalente a aprovação de migração.
**Estado:** NOT_STARTED.

### FASE 05/06 [F-000001-000037-005] — Deliberação sobre mudança produtiva

**Executor:** HUMAN, se houver proposta de alteração material, na conversa de decisão do titular; G0 apenas fornece parecer/alternativas.
**Entregas:** decisão explícita de manter o root, reforçar controles, adotar arquitetura segregada ou postergar; definir necessidade de EA de implementação, executor técnico e autorização de mudança.
**Gate:** `EA037_HUMAN_DISPOSITION_RECORDED` quando decisão for necessária. Sem decisão => `WAITING_HUMAN_DECISION`; não executar mudança. A auditoria pode ser encerrada documentalmente com recomendação e decisão pendente, sem fingir homologação de execução.
**Estado:** NOT_STARTED.

### FASE 06/06 [F-000001-000037-006] — Auditoria de encerramento e sucessão

**Executor:** CHAT/G0 para conferir provas e recibos; CODEX somente se testes técnicos residuais estiverem classificados/autorizados como ações separadas.
**Entregas:** relatório final de auditoria, classificação de riscos/achados, readback dos registros locais e globais, estado e próximos responsáveis; decisão humana ou pendência preservada.
**Gate terminal:** `EA037_PUBLICATION_AUDIT_RECORDED_WITH_EVIDENCE` (conclusão do diagnóstico, **não** aprovação de mudança no Pages) ou encerramento condicionado `BLOCKED_WITH_CAUSE`.
**Estado:** NOT_STARTED.

## 4. Sucessão, executores e segurança

Matriz executável: [EA-000001-000037-actions.json](EA-000001-000037-actions.json). Antes de ações materiais verificar `action_id` catalogado, executor real, escopo, ferramentas, autorização, pré-condições e custos. O Chat não assume CODEX. Para tarefas locais: o diretório absoluto do checkout/VS Code **não foi comprovado**; preencher após preflight, nunca inventar. Nenhum teste requer solicitar privilégios elevados, alterar branch principal, recriar site, mexer em GitHub Settings nem executar workflow novo sem mandato separado.

Se a execução de F002–F003 não tiver acesso local ou ambiente reprodutível, registrar `BLOCKED_CAPABILITY` e seguir apenas trabalho documental independente com evidência existente. Continuar por fases autorizadas até bloqueio material ou decisão humana; nunca substituir ausência de evidência por conclusão automática.

## 5. Resultados esperados (ainda não realizados)

1. Inventário **observado** dos arquivos do site, não só listagem Git.
2. Evidências independentes de controle das exclusões e não exposição indevida.
3. Matriz de riscos e alternativas com recomendação não predeterminada.
4. Decisão humana fundamentada antes de qualquer alteração de publicação.
5. Relatório, hashes, commits, owner e próximo passo, sem perda de conteúdo editorial ou história Git.

**Resultado da constituição:** registro de estratégia e planejamento; nenhuma migração, auditoria HTTP/build completa ou mudança produtiva executada.
