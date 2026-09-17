# Inventário inicial para backfill de Estratégias Autônomas

**strategy_id do inventário:** `STRAT-CEM-20260917-003`  
**data:** 17/09/2026  
**regra:** nenhum `BACKFILLED` sem evidência persistente suficiente.

## 1. TCM-001 — História da Crise Mundial

**Classificação:** COMPROVADA  
**strategy_id a atribuir no backfill:** `STRAT-CEM-20260917-004`

### Evidências

- `biblioteca/traducoes/projetos/001-traducao.md` identifica formalmente o projeto `TCM-001`, descreve fluxo próprio, corpus de 17 unidades, estado editorial e histórico v0.1 em 13/09/2026;
- `biblioteca/traducoes/projetos/001-revisao-humana.md` registra abertura da revisão em 13/09/2026, estado próprio, critérios, blocos, decisões humanas e commits;
- `PROJECT_STATE.json` mantém `TCM-001` como frente autônoma, com estado, arquivos canônicos, marcos, restrições e próximo passo.

### Conclusão

Existe unidade autônoma de trabalho com objeto, corpus, fluxo, estados, arquivos canônicos e continuidade própria. A estratégia pode ser backfillada sem reconstruir sua data inicial exata além do que os documentos comprovam.

---

## 2. DOS-PLR-BB-2026 — PLR do Banco do Brasil

**Classificação:** COMPROVADA  
**strategy_id a atribuir no backfill:** `STRAT-CEM-20260917-005`

### Evidências

- `editorial/documentos/dossie-plr-bb-2026.md` possui ID próprio, data de criação em 16/09/2026, objeto, pergunta central e matriz probatória;
- `PROJECT_STATE.json` declara `strategy_status: REGISTRADA`, descreve a estratégia, fase editorial, gates, arquivos de suporte, achados, restrições e próximo passo;
- há múltiplos artefatos próprios: auditoria das 18 bases, análise de instrumentos e regras, contraste documental, rascunho de artigo, auditoria editorial e solicitação de manifestação ao Banco do Brasil.

### Conclusão

A frente possui objetivo identificável, fases/gates e artefatos próprios. É Estratégia Autônoma comprovada e continua ativa em estado editorial/documental.

---

## 3. WHATSAPP-ACT-BB-18-BASES-2026

**Classificação:** COMPROVADA  
**strategy_id a atribuir no backfill:** `STRAT-CEM-20260917-006`

### Evidências

- `editorial/documentos/estrategia-whatsapp-18-bases-act-bb-2026.md` se autodeclara “Estratégia autônoma”, informa criação em 17/09/2026, objetivo, estratégia-mãe, Plano de Fases e entrega final;
- todas as seis fases estão marcadas como concluídas no documento;
- `PROJECT_STATE.json` registra `strategy_status: REGISTRADA E CONCLUÍDA`, arquivos canônicos, resultados e inexistência de passo pendente;
- entrega final persistida em `editorial/documentos/mensagem-whatsapp-bases-act-bb-2026.md`.

### Conclusão

Estratégia derivada e autônoma, comprovadamente concluída, relacionada a `DOS-PLR-BB-2026` sem substituí-la.

---

## 4. Refundação e implantação do Observatório Classe e Massas

**Classificação:** COMPROVADA  
**strategy_id a atribuir no backfill:** `STRAT-CEM-20260917-007`

### Evidências

- `observatorio/documentos/00_Observatorio_Classe_e_Massas_Refundacao_Identidade.md` registra decisão canônica de refundação; histórico v3.0 em 11/09/2026 e v3.1 em 12/09/2026;
- o documento define sujeito, objeto geral, horizonte estratégico, dimensões analíticas, pergunta estratégica e regra de preservação;
- `observatorio/documentos/07_Roadmap_do_Observatorio_Classe_e_Massas.md`, aprovado em 13/09/2026, declara ser guia canônico de fases, dependências, entregas e critérios de conclusão;
- o roadmap registra Fase 0 concluída, Fase 1 em execução, Fase 2 em preparação e fases posteriores ainda não abertas.

### Conclusão

Não é apenas um conjunto de documentos: existe objetivo estratégico geral, decisão de refundação, sequência de fases, dependências e gates. A estratégia pode ser backfillada como programa estrutural do Observatório, sem confundi-la com a estratégia transversal de governança `STRAT-CEM-20260917-001`.

---

## 5. Candidatas ainda não aptas a backfill neste ciclo

Os seguintes conjuntos possuem artefatos relevantes, mas não serão transformados automaticamente em Estratégias Autônomas neste ciclo sem leitura adicional ou evidência de unidade estratégica própria:

- produção e modelos do Ministério Público do Trabalho (MPT);
- conjunto de pedidos pela Lei de Acesso à Informação (LAI);
- artigos individuais publicados em `artigos/2026/`;
- diretriz editorial de notícias;
- documentos históricos específicos do Observatório do Movimento Sindical Bancário anteriores à refundação;
- ferramentas e automações do repositório.

A existência de múltiplos arquivos não basta, por si só, para provar uma Estratégia Autônoma distinta. Esses conjuntos ficam classificados como **PENDENTES DE EVIDÊNCIA/CLASSIFICAÇÃO** para lote posterior.

## Resultado do lote inicial

- candidatas examinadas com profundidade: 4;
- comprovadas e aptas a `BACKFILLED`: 4;
- rejeitadas por falta de prova: 0;
- conjuntos deixados para lote posterior: MPT, LAI, artigos individuais, diretriz editorial, arquivos bancários históricos e ferramentas.
