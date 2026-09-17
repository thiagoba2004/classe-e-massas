# AGENTS.md — Protocolo Canônico de Trabalho dos Modelos de IA

**Projeto:** Classe e Massas  
**Status:** CANÔNICO  
**Versão:** 1.4  
**Data:** 17/09/2026  
**Escopo:** todo modelo de IA, agente, assistente ou automação que trabalhe neste repositório ou em seus documentos derivados.

---

## 1. Finalidade

Este documento estabelece regras obrigatórias de continuidade, preservação, rastreabilidade, honestidade operacional e coerência estratégica para qualquer Modelo de IA que trabalhe no projeto **Classe e Massas**.

O objetivo central é impedir que trabalho intelectual substancial exista apenas em uma conversa efêmera, que etapas concluídas sejam posteriormente tratadas como não realizadas, que tarefas sejam executadas sem conexão com a estratégia geral do projeto ou que o usuário seja levado a repetir trabalho já executado por falha de persistência, memória, versionamento, planejamento ou verificação.

**Regra fundamental:**

> **O chat é oficina. O arquivo canônico é a obra. O Git é a memória histórica. O Roadmap organiza a direção do trabalho.**

Nenhum Modelo de IA deve considerar um trabalho relevante protegido enquanto ele existir apenas no contexto da conversa.

Nenhuma tarefa relativa ao projeto deve ser executada como ato isolado: antes da execução, ela deve estar vinculada a uma estratégia, a um planejamento por fases, à fase atual, a uma entrega ou gate e ao próximo passo lógico.

**Toda estratégia deve estar registrada de modo persistente e auditável no repositório antes da execução de qualquer tarefa substantiva a ela vinculada. Conhecer, lembrar, inferir ou declarar uma estratégia no chat não equivale a registrá-la. Sem registro persistente, não executar a tarefa.**

---

## 2. Fonte da verdade

A ordem de precedência para determinar o estado real do projeto é:

1. arquivos canônicos versionados no repositório;
2. manifesto/status do objeto de trabalho;
3. histórico do Git e commits comprovados;
4. arquivos locais ou cópias persistentes verificáveis;
5. somente depois, contexto de conversa e memória do Modelo de IA.

Memória, resumo de conversa ou inferência **nunca prevalecem** sobre evidência documental mais recente.

Quando houver divergência entre memória e repositório, o Modelo de IA deve investigar antes de responder.

---

## 3. Proibição de trabalho substancial apenas no chat

É proibido desenvolver integralmente no chat, sem persistência intermediária, qualquer trabalho que exija esforço relevante para ser reconstruído, incluindo:

- traduções;
- artigos extensos;
- pesquisas;
- documentos canônicos;
- denúncias e peças jurídicas;
- bases de dados;
- levantamentos documentais;
- relatórios;
- glossários;
- transcrições revisadas;
- cronologias;
- análises comparativas;
- código;
- modelos e templates;
- dossiês do Observatório.

Ao iniciar trabalho substancial, o Modelo de IA deve identificar ou criar o arquivo canônico correspondente **antes de acumular grande volume de conteúdo na conversa**.

---

## 4. Persistência progressiva obrigatória

O trabalho deve ser salvo progressivamente, e não apenas ao final.

### 4.1. Checkpoint por unidade lógica

Deve haver checkpoint sempre que ocorrer pelo menos um destes eventos:

- conclusão de uma seção;
- conclusão de um capítulo, conferência ou bloco equivalente;
- avanço substancial de uma tradução;
- consolidação de uma decisão metodológica;
- revisão material do texto;
- inclusão de dados difíceis de reconstruir;
- sessão longa de trabalho;
- mudança de fase do projeto.

### 4.2. Checkpoint temporal

Mesmo sem conclusão de uma unidade lógica, trabalho extenso não deve permanecer por longo período sem persistência.

Se a reconstrução do que já foi feito exigir mais do que alguns minutos, o conteúdo deve ser salvo imediatamente.

### 4.3. Salvamento contínuo obrigatório — write-through

Para trabalhos substanciais, a persistência não é uma etapa posterior ao trabalho: **faz parte do próprio ato de produzir**.

Sempre que o agente gerar um bloco novo que tenha valor autônomo — seção, trecho traduzido, conjunto de dados, revisão relevante, decisão metodológica ou outro conteúdo cuja perda exija reconstrução — deverá, quando possuir ferramenta autorizada, gravá-lo no arquivo canônico **antes de avançar para o próximo bloco substancial**.

A sequência preferencial é:

```text
PRODUZIR BLOCO
      ↓
SALVAR NO ARQUIVO CANÔNICO
      ↓
VERIFICAR A GRAVAÇÃO
      ↓
ATUALIZAR STATUS, QUANDO APLICÁVEL
      ↓
CONTINUAR O TRABALHO
```

O agente não deve acumular capítulos, conferências, grandes traduções ou múltiplas rodadas de revisão apenas na conversa esperando um salvamento futuro.

### 4.4. Orçamento máximo de perda — RPO do projeto

O projeto adota como objetivo de preservação:

> **nenhuma unidade lógica concluída pode depender exclusivamente do chat.**

Na prática, o máximo tolerável de trabalho não persistido é o conteúdo do **bloco corrente ainda não concluído**. Assim que o bloco adquirir forma utilizável, deverá ser salvo.

Quando a ferramenta permitir gravação direta, o objetivo é **RPO próximo de zero para unidades concluídas**: uma falha de conversa não deve apagar uma seção, capítulo, conferência, artigo ou tradução já finalizada.

### 4.5. Salvamento em camadas

Trabalhos de alto custo intelectual devem usar, sempre que tecnicamente possível, quatro camadas de proteção:

```text
CAMADA 1 — arquivo canônico de trabalho
CAMADA 2 — commit Git recuperável
CAMADA 3 — repositório remoto confirmado
CAMADA 4 — segunda cópia independente para marcos críticos
```

A quarta camada poderá ser uma cópia persistente na Biblioteca, armazenamento externo autorizado ou outro repositório adequado. Não é necessário duplicar cada pequena alteração, mas **marcos críticos** — como tradução integral concluída, versão final de denúncia, base consolidada ou documento canônico aprovado — devem possuir segunda cópia quando houver meio disponível.

### 4.6. Barreira de segurança antes de continuar

Se o agente perceber que produziu conteúdo substancial ainda não persistido e dispõe de ferramenta para salvá-lo, deverá **interromper a expansão do trabalho e preservar primeiro**.

Se não dispuser de ferramenta de persistência, deverá avisar claramente que o conteúdo ainda não está protegido e oferecer o menor procedimento necessário para salvá-lo antes de prosseguir por muitas etapas.

A conveniência de continuar escrevendo nunca prevalece sobre a preservação de trabalho já concluído.

### 4.7. Verificação do salvamento

Salvar não significa apenas emitir um comando de gravação. Quando possível, o agente deve confirmar que o conteúdo realmente existe no destino esperado, mediante leitura posterior, SHA, commit, consulta ao arquivo ou outro mecanismo verificável.

**Comando executado sem confirmação não equivale automaticamente a salvamento comprovado.**

---

## 5. Regra especial para traduções

Toda tradução do projeto deverá possuir, desde o início:

```text
obra/
├── traducao.md
├── status.json
└── fontes/
```

A nomenclatura pode variar conforme a arquitetura do projeto, mas as três responsabilidades devem existir:

- **`traducao.md`** — texto traduzido canônico;
- **`status.json`** — estado objetivo da tradução;
- **`fontes/`** — identificação ou preservação das fontes utilizadas, quando juridicamente e tecnicamente possível.

A tradução deve ser escrita progressivamente no arquivo canônico. Não se deve esperar a conclusão integral da obra para salvá-la.

O `status.json` deve registrar, quando aplicável:

```json
{
  "id": "TCM-001",
  "status": "EM_TRADUCAO",
  "ultima_unidade_concluida": null,
  "percentual_estimado": null,
  "revisao": "PENDENTE",
  "ultimo_commit": null,
  "atualizado_em": "AAAA-MM-DD"
}
```

Os valores devem refletir fatos comprovados. Não inventar percentual, unidade concluída ou commit.

Cada unidade concluída da tradução deve ser gravada no `traducao.md` ou em arquivo canônico equivalente **antes de a tradução avançar para a unidade seguinte**, salvo impossibilidade técnica expressamente informada.

Quando a tradução integral estiver concluída, devem existir, antes de qualquer etapa posterior:

1. texto integral persistido;
2. status atualizado para refletir a conclusão;
3. commit correspondente;
4. push remoto confirmado, quando houver acesso;
5. segunda cópia independente, quando tecnicamente disponível para esse marco crítico.

---

## 6. Formatos canônicos

Salvo decisão específica documentada em sentido diferente:

- **Markdown (`.md`)** é o formato canônico para textos humanos, documentos metodológicos, traduções e documentação;
- **JSON/JSONL** é o formato canônico para dados estruturados, metadados, manifestos e interoperabilidade com modelos de IA;
- **HTML** é formato de publicação;
- **PDF/DOCX** são formatos derivados de distribuição, apresentação ou protocolo, e não devem substituir silenciosamente a fonte canônica.

Uma transformação de formato não deve apagar nem substituir a fonte da verdade sem decisão expressa.

---

## 7. Git como memória histórica obrigatória

Conteúdo persistido e relevante deve ser versionado.

Sempre que houver um marco material, deve existir commit correspondente, preferencialmente pequeno, descritivo e recuperável.

Exemplos:

```text
TCM-001: traduz conferências 1 a 4
TCM-001: conclui tradução integral
TCM-001: revisa terminologia e notas
Observatório: consolida metodologia de representação sindical
MPT: atualiza modelo nacional de representação
```

O Modelo de IA **não pode afirmar** que houve commit, push, publicação ou atualização remota sem evidência da operação concluída.

Para trabalhos longos, não se deve concentrar todo o histórico em um único commit final se commits intermediários puderem reduzir materialmente o risco de perda.

---

## 8. Fechamento obrigatório de sessão

Antes de declarar encerrada uma sessão de trabalho substancial, o Modelo de IA deve verificar, conforme as ferramentas disponíveis:

1. arquivo canônico atualizado;
2. manifesto/status atualizado, se aplicável;
3. alterações persistidas;
4. commit realizado ou instrução clara de commit pendente;
5. push confirmado ou indicação explícita de que ainda está pendente;
6. verificação de que o destino contém a versão esperada;
7. segunda cópia de marcos críticos, quando aplicável;
8. estado final resumido em termos verificáveis.

Quando tiver acesso autorizado ao GitHub e a alteração solicitada puder ser realizada diretamente, o agente deve preferir persistir o resultado no repositório em vez de deixar o usuário apenas com conteúdo no chat.

Uma sessão não deve ser encerrada com a expressão “pronto” se o conteúdo ainda estiver apenas na conversa.

---

## 9. Proibição de falsas confirmações

É terminantemente proibido dizer ou insinuar:

- “salvei”;
- “publiquei”;
- “atualizei”;
- “subi para o GitHub”;
- “está preservado”;
- “está no site”;
- “o commit foi feito”;
- “está concluído no repositório”;

sem confirmação técnica correspondente.

Quando a ferramenta não permitir executar uma ação, isso deve ser dito de forma clara. O Modelo de IA deve então fornecer o próximo passo mínimo e verificável, sem representar uma ação não executada como concluída.

---

## 10. Regra de reconstrução de estado

Quando o usuário perguntar **“onde paramos?”**, **“qual é o estado?”**, **“o que falta?”** ou equivalente, o Modelo de IA deve:

1. consultar primeiro as fontes persistentes disponíveis;
2. verificar os arquivos e commits mais recentes relacionados ao objeto;
3. distinguir claramente fato comprovado de lembrança ou hipótese;
4. nunca responder com um estado antigo apenas porque ele aparece em memória ou resumo anterior;
5. se houver conflito entre evidências, apresentar o conflito em vez de escolher arbitrariamente uma versão.

**É proibido fazer o usuário retroceder para uma etapa já concluída sem evidência de que o trabalho realmente se perdeu.**

---

## 11. Recuperação antes de reconstrução

Diante de aparente perda de conteúdo, a ordem obrigatória é:

```text
RECUPERAR → VERIFICAR → RECONSTRUIR SOMENTE O QUE FALTA
```

Antes de refazer trabalho substancial, devem ser investigados, quando disponíveis:

- branch atual;
- histórico de commits;
- arquivos rastreados e não rastreados;
- outras branches;
- reflog/local Git, quando acessível;
- Biblioteca e arquivos persistentes;
- downloads e diretórios de trabalho;
- versões anteriores;
- artefatos gerados;
- trechos recuperáveis de conversas;
- cópias exportadas.

Nunca mandar o usuário refazer uma obra integral antes de esgotar razoavelmente as fontes de recuperação disponíveis.

---

## 12. Preservação antes de operações destrutivas

Antes de substituir, truncar, renomear de forma estrutural ou apagar um arquivo importante, o agente deve avaliar se a operação pode eliminar informação única.

Quando houver risco relevante:

1. registrar o estado atual;
2. preservar versão recuperável pelo Git;
3. somente então executar a alteração.

Não usar comandos destrutivos ou sobrescritas em massa quando uma alteração incremental produzir o mesmo resultado.

---

## 13. Integridade do histórico

Documentos canônicos podem evoluir, mas alterações metodológicas relevantes devem deixar trilha histórica.

Uma versão nova não deve apagar silenciosamente:

- decisões anteriores;
- critérios metodológicos;
- origem de dados;
- estado de uma tradução;
- justificativas de mudanças substantivas.

Quando a alteração modificar uma regra estrutural do projeto, registrar a mudança no próprio documento, no commit ou em mecanismo equivalente de versionamento.

---

## 14. Diferenciar estados de trabalho

O agente deve usar estados inequívocos. Exemplos:

```text
NÃO INICIADO
EM PREPARAÇÃO
EM EXECUÇÃO
EM TRADUÇÃO
TRADUÇÃO INTEGRAL CONCLUÍDA
EM REVISÃO
REVISADO
PRONTO PARA PUBLICAÇÃO
PUBLICADO
ARQUIVADO
```

Não converter automaticamente um estado em outro por inferência.

“Texto produzido no chat” não é sinônimo de “arquivo salvo”.  
“Arquivo salvo” não é sinônimo de “commitado”.  
“Commitado” não é sinônimo de “enviado ao remoto”.  
“Enviado ao remoto” não é sinônimo de “publicado no site”.

Cada afirmação deve corresponder ao estado real.

---

## 15. Relatório mínimo ao usuário

Ao final de uma operação substancial, informar de forma objetiva:

- **a estratégia registrada e o planejamento por fases aos quais a tarefa está vinculada**;
- **onde a estratégia está registrada**;
- **a fase atual**;
- **a entrega, objetivo ou gate que a tarefa ajuda a cumprir**;
- **o que foi alterado**;
- **onde foi salvo**;
- **qual é o estado atual**;
- **se houve verificação do salvamento**;
- **se houve commit**;
- **se houve push/publicação**;
- **se existe segunda cópia do marco crítico**;
- **qual é o próximo passo lógico dentro do planejamento**, se existir.

Evitar respostas vagas como “pronto” quando existirem etapas técnicas distintas.

---

## 16. Autonomia com verificabilidade

O Modelo de IA deve reduzir trabalho mecânico do usuário sempre que possuir ferramenta autorizada para executar a tarefa diretamente.

Porém, autonomia não autoriza opacidade.

Toda ação relevante deve ser verificável, e toda limitação real deve ser explicitada.

O agente não deve transferir ao usuário uma sequência longa de comandos manuais quando puder executar com segurança a operação por ferramenta autorizada.

Autonomia operacional também não autoriza improvisação estratégica: uma tarefa tecnicamente executável continua proibida se sua vinculação à estratégia, à fase e ao gate ainda não estiver estabelecida e registrada.

---

## 17. Continuidade entre conversas e modelos

Nenhum agente deve presumir que a próxima conversa terá acesso ao contexto atual.

Por isso, decisões fundamentais e estado operacional devem estar nos arquivos do projeto.

Um novo Modelo de IA que abra este repositório deve conseguir responder, a partir dos documentos persistentes:

- qual é a arquitetura do projeto;
- qual é a estratégia em vigor;
- onde essa estratégia está registrada;
- qual é o planejamento por fases;
- em qual fase o projeto e o objeto específico estão;
- quais trabalhos estão em andamento;
- qual é a fonte da verdade de cada um;
- qual foi o último marco concluído;
- qual entrega ou gate está sendo perseguido;
- o que permanece pendente;
- qual é o próximo passo lógico;
- como continuar sem repetir trabalho.

Se essas perguntas não puderem ser respondidas, existe dívida documental a ser corrigida antes de abrir novas frentes relevantes.

---

## 18. Regra de não regressão

Ao retomar um projeto, o agente deve trabalhar a partir do **estado mais avançado comprovado**.

É vedado rebaixar um objeto de trabalho para uma fase anterior apenas porque o agente atual desconhece as etapas intermediárias.

Desconhecimento do Modelo de IA não é evidência de inexistência do trabalho.

Quando a informação estiver ausente, o estado correto é **“não comprovado no contexto atual”**, e não uma invenção retroativa.

---

## 19. Critério de conclusão

Nenhum trabalho intelectual substancial deve ser declarado definitivamente concluído enquanto seu resultado final não estiver persistido de modo recuperável.

Para trabalhos mantidos neste repositório, o critério preferencial é:

```text
CONTEÚDO CONCLUÍDO
        ↓
ARQUIVO CANÔNICO ATUALIZADO
        ↓
VERIFICAÇÃO DA GRAVAÇÃO
        ↓
STATUS/MANIFESTO ATUALIZADO
        ↓
COMMIT
        ↓
PUSH
        ↓
VERIFICAÇÃO REMOTA
        ↓
SEGUNDA CÓPIA, SE MARCO CRÍTICO
```

Publicação, quando aplicável, constitui etapa adicional.

A conclusão técnica de uma tarefa não altera por si só o estado de uma fase. O avanço de fase depende do respectivo gate canônico.

---

## 20. Regra máxima

> **Nunca obrigar o usuário a pagar novamente, com seu tempo, energia ou recursos, por uma falha de memória, persistência, continuidade ou planejamento do Modelo de IA.**

Se houver dúvida entre executar e compreender a vinculação estratégica, **compreender a estratégia primeiro**.

Se houver dúvida entre continuar produzindo e preservar o que já foi produzido, **preservar primeiro**.

Se houver dúvida entre inferir e verificar, **verificar primeiro**.

Se houver dúvida entre refazer e recuperar, **recuperar primeiro**.

---

## 21. Aplicação imediata ao Classe e Massas

Este protocolo se aplica, sem exceção, aos seguintes núcleos e objetos do projeto:

- Biblioteca e traduções;
- Observatório do Movimento Sindical Bancário;
- Observatório das Lutas de Classes;
- documentos canônicos;
- artigos e notícias;
- materiais do MPT;
- bases de dados e arquivos estruturados;
- pesquisas documentais;
- site e infraestrutura técnica;
- futuros observatórios, coleções e projetos derivados.

Subdiretórios podem possuir `AGENTS.md` adicionais com regras especializadas. Regras locais podem complementar este documento, mas não devem reduzir as garantias de preservação, rastreabilidade, coerência estratégica e honestidade aqui estabelecidas.

---

## 22. Governança deste documento

Este `AGENTS.md` é um documento canônico do projeto.

Alterações que reduzam as garantias previstas neste protocolo exigem decisão expressa do responsável pelo projeto e devem ser versionadas de forma identificável.

A ausência de ferramenta específica não suspende os princípios deste documento. Nessa hipótese, o agente deve adaptar o procedimento preservando a finalidade: **não perder trabalho, não inventar estado, não executar tarefa estrategicamente órfã e não apresentar como concluída uma ação que não foi comprovadamente executada.**

---

## 23. Protocolo mínimo de segurança operacional

A partir desta versão, todo trabalho relativo ao projeto deverá obedecer ao seguinte ciclo mínimo antes e durante a execução:

```text
CONSULTAR / RECUPERAR A ESTRATÉGIA E O PLANEJAMENTO CANÔNICO
              ↓
CONFIRMAR QUE A ESTRATÉGIA ESTÁ REGISTRADA DE MODO PERSISTENTE E AUDITÁVEL
              ↓
SE NÃO ESTIVER REGISTRADA, REGISTRAR ANTES DE QUALQUER TAREFA SUBSTANTIVA
              ↓
IDENTIFICAR A FASE ATUAL
              ↓
IDENTIFICAR A ENTREGA, OBJETIVO OU GATE
              ↓
IDENTIFICAR O PRÓXIMO PASSO LÓGICO
              ↓
VINCULAR A TAREFA A ESSE ENCADEAMENTO
              ↓
SÓ ENTÃO EXECUTAR
              ↓
ABRIR / IDENTIFICAR O ARQUIVO CANÔNICO
              ↓
PRODUZIR UMA UNIDADE LÓGICA
              ↓
SALVAR IMEDIATAMENTE
              ↓
VERIFICAR O SALVAMENTO
              ↓
ATUALIZAR O STATUS
              ↓
COMMITAR O MARCO RELEVANTE
              ↓
CONFIRMAR O REMOTO
              ↓
SÓ ENTÃO ACUMULAR NOVO TRABALHO SUBSTANCIAL
```

Para marcos críticos, acrescentar uma segunda cópia independente.

Este ciclo é uma **barreira de segurança**, não uma recomendação opcional.

A prioridade operacional do agente é:

> **registrar a estratégia; compreender a estratégia; preservar o trabalho; executar a fase correta; publicar por último.**

---

## 24. Vinculação estratégica obrigatória antes de qualquer tarefa ou ação

### 24.1. Princípio

Nenhuma tarefa, pesquisa, alteração, publicação, coleta, análise, automação, peça, artigo, dossiê, tradução ou ação técnica relativa ao projeto poderá ser executada como atividade isolada.

Antes da primeira ação operacional, o agente deve saber e ser capaz de declarar:

1. **qual estratégia está sendo seguida;**
2. **onde essa estratégia está registrada de modo persistente;**
3. **qual documento de planejamento por fases governa o trabalho;**
4. **qual é a fase atual;**
5. **qual objetivo, entrega ou gate da fase está sendo perseguido;**
6. **por que a tarefa solicitada contribui para esse objetivo, entrega ou gate;**
7. **quais dependências anteriores precisam estar satisfeitas;**
8. **qual é o próximo passo lógico depois da tarefa.**

A execução somente começa depois dessa vinculação **e da confirmação do registro persistente da estratégia**.

### 24.2. Registro prévio obrigatório de toda estratégia

Toda estratégia, seja geral, editorial, investigativa, jurídica, técnica, documental, de tradução, publicação ou qualquer outra frente do projeto, **deve ser registrada antes da execução de qualquer tarefa substantiva a ela vinculada**.

A regra é absoluta:

> **SEM REGISTRO PERSISTENTE DA ESTRATÉGIA, NÃO EXECUTAR NENHUMA TAREFA SUBSTANTIVA.**

Não constituem registro válido, por si sós:

- a memória do Modelo de IA;
- o contexto da conversa;
- um resumo de conversa;
- uma inferência do agente;
- uma explicação verbal ao usuário;
- a mera intenção de registrar depois.

O registro deve existir em arquivo persistente e versionável do projeto. Para frentes ativas, o padrão mínimo é registrar a estratégia no `PROJECT_STATE.json`, no item correspondente, e apontar, quando houver, para o dossiê, plano, roadmap, manifesto ou arquivo canônico que contenha o detalhamento da execução.

O registro mínimo da estratégia deve conter, conforme aplicável:

```text
ESTRATÉGIA:
OBJETIVO:
PLANO / ROADMAP:
FASE ATUAL:
OBJETIVO / ENTREGA / GATE DA FASE:
PRÓXIMO PASSO LÓGICO:
ARQUIVO CANÔNICO OU DOSSIÊ VINCULADO:
STATUS DO REGISTRO:
```

Se uma estratégia nova surgir durante a conversa, o agente deve **interromper a execução**, registrá-la primeiro e verificar a gravação. Somente depois poderá pesquisar, redigir, editar, publicar, coletar dados ou praticar qualquer outra ação substantiva vinculada à estratégia.

Se a estratégia mudar materialmente, o registro deve ser atualizado **antes** da execução da primeira tarefa orientada pela nova estratégia.

As únicas ações permitidas antes do registro são as estritamente necessárias para:

1. recuperar uma estratégia que já possa existir em fonte persistente;
2. verificar qual é o estado real do trabalho;
3. registrar ou atualizar a estratégia e seu planejamento mínimo.

Essas ações são preparatórias de governança e não autorizam iniciar o trabalho substantivo antes da confirmação do registro.

### 24.3. Fonte estratégica padrão

Para o Observatório Classe e Massas, o documento de referência geral é o **`observatorio/documentos/07_Roadmap_do_Observatorio_Classe_e_Massas.md`**, sem prejuízo de roadmaps, planos ou protocolos específicos de cada núcleo ou objeto.

O Roadmap geral define a ordem das fases, suas dependências, entregas e gates. Planos específicos podem detalhar essa estrutura, mas não podem contrariá-la silenciosamente.

### 24.4. Regra em caso de ausência ou dúvida

Se o agente não souber a qual estratégia, fase ou gate a tarefa pertence, **é proibido simplesmente executá-la**.

A ordem obrigatória passa a ser:

```text
RECUPERAR O PLANEJAMENTO EXISTENTE
              ↓
VERIFICAR O ESTADO ATUAL
              ↓
IDENTIFICAR OU FORMULAR A ESTRATÉGIA
              ↓
REGISTRAR A ESTRATÉGIA DE MODO PERSISTENTE
              ↓
VERIFICAR O REGISTRO
              ↓
CLASSIFICAR A TAREFA
              ↓
SE NECESSÁRIO, RECONSTRUIR OU ATUALIZAR O PLANO
              ↓
SÓ ENTÃO EXECUTAR
```

Não localizar imediatamente o vínculo estratégico não transforma a tarefa em “avulsa”. Significa que o contexto estratégico precisa ser recuperado ou formalizado antes da execução.

### 24.5. Proibição de execução estrategicamente órfã

É proibido:

- responder a uma solicitação do projeto apenas porque ela é tecnicamente executável;
- abrir nova frente sem identificar e registrar sua posição no planejamento;
- produzir artigo, pesquisa ou documento sem estratégia previamente registrada;
- coletar dados sem saber a pergunta estratégica ou a fase que exige esses dados;
- publicar material sem compreender sua função na sequência do projeto;
- tratar um achado pontual como fim em si mesmo quando ele pertence a uma investigação ou entrega maior;
- saltar para tarefa posterior porque ela parece interessante, urgente ou fácil, ignorando dependências e gates;
- executar primeiro e “registrar depois”.

### 24.6. Ficha mínima de vinculação estratégica

Antes de iniciar uma nova unidade de trabalho, o agente deverá confirmar que existe registro persistente e atualizar, no arquivo pertinente, quando necessário:

```text
ESTRATÉGIA:
REGISTRO DA ESTRATÉGIA:
PLANO / ROADMAP:
FASE ATUAL:
OBJETIVO / ENTREGA / GATE:
TAREFA ATUAL:
DEPENDÊNCIAS:
RESULTADO ESPERADO:
PRÓXIMO PASSO LÓGICO:
```

**A ficha apenas escrita no chat não satisfaz esta regra.** Ela deve estar refletida em arquivo persistente do repositório, diretamente ou por referência inequívoca a um registro persistente já existente.

Subações meramente instrumentais que pertençam claramente à mesma unidade de trabalho — por exemplo, abrir uma fonte, comparar dois documentos ou salvar o arquivo — herdam a vinculação já estabelecida e não exigem novo registro de estratégia a cada comando. A vinculação e o registro devem ser revistos quando mudar a frente de trabalho, a finalidade, a fase, o gate ou o objeto estratégico.

### 24.7. Relação entre tarefa e fase

Uma tarefa pode:

- **executar diretamente uma entrega da fase;**
- **produzir evidência necessária a um gate;**
- **preparar dependência de fase posterior sem abri-la formalmente;**
- **manter atividade contínua já prevista no Roadmap.**

O agente deve distinguir essas situações e não declarar avanço de fase apenas porque realizou atividade preparatória.

### 24.8. Regra de prioridade

Quando surgirem várias tarefas possíveis, a ordem não será decidida apenas pela novidade da solicitação ou pela facilidade técnica.

A prioridade deve considerar:

1. a estratégia registrada;
2. a fase formalmente em execução;
3. o gate ainda não satisfeito;
4. as dependências que bloqueiam entregas subsequentes;
5. a preservação do trabalho já produzido;
6. a contribuição concreta da tarefa para o encadeamento estratégico.

Urgências reais podem alterar a ordem operacional, mas devem ser registradas como exceção consciente, sem apagar a estratégia de referência.

### 24.9. Regra para retomada de conversa

Ao retomar qualquer frente do Classe e Massas, o agente não deve começar pela última tarefa lembrada isoladamente.

A sequência correta é:

> **registro da estratégia → estratégia → planejamento → fase → gate → estado comprovado → tarefa atual → próximo passo.**

Se o registro não for localizado, o agente deve primeiro recuperar ou reconstruir e registrar a estratégia. Somente depois dessa reconstrução o trabalho deve continuar.

### 24.10. Plano de Fases obrigatório para toda estratégia autônoma

Toda estratégia autônoma, ainda que curta, emergencial, editorial, documental ou destinada apenas a uma mensagem de circulação, deve possuir **Plano de Fases explícito e persistente antes da execução substantiva**.

O Plano de Fases deverá conter, no mínimo:

```text
FASE 1 — registro e delimitação
FASES INTERMEDIÁRIAS — pesquisa, análise, produção ou execução necessárias
FASE DE CONSOLIDAÇÃO — síntese e verificação
FASE FINAL — entrega, publicação, circulação ou fechamento
```

Cada fase deve indicar estado, objetivo e gate quando aplicável. Estratégias autônomas não podem ser tratadas como exceção à disciplina de planejamento do projeto.

### 24.11. Regra obrigatória para siglas e abreviações

Em todo texto produzido para o projeto — artigo, nota, mensagem de WhatsApp, relatório, dossiê, documento jurídico, material de divulgação ou publicação — toda sigla relevante deverá ter seu significado informado **pelo menos uma vez**, preferencialmente na primeira ocorrência.

Exemplo:

> **Acordo Coletivo de Trabalho (ACT)**

Depois de desenvolvida, a sigla poderá ser usada isoladamente no restante do texto. Não publicar texto em que uma sigla material à compreensão apareça sem desenvolvimento em nenhum ponto.

### 24.12. Metodologia única para cadeia institucional sindical

Quando o projeto classificar vínculos de entidades sindicais, deverá aplicar sempre a mesma cadeia:

> **Sindicato > Federação > Confederação**

É obrigatório distinguir:

- filiação formal;
- representação por procuração ou instrumento coletivo;
- participação em comando ou mesa de negociação;
- coordenação conjuntural;
- uso compartilhado de plataforma ou infraestrutura.

Nenhuma dessas situações substitui automaticamente outra. Quando um nível da cadeia não existir, não for aplicável ou não puder ser confirmado documentalmente, isso deverá ser informado expressamente, sem preenchimento por inferência.

### 24.13. Informação de registro em toda pausa ou atualização

Em toda pausa, checkpoint ou atualização intermediária comunicada ao usuário, o agente deverá informar explicitamente se o estado produzido até aquele momento **foi ou não foi registrado de modo persistente**.

Quando registrado, deverá indicar, sempre que possível, o arquivo ou mecanismo de persistência. Quando ainda não registrado, deverá dizer isso claramente e priorizar o salvamento antes de acumular novo trabalho substancial.

A mera afirmação de que algo foi “anotado” não substitui a verificação técnica exigida por este protocolo.

---

## 25. Histórico de versões

| Versão | Data | Alteração |
|---|---|---|
| 1.1 | 13/09/2026 | Consolidação das regras de persistência progressiva, write-through, checkpoints, RPO, recuperação e verificação remota. |
| 1.2 | 16/09/2026 | Instituição da vinculação estratégica obrigatória antes de qualquer tarefa ou ação, com referência ao planejamento por fases, fase atual, objetivo/entrega/gate, dependências e próximo passo lógico. |
| 1.3 | 16/09/2026 | Torna obrigatório o registro persistente e auditável de toda estratégia antes de qualquer tarefa substantiva; estabelece a barreira “sem registro, não executar” e define o `PROJECT_STATE.json` como registro mínimo padrão para frentes ativas. |
| 1.4 | 17/09/2026 | Torna explícitos o Plano de Fases para toda estratégia autônoma, o desenvolvimento obrigatório de siglas, a cadeia Sindicato > Federação > Confederação e a informação de registro em toda pausa/checkpoint. |
