# TCM-001 — Protocolo de Tradução Integral, Revisão Humana e Versionamento

**Projeto:** História da Crise Mundial — Curso de Conferências (1923–1924)  
**Versão:** 1.1  
**Data:** 13 de setembro de 2026  
**Status:** ATIVO  
**Regra operacional aprovada:** **TRADUZIR TODO O CORPUS PRIMEIRO; REVISAR E APROVAR INTEGRALMENTE DEPOIS**

---

## 1. Decisão editorial

O TCM-001 não será interrompido para aprovação humana de cada conferência, seção ou decisão terminológica intermediária.

A inteligência artificial produzirá uma **tradução integral de trabalho de todo o corpus elegível**, em português do Brasil. Dúvidas, alternativas, leituras problemáticas e decisões terminológicas permanecerão registradas no glossário e nas notas de trabalho, mas **não bloquearão o avanço para as unidades seguintes**.

Somente depois de concluída a tradução de todas as unidades previstas será aberta a etapa de **REVISÃO HUMANA INTEGRAL**.

## 2. Responsabilidade humana

A aprovação editorial final do conjunto será responsabilidade do **Editor Responsável do Classe e Massas**.

A função é humana e não pode ser delegada integralmente à inteligência artificial. Na etapa de revisão integral, o responsável deverá:

1. confrontar a tradução completa com os originais espanhóis adotados como fonte;
2. verificar a aplicação do glossário e decidir as alternativas ainda abertas;
3. conferir nomes próprios, datas, citações, instituições e referências históricas;
4. revisar fluência e correção do português do Brasil sem reescrever o pensamento do autor;
5. validar notas do tradutor e notas editoriais;
6. confirmar que nenhuma lacuna documental foi preenchida por inferência;
7. verificar a correta distinção entre texto autoral, notas do autor e documentos de terceiros;
8. registrar uma aprovação explícita da **obra como conjunto**.

A identificação nominal do revisor deverá constar nos metadados antes da publicação da versão pública v1.0. Enquanto a aprovação integral não estiver registrada, todo o texto permanecerá marcado como **RASCUNHO INTEGRAL — NÃO APROVADO PARA PUBLICAÇÃO COMO EDIÇÃO REVISADA**.

## 3. Papel da inteligência artificial

A IA poderá:

- produzir o rascunho integral da tradução;
- avançar por todas as conferências sem aguardar aprovação intermediária;
- comparar passagens com o original;
- manter consistência terminológica;
- registrar alternativas de tradução;
- detectar omissões, repetições e possíveis erros de transcrição;
- realizar revisão ortográfica e estilística preliminar;
- preparar o texto completo para a revisão humana.

A IA não poderá:

- aprovar a versão final;
- inventar trechos ausentes;
- transformar notas esquemáticas em discursos completos;
- resolver silenciosamente leitura duvidosa de manuscrito;
- atribuir a Mariátegui texto de terceiro;
- copiar traduções contemporâneas protegidas;
- apresentar o rascunho como edição revisada antes da aprovação humana integral.

## 4. Unidade de revisão

A **unidade de produção** continua sendo cada conferência ou documento, para permitir rastreabilidade documental.

A **unidade de aprovação**, porém, é a obra completa do TCM-001.

Isso significa que cada unidade poderá ter internamente estados de progresso, mas nenhuma delas precisa ser submetida ao Editor Responsável antes de a tradução integral estar concluída.

## 5. Estados do projeto

O fluxo do projeto passa a ser:

- **EM TRADUÇÃO — RASCUNHO PARCIAL** — nem todas as unidades foram traduzidas;
- **RASCUNHO INTEGRAL v0.1** — todas as unidades previstas foram traduzidas, com lacunas documentais corretamente identificadas;
- **CONFRONTO INTEGRAL COM OS ORIGINAIS** — comparação sistemática do conjunto;
- **REVISÃO TERMINOLÓGICA INTEGRAL** — glossário e conceitos harmonizados;
- **REVISÃO DE PORTUGUÊS INTEGRAL** — forma brasileira revisada;
- **REVISÃO HUMANA INTEGRAL** — responsável humano examina a obra completa;
- **CANDIDATO À PUBLICAÇÃO v1.0** — revisão humana encerrada e ajustes finais incorporados;
- **APROVADA v1.0** — aprovação explícita registrada;
- **PUBLICADA v1.0** — edição pública disponível.

## 6. Numeração de versões

### v0.x — trabalho interno

- **v0.1 parcial:** tradução em andamento;
- **v0.1 integral:** primeiro rascunho que contém todas as unidades previstas;
- **v0.2, v0.3...:** confronto, harmonização terminológica e revisão linguística do conjunto;
- nenhuma versão v0.x será apresentada como edição final.

### v1.0 — primeira versão pública integral revisada

Somente poderá ser criada depois da revisão humana integral e da aprovação explícita do conjunto.

### v1.x — correções

Correções posteriores que não alterem substancialmente o texto-base ou o método.

### v2.0 — revisão maior

Usar quando houver novo testemunho textual, alteração importante do texto-base ou retradução substancial.

## 7. Registro mínimo de aprovação integral

Antes da publicação, os metadados gerais do projeto deverão conter:

```json
{
  "revisao_humana_integral": {
    "responsavel": "NOME DO RESPONSÁVEL HUMANO",
    "data": "AAAA-MM-DD",
    "versao_aprovada": "v1.0",
    "escopo": "obra completa",
    "aprovada": true
  }
}
```

Sem `aprovada: true`, nenhuma automação ou página deverá rotular o texto como versão revisada, definitiva ou integralmente aprovada.

## 8. Tratamento das dúvidas durante a tradução

Uma dúvida de tradução não interromperá o fluxo. Ela deverá ser registrada com uma das etiquetas:

- **[DECISÃO PROVISÓRIA]** — solução adotada provisoriamente;
- **[ALTERNATIVA]** — outra solução plausível;
- **[LEITURA DUVIDOSA]** — incerteza do testemunho textual;
- **[N. do T.]** — explicação necessária do tradutor;
- **[LACUNA DOCUMENTAL]** — ausência efetiva no corpus.

Na revisão humana integral, todas as marcações pendentes deverão ser resolvidas ou mantidas de forma editorialmente justificada.

## 9. Materiais de terceiro

Documentos de imprensa ou de terceiros necessários para representar unidades sem texto autoral integral poderão ser traduzidos quando juridicamente elegíveis, mas sempre em seção e rotulagem próprias.

Nunca serão fundidos ao texto de Mariátegui nem apresentados como palavras do autor.

## 10. Registro de alterações

Toda mudança material continuará rastreável por Git. A partir da v1.0, haverá histórico editorial contendo:

- versão anterior;
- versão nova;
- data;
- responsável;
- natureza da alteração;
- trechos ou critérios afetados.

## 11. Publicação

Durante a fase de tradução, o site público poderá informar apenas o **estado e o progresso do projeto**. O rascunho integral não será apresentado como edição aprovada.

A publicação textual da obra como edição das Traduções Classe e Massas ocorrerá somente depois da aprovação humana integral.

---

**Regra final aprovada:** primeiro traduzir integralmente; depois confrontar, revisar e aprovar integralmente. A revisão humana permanece obrigatória, mas deixa de funcionar como barreira entre uma conferência e outra.
