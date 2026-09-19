# Estratégia Autônoma EA-000001-000019 — Normalização do Menu Global do Site

**Projeto:** PRJ-000001 — Classe e Massas  
**Origem:** irregularidade A-06 registrada em `governanca/auditoria-site-modelos-publicos-2026-09-19.md`  
**Escopo inicial comprovado:** 26 páginas públicas com menu global incompleto ou desatualizado.

## Objetivo

Normalizar o menu global das páginas públicas históricas do Site Classe e Massas para o padrão vigente, preservando conteúdo editorial, links locais, acessibilidade móvel, marcação `aria-current` quando aplicável e integridade dos caminhos relativos.

## Regra de segurança

A alteração do cabeçalho é transversal. Antes de modificar páginas em lote, deve ser identificado o menu canônico vigente e calculado o caminho relativo correto para cada página. Nenhuma página deve receber links quebrados ou perder marcação contextual da seção atual.

## Plano de Fases

### FASE 01/05 [F-000001-000019-001] — Registro e baseline
Confirmar a lista das 26 páginas apontadas na auditoria, identificar o menu global canônico vigente e registrar as diferenças estruturais por grupo de profundidade/caminho.

**Gate:** inventário confirmado e padrão canônico identificado antes de qualquer alteração em lote.

### FASE 02/05 [F-000001-000019-002] — Modelo de normalização
Definir o bloco de navegação global a ser aplicado, incluindo itens obrigatórios, classes, `aria-label`, `aria-current` e regras de caminhos relativos para páginas de diferentes diretórios.

**Gate:** modelo validado contra pelo menos uma página moderna e uma página histórica de cada profundidade relevante.

### FASE 03/05 [F-000001-000019-003] — Remediação das 26 páginas
Atualizar somente o cabeçalho/menu global das páginas do escopo, preservando corpo, metadados editoriais, scripts, estilos, conteúdo e navegação local.

**Gate:** 26/26 páginas persistidas e sem regressão estrutural evidente.

### FASE 04/05 [F-000001-000019-004] — Auditoria regressiva
Verificar as páginas alteradas quanto a: itens do menu, caminhos relativos, `aria-current`, IDs duplicados, fechamento HTML, scripts e links internos do cabeçalho.

**Gate:** zero inconsistências abertas atribuíveis à remediação.

### FASE 05/05 [F-000001-000019-005] — Verificação pública e fechamento
Confirmar o estado final no repositório e, quando tecnicamente verificável, no Site Público; registrar relatório, atualizar `PROJECT_STATE.json`, `STRATEGY_LOG.jsonl` e fechar a estratégia.

**Gate:** estado persistido, versionado, auditado e rastreável.

## Escopo inicial — 26 páginas

### Artigos — 10
- `artigos/2026/quando-o-cliente-vira-fiscal-do-trabalhador.html`
- `artigos/2026/democracia-para-a-base-quem-controla-o-poder.html`
- `artigos/2026/quando-a-oposicao-reproduz-a-burocracia-que-combate.html`
- `artigos/2026/assembleia-nao-e-cheque-em-branco-bahia.html`
- `artigos/2026/anatomia-do-peleguismo-sindical.html`
- `artigos/2026/ano-eleitoral-aumento-real-banco-do-brasil.html`
- `artigos/2026/vanguarda-nao-e-autoproclamacao.html`
- `artigos/2026/o-direito-nao-socorre-aos-que-dormem.html`
- `artigos/2026/fraude-das-assembleias-virtuais.html`
- `artigos/2026/450-mil-bancarios.html`

### LAI — 9
- `lai/banco-do-brasil-plr-2026.html`
- `lai/banco-do-brasil.html`
- `lai/sest-cgpar.html`
- `lai/agu.html`
- `lai/ministerio-fazenda.html`
- `lai/tse.html`
- `lai/tcu.html`
- `lai/pge-sp.html`
- `lai/estatais-federais.html`

### Biblioteca — 4
- `biblioteca/auditoria.html`
- `biblioteca/traducoes/index.html`
- `biblioteca/traducoes/politica.html`
- `biblioteca/traducoes/projeto-001.html`

### Observatório — 2
- `observatorio/documentos/index.html`
- `observatorio/documentos/07_Roadmap_do_Observatorio_Classe_e_Massas.html`

### Fale Conosco — 1
- `fale-conosco/index.html`

## Padrão global de referência

O menu vigente contém:

`Início · Notícias · Artigos · Observatório · Biblioteca · MPT · LAI · Fale Conosco`

A referência inicial de implementação é `noticias/index.html`, cuja navegação usa `nav class="nav global-nav"` e `aria-label="Navegação principal"`.
