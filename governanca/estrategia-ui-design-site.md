# Estratégia — Sistema de UI Design do Classe e Massas

**ID:** STRAT-CEM-20260917-010  
**Data:** 17/09/2026  
**Status:** EM EXECUÇÃO

## Objetivo

Transformar a identidade visual já existente do Classe e Massas em um sistema de interface coerente, responsivo, acessível e sustentável, preservando sua linguagem editorial de jornal impresso e evitando alterações cosméticas isoladas.

## Diagnóstico inicial

1. O site possui cerca de 54 páginas HTML e apenas dois arquivos CSS permanentes, mas várias páginas mantêm CSS embutido e há estilos injetados por JavaScript.
2. A identidade base é forte e deve ser preservada: fundo claro, tinta escura, Georgia para leitura/títulos e Arial para navegação/metadados.
3. A navegação global não é uniforme em todas as páginas e, no celular, o menu quebra em várias linhas, aumentando muito o cabeçalho.
4. Existem múltiplas larguras de conteúdo sem uma escala explícita: 820, 920, 1050 e 1060 px.
5. O componente `.home-card` é utilizado para finalidades diferentes, fazendo listagens de matérias herdarem títulos e espaçamentos excessivos.
6. Botões, caixas, notas, grids e formulários possuem tratamentos visuais diferentes conforme a seção.
7. Notícias, LAI, Fale Conosco e Observatório já possuem micro-sistemas próprios; precisam ser reconciliados com o sistema global.
8. A experiência mobile deve ser considerada primeiro: área de toque, tamanho de títulos, navegação, ritmo vertical e densidade de informação.

## Direção visual proposta

- manter a estética **editorial / jornal impresso**, sem aparência de portal corporativo;
- paleta principal: papel claro + tinta quase preta;
- usar uma única cor de acento, de forma restrita, para estados ativos e destaques;
- hierarquia tipográfica mais controlada e responsiva;
- títulos fortes, mas menores no celular;
- mais espaço em branco entre grupos de informação;
- menos caixas desnecessárias;
- bordas e regras horizontais como linguagem editorial principal;
- botões com três variantes canônicas: primário, secundário e link de ação;
- componentes reutilizáveis em vez de CSS local por página.

## Plano de fases

### Fase 1 — Design tokens e fundação — CONCLUÍDA
Variáveis globais de cor, tipografia, largura, espaçamento, borda, foco e tamanho mínimo de toque implementadas em `css/style.css`.

### Fase 2 — Cabeçalho e navegação — CONCLUÍDA
Cabeçalho global normalizado. No desktop, os destinos permanecem visíveis; no celular, a navegação ocupa uma faixa horizontal rolável em uma única linha, sem submenu e sem empilhamento vertical. Quando o menu é reconstruído pelo `main.js`, a seção ativa é centralizada automaticamente na faixa.

### Fase 3 — Tipografia e ritmo editorial — CONCLUÍDA
Hierarquia global de h1, h2, h3 e h4, kicker, dek, meta, subtítulos, corpo, listas, citações, legendas e links padronizada em `css/style.css`. O ritmo vertical foi compactado em documentos extensos e ajustado especificamente para telas móveis.

### Fase 4 — Componentes — CONCLUÍDA
Componentes canônicos criados em `css/style.css` para:
- botões primário, secundário e terciário/link de ação;
- cards editoriais;
- notas e alertas;
- caixas documentais;
- grids responsivos;
- formulários;
- navegação interna de seção.

Foi preservada compatibilidade visual com classes existentes como `.home-card`, `.note`, `.contact-note`, `.method-note`, `.library-note`, `.form-row`, `.field`, `.protocol-info` e `.form-status`.

### Fase 5 — Páginas de índice — CONCLUÍDA
O sistema foi aplicado a Home, Notícias, Artigos, Observatório, Biblioteca, MPT, LAI e Fale Conosco.

- Home: tratada como capa editorial enxuta, sem reintrodução de cards de menu.
- Notícias e Artigos: índices convertidos para cards editoriais e hero canônico.
- Observatório e Biblioteca: preservada maior densidade de pesquisa, com largura ampla e ações canônicas.
- MPT e LAI: integrados ao sistema de serviço/documentação.
- Fale Conosco: integração visual por CSS global, sem regravar o HTML que contém a lógica operacional do formulário.

### Fase 6 — Páginas de leitura — CONCLUÍDA
A camada global de leitura foi aplicada aos artigos, notícias, páginas LAI e páginas do MPT, normalizando largura, hero, blocos documentais, tabelas, avisos, ações e comportamento móvel.

As quatro páginas individuais do MPT passaram a usar navegação global completa e `main.js`.

Os documentos canônicos do Observatório que utilizam HTML autônomo tiveram seu template visual alinhado ao sistema do site, preservando integralmente o conteúdo documental.

### Fase 7 — Mobile e acessibilidade — CONCLUÍDA
A auditoria técnica contemplou:
- área mínima de toque e controles de formulário;
- foco visível e navegação por teclado;
- skip link para bypass de navegação;
- contraste da paleta;
- mídia responsiva;
- tabelas e blocos `pre` em telas estreitas;
- preferências de redução de movimento e aumento de contraste;
- comportamento do menu horizontal entre 360 e 430 px;
- estados dinâmicos com ARIA.

Contrastes verificados na paleta principal:
- tinta sobre papel: 15,6:1;
- texto atenuado sobre papel: 6,78:1;
- acento sobre papel: 6,38:1;
- branco sobre acento: 7,19:1.

As páginas de Notícias e o Roadmap voltaram a carregar o `main.js` com versão de cache específica. Os documentos canônicos autônomos do Observatório receberam skip link próprio.

### Fase 8 — Limpeza técnica — CONCLUÍDA
A consolidação técnica removeu CSS injetado pelo JavaScript e eliminou CSS embutido redundante das famílias Fale Conosco, LAI, MPT e da notícia sobre a LAI/e-mail ao BB.

Os estilos específicos do MPT foram migrados para `css/style.css`, preservando os componentes próprios da seção. Regras antigas de `.news-tools` foram removidas e a sobreposição de largura da Central LAI foi corrigida.

Exceção intencional: os documentos HTML autônomos do Observatório continuam com CSS embutido próprio porque foram concebidos para funcionar de forma isolada e não dependem da folha global.

### Fase 9 — Auditoria visual final
Revisar as principais páginas em desktop e celular e corrigir regressões antes de encerrar a estratégia.

## Regra de implementação

Nenhuma mudança global de UI será aplicada antes da aprovação deste plano. A execução será incremental, com verificação após cada fase.
