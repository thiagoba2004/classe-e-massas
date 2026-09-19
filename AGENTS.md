# AGENTS.md — Protocolo Canônico de Trabalho dos Modelos de IA

**Projeto:** `CEM — Classe e Massas`  
**Código do Projeto:** `CEM`  
**Denominação do Projeto:** `Classe e Massas`  
**Status:** CANÔNICO  
**Versão:** 2.1  
**Data:** 19/09/2026  
**generated_from_kernel:** `1.3`  
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

## 2. Hierarquia normativa e fonte da verdade

Quando houver dúvida sobre qual regra ou estado prevalece, usar a seguinte ordem:

1. este `AGENTS.md` v2.0 para regras vigentes do projeto;
2. arquivos canônicos específicos do objeto de trabalho;
3. `PROJECT_STATE.json` e manifestos/status específicos para estado corrente;
4. `STRATEGY_LOG.jsonl` para história das Estratégias Autônomas;
5. `REQUEST_LOG.jsonl` para sequência de pedidos;
6. Roadmaps, Planos de Fases e documentos de governança específicos;
7. `AGENTS.md` v1.8 incorporado por referência, para regras locais não substituídas;
8. `AGENTS_KERNEL.md` 1.3, como núcleo universal vigente;
9. histórico Git e commits comprovados;
10. somente depois, contexto de conversa ou memória do Modelo de IA.

Memória, resumo de conversa ou inferência **nunca prevalecem** sobre evidência documental mais recente.

Se houver conflito entre versões anteriores e a v2.0, **a v2.0 prevalece**.

Se houver conflito entre o kernel 1.3 e uma regra local mais rigorosa que não contrarie a finalidade universal do kernel, **a regra local mais rigorosa é preservada**.

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
strategy_id
strategy_name
```

O `strategy_id` é o código estável da estratégia. O `strategy_name` é sua denominação humana inequívoca.

No Classe e Massas, novas estratégias devem seguir:

```text
STRAT-CEM-AAAAMMDD-NNN
```

Toda Estratégia Autônoma deve possuir registro persistente, sequencial e auditável no `STRATEGY_LOG.jsonl` antes da execução substantiva.

> **ESTRATÉGIA AUTÔNOMA NOVA = `strategy_id` NOVO + EVENTO `CREATED` PERSISTIDO ANTES DA EXECUÇÃO SUBSTANTIVA.**

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
PROJECT_NAME
STRATEGY_ID
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

No texto humano, usar obrigatoriamente:

```text
FASE 01/05 (F01) — Registro e delimitação
FASE 02/05 (F02) — ...
FASE 05/05 (F05) — Verificação e fechamento
```

`phase_number` deve ser inteiro sequencial iniciado em 1; `phase_code` deve usar dois algarismos (`F01`, `F02`, ...); `phase_total` deve indicar o total vigente do plano; e `phase_name` deve ser uma denominação humana inequívoca.

É proibido manter rótulos não numerados como “FASE FINAL” ou “FASE DE CONSOLIDAÇÃO” isoladamente. A função pode constar da denominação, mas a posição numérica é obrigatória.

Cada fase deve indicar também estado, objetivo e gate quando aplicável.

A conclusão técnica de uma tarefa não altera automaticamente o estado da fase; o avanço depende do gate correspondente.

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

### 8.2. Formatos canônicos e trio obrigatório para textos editoriais

Salvo decisão específica documentada:

- Markdown (`.md`) — fonte textual canônica para textos humanos, documentação, metodologia, traduções e conteúdo editorial;
- JSON/JSONL — dados estruturados, metadados, representação legível por máquina e interoperabilidade;
- HTML — artefato de publicação;
- PDF/DOCX — formatos derivados de distribuição, apresentação ou protocolo.

Transformação de formato não substitui silenciosamente a fonte da verdade.

#### 8.2.1. Regra dos três artefatos

Todo **texto editorial ou publicável** mantido pelo projeto — incluindo artigos, notícias, editoriais, notas, dossiês, documentos canônicos destinados à publicação e outros conteúdos textuais equivalentes — deve possuir, como regra obrigatória, três artefatos coordenados:

```text
NOME-ESTAVEL.md
NOME-ESTAVEL.html
NOME-ESTAVEL.json
```

As responsabilidades são distintas e complementares:

1. **Markdown (`.md`) — fonte textual canônica.** É o arquivo prioritário para redação, revisão humana, comparação textual e preservação do conteúdo.
2. **HTML (`.html`) — publicação.** É a representação pública ou publicável do texto e deve ser derivável ou verificável contra o Markdown.
3. **JSON (`.json`) — representação estruturada.** Deve conter metadados suficientes para identificar, auditar, comparar e processar o texto por modelos de IA, automações e ferramentas. Deve apontar para os arquivos Markdown e HTML correspondentes e, quando aplicável, representar de forma estruturada seções, referências ou conteúdo necessário à análise automatizada.

O uso do mesmo basename/slug nos três artefatos é obrigatório sempre que tecnicamente possível. Quando a arquitetura exigir nomes diferentes, o vínculo entre eles deve ser explícito no JSON.

#### 8.2.2. Sincronização obrigatória

Alteração material em título, linha fina/subtítulo, autoria, data, corpo, referências, status editorial, slug ou outro dado relevante deve ser refletida nos três artefatos antes de o trabalho ser declarado concluído ou atualizado.

O JSON correspondente deve registrar, no mínimo quando aplicável:

```text
id ou slug
tipo de conteúdo
título
status
data de publicação
data de atualização
caminho da fonte Markdown
caminho do HTML publicado/publicável
referência de versão, commit ou hash quando disponível
```

Não é permitido manter silenciosamente um HTML publicado sem sua fonte Markdown correspondente, nem um texto editorial sem seu JSON correspondente.

#### 8.2.3. Gate de conclusão editorial

Um texto editorial/publicável somente pode atingir estado equivalente a `PRONTO PARA PUBLICAÇÃO`, `PUBLICADO`, `ATUALIZADO` ou `CONCLUÍDO` quando:

- os três artefatos existirem;
- a relação entre eles estiver identificável;
- Markdown e HTML estiverem materialmente coerentes;
- o JSON corresponder à versão vigente;
- a persistência e o versionamento tiverem sido verificados.

Publicar o HTML não sana a ausência do Markdown ou do JSON.

#### 8.2.4. Exceções

Exceção à regra dos três artefatos somente é válida quando houver **decisão específica, expressa, persistente e versionada** que indique:

- o objeto excepcional;
- a razão técnica, jurídica ou arquitetural;
- o formato dispensado;
- a fonte da verdade substitutiva;
- o prazo ou condição de revisão, quando temporária.

Páginas puramente operacionais, índices gerados, CSS, JavaScript, logs, arquivos de dados sem natureza textual editorial e outros artefatos técnicos não são transformados em “texto editorial” apenas por existirem no site.

A ausência histórica de um dos três artefatos é uma **lacuna documental a corrigir**, e não precedente para novas publicações incompletas.

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
PROJETO: CEM — Classe e Massas
ESTRATÉGIA AUTÔNOMA: <STRATEGY_ID> — <STRATEGY_NAME>
FASE: <PHASE_NUMBER>/<PHASE_TOTAL> (<PHASE_CODE>) — <PHASE_NAME>
ESTADO: <estado comprovado>
ONDE PARAMOS: <ponto exato comprovado>
PRÓXIMO PASSO LÓGICO: <próximo passo comprovado pelo plano>
```

Código e denominação são obrigatórios para Projeto e Estratégia Autônoma. Número, total, código e denominação são obrigatórios para a Fase.

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
| 2.1 | 19/09/2026 | Institui governança numérica: `CEM — Classe e Massas` como código + denominação do Projeto; código + denominação obrigatórios para toda Estratégia Autônoma; Planos de Fases integralmente numerados com `phase_number`, `phase_total`, `phase_code` e `phase_name`; e padrão determinístico para respostas de continuidade. |

---

## 18. Princípio final

> **O objetivo deste protocolo não é apenas orientar respostas. É garantir que qualquer Modelo de IA consiga entrar no projeto, reconstruir seu estado, recuperar seu histórico, executar a fase correta, preservar o trabalho e continuar sem obrigar o usuário a reconstruir o passado.**
