# Auditoria integral da triplicidade editorial — 18/09/2026

**Projeto:** Classe e Massas  
**strategy_id:** `STRAT-CEM-20260918-002`  
**Regra auditada:** `AGENTS.md` v2.0, itens 8.2.1 a 8.2.4  
**Escopo:** todos os arquivos HTML presentes no repositório que compõem o site.

## 1. Resultado executivo

Foram identificados **54 arquivos HTML**.

- **41** foram classificados como textos editoriais/documentais autônomos e, portanto, sujeitos à regra obrigatória `.md + .html + .json`.
- **13** foram classificados como índices, páginas operacionais, página de erro ou template técnico e ficaram fora da regra, nos termos da exceção expressa do AGENTS v2.0.
- **0** arquivos permaneceram sem classificação.
- Ao início da auditoria, apenas **12 de 41** textos aplicáveis possuíam Markdown com o mesmo basename e **0 de 41** possuíam JSON com o mesmo basename.
- Ao final, **41 de 41** possuem Markdown e **41 de 41** possuem JSON com o mesmo basename do HTML.
- **41 de 41** textos aplicáveis estão estruturalmente conformes.
- **0** inconsistências estruturais permanecem abertas.

## 2. Saneamento executado

Foram criados **70 novos artefatos canônicos**:

- **29 arquivos Markdown**:
  - 27 reconstruídos a partir do conteúdo HTML já publicado, sem alteração do HTML;
  - 2 criados como aliases canônicos de fontes Markdown preexistentes (`biblioteca/auditoria-idioma.md` → `biblioteca/auditoria.md`; política editorial de traduções → `biblioteca/traducoes/politica.md`).
- **41 arquivos JSON** com o mesmo basename dos HTML correspondentes.

Os **12 Markdown já existentes** — 11 documentos do Observatório e a Diretriz Canônica da Linha Editorial de Notícias — foram preservados.

Os antigos `*.metadata.json` do Observatório e da diretriz editorial também foram preservados. O novo `NOME-ESTAVEL.json` passa a cumprir a regra do AGENTS v2.0 e registra o vínculo entre Markdown, HTML e metadados legados.

## 3. Critérios aplicados

Para texto aplicável, o gate foi:

```text
HTML publicado existe
+
Markdown de mesmo basename existe
+
JSON de mesmo basename existe
=
CONFORME
```

A relação entre os três artefatos é verificável pelo basename e pelo manifesto incorporado aos JSON novos.

Nenhum artigo, notícia, pedido de LAI, documento do MPT, documento autônomo da Biblioteca, diretriz editorial ou documento canônico do Observatório foi dispensado por mera prática histórica.

## 4. Matriz integral

| HTML | Classificação | Markdown | JSON | Fundamento |
|---|---|:---:|:---:|---|
| `404.html` | EXCLUIDO | — | — | Página de erro operacional |
| `artigos/2026/450-mil-bancarios.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `artigos/2026/anatomia-do-peleguismo-sindical.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `artigos/2026/ano-eleitoral-aumento-real-banco-do-brasil.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `artigos/2026/assembleia-nao-e-cheque-em-branco-bahia.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `artigos/2026/democracia-para-a-base-quem-controla-o-poder.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `artigos/2026/fraude-das-assembleias-virtuais.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `artigos/2026/o-direito-nao-socorre-aos-que-dormem.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `artigos/2026/quando-a-oposicao-reproduz-a-burocracia-que-combate.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `artigos/2026/vanguarda-nao-e-autoproclamacao.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `artigos/index.html` | EXCLUIDO | — | — | Índice de seção |
| `biblioteca/auditoria.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `biblioteca/index.html` | EXCLUIDO | — | — | Índice de seção |
| `biblioteca/traducoes/index.html` | EXCLUIDO | — | — | Índice de seção |
| `biblioteca/traducoes/politica.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `biblioteca/traducoes/projeto-001.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `editorial/documentos/01_Diretriz_Canonica_Linha_Editorial_Noticias.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `fale-conosco/index.html` | EXCLUIDO | — | — | Formulário/página operacional |
| `fale-conosco/recebido.html` | EXCLUIDO | — | — | Confirmação operacional de formulário |
| `index.html` | EXCLUIDO | — | — | Página inicial/índice de navegação |
| `lai/agu.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `lai/arquivo/banco-do-brasil-plr-2026-edicao-1-2026-09-16.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `lai/banco-do-brasil-plr-2026.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `lai/banco-do-brasil.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `lai/estatais-federais.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `lai/index.html` | EXCLUIDO | — | — | Índice/Central LAI |
| `lai/ministerio-fazenda.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `lai/pge-sp.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `lai/sest-cgpar.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `lai/tcu.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `lai/tse.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `mpt/guia-nacional.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `mpt/index.html` | EXCLUIDO | — | — | Índice de seção |
| `mpt/modelo-bb-bahia-greve-2026.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `mpt/modelo-representacao.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `mpt/nota-tecnico-juridica.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `noticias/2026/bases-sindicais-que-nao-assinaram-o-act-do-bb-2026-2028-ate-14h-de-11-09.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `noticias/2026/classe-e-massas-protocola-lai-e-cobra-manifestacao-do-bb-sobre-plr-2026.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `noticias/index.html` | EXCLUIDO | — | — | Índice de seção |
| `noticias/principio-sintese.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `observatorio/documentos/00_Observatorio_Classe_e_Massas_Refundacao_Identidade.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `observatorio/documentos/01_Observatorio_da_Classe_Trabalhadora.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `observatorio/documentos/02_Observatorio_do_Movimento_dos_Trabalhadores.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `observatorio/documentos/03_Observatorio_das_Lutas_de_Classes.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `observatorio/documentos/04_Rede_de_Observatorios_Setoriais_e_Nucleo_Bancario.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `observatorio/documentos/05_Mapas_do_Trabalho_do_Capital_e_Relacoes_de_Forca.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `observatorio/documentos/06_Arquitetura_Publica_Metodo_e_Governanca.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `observatorio/documentos/07_Roadmap_do_Observatorio_Classe_e_Massas.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `observatorio/documentos/Observatorio_Classe_e_Massas_Diretriz_Canonica_Arquitetura_Documental.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `observatorio/documentos/Observatorio_Movimento_Sindical_Bancario_Diretriz_Canonica_Arquitetura_Codex.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `observatorio/documentos/Observatorio_Movimento_Sindical_Bancario_Documento_Canonico_Fundacao.html` | APLICAVEL | ✅ | ✅ | Texto editorial/documental autônomo |
| `observatorio/documentos/index.html` | EXCLUIDO | — | — | Catálogo/índice documental |
| `observatorio/index.html` | EXCLUIDO | — | — | Índice de seção |
| `templates/artigo.html` | EXCLUIDO | — | — | Template técnico |

## 5. Commits de saneamento

- `ca013ea6ada17960e98467f739c96c050ee269dc` — 9 artigos;
- `cd551d1e1ca8f3ad1e16922d9e1994c0e7c067ba` — Notícias e MPT;
- `d6adef341b4719d9a25feab331bfaa30f6862a5c` — Central LAI;
- `e628043cbfc18bcf8a845595e43ba302b081dc40` — Biblioteca e diretriz editorial;
- `8dd6e0d1e806212ccd404b4e25a88796a0f489f6` — documentos canônicos do Observatório.

## 6. Gate final

**SATISFEITO.**

Todos os HTML do repositório foram classificados. Todos os 41 textos aos quais a regra se aplica possuem agora os três formatos exigidos. Não há exceção documental pendente nem HTML editorial aplicável sem Markdown e JSON correspondentes.

## 7. Regra para continuidade

A auditoria corrige o passivo histórico. A partir deste marco, novos textos devem nascer já no fluxo:

```text
CRIAR/ATUALIZAR MARKDOWN
→ SINCRONIZAR JSON
→ GERAR/ATUALIZAR HTML
→ VERIFICAR OS TRÊS
→ PUBLICAR/DECLARAR CONCLUÍDO
```

O saneamento retroativo não autoriza voltar ao fluxo HTML isolado.
