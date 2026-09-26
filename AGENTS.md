# AGENTS.md — Protocolo Canônico de Trabalho dos Modelos de IA

**Projeto:** `PRJ-000001 — Classe e Massas`  
**Código canônico do Projeto:** `PRJ-000001`  
**Sequência do Projeto:** `000001`  
**Alias mnemônico:** `CEM`  
**Denominação do Projeto:** `Classe e Massas`  
**project_id legado:** `classe-e-massas`  
**Status:** CANÔNICO  
**Versão:** 3.3  
**Data:** 26/09/2026  
**generated_from_kernel:** `1.8`  
**Kernel de referência:** `thiagoba2004/gerador-de-agents/AGENTS_KERNEL.md`  
**Escopo:** todo modelo de IA, agente, assistente ou automação que trabalhe neste repositório ou em seus documentos derivados.

---

## 1. Finalidade e continuidade normativa

Este documento estabelece regras obrigatórias de continuidade, preservação, rastreabilidade, honestidade operacional e coerência estratégica para qualquer Modelo de IA que trabalhe no projeto **Classe e Massas**.

A versão 1.9 é uma **migração controlada** da versão 1.8 para o núcleo universal `AGENTS_KERNEL.md` 1.2 do Projeto Gerador de Agents.

A migração **não revoga nem reduz** as regras específicas e mais rigorosas já existentes no Classe e Massas.

A versão integral anterior permanece recuperável pelo Git no blob:

```text
0c0fc7bd17de1084728ed1f1f2c4aa61405d1a86
```

Há também referência histórica em:

```text
governanca/AGENTS_BASE_v1.8.md
governanca/AGENTS_BASE_v1.8_FULL_COPY_NOTICE.md
```

### 1.1. Regra de incorporação por referência

**Todas as regras do `AGENTS.md` v1.8 permanecem normativas por incorporação por referência, exceto os trechos expressamente substituídos nesta versão.**

Ficam especificamente substituídos pela versão 1.9:

- o ciclo operacional do antigo item 23, na parte que determinava mensagem ao usuário antes do registro;
- o antigo item 24.14 — “Confirmação imediata antes do registro e de qualquer processamento”;
- o antigo item 24.15 — “Registro obrigatório de todos os pedidos após a confirmação imediata e antes da execução substantiva”;
- quaisquer frases, fluxos ou referências cruzadas da v1.8 que determinem **mensagem ao usuário antes da confirmação técnica do registro persistente**.

Todos os demais itens, subitens, regras locais, critérios, salvaguardas, estados, metodologias e obrigações da v1.8 permanecem em vigor quando não conflitarem com esta versão.

### 1.2. Regra fundamental preservada

> **O chat é oficina. O arquivo canônico é a obra. O Git é a memória histórica. O Roadmap organiza a direção do trabalho.**

Nenhum trabalho relevante é considerado protegido enquanto existir apenas no contexto da conversa.

Nenhuma tarefa relativa ao projeto pode ser executada como ato isolado: deve estar vinculada a uma estratégia, Plano de Fases, fase atual, entrega ou gate e próximo passo lógico.

> **Sem registro persistente da estratégia, não executar tarefa substantiva.**

---

### Ponte bidirecional com o Coordenador Geral

Antes de tratar pedidos com **possível repercussão transversal**, **dúvida de pertencimento/roteamento**, possível vínculo com a **governança global** ou sinais de **candidato a novo Projeto**, consultar, quando a Biblioteca estiver acessível:

`/Governanca-Geral-Modelos-IA/00_BOOTSTRAP_COORDENADOR_GERAL.md`

Regras:

- pedidos inequivocamente locais e já abrangidos por este Projeto seguem diretamente este `AGENTS.md`, sem consulta obrigatória ao Bootstrap;
- a consulta ao Bootstrap é condicional e serve para classificar/rotear, não para substituir a governança local;
- evitar loop de roteamento: Bootstrap → Projeto é entrada normal; Projeto → Bootstrap ocorre apenas diante de dúvida, repercussão transversal ou governança global;
- se a Biblioteca/Bootstrap não estiver acessível na sessão, não inventar seu conteúdo; registrar a limitação quando material e prosseguir pela governança local comprovada;
- conversas classificadas como casuais/efêmeras pelo Coordenador Geral não devem ser artificialmente absorvidas por este Projeto.

### Arquitetura universal de ambientes v2

Este Projeto adota a arquitetura global de seis planos: **G** (identidade), **A** (superfície), **E** (executor), **C** (contexto/memória), **K** (fontes de conhecimento) e **P** (persistência/publicação).

Fonte global: `thiagoba2004/governanca-geral-modelos-ia/ARQUITETURA_UNIVERSAL_AMBIENTES_EXECUCAO_PERSISTENCIA.md`.

Regras locais:

- Projeto ChatGPT não é sinônimo deste Projeto de Governança;
- **memória exclusiva do Projeto ChatGPT é o padrão**, salvo decisão expressa;
- memória exclusiva reduz contaminação contextual, mas não elimina alucinações nem prevalece sobre fontes persistentes;
- Work não está disponível dentro do Projeto ChatGPT isolado; quando necessário, executar fora dessa fronteira mediante **handoff explícito**;
- fontes anexadas ao Projeto ChatGPT formam **Core Context curado**, não o repositório integral;
- Biblioteca e nuvens conectadas são fontes operacionais;
- GitHub deste Projeto é a fonte versionada canônica de estado, regras e histórico;
- filesystem local/Notebook é working copy/cache e nunca deve ser a única cópia necessária à continuidade;
- Codex deve devolver alterações relevantes ao repositório;
- o handoff para Work/Codex transfere somente o contexto necessário, com sensibilidade e destino canônico definidos.

O `EXECUTION_ENVIRONMENT_PROFILE.json` schema v2 registra a política local.

## 2. Hierarquia normativa e fonte da verdade

Quando houver dúvida sobre qual regra ou estado prevalece, usar a seguinte ordem:

1. este `AGENTS.md` v2.2 para regras vigentes do projeto;
2. arquivos canônicos específicos do objeto de trabalho;
3. `PROJECT_STATE.json` e manifestos/status específicos para estado corrente;
4. `STRATEGY_LOG.jsonl` para história das Estratégias Autônomas;
5. `REQUEST_LOG.jsonl` para sequência de pedidos;
6. Roadmaps, Planos de Fases e documentos de governança específicos;
7. `AGENTS.md` v1.8 incorporado por referência, para regras locais não substituídas;
8. `AGENTS_KERNEL.md` 1.4, como núcleo universal vigente;
9. histórico Git e commits comprovados;
10. somente depois, contexto de conversa ou memória do Modelo de IA.

Memória, resumo de conversa ou inferência **nunca prevalecem** sobre evidência documental mais recente.

Se houver conflito entre versões anteriores e a v2.2, **a v2.2 prevalece**.

Se houver conflito entre o kernel 1.4 e uma regra local mais rigorosa que não contrarie a finalidade universal do kernel, **a regra local mais rigorosa é preservada**.

---

## 3. Ordem obrigatória para todo novo pedido

Ao receber **qualquer novo prompt, mensagem, correção, complemento, saudação, pergunta, determinação, interrupção ou alteração de instrução** no contexto do projeto, a ordem é obrigatória:

```text
RECEBER O PEDIDO
      ↓
REGISTRAR NO REQUEST_LOG.jsonl
      ↓
VERIFICAR TECNICAMENTE QUE O REGISTRO FOI PERSISTIDO
      ↓
INFORMAR AO USUÁRIO: “PEDIDO REGISTRADO.”
      ↓
INFORMAR QUE IRÁ LER O PROMPT, ANALISAR E TOMAR AS PROVIDÊNCIAS NECESSÁRIAS
      ↓
IDENTIFICAR SE O PEDIDO CRIA, RETOMA OU ALTERA MATERIALMENTE UMA ESTRATÉGIA AUTÔNOMA
      ↓
SE SIM, CRIAR OU RECUPERAR O strategy_id E REGISTRAR O EVENTO NO STRATEGY_LOG.jsonl
      ↓
VERIFICAR O REGISTRO DA ESTRATÉGIA
      ↓
IDENTIFICAR PLANO, FASE, GATE, DEPENDÊNCIAS E PRÓXIMO PASSO
      ↓
SÓ ENTÃO EXECUTAR A SOLICITAÇÃO SUBSTANTIVA
```

### 3.1. Proibição de falsa confirmação

É proibido escrever **“Pedido registrado.”** antes de a persistência ter sido tecnicamente confirmada.

Se o registro falhar, o agente deve informar a falha e priorizar a recuperação do mecanismo de registro. Não pode representar o pedido como registrado.

### 3.2. Silêncio operacional

A versão 1.9 reconhece a finalidade legítima que motivou a v1.7 — impedir a sensação de travamento —, mas resolve o problema por outra ordem: **o registro vem primeiro**.

O agente deve realizar o registro inicial com a maior brevidade tecnicamente possível e, imediatamente após a confirmação, comunicar ao usuário:

> **Pedido registrado. Vou ler o prompt, analisar e tomar as providências necessárias.**

Essa mensagem pode ser dividida em duas frases ou atualizações, mas nunca pode preceder a confirmação técnica do registro.

---

## 4. Registro obrigatório de todos os pedidos

O `REQUEST_LOG.jsonl` é a fonte primária da sequência de solicitações do usuário.

Cada registro deve conter, sempre que tecnicamente possível:

```text
request_id
marcador temporal
origem da interação
texto integral ou representação fiel do pedido
escopo ou frente
estratégia vinculada, quando conhecida
strategy_id, quando conhecido
estado do pedido
ação solicitada
referências aos resultados, quando existirem
```

O `request_id` deve ser único e suficientemente sequencial para reconstruir a ordem dos pedidos.

Quando o usuário perguntar **“qual foi meu último pedido?”**, **“onde paramos?”**, **“o que eu pedi?”** ou equivalente, o agente deve consultar prioritariamente o `REQUEST_LOG.jsonl` e as demais fontes canônicas aplicáveis.

Interrupções do usuário durante tarefa em andamento são novos pedidos e devem ser registradas sem apagar o pedido anterior. O novo pedido pode suspender, complementar, corrigir ou consultar a tarefa anterior; essa relação deve permanecer rastreável.

---

## 5. Estratégias Autônomas e vinculação estratégica

Toda Estratégia Autônoma deve possuir identificação canônica composta por:

```text
strategy_code
strategy_name
```

O `strategy_code` é numérico, hierárquico, imutável e independente da denominação.

No Projeto `PRJ-000001`, novas estratégias seguem:

```text
EA-000001-EEEEEE
```

onde `EEEEEE` é a sequência monotônica de seis algarismos da Estratégia dentro do Projeto.

Para Estratégias novas, `strategy_id = strategy_code`. Os identificadores históricos `STRAT-CEM-...` permanecem preservados como `legacy_strategy_id` ou mapeamento equivalente e não são reescritos.

A sigla `CEM` é apenas alias mnemônico e não participa da formação do código.

Toda Estratégia Autônoma deve possuir registro persistente, sequencial e auditável no `STRATEGY_LOG.jsonl` antes da execução substantiva.

> **ESTRATÉGIA AUTÔNOMA NOVA = `strategy_code` NOVO + `strategy_name` + EVENTO `CREATED` PERSISTIDO ANTES DA EXECUÇÃO SUBSTANTIVA.**

O `PROJECT_STATE.json` representa a fotografia corrente; o `STRATEGY_LOG.jsonl` representa a história cronológica e append-only. Um não substitui o outro.

Eventos mínimos permanecem:

```text
CREATED
UPDATED
PAUSED
RESUMED
SUPERSEDED
CONCLUDED
CANCELLED
BACKFILLED
```

Antes da execução, o agente deve conseguir identificar:

```text
PROJECT_CODE
PROJECT_ALIAS
PROJECT_NAME
STRATEGY_CODE
STRATEGY_NAME
REGISTRO DA ESTRATÉGIA
PLANO / ROADMAP
PHASE_NUMBER
PHASE_TOTAL
PHASE_CODE
PHASE_NAME
OBJETIVO / ENTREGA / GATE
TAREFA ATUAL
DEPENDÊNCIAS
RESULTADO ESPERADO
PRÓXIMO PASSO LÓGICO
```

A ficha apenas escrita no chat não satisfaz a regra: a vinculação deve existir em fonte persistente.

Backfill histórico somente pode ser realizado com evidência persistente suficiente. Memória incerta não pode ser apresentada como fato.

---

## 6. Plano de Fases obrigatório

Toda Estratégia Autônoma, ainda que curta, emergencial, editorial, jurídica, documental ou técnica, deve possuir Plano de Fases explícito, persistente e integralmente numerado antes da execução substantiva.

Cada fase deve possuir:

```text
phase_number
phase_total
phase_code
phase_name
```

O `phase_code` deve herdar numericamente o Projeto e a Estratégia:

```text
F-PPPPPP-EEEEEE-FFF
```

No texto humano, usar obrigatoriamente:

```text
FASE 01/05 [F-000001-000014-001] — Registro e delimitação
FASE 02/05 [F-000001-000014-002] — ...
FASE 05/05 [F-000001-000014-005] — Verificação e fechamento
```

`phase_number` deve ser inteiro sequencial iniciado em 1; `phase_code` é o código hierárquico da fase; `phase_total` deve indicar o total vigente do plano; e `phase_name` deve ser uma denominação humana inequívoca.

É proibido manter rótulos não numerados como “FASE FINAL” ou “FASE DE CONSOLIDAÇÃO” isoladamente. A função pode constar da denominação, mas a posição numérica é obrigatória.

Cada fase deve indicar também estado, objetivo e gate quando aplicável.

A conclusão técnica de uma tarefa não altera automaticamente o estado da fase; o avanço depende do gate correspondente.

Estratégias anteriores à v2.1 não terão o histórico reescrito. Porém, ao serem retomadas, o Plano de Fases vigente deve ser normalizado para `phase_number` + `phase_total` + `phase_code` + `phase_name` antes de nova execução substantiva. A normalização deve apoiar-se em evidência persistente e nunca em numeração inventada retroativamente.

---

## 7. Persistência, write-through e proteção contra perda

Permanecem integralmente em vigor as regras da v1.8 sobre:

- proibição de trabalho substancial apenas no chat;
- persistência progressiva;
- checkpoint por unidade lógica;
- checkpoint temporal;
- write-through;
- RPO próximo de zero para unidades concluídas;
- salvamento em camadas;
- barreira de segurança antes de continuar;
- verificação independente do salvamento;
- Git como memória histórica;
- segunda cópia para marcos críticos quando tecnicamente possível;
- recuperação antes de reconstrução;
- preservação antes de operações destrutivas;
- integridade do histórico;
- diferenciação entre produzido, salvo, versionado, enviado ao remoto e publicado;
- fechamento obrigatório de sessão;
- proibição de falsas confirmações;
- regra de não regressão.

A sequência operacional preferencial permanece:

```text
PRODUZIR UNIDADE LÓGICA
      ↓
SALVAR NO ARQUIVO CANÔNICO
      ↓
VERIFICAR A GRAVAÇÃO
      ↓
ATUALIZAR STATUS / ESTADO
      ↓
VERSIONAR O MARCO RELEVANTE
      ↓
CONFIRMAR O REMOTO
      ↓
CONTINUAR
```

---

## 8. Regras locais específicas preservadas

A migração para o kernel 1.2 **não transforma o Classe e Massas em um projeto genérico**. Permanecem vigentes as regras locais da v1.8, inclusive:

### 8.1. Traduções

Toda tradução deve manter responsabilidades equivalentes a:

```text
traducao.md
status.json
fontes/
```

A tradução deve ser persistida progressivamente. Unidade concluída deve ser salva antes do avanço para a seguinte, salvo impossibilidade técnica expressamente informada.

A conclusão integral exige texto persistido, status atualizado, commit, remoto confirmado quando disponível e segunda cópia quando tecnicamente aplicável a marco crítico.

### 8.2. Formatos canônicos e política condicional de JSON

Padrão vigente:

- Markdown (`.md`) — fonte textual canônica para conteúdo editorial, documentação, metodologia, traduções e textos humanos;
- HTML (`.html`) — artefato público quando houver publicação no Site;
- JSON/JSONL — somente para **dados estruturados com função objetiva de máquina**;
- PDF/DOCX — derivados de distribuição, apresentação ou protocolo quando necessários.

#### 8.2.1. Regra padrão para textos editoriais/publicáveis

Para texto editorial ou publicável, a regra normal é:

```text
Markdown canônico
+
HTML quando publicado
```

**Não existe mais obrigação de criar um JSON correspondente ao texto.**

É proibido criar `NOME-ESTAVEL.json` apenas para repetir:
- título, subtítulo ou descrição;
- outline/seções;
- status editorial já recuperável;
- caminhos do Markdown e do HTML;
- links que já constam do texto;
- conteúdo narrativo já preservado nos formatos humano e público.

#### 8.2.2. Quando JSON/JSONL é justificável

JSON/JSONL deve existir quando houver finalidade estruturada concreta, por exemplo:

- `PROJECT_STATE.json`, mapas e estados correntes;
- `REQUEST_LOG.jsonl`, `STRATEGY_LOG.jsonl` e registros append-only;
- configuração de ferramentas e automações;
- datasets, catálogos, taxonomias, rankings e séries;
- glossários estruturados;
- metadados documentais realmente consumidos como dados;
- schemas e fixtures;
- corpus ou manifests de tradução com estado e relações;
- dados destinados a script, API, busca estruturada, filtro, cálculo, validação ou interoperabilidade comprovada.

Antes de criar um JSON novo, registrar mental ou documentalmente:

```text
QUAL PROCESSO CONSOME ESTE JSON?
QUAL INFORMAÇÃO ESTRUTURADA ELE PRESERVA QUE O MARKDOWN NÃO ATENDE?
```

Se não houver resposta concreta, **não criar**.

#### 8.2.3. Sincronização

- conteúdo textual: sincronizar Markdown e HTML publicado;
- dado estruturado: atualizar o JSON/JSONL apenas quando sua função de dados exigir;
- nenhuma alteração editorial deve criar automaticamente um terceiro artefato JSON.

#### 8.2.4. Preservação histórica

A antiga regra de triplicidade `.md + .html + .json` foi revogada em 20/09/2026 por decisão expressa do usuário.

Os JSON redundantes criados exclusivamente para cumprir aquela regra devem ser removidos do estado corrente do repositório. O histórico Git preserva integralmente as versões anteriores e a auditoria histórica de 18/09/2026.

A revogação **não autoriza apagar** JSON estruturais úteis, arquivos de configuração, estado, registros, catálogos, metadados funcionais, taxonomias, glossários ou bases de dados.

### 8.3. Siglas e abreviações

Toda sigla relevante deve ter o significado informado pelo menos uma vez, preferencialmente na primeira ocorrência.

Exemplo:

> **Acordo Coletivo de Trabalho (ACT)**

### 8.4. Cadeia institucional sindical

Ao classificar vínculos sindicais, usar sempre:

> **Sindicato > Federação > Confederação**

Distinguir obrigatoriamente filiação formal, representação por instrumento ou procuração, participação em comando ou mesa, coordenação conjuntural e compartilhamento de infraestrutura.

Quando um nível não existir, não for aplicável ou não puder ser confirmado, informar expressamente, sem preencher por inferência.

### 8.5. Observatório e roadmaps específicos

Para o Observatório Classe e Massas, permanece como referência geral:

```text
observatorio/documentos/07_Roadmap_do_Observatorio_Classe_e_Massas.md
```

Planos específicos podem detalhar essa estrutura, mas não podem contrariá-la silenciosamente.

### 8.6. Checkpoints

Em toda pausa ou atualização intermediária, informar se o estado produzido foi ou não persistido. Quando houver Estratégia Autônoma, indicar `strategy_id` e se o evento material mais recente foi refletido no `STRATEGY_LOG.jsonl`.

### 8.7. Padrão obrigatório para Modelos publicados no Site

Sempre que o Site Classe e Massas disponibilizar um **Modelo** reutilizável — em qualquer Menu ou seção, incluindo LAI, MPT, Notícias, Artigos, Fale Conosco ou futuras áreas — a interface pública deve obedecer cumulativamente às regras abaixo.

#### 8.7.1. Botão COPIAR MODELO

1. Todo Modelo público deve possuir botão com o rótulo canônico **`COPIAR MODELO`**.
2. O botão deve ficar **imediatamente acima do texto exato do Modelo que será copiado**.
3. Entre o botão e o bloco copiável não pode existir texto explicativo, nota, outro botão, chamada, link, caixa editorial ou qualquer elemento que rompa a relação visual direta.
4. O botão deve copiar somente o conteúdo do Modelo, sem título editorial, introdução, notas metodológicas, histórico de revisão ou conteúdo posterior.
5. É vedado posicionar o botão apenas em uma barra geral de ações distante do Modelo.
6. A publicação de um Modelo sem o botão, com o botão distante do texto, com alvo incorreto ou com rótulo divergente constitui **irregularidade de publicação** e deve ser corrigida antes de o artefato ser considerado verificado publicamente.

#### 8.7.2. Somente a edição vigente pode permanecer no Site Público

1. O Site Público deve disponibilizar **somente a edição vigente** de cada Modelo.
2. É proibido publicar ou manter no Site Público botões, links, cards, menus, rotas de navegação ou outros **portões de acesso** para edições anteriores de Modelos, inclusive rótulos como `VER 1ª EDIÇÃO`, `VERSÃO ANTERIOR`, `ARQUIVO`, `HISTÓRICO` ou equivalentes.
3. A página pública vigente não deve promover ou destacar numeração de edição anterior nem seção comparativa que funcione como acesso editorial à versão superada.
4. Versões históricas devem ser preservadas pela memória do Git, commits, tags, arquivos de governança ou outro mecanismo **não publicado no Site Público**.
5. Quando uma nova edição substituir outra, a versão HTML pública superada deve ser retirada do conjunto publicado; o histórico não deve depender de manter uma URL pública da edição anterior.
6. Esta regra não proíbe histórico técnico no repositório ou Git. Proíbe sua **exposição como conteúdo navegável do Site Público**.

#### 8.7.3. Gate de verificação de Modelos

Antes de declarar um Modelo `PUBLICADO` ou `ATUALIZADO`, verificar:

- existência de **COPIAR MODELO**;
- posição imediatamente acima do texto copiável;
- alvo correto da função de cópia;
- inexistência de acesso público a edição superada;
- inexistência de links internos apontando para versão histórica do Modelo;
- coerência entre Markdown, HTML e JSON vigentes.

### 8.8. Padrão obrigatório para conteúdo audiovisual

A área pública **Vídeos** constitui núcleo editorial permanente do Projeto Classe e Massas. Todo conteúdo audiovisual deve obedecer às regras abaixo.

#### 8.8.1. Estados de produção

1. Todo vídeo deve possuir estado explícito: `EM_PRODUCAO`, `EM_REVISAO` ou `PUBLICADO`.
2. É proibido marcar um vídeo como `PUBLICADO` antes de existir arquivo ou URL audiovisual real, revisado e acessível.
3. Páginas de vídeos ainda não concluídos devem informar claramente **EM PRODUÇÃO** e não podem conter player, thumbnail ou URL fictícios.

#### 8.8.2. Dramatização e realidade documental

1. Dramatizações devem ser identificadas de forma inequívoca como ficcionais.
2. É proibido representar pessoa real, banco real, logotipo, uniforme ou identidade visual reconhecível como se a dramatização fosse registro factual sem base documental e autorização adequada.
3. Quando um vídeo for inspirado em relato, documento ou artigo, a fonte editorial deve ser registrada.
4. O roteiro deve distinguir: fato documentado, interpretação editorial e dramatização.

#### 8.8.3. Pacote canônico de produção

Todo vídeo relevante deve manter, conforme aplicável:

- roteiro;
- plano de cenas;
- prompts de geração;
- ficha de continuidade de personagens e cenários;
- narração;
- legendas;
- ficha técnica;
- fontes;
- metadados estruturados;
- referência ao arquivo ou URL final quando publicado.

#### 8.8.4. Qualidade e direitos

1. Priorizar áudio, imagens e materiais próprios, licenciados ou expressamente autorizados para o uso pretendido.
2. Revisar termos de uso da ferramenta de IA e licenças dos materiais incorporados antes da publicação.
3. Conteúdo gerado por IA deve passar por revisão humana integral antes de atingir estado `PUBLICADO`.
4. Nenhuma alegação de resolução, qualidade, licença ou ausência de marca d'água pode ser registrada sem verificação do arquivo final ou da condição vigente da ferramenta.

#### 8.8.5. Vídeos dentro do hub Publicações

O item **Vídeos** integra o hub público **Publicações**, ao lado de **Notícias**, **Artigos** e **Observatório**. Ele **não** é item autônomo do menu global de primeiro nível.

A navegação global canônica é:

```text
Início · Publicações · Biblioteca · MPT · LAI · Fale Conosco
```

A promoção futura de **Vídeos** novamente ao primeiro nível exige decisão arquitetural expressa, persistente e versionada.

---

## 9. Protocolo mínimo de segurança operacional — substitui o antigo item 23 da v1.8

Todo trabalho relativo ao projeto deve obedecer ao seguinte ciclo:

```text
REGISTRAR O PEDIDO NO REQUEST_LOG.jsonl
              ↓
VERIFICAR QUE O REGISTRO FOI PERSISTIDO
              ↓
INFORMAR AO USUÁRIO: “PEDIDO REGISTRADO.”
              ↓
INFORMAR QUE IRÁ LER O PROMPT, ANALISAR E TOMAR AS PROVIDÊNCIAS NECESSÁRIAS
              ↓
IDENTIFICAR SE O PEDIDO CRIA, RETOMA OU ALTERA MATERIALMENTE UMA ESTRATÉGIA AUTÔNOMA
              ↓
SE SIM, CRIAR OU RECUPERAR O strategy_id E REGISTRAR O EVENTO NO STRATEGY_LOG.jsonl
              ↓
VERIFICAR QUE O EVENTO DE ESTRATÉGIA FOI PERSISTIDO
              ↓
REFLETIR O ESTADO CORRENTE NO PROJECT_STATE.json OU EQUIVALENTE
              ↓
RECUPERAR E CONFIRMAR ESTRATÉGIA E PLANEJAMENTO
              ↓
IDENTIFICAR FASE, GATE, DEPENDÊNCIAS E PRÓXIMO PASSO
              ↓
SÓ ENTÃO EXECUTAR
              ↓
ABRIR / IDENTIFICAR O ARQUIVO CANÔNICO
              ↓
PRODUZIR UMA UNIDADE LÓGICA
              ↓
SALVAR
              ↓
VERIFICAR
              ↓
ATUALIZAR ESTADO E EVENTO DE ESTRATÉGIA, QUANDO HOUVER MUDANÇA MATERIAL
              ↓
VERSIONAR O MARCO RELEVANTE
              ↓
CONFIRMAR O REMOTO
              ↓
SÓ ENTÃO ACUMULAR NOVO TRABALHO SUBSTANCIAL
```

Para marcos críticos, acrescentar segunda cópia independente quando tecnicamente possível.

Este ciclo é **barreira de segurança**, não recomendação opcional.

---

## 10. Regra substitutiva do antigo item 24.14 da v1.8

### 10.1. Confirmação imediata após o registro técnico

Ao receber qualquer nova interação do usuário no contexto do projeto, o agente deve priorizar o registro persistente no `REQUEST_LOG.jsonl`.

Assim que o registro estiver tecnicamente confirmado, deve informar imediatamente:

> **Pedido registrado. Vou ler o prompt, analisar e tomar as providências necessárias.**

É proibido colocar mensagem de recebimento, promessa de análise ou declaração de registro **antes** da confirmação técnica do registro, salvo comunicação estritamente necessária para informar falha real do próprio mecanismo de registro.

Se o registro não puder ser efetuado, o agente deve informar a falha de modo transparente e não iniciar execução substantiva até recuperar o mecanismo ou documentar a impossibilidade conforme as regras de governança aplicáveis.

---

## 11. Regra substitutiva do antigo item 24.15 da v1.8

### 11.1. Registro obrigatório de todos os pedidos antes da comunicação de processamento e da execução substantiva

Todo novo pedido, mensagem, correção, complemento, saudação, pergunta, determinação, interrupção ou alteração de instrução deve ser registrado de modo persistente, sequencial e rastreável **antes da comunicação “Pedido registrado” e antes da execução substantiva**.

A regra operacional é:

> **PRIMEIRO REGISTRAR E VERIFICAR. DEPOIS INFORMAR “PEDIDO REGISTRADO” E QUE IRÁ LER, ANALISAR E TOMAR AS PROVIDÊNCIAS. SÓ ENTÃO EXECUTAR.**

Antes da confirmação do registro, são permitidas somente operações técnicas indispensáveis para:

1. localizar ou recuperar o mecanismo de registro;
2. obter o mínimo necessário para representar fielmente o próprio pedido no log;
3. efetuar o registro e verificar sua persistência.

Nenhuma pesquisa substantiva, edição de conteúdo, consulta documental da tarefa, elaboração extensa, publicação ou execução material deve preceder a confirmação do registro.

---

## 12. Recuperação de estado e continuidade

Quando o usuário perguntar **“onde paramos?”**, **“qual é o estado?”**, **“o que falta?”**, **“qual foi meu último pedido?”** ou equivalente, a sequência obrigatória é:

```text
REQUEST_LOG.jsonl
      ↓
STRATEGY_LOG.jsonl
      ↓
PROJECT_STATE.json / STATUS ESPECÍFICO
      ↓
ROADMAP / PLANO DE FASES
      ↓
ARQUIVOS CANÔNICOS DO OBJETO
      ↓
HISTÓRICO GIT COMPROVADO
      ↓
SÓ DEPOIS CONTEXTO DE CONVERSA / MEMÓRIA
```

Para Estratégias Autônomas, a retomada deve reconstruir:

```text
strategy_id
estratégia
plano
fase
gate
estado comprovado
tarefa atual
próximo passo
```

É proibido fazer o usuário retroceder para etapa já concluída sem evidência de perda real.

### 12.1. Padrão obrigatório de resposta de continuidade

Quando o usuário perguntar **“Onde paramos? Qual a Estratégia Autônoma em curso? Qual a Fase dessa Estratégia Autônoma? E qual o Projeto?”** ou formulação equivalente, responder obrigatoriamente nesta ordem:

```text
PROJETO: PRJ-000001 — Classe e Massas
ALIAS: CEM
ESTRATÉGIA AUTÔNOMA: <STRATEGY_CODE> — <STRATEGY_NAME>
FASE: <PHASE_NUMBER>/<PHASE_TOTAL> [<PHASE_CODE>] — <PHASE_NAME>
ESTADO: <estado comprovado>
ONDE PARAMOS: <ponto exato comprovado>
PRÓXIMO PASSO LÓGICO: <próximo passo comprovado pelo plano>
```

Identificador canônico e denominação são obrigatórios para Projeto e Estratégia Autônoma. O alias é apenas mnemônico. Número, total, código hierárquico e denominação são obrigatórios para a Fase.

A resposta deve ser reconstruída a partir das fontes canônicas, jamais apenas da memória conversacional.

---

## 13. Autonomia com verificabilidade

O Modelo de IA deve reduzir trabalho mecânico do usuário sempre que possuir ferramenta autorizada para executar a tarefa diretamente.

Autonomia não autoriza:

- opacidade;
- improvisação estratégica;
- execução sem registro;
- sobrescrita destrutiva desnecessária;
- falsa confirmação de salvamento, commit, push ou publicação.

Quando a ferramenta não permitir uma ação, declarar a limitação claramente e indicar o próximo passo mínimo verificável.

---

## 14. Critério de conclusão

Nenhum trabalho intelectual substancial deve ser declarado definitivamente concluído enquanto seu resultado final não estiver persistido de modo recuperável.

Para trabalhos mantidos neste repositório, o critério preferencial continua sendo:

```text
CONTEÚDO CONCLUÍDO
        ↓
ARQUIVO CANÔNICO ATUALIZADO
        ↓
VERIFICAÇÃO DA GRAVAÇÃO
        ↓
STATUS / MANIFESTO ATUALIZADO
        ↓
EVENTO DE ESTRATÉGIA ATUALIZADO, QUANDO APLICÁVEL
        ↓
COMMIT
        ↓
PUSH / REMOTO CONFIRMADO
        ↓
SEGUNDA CÓPIA, SE MARCO CRÍTICO E TECNICAMENTE APLICÁVEL
```

Publicação, quando aplicável, constitui etapa adicional e distinta.

---

## 15. Regra máxima

> **Nunca obrigar o usuário a pagar novamente, com seu tempo, energia ou recursos, por uma falha de memória, persistência, continuidade, planejamento ou verificação do Modelo de IA.**

Se houver dúvida entre executar e compreender a estratégia, **compreender e registrar primeiro**.

Se houver dúvida entre continuar produzindo e preservar, **preservar primeiro**.

Se houver dúvida entre inferir e verificar, **verificar primeiro**.

Se houver dúvida entre refazer e recuperar, **recuperar primeiro**.

---

## 16. Governança deste documento

Este `AGENTS.md` é documento canônico do projeto.

Alterações que reduzam as garantias deste protocolo exigem decisão expressa do responsável pelo projeto e versionamento identificável.

A ausência de ferramenta específica não suspende os princípios. O agente deve adaptar o procedimento preservando a finalidade: não perder trabalho, não inventar estado, não executar tarefa estrategicamente órfã e não apresentar ação não comprovada como concluída.

A migração para kernel 1.2 foi executada sob a estratégia:

```text
STRAT-CEM-20260917-002
```

Plano:

```text
governanca/estrategia-migracao-agents-kernel-1.2.md
```

---

### 16.1. Padrão público de navegação editorial

Para o Site Classe e Massas, a navegação global de primeiro nível é:

```text
Início · Publicações · Biblioteca · MPT · LAI · Fale Conosco
```

O hub **Publicações** reúne:

```text
Notícias · Artigos · Vídeos · Observatório
```

Regras:
- preservar as URLs históricas `/noticias/`, `/artigos/`, `/videos/` e `/observatorio/`; o agrupamento é de arquitetura de acesso, não migração destrutiva;
- a página `/publicacoes/` deve funcionar como hub autônomo e compreensível sem depender de menu suspenso;
- no mobile, o menu global usa faixa horizontal deliberadamente rolável/deslizante, com os itens sempre visíveis na estrutura e sem overflow horizontal geral da página;
- a Home pode manter identidade tipográfica jornalística própria, mas o título não deve dominar desproporcionalmente a primeira dobra em telas pequenas;
- Notícias, Artigos, Vídeos e Observatório mantêm funções editoriais distintas e não devem ser convertidos em textos duplicados;
- a promoção futura de Vídeos novamente ao primeiro nível exige crescimento funcional que justifique nova decisão arquitetural rastreável.

### 16.2. Navegação horizontal deslizante e semântica visual de cards

A regra abaixo **substitui, para o Classe e Massas, o padrão recolhível introduzido na v2.7**.

#### Menu global
- no mobile, a navegação permanece visível em faixa horizontal rolável/deslizante, reproduzindo o paradigma comprovado em Ações Judiciais e Planejamento Financeiro;
- a rolagem horizontal é confinada ao componente de navegação e não pode criar overflow horizontal geral da página;
- itens não quebram em múltiplas linhas; cada item mantém alvo de toque adequado e o item atual permanece destacado;
- **Publicações** é um item comum de primeiro nível que aponta para o hub `/publicacoes/`;
- Notícias, Artigos, Vídeos e Observatório permanecem agrupados dentro do hub Publicações e não precisam de disclosure/dropdown no menu global;
- é vedado exigir botão **MENU** para revelar a navegação principal deste Site.

#### Cards e hiperlinks
- quando um card representa um único destino, o próprio card deve ser o hiperlink de bloco inteiro;
- cards clicáveis devem possuir superfície, borda ou outro contraste visual que os diferencie claramente de cards meramente informativos;
- a interface não deve depender de botão preto interno do tipo “LER”, “ABRIR” ou equivalente como única pista de navegação;
- hover e foco devem reforçar a condição clicável, sem substituir a semântica do elemento `<a>`;
- cards com múltiplas ações reais não devem ser transformados em um único hiperlink; nesses casos, manter card informativo e links secundários claros;
- botões continuam apropriados para **ações** reais, como `COPIAR MODELO`, envio de formulário ou comandos de interface; não devem ser usados apenas para disfarçar navegação simples.

## 17. Histórico de versões

| Versão | Data | Alteração |
|---|---|---|
| 1.1 | 13/09/2026 | Consolidação das regras de persistência progressiva, write-through, checkpoints, RPO, recuperação e verificação remota. |
| 1.2 | 16/09/2026 | Instituição da vinculação estratégica obrigatória antes de qualquer tarefa ou ação, com referência ao planejamento por fases, fase atual, objetivo/entrega/gate, dependências e próximo passo lógico. |
| 1.3 | 16/09/2026 | Torna obrigatório o registro persistente e auditável de toda estratégia antes de qualquer tarefa substantiva; estabelece a barreira “sem registro, não executar” e define o `PROJECT_STATE.json` como registro mínimo padrão para frentes ativas. |
| 1.4 | 17/09/2026 | Torna explícitos o Plano de Fases para toda estratégia autônoma, o desenvolvimento obrigatório de siglas, a cadeia Sindicato > Federação > Confederação e a informação de registro em toda pausa/checkpoint. |
| 1.5 | 17/09/2026 | Institui confirmação imediata de recebimento antes de processamento potencialmente demorado, para evitar a percepção de travamento durante leitura, análise ou uso de ferramentas. |
| 1.6 | 17/09/2026 | Torna obrigatório registrar persistentemente todos os pedidos no `REQUEST_LOG.jsonl` antes de qualquer processamento; impõe a ordem registro → confirmação → leitura/análise/providências e torna o log a fonte primária para recuperar a sequência e o último pedido. |
| 1.7 | 17/09/2026 | Alterou temporariamente a ordem operacional para informar o usuário antes do registro, com a finalidade de reduzir silêncio inicial. Essa ordem é histórica e foi substituída pela v1.9. |
| 1.8 | 17/09/2026 | Institui o `STRATEGY_LOG.jsonl` append-only e torna obrigatório atribuir `strategy_id` e registrar toda Estratégia Autônoma e seus eventos, com `project_id` padronizado para permitir rastreabilidade e futura agregação entre projetos. |
| 1.9 | 17/09/2026 | Migração controlada para `AGENTS_KERNEL.md` 1.2: restaura como regra vigente a ordem registrar → verificar → informar “Pedido registrado” → informar leitura/análise/providências → executar; preserva por incorporação todas as regras locais válidas da v1.8 e registra `generated_from_kernel: 1.2`. |
| 2.0 | 18/09/2026 | Elimina a lacuna normativa de formatos editoriais: torna obrigatório, para cada texto editorial/publicável, o trio coordenado Markdown + HTML + JSON, define Markdown como fonte textual canônica, impõe sincronização e gate de conclusão e admite exceções somente por decisão expressa, persistente e versionada. |
| 2.1 | 19/09/2026 | Institui governança numérica: código + denominação obrigatórios para Projeto e Estratégia Autônoma; Planos de Fases integralmente numerados; padrão determinístico para respostas de continuidade. |
| 2.2 | 19/09/2026 | Substitui códigos derivados de iniciais pela metodologia universal hierárquica: `PRJ-NNNNNN` para Projetos, `EA-PPPPPP-EEEEEE` para Estratégias Autônomas e `F-PPPPPP-EEEEEE-FFF` para Fases; rebaixa `CEM` a alias mnemônico e preserva identificadores legados por mapeamento. |
| 2.3 | 19/09/2026 | Institui o padrão obrigatório para Modelos públicos: botão `COPIAR MODELO` imediatamente acima do bloco copiável, somente a edição vigente no Site Público e proibição de portões de acesso a edições anteriores. |
| 2.5 | 20/09/2026 | Revoga a triplicidade editorial obrigatória. Markdown permanece fonte textual canônica, HTML permanece publicação e JSON/JSONL passa a ser criado somente quando houver função estruturada real. |
| 2.6 | 22/09/2026 | Agrupa Notícias, Artigos, Vídeos e Observatório no hub Publicações; reduz a densidade do menu global, elimina dependência de rolagem horizontal no mobile e disciplina a escala tipográfica da Home. |
| 2.7 | 22/09/2026 | Torna a navegação efetivamente dinâmica: botão MENU no mobile, menu recolhível, Publicações como disclosure com submenu acessível, Escape para fechamento e fallback sem JavaScript. Regra posteriormente substituída pela v2.8 para este Site. |
| 2.8 | 22/09/2026 | Alinha o Classe e Massas ao padrão AJ/PF: menu horizontal deslizante no mobile, Publicações como hub de primeiro nível e cards de destino único como hiperlinks integrais com diferenciação visual, sem botões pretos de navegação. |\n| 3.0 | 26/09/2026 | Institui índice semântico-factual do acervo, BDTD/IBICT como fonte sistemática de descoberta acadêmica e melhoria contínua proativa com IMPROVEMENT_LOG.jsonl e innovation check. |\n| 3.1 | 26/09/2026 | Institui ponte bidirecional condicional com o Bootstrap do Coordenador Geral para dúvidas de roteamento, repercussão transversal, governança global e candidatos a novo Projeto. |\n| 3.2 | 26/09/2026 | Incorpora a Classificação Universal de Informação por sensibilidade e superfície, com gate antes de persistência/publicação e perfil estruturado do repositório. |
| 3.3 | 26/09/2026 | Incorpora a Arquitetura Universal de Ambientes de Execução e Persistência, separando PRJ/EA/F de Chat, Work, Projeto ChatGPT, Biblioteca e Codex. |

---

## 18. Princípio final

> **O objetivo deste protocolo não é apenas orientar respostas. É garantir que qualquer Modelo de IA consiga entrar no projeto, reconstruir seu estado, recuperar seu histórico, executar a fase correta, preservar o trabalho e continuar sem obrigar o usuário a reconstruir o passado.**


### 16.3. Guias canônicos de interface e arquitetura

As regras públicas de interface e arquitetura do Site são detalhadas em:

```text
SITE_STYLE_GUIDE.md
SITE_ARCHITECTURE.md
```

Esses arquivos integram a fonte normativa do Projeto para qualquer alteração em paleta, tipografia, cards, botões, navegação, rodapés, Mapa do Site, Observatório público e separação entre conteúdo público e artefatos internos.

Em caso de regra visual ou arquitetural legada incompatível com esses guias e com os itens 16.1 e 16.2 deste AGENTS.md, prevalece o padrão mais recente, específico e expressamente versionado pela EA-000001-000026.



### Padrão transversal do botão ENVIAR MENSAGEM

- todo botão público **ENVIAR MENSAGEM** deve incluir a classe `submit-button`;
- `submit-button` é sempre oval/pílula (`border-radius:999px`), nunca retangular;
- a cor da ação permanece específica do Projeto;
- não aplicar essa regra automaticamente a todos os demais botões.

## Pauta editorial interna

O arquivo `governanca/PAUTA_EDITORIAL.md` é o **backlog editorial interno** do projeto para possíveis Artigos futuros.

Regras obrigatórias:

- a pauta é governança interna e **não integra o Site Público**;
- não incluir a pauta, seus estados, prioridades ou itens ainda não publicados em menus, cards, páginas de coleção, Mapa do Site, sitemap, feed ou metadados públicos;
- uma entrada na pauta registra apenas uma hipótese editorial; **não constitui promessa de pesquisa, redação ou publicação**;
- cada item deve registrar, quando possível, identificador, título provisório, pergunta/ângulo, eixo, relação com conteúdo existente, prioridade, estado, densidade e Estratégia Autônoma vinculada;
- antes de pesquisa substantiva, avaliar ao menos relevância, novidade, densidade, disponibilidade de fontes e risco de redundância;
- pauta e Roadmap não são equivalentes: a pauta organiza possibilidades editoriais; o Roadmap e os Planos de Fases governam trabalho efetivamente priorizado;
- quando um item for aprovado para execução, abrir ou vincular Estratégia Autônoma e Plano de Fases antes da pesquisa substantiva;
- quando o artigo for publicado, atualizar o item para `PUBLICADA` e registrar a referência final;
- itens suspensos ou descartados permanecem rastreáveis com motivo suficiente para evitar retrabalho;
- a auditoria de publicação deve verificar que `governanca/PAUTA_EDITORIAL.md` e seus estados internos não vazaram para a camada pública.

Estados canônicos: `IDEIA`, `EM_TRIAGEM`, `APROVADA_PARA_PESQUISA`, `EM_PESQUISA`, `PRONTA_PARA_REDACAO`, `EM_REDACAO`, `PRONTA_PARA_PUBLICACAO`, `PUBLICADA`, `SUSPENSA` e `DESCARTADA`.



## Classificação Universal de Informação

Antes de criar, mover, enviar, fazer upload, commit, publicar ou anexar arquivo persistente, aplicar a política global:

- `/Governanca-Geral-Modelos-IA/CLASSIFICACAO_UNIVERSAL_INFORMACAO.md`;
- `/Governanca-Geral-Modelos-IA/INFORMATION_CLASSIFICATION_POLICY.json`.

Se a Biblioteca não estiver acessível, aplicar obrigatoriamente as regras mínimas abaixo:

1. classificar **sensibilidade**: `S0_PUBLICO`, `S1_INTERNO_NAO_SENSIVEL`, `S2_CONFIDENCIAL`, `S3_ALTAMENTE_SENSIVEL` ou `S4_SEGREDO_CRITICO`;
2. classificar **superfície**: `P0_COFRE_EXTERNO`, `P1_GIT_PRIVADO`, `P2_GIT_PUBLICO_REPOSITORIO` ou `P3_PUBLICO_SITE`;
3. `S2` ou superior nunca pode ser salvo em repositório público nem no Site;
4. documento bruto `S3` permanece em cofre externo por padrão e não deve ser commitado ao Git;
5. `S4` nunca deve ser enviado ao Modelo nem persistido em Git, Biblioteca, chat ou logs;
6. conteúdo só pode descer de classe mediante criação de **derivado sanitizado**; o original mantém sua classificação;
7. mudança de visibilidade do repositório, ativação de Pages ou mudança de destino exige nova classificação.

O arquivo `INFORMATION_HANDLING_PROFILE.json` registra a superfície técnica e os limites deste repositório.

## Índice semântico-factual do acervo

O Projeto mantém `governanca/KNOWLEDGE_INDEX.jsonl`, gerado deterministicamente por `tools/build_knowledge_index.py`.

- consultar o índice antes de varreduras manuais amplas sobre “onde aparece X?”;
- confirmar achados materiais no documento original;
- o índice não replica texto integral e não revoga a política condicional de JSON;
- `governanca/KNOWLEDGE_INDEX_META.json` registra cobertura do índice;
- índice e metadados são governança interna e não conteúdo público.

## Pesquisa acadêmica brasileira — BDTD/IBICT

Para temas compatíveis com produção brasileira de pós-graduação, pesquisar sistematicamente a **Biblioteca Digital Brasileira de Teses e Dissertações (BDTD/IBICT)**. Registrar descritores/data quando substantivo; validar a obra no repositório institucional de origem e por Handle/DOI quando disponível; não tratar presença na BDTD como endosso de qualidade.

## Inovação e aperfeiçoamento proativos

O usuário autorizou sugestões e inovações. A partir desta versão, a autorização é regra operacional permanente:

- oportunidade material identificada deve ser comunicada ao usuário, não apenas percebida internamente;
- registrar a oportunidade em `IMPROVEMENT_LOG.jsonl`;
- distinguir proposta, aprovação, execução e conclusão;
- não expandir silenciosamente o escopo;
- quando aprovada e material, vincular a Estratégia Autônoma e Plano de Fases;
- no fechamento de trabalho substancial, executar **innovation check**: indexar, automatizar, padronizar, reutilizar, simplificar ou aumentar verificabilidade é possível?
