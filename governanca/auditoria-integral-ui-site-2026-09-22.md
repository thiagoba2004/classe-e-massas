# Auditoria Integral de Interface e Coerência Visual — Site Classe e Massas

**Projeto:** PRJ-000001 — Classe e Massas  
**Estratégia:** EA-000001-000025 — Auditoria integral de interface e coerência visual do Site Classe e Massas  
**Data:** 22/09/2026  
**Escopo:** 60 arquivos HTML públicos existentes na árvore do repositório, CSS global, CSS específico do Observatório, JavaScript de navegação e comparação estrutural com Ações Judiciais e Planejamento Financeiro.

## Parecer executivo

O Site Classe e Massas não está visualmente nem estruturalmente consolidado em um único sistema de interface. Existem múltiplas gerações de componentes convivendo no mesmo CSS e nas páginas públicas.

A captura fornecida pelo usuário é compatível com os achados do código: navegação secundária transformada em caixas grandes no mobile, títulos editoriais excessivamente grandes, CTAs pretos de navegação e superfícies de cards sem uma semântica cromática coerente com a identidade original do Classe e Massas.

A EA-000001-000024 resolveu pontos localizados, mas introduziu uma regressão cromática global em `.resource-card` e não auditou as demais famílias de páginas. O gate anterior foi estreito demais.

## 1. Paleta e cards — CRÍTICO

A paleta-base do Classe e Massas é:
- `--paper: #f5f1e8`
- `--paper-raised: #fffdf8`
- `--ink: #191919`
- `--ink-strong: #111`
- `--ink-muted: #57534d`
- `--line: #242321`
- `--line-soft: #b9b3a8`
- `--accent: #9f2f2f`

Entretanto, a EA-000001-000024 adicionou diretamente no CSS global dos cards clicáveis:
- `#e5ecef`
- `#aebbc2`
- `#7f929d`
- `#dbe6ea`

Essas cores formam uma família azul/cinza fria e não derivam dos tokens cromáticos do Classe e Massas.

Consequência: qualquer `a.resource-card` passou a receber essa aparência. A varredura encontrou **30 ocorrências de `resource-card`** em páginas HTML, abrangendo Publicações, LAI e MPT.

O MPT acrescenta ainda quatro famílias próprias de cores:
- azul;
- pêssego/terracota;
- amarelo/ocre;
- verde.

O Observatório possui CSS próprio com `--observatorio-ink: #17243a` e `--observatorio-pale: #e8edf3`, reforçando uma segunda identidade azul dentro do mesmo Site.

**Conclusão:** o azul foi uma escolha de implementação incorreta. A diferenciação de cards clicáveis deve permanecer dentro da paleta do próprio Classe e Massas, usando variações mais escuras/contrastantes do papel, linhas e tinta, com o vermelho apenas como acento.

## 2. Tipografia — CRÍTICO

O padrão global atual ainda mantém escalas de display:
- `h1: clamp(2rem, 5.3vw, 3.45rem)`;
- Home: até `4.6rem` no desktop e `3.2rem` no mobile;
- títulos de cards editoriais: até `2.15rem`;
- nomes de teóricos da Biblioteca: `3.15rem`, reduzidos apenas para `2.45rem` no mobile;
- seções MPT chegam a `2.35rem`;
- blocos legados de Guia, Modelo e Nota contêm declarações entre `3.6rem` e `3.8rem`.

Isso explica diretamente a captura: o título longo do modelo em Notícias ocupa várias linhas com escala desproporcional ao texto.

O padrão dos Sites Ações Judiciais e Planejamento Financeiro trabalha com H1 próximo de 1,5–1,9rem nas páginas internas e cerca de 1,75–2,1/2,25rem nas Homes. O Classe e Massas permanece fora dessa escala.

## 3. Coleções editoriais — CRÍTICO

As páginas:
- `noticias/index.html`;
- `artigos/index.html`;
- `videos/index.html`

ainda usam a estrutura antiga:
- título `h2` não clicável;
- resumo;
- botão preto separado “Ler notícia”, “Ler artigo completo”, “Ler modelo” ou “Ver projeto do vídeo”.

Isso contradiz o padrão Coleção → Detalhe já consolidado no Gerador e nos projetos Ações Judiciais e Planejamento Financeiro, nos quais o próprio item/card é o hiperlink principal.

A captura fornecida pelo usuário mostra exatamente esse problema em `noticias/index.html`.

Foram detectados **68 elementos com classes de botão/CTA** nos 60 HTML auditados. Nem todos são irregulares: `COPIAR MODELO`, envio, comandos e ações reais devem continuar como botões. O problema é usar a mesma linguagem visual de botão para navegação simples.

## 4. Navegação secundária — ALTO

No mobile:
`.section-nav{display:grid;grid-template-columns:1fr}`
e
`.section-nav a{width:100%}`.

Resultado: links contextuais como PUBLICAÇÕES, PARTICIPE DA PAUTA, LINHA EDITORIAL e PRINCÍPIO SÍNTESE viram quatro caixas grandes empilhadas, exatamente como aparece na captura.

Essa solução compete visualmente com o conteúdo principal e cria uma segunda “barra de menu” muito pesada dentro da página.

## 5. Menu global — ALTO

A arquitetura vigente é:
`Início · Publicações · Biblioteca · MPT · LAI · Fale Conosco`.

Porém, somente **7 dos 60 HTML** já trazem essa estrutura diretamente no HTML-fonte. **52 páginas** ainda carregam no markup o menu antigo com Notícias, Artigos, Vídeos e Observatório como itens independentes; uma página não possui nav.

Em páginas que carregam `js/main.js`, o JavaScript corrige o menu em tempo de execução. Isso significa que a estrutura HTML continua divergente e o fallback sem JavaScript está desatualizado.

Além disso, **13 dos 60 HTML não carregam `main.js`**. Nessas páginas, o menu antigo não é corrigido em runtime.

Arquivos sem `main.js`:
- `artigos/2026/fraude-das-assembleias-virtuais.html`;
- `artigos/2026/o-direito-nao-socorre-aos-que-dormem.html`;
- `artigos/2026/vanguarda-nao-e-autoproclamacao.html`;
- dez documentos HTML do diretório `observatorio/documentos/`.

## 6. Fragmentação de CSS — ALTO

O CSS global contém **33 cores hexadecimais distintas** em 46 ocorrências, além das 9 cores específicas do `observatorio/observatorio.css`.

Foram detectados **26 blocos `<style>` embutidos em 14 arquivos HTML**. Isso mantém estilos legados fora da folha global e aumenta a possibilidade de colisão de cascata.

O `css/style.css` também conserva grandes blocos “migrados” para Guia, Modelo, Nota, Biblioteca e MPT, vários com escalas tipográficas anteriores. A folha global tornou-se uma sobreposição de gerações de UI, em vez de um sistema de componentes pequeno e previsível.

## 7. Observatório público — CRÍTICO

`observatorio/index.html` ainda expõe linguagem e conteúdo de governança interna:
- “ROADMAP • ESTADO ATUAL DO PROJETO”;
- “Fase 0”, “Fase 1”, “Fase 2”;
- “próximo gate estratégico”;
- “Documentos canônicos”;
- referência pública ao uso de Markdown, HTML e JSON/JSONL.

Isso conflita com a diretriz já adotada para Observatórios públicos: apresentar o estado do conhecimento, sínteses, mudanças analisadas, questões em aberto e fontes — sem expor fases, gates e mecanismos internos de produção.

Também existe uma coleção pública de documentos canônicos do Observatório, com CSS próprio, menu legado e nomenclatura de governança.

## 8. Pré-publicação e rascunhos na árvore do Pages — ALTO/RISCO

A árvore que alimenta o GitHub Pages contém:
- `editorial/rascunhos/...html`;
- documentos de governança/editoriais em HTML;
- `PROJECT_STATE.json`;
- `REQUEST_LOG.jsonl`;
- `STRATEGY_LOG.jsonl`;
- diretório `governanca/`.

Não existe `_config.yml` no repositório para declarar exclusões da publicação e `robots.txt` contém `Allow: /`.

A ferramenta de navegação utilizada nesta auditoria não conseguiu verificar diretamente as URLs desses arquivos no GitHub Pages. Portanto, a exposição efetiva deve ser testada antes de ser tratada como fato consumado. Mesmo assim, a arquitetura atual apresenta risco real de publicar artefatos que deveriam ser apenas memória de repositório.

## 9. Mapa do Site e rodapé — ALTO

O Gerador exige página Mapa do Site e link correspondente no rodapé. O repositório Classe e Massas não possui `SITE_ARCHITECTURE.md`, `SITE_STYLE_GUIDE.md` nem rota `mapa-do-site/index.html`.

Os rodapés do Classe e Massas continuam, em grande parte, apenas como texto de identificação, sem o padrão de navegação auxiliar já aplicado nos Sites Ações Judiciais e Planejamento Financeiro.

## 10. Governança do próprio padrão — MÉDIO

O `AGENTS.md` foi atualizado para v2.8, mas `PROJECT_STATE.json` ainda registra, em campos internos de continuidade/governança, versões 2.7. Isso não é problema visual para o público, mas comprova que a sincronização normativa da estratégia anterior ficou incompleta.

## 11. Causa-raiz

A causa não é um único erro de CSS. O Site acumulou:

1. identidade editorial antiga com tipografia de jornal/display;
2. componentes novos do Gerador;
3. páginas legadas com CSS embutido;
4. CSS específico do Observatório;
5. scripts usados como “corretor” de markup antigo;
6. alterações pontuais feitas sem uma auditoria transversal de todas as famílias de páginas.

A EA-000001-000024 foi excessivamente localizada: corrigiu menu e três cards MPT, mas não aplicou um gate capaz de impedir regressões globais de cor, tipografia, coleções, Observatório e páginas legadas.

## Classificação consolidada

### CRÍTICOS
1. paleta fragmentada / azul introduzido fora da identidade;
2. tipografia excessiva e inconsistente;
3. coleções Notícias/Artigos/Vídeos fora do padrão Coleção → Detalhe;
4. Observatório público expondo governança interna.

### ALTOS
5. section-nav em caixas gigantes no mobile;
6. menu-fonte antigo em 52/60 páginas e 13 páginas sem normalização JS;
7. CSS fragmentado e 26 blocos inline;
8. risco de artefatos internos na árvore publicada;
9. ausência de Mapa do Site e de guias canônicos de arquitetura/estilo.

### MÉDIO
10. versões de governança 2.7/2.8 dessincronizadas no estado.

## Plano corretivo recomendado — NÃO EXECUTADO NESTA AUDITORIA

1. congelar novas alterações visuais isoladas;
2. criar `SITE_STYLE_GUIDE.md` e `SITE_ARCHITECTURE.md`;
3. reduzir e unificar a escala tipográfica;
4. eliminar cores arbitrárias e definir uma escala tonal derivada da paleta do Classe e Massas;
5. refatorar Notícias, Artigos e Vídeos para Coleção → Detalhe com cards/títulos clicáveis;
6. redesenhar `.section-nav` para navegação contextual compacta;
7. sincronizar o markup do menu em todos os HTML e eliminar dependência do JS para corrigir arquitetura;
8. retirar CSS embutido e consolidar componentes;
9. reconstruir o Observatório público como estado do conhecimento, retirando roadmap/gates/formats internos;
10. separar de forma comprovada artefatos públicos e internos no pipeline do Pages;
11. criar Mapa do Site e padronizar rodapés;
12. testar 360 px, 390 px, 412 px e desktop, página por página, antes do deploy final.

## Gate da auditoria

**AUDITORIA CONCLUÍDA COM NÃO CONFORMIDADES SISTÊMICAS.**

Não é recomendável continuar fazendo correções isoladas por página. O próximo passo lógico é uma estratégia corretiva única, transversal e faseada.
