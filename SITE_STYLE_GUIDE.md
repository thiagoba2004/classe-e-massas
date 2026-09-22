# Guia de Identidade Visual — Classe e Massas

## Princípio

A identidade pública do Classe e Massas deve transmitir jornalismo operário contemporâneo, pesquisa crítica, rigor documental e leitura editorial. O Site pode reutilizar padrões funcionais comprovados em outros projetos, mas sua aparência deve permanecer própria.

## Design tokens

- fundo principal / papel: `#f5f1e8`;
- superfície elevada: `#fffdf8`;
- superfície navegável: `#ebe4d8`;
- superfície navegável em hover: `#dfd3c3`;
- texto: `#191919`;
- texto forte: `#111111`;
- texto secundário: `#57534d`;
- linha forte: `#242321`;
- linha suave: `#b9b3a8`;
- acento editorial: `#9f2f2f`;
- acento profundo: `#7f2424`.

É vedada a introdução de azul, verde, turquesa, pêssego ou outra família cromática como cor estrutural de componentes globais sem decisão arquitetural explícita.

## Tipografia

- títulos editoriais: Georgia / Times New Roman;
- corpo, navegação e interface: Arial / Helvetica quando a função for de interface; Georgia / Times New Roman para leitura longa;
- corpo base: aproximadamente `1rem`;
- `h1` de páginas internas: `clamp(1.5rem, 2.7vw, 1.9rem)`;
- `h1` da Home: `clamp(1.8rem, 3.5vw, 2.2rem)`;
- `h2`: aproximadamente `1.2rem–1.45rem`;
- `h3`: aproximadamente `1.05rem–1.2rem`;
- títulos de cards/coleções não devem funcionar como display typography; devem permanecer próximos da escala do texto corrente;
- no mobile, títulos longos não podem dominar a viewport.

## Semântica visual de interação

A aparência deve indicar o comportamento do componente sem rótulos redundantes.

### Card clicável

`a.resource-card` e equivalentes de coleção:
- fundo `#ebe4d8`;
- borda derivada da paleta neutra;
- faixa superior ou detalhe em `#9f2f2f`;
- hover em `#dfd3c3`;
- leve elevação;
- todo o card é o hiperlink.

O card clicável nunca usa azul para indicar navegação.

### Card estático

`article.resource-card` e equivalentes:
- fundo `#fffdf8` ou papel;
- borda neutra;
- sem elevação ou deslocamento de hover;
- nenhum comportamento visual que sugira clique.

### Botões e hierarquia de ações

Botão preenchido é reservado a **ação real**:
- copiar;
- enviar;
- confirmar;
- executar comando.

A hierarquia cromática é semântica:
- **ação primária real**: fundo `#9f2f2f` (vermelho editorial), texto branco;
- **hover/foco da ação primária**: `#7f2424`, texto branco;
- **ação secundária**: tratamento tonal ou outlined derivado da paleta papel/tinta/vermelho;
- **estado desabilitado**: mantém a identidade da ação, com redução de ênfase visual;
- preto é tinta/estrutura e não deve ser o preenchimento automático de CTA apenas por tradição de componente.

Navegação simples não deve usar botão preenchido “Ler…”, “Ver…” ou “Acessar…”. Para navegação usar:
- card clicável;
- título/link;
- link textual;
- navegação contextual compacta.

A cor não substitui semântica: links continuam links e ações continuam botões. O contraste e o estado de foco devem permanecer perceptíveis independentemente da cor.

## Navegação

### Menu global

Arquitetura:
`Início · Publicações · Biblioteca · MPT · LAI · Fale Conosco`.

Notícias, Artigos, Vídeos e Observatório pertencem ao hub **Publicações** e não aparecem como itens autônomos do menu global.

Em telas estreitas, o menu global é horizontal, rolável e deslizante, sem botão MENU e sem empilhar todos os itens verticalmente.

### Navegação contextual

`.section-nav` deve ser compacta. No mobile, também deve permanecer horizontal rolável quando houver vários itens; não deve virar uma pilha de caixas de largura total.

## Coleções

Notícias, Artigos, Vídeos, LAI, MPT e demais listagens seguem o padrão **Coleção → Detalhe**:
- item principal inteiramente clicável quando houver destino único;
- título e resumo fazem parte do card;
- não adicionar CTA preto redundante dentro do card.

## Home

A Home é institucional, enxuta e não funciona como catálogo completo de menus. A marca “Classe e Massas” não deve usar escala de manchete gigante.

## Observatório

A camada pública apresenta:
- sínteses;
- objetos de pesquisa;
- questões em aberto;
- mudanças acompanhadas;
- fontes e resultados públicos.

Não expõe:
- fases internas;
- gates;
- roadmap operacional;
- nomes de formatos de trabalho como Markdown/JSON;
- documentação canônica interna como se fosse conteúdo editorial.

## Mobile

Testar ao menos 360 px, 390 px e 412 px.

Regras:
- ausência de overflow geral;
- menu global rolável horizontalmente;
- navegação contextual compacta;
- cards em uma coluna quando necessário;
- títulos moderados;
- tabelas podem ter rolagem própria.

## Regra de consistência

Qualquer nova família de componente deve derivar destes tokens. Cores hardcoded fora desta paleta devem ser tratadas como exceção documentada ou irregularidade.


### Botão ENVIAR MENSAGEM — padrão transversal

Nos Sites do ecossistema, o botão real **ENVIAR MENSAGEM** usa a classe adicional `submit-button` e deve ser sempre **oval/pílula**, nunca retangular:

- `border-radius: 999px`;
- a forma é comum entre os Sites;
- a cor continua sendo a cor primária de ação de cada Projeto;
- o componente continua sendo `<button type="submit">`, nunca link.
