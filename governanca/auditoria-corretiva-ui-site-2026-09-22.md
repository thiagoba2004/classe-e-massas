# Auditoria Corretiva de Interface — Site Classe e Massas

**Projeto:** PRJ-000001 — Classe e Massas  
**Estratégia:** EA-000001-000026 — Correção transversal de interface e arquitetura pública do Site Classe e Massas  
**Data:** 22/09/2026  
**Auditoria de origem:** `governanca/auditoria-integral-ui-site-2026-09-22.md`

## Parecer executivo

A correção transversal eliminou as não conformidades críticas e altas apontadas na auditoria anterior na superfície pública do Site.

O problema cromático indicado pelo usuário estava correto: a implementação anterior havia introduzido uma família azul/cinza fria em cards clicáveis, incompatível com a identidade papel–tinta–vermelho do Classe e Massas. Essa paleta foi removida.

A arquitetura pública, a semântica de navegação, a escala tipográfica e a separação entre artefatos públicos e internos foram consolidadas.

## 1. Superfície pública auditada

Após a configuração explícita de exclusões do GitHub Pages, foram auditados **47 arquivos HTML públicos**.

Critérios verificados programaticamente em 47/47:
- exatamente um `<h1>`;
- menu global canônico presente;
- item **Publicações** presente no menu;
- ausência de Notícias, Artigos, Vídeos e Observatório como itens autônomos do menu global;
- ausência de blocos `<style>` embutidos;
- link para **Mapa do Site** no rodapé;
- carregamento de `js/main.js`.

**Resultado: 47/47 sem anomalias nesses critérios.**

## 2. Paleta e cards

### Paleta canônica
- papel: `#f5f1e8`;
- superfície elevada: `#fffdf8`;
- superfície clicável: `#ebe4d8`;
- hover clicável: `#dfd3c3`;
- tinta: `#191919` / `#111`;
- vermelho editorial: `#9f2f2f`;
- vermelho profundo: `#7f2424`.

Foram removidas do CSS público as famílias azuis, verdes, ocres e pêssego usadas anteriormente em cards e componentes do MPT.

O padrão final é:
- `a.resource-card`: superfície de papel mais escura, faixa/acento vermelho e hover ainda mais escuro;
- `article.resource-card`: superfície neutra, sem comportamento de hover que sugira clique.

Verificação automática:
- paleta azul anterior ausente;
- cards clicáveis usam `--paper-link`;
- cards estáticos usam `--paper-raised`;
- chaves CSS balanceadas: **525/525**.

## 3. Tipografia

A escala de display foi substituída por escala editorial moderada:
- H1 interno: `clamp(1.5rem, 2.7vw, 1.9rem)`;
- H1 da Home: `clamp(1.8rem, 3.5vw, 2.2rem)`;
- H2 e títulos de cards reduzidos para a faixa aproximada de 1.2–1.45rem;
- nomes de autores, títulos MPT e componentes legados também foram normalizados.

No mobile, o H1 da Home é limitado a `1.8rem`.

## 4. Coleções editoriais

Foram convertidos para o padrão **Coleção → Detalhe**:
- Notícias: **3 cards clicáveis**;
- Artigos: **10 cards clicáveis**;
- Vídeos: **1 card clicável**.

Total convertido: **14 itens**.

Verificação:
- botões pretos de navegação “Ler/Ver” nessas três coleções: **0**;
- o próprio card é o hiperlink principal.

Botões preenchidos permanecem reservados a ações reais, como copiar, enviar ou confirmar.

## 5. Navegação

Menu global canônico:

```text
Início · Publicações · Biblioteca · MPT · LAI · Fale Conosco
```

O hub **Publicações** reúne:
- Notícias;
- Artigos;
- Vídeos;
- Observatório.

O HTML-fonte das páginas públicas principais foi sincronizado; a arquitetura não depende mais do JavaScript para esconder o menu antigo.

Foi criado:
- `/mapa-do-site/`.

Os rodapés públicos passaram a oferecer:
- Mapa do Site;
- Fale Conosco.

## 6. Responsividade

Auditoria estática das regras CSS confirmou:

- breakpoint global em até **880 px**:
  - menu com `flex-wrap: nowrap`;
  - `overflow-x: auto`;
  - rolagem horizontal confinada à navegação;

- breakpoint em até **700 px**:
  - `.section-nav` horizontal e rolável;
  - cards de serviço em uma coluna;
  - H1 da Home reduzido;
  - títulos editoriais reduzidos.

As larguras-alvo de **360 px, 390 px e 412 px** estão dentro desses breakpoints e recebem as mesmas regras responsivas auditadas.

A ferramenta disponível nesta sessão não oferece renderização gráfica direta do GitHub Pages nessas três larguras. Portanto, o gate foi baseado em estrutura HTML, regras CSS, semântica e build. Uma captura real em aparelho continua sendo evidência complementar útil, não requisito para a consistência do código.

## 7. Observatório

A Home pública do Observatório foi reconstruída.

Removidos da superfície pública:
- Roadmap;
- fases;
- gates;
- menções a Markdown;
- menções a JSON;
- catálogo de documentos canônicos;
- CSS azul específico.

A página agora apresenta:
- campos de observação;
- frente de pesquisa;
- questões em acompanhamento;
- fontes e método;
- acessos a áreas públicas relacionadas.

Verificação automatizada em `observatorio/index.html`:
- “Roadmap”: ausente;
- “Fase”: ausente;
- “gate”: ausente;
- “Markdown”: ausente;
- “JSON”: ausente;
- `observatorio.css`: ausente;
- “Documentos canônicos”: ausente.

## 8. CSS embutido e legado

A auditoria anterior encontrou 26 blocos `<style>` em 14 arquivos.

Após exclusão dos artefatos internos e migração dos estilos públicos:
- blocos `<style>` na superfície pública: **0**.

Os últimos três blocos públicos foram migrados de:
- `artigos/2026/ano-eleitoral-aumento-real-banco-do-brasil.html`;
- `biblioteca/auditoria.html`;
- `editorial/documentos/01_Diretriz_Canonica_Linha_Editorial_Noticias.html`.

## 9. Separação público/interno

Foi criado `_config.yml` para excluir do GitHub Pages:
- `AGENTS.md`;
- `PROJECT_STATE.json`;
- `REQUEST_LOG.jsonl`;
- `STRATEGY_LOG.jsonl`;
- `SITE_ARCHITECTURE.md`;
- `SITE_STYLE_GUIDE.md`;
- `README.md`;
- `governanca/`;
- `tools/`;
- `templates/`;
- `editorial/rascunhos/`;
- `observatorio/documentos/`;
- `observatorio/observatorio.css`.

Isso elimina o risco arquitetural identificado na auditoria anterior de tratar memória e governança internas como superfície editorial pública.

## 10. Governança preventiva

Criados:
- `SITE_STYLE_GUIDE.md`;
- `SITE_ARCHITECTURE.md`.

O `AGENTS.md` foi atualizado para **v2.9**:
- Vídeos pertence ao hub Publicações;
- menu global canônico fixado;
- navegação horizontal deslizante normatizada;
- semântica card clicável x card estático normatizada;
- os dois guias canônicos passam a integrar a fonte normativa do projeto.

A antiga regra 8.8.5 que colocava Vídeos diretamente no menu global foi substituída.

## 11. Deploy

O GitHub Pages executou com sucesso o build/deploy do commit:

`472aa7208eb6816f9758a9cd6d8ea632759b61e6`

Run:
`35788703548`

Conclusão:
`success`.

Esse commit é posterior às alterações públicas de CSS, Observatório, menu-fonte, rodapés, Mapa do Site, coleções e `_config.yml`.

Os commits posteriores relativos a AGENTS/relatórios/estado não alteram a superfície pública por estarem excluídos do Pages.

## Gate final da auditoria corretiva

**APROVADO NO CÓDIGO E NO PIPELINE DE PUBLICAÇÃO.**

Não permanecem não conformidades críticas ou altas abertas dentre as apontadas pela EA-000001-000025.

Ponto de observação residual: a confirmação visual em dispositivo real pode revelar detalhe de renderização dependente de navegador/fonte/cache que não seja detectável por auditoria estática. Qualquer captura futura divergente deve ser tratada como regressão visual específica, não como estado presumido do código.
