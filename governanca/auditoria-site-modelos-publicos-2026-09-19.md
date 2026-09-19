# Auditoria do Site — Modelos Públicos, Edições Históricas e Consistência de Navegação

**Projeto:** PRJ-000001 — Classe e Massas  
**Estratégia:** EA-000001-000018 — Padrão de Modelos Públicos e Auditoria do Site  
**Data:** 19/09/2026  
**Escopo:** páginas públicas alcançáveis pelos menus principais e subíndices examinados; regras de Modelos; exposição de edições anteriores; metadados de publicação; estrutura HTML básica; consistência do menu global.

## 1. Universo examinado

Foram examinadas **51 páginas HTML públicas vinculadas aos menus e subíndices** de:

- Início;
- Notícias;
- Artigos;
- LAI;
- MPT;
- Observatório;
- Biblioteca;
- Fale Conosco.

Além disso, foram examinados os três arquivos históricos da 1ª edição do Modelo LAI sobre PLR do Banco do Brasil e os artefatos JSON dos Modelos alterados nesta estratégia.

## 2. Critérios

A auditoria verificou:

1. presença do botão canônico **COPIAR MODELO**;
2. posição do botão imediatamente acima do conteúdo copiável;
3. inexistência de botão/label legado como “Copiar pedido”;
4. inexistência de portões públicos para edições anteriores de Modelos;
5. inexistência de `noindex` indevido nas páginas públicas examinadas;
6. IDs HTML duplicados;
7. fechamento estrutural básico do documento HTML;
8. duplicações estruturais evidentes nos índices;
9. consistência entre HTML alterado e `html_blob_sha` registrado no JSON;
10. presença do menu global vigente.

## 3. Achados e remediações

### A-01 — Edição anterior de Modelo publicamente acessível — CORRIGIDO — criticidade alta

**Achado:** a página `lai/banco-do-brasil-plr-2026.html` oferecia botão **VER 1ª EDIÇÃO** e a edição histórica permanecia materialmente publicada em:

- `lai/arquivo/banco-do-brasil-plr-2026-edicao-1-2026-09-16.html`;
- `lai/arquivo/banco-do-brasil-plr-2026-edicao-1-2026-09-16.md`;
- `lai/arquivo/banco-do-brasil-plr-2026-edicao-1-2026-09-16.json`.

**Remediação:**
- botão removido;
- referências públicas a “1ª edição” e “2ª edição” removidas da página vigente;
- seção comparativa “O que mudou nesta edição” retirada do artefato público;
- trio histórico removido da árvore atual do site;
- histórico preservado no Git;
- verificação posterior confirmou que os três caminhos históricos não existem mais na branch vigente.

### A-02 — Botão de cópia ausente, distante ou com rótulo não canônico — CORRIGIDO — criticidade alta

Foram auditadas **12 páginas que disponibilizam Modelos reutilizáveis**:

#### LAI
1. `lai/banco-do-brasil-plr-2026.html`
2. `lai/banco-do-brasil.html`
3. `lai/sest-cgpar.html`
4. `lai/agu.html`
5. `lai/ministerio-fazenda.html`
6. `lai/tse.html`
7. `lai/tcu.html`
8. `lai/pge-sp.html`
9. `lai/estatais-federais.html`

#### MPT
10. `mpt/modelo-representacao.html`
11. `mpt/modelo-bb-bahia-greve-2026.html`

#### Notícias
12. `noticias/2026/modelo-pedido-posicionamento-assessorias-imprensa-bancos-fiscalizacao-produtividade.html`

**Situação anterior:** havia páginas com “Copiar pedido” em barra de ações distante do texto, Modelos MPT sem botão de cópia e uma notícia-modelo sem mecanismo de cópia.

**Remediação:** as 12 páginas passaram a ter:

- rótulo exato **COPIAR MODELO**;
- botão imediatamente acima do bloco copiável;
- alvo de cópia limitado ao corpo do Modelo;
- ausência de elemento editorial intermediário entre botão e conteúdo.

**Verificação:** 12/12 aprovadas no teste estrutural posterior.

### A-03 — Central LAI ainda promovia “2ª EDIÇÃO” — CORRIGIDO — criticidade média

**Achado:** `lai/index.html` ainda apresentava o card da PLR como “2ª EDIÇÃO • PLR 2026”.

**Remediação:** substituído por **MODELO • PLR 2026**, preservando apenas a edição vigente como referência pública.

### A-04 — Bloco `index-hero` duplicado na Central LAI — CORRIGIDO — criticidade média

**Achado:** `lai/index.html` continha `<section class="index-hero">` aninhado inutilmente dentro de outro bloco idêntico.

**Remediação:** estrutura duplicada removida e verificada.

### A-05 — Hash do HTML publicado desatualizado em metadados JSON — CORRIGIDO — criticidade média

As alterações de interface modificaram os blobs HTML, tornando obsoletos os valores anteriores de `publication.html_blob_sha`.

**Remediação:** metadados sincronizados nos JSON dos Modelos LAI, MPT e notícia-modelo afetados.

### A-06 — Menu global inconsistente em páginas históricas — PENDENTE — criticidade média

A auditoria identificou **26 páginas públicas** que não apresentam todos os itens do menu global vigente.

#### Artigos — 10 páginas
- `artigos/2026/quando-o-cliente-vira-fiscal-do-trabalhador.html`;
- `artigos/2026/democracia-para-a-base-quem-controla-o-poder.html`;
- `artigos/2026/quando-a-oposicao-reproduz-a-burocracia-que-combate.html`;
- `artigos/2026/assembleia-nao-e-cheque-em-branco-bahia.html`;
- `artigos/2026/anatomia-do-peleguismo-sindical.html`;
- `artigos/2026/ano-eleitoral-aumento-real-banco-do-brasil.html`;
- `artigos/2026/vanguarda-nao-e-autoproclamacao.html`;
- `artigos/2026/o-direito-nao-socorre-aos-que-dormem.html`;
- `artigos/2026/fraude-das-assembleias-virtuais.html`;
- `artigos/2026/450-mil-bancarios.html`.

#### LAI — 9 páginas
- `lai/banco-do-brasil-plr-2026.html`;
- `lai/banco-do-brasil.html`;
- `lai/sest-cgpar.html`;
- `lai/agu.html`;
- `lai/ministerio-fazenda.html`;
- `lai/tse.html`;
- `lai/tcu.html`;
- `lai/pge-sp.html`;
- `lai/estatais-federais.html`.

#### Biblioteca — 4 páginas
- `biblioteca/auditoria.html`;
- `biblioteca/traducoes/index.html`;
- `biblioteca/traducoes/politica.html`;
- `biblioteca/traducoes/projeto-001.html`.

#### Observatório — 2 páginas
- `observatorio/documentos/index.html`;
- `observatorio/documentos/07_Roadmap_do_Observatorio_Classe_e_Massas.html`.

#### Fale Conosco — 1 página
- `fale-conosco/index.html`.

**Natureza:** páginas criadas em momentos diferentes preservam versões antigas ou reduzidas do cabeçalho.

**Estado:** registrado como irregularidade de UI/navegação, mas **não remediado automaticamente nesta estratégia**, por ultrapassar o objeto específico das regras de Modelos e envolver alteração transversal de 26 páginas. Deve constituir frente própria de normalização do menu global.

## 4. Testes sem irregularidade detectada

Nas 51 páginas públicas examinadas:

- nenhum `noindex` indevido foi detectado;
- nenhum ID HTML duplicado foi detectado;
- todos os documentos examinados apresentaram fechamento `</html>`;
- depois da remediação, nenhum portão visível para edição anterior de Modelo foi detectado nas páginas examinadas;
- as 12 páginas de Modelos auditadas passaram no padrão de **COPIAR MODELO**.

## 5. Regra canônica implantada

O padrão foi materializado em:

- `AGENTS.md` do Classe e Massas — versão 2.3;
- `AGENTS.md` do Gerador de Agents;
- `modules/publication.md` do Gerador;
- `templates/AGENTS.example.md` do Gerador;
- `CHANGELOG.md` do Gerador — versão 1.7.

Para projetos com publicação de Modelos, a regra reutilizável passa a ser:

> **Todo Modelo público deve possuir botão COPIAR MODELO imediatamente acima do texto copiável. Somente a edição vigente pode permanecer no Site Público; versões anteriores são preservadas pelo Git, sem portões públicos de acesso.**

## 6. Conclusão

O passivo diretamente relacionado a **Modelos públicos e edições anteriores** foi corrigido.

Permanece uma frente identificada e separável: **normalização do menu global em 26 páginas públicas antigas**. Essa irregularidade não compromete o conteúdo editorial dos textos, mas produz experiência de navegação desigual e deve ser tratada em estratégia própria para evitar uma alteração transversal não auditada dentro desta frente.
