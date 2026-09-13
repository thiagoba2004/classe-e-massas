# TCM-001 — Protocolo de Revisão Humana e Versionamento

**Projeto:** História da Crise Mundial — Curso de Conferências (1923–1924)  
**Versão:** 1.0  
**Data:** 13 de setembro de 2026  
**Status:** ATIVO

---

## 1. Responsabilidade humana

A revisão humana final de cada unidade será responsabilidade do **Editor Responsável do Classe e Massas**.

A função é humana e não pode ser delegada integralmente a inteligência artificial. Antes de uma unidade ser publicada como tradução revisada, o responsável deverá:

1. confrontar o texto traduzido com o original espanhol adotado como fonte;
2. verificar termos do glossário e justificar exceções;
3. conferir nomes próprios, datas, citações, instituições e referências históricas;
4. revisar fluência e correção do português do Brasil sem reescrever o pensamento do autor;
5. validar notas do tradutor e notas editoriais;
6. confirmar que nenhuma lacuna foi preenchida por inferência;
7. registrar aprovação explícita da versão.

A identificação nominal do revisor deverá constar nos metadados antes da publicação de uma versão pública final. Enquanto o nome não estiver registrado, versões de trabalho poderão existir no repositório, mas permanecerão marcadas como **NÃO APROVADAS PARA PUBLICAÇÃO COMO EDIÇÃO REVISADA**.

## 2. Papel da inteligência artificial

A IA poderá auxiliar em:

- rascunho inicial de tradução;
- comparação frase a frase;
- consistência terminológica;
- levantamento de variantes;
- revisão ortográfica e estilística;
- detecção de omissões ou repetições.

A IA não poderá:

- aprovar a versão final;
- inventar trechos ausentes;
- resolver silenciosamente leitura duvidosa de manuscrito;
- substituir decisão editorial em divergência textual;
- atribuir a Mariátegui texto de terceiro;
- remover ambiguidades reais do original sem registro.

## 3. Estados de cada unidade

Cada conferência ou documento traduzido deverá usar um dos estados:

- **FONTE IDENTIFICADA** — testemunho textual definido;
- **RASCUNHO v0.x** — tradução inicial em andamento;
- **CONFRONTO COM ORIGINAL** — comparação integral linha a linha;
- **REVISÃO TERMINOLÓGICA** — glossário e conceitos revisados;
- **REVISÃO DE PORTUGUÊS** — forma brasileira revisada;
- **REVISÃO HUMANA FINAL** — responsável humano conferindo a versão candidata;
- **APROVADA** — versão liberada para publicação;
- **PUBLICADA** — versão disponível na edição pública.

## 4. Numeração de versões

### v0.x — trabalho interno

- v0.1: primeiro rascunho integral da unidade;
- v0.2, v0.3...: revisões de confronto, terminologia e português;
- nenhuma versão v0.x será apresentada como edição final.

### v1.0 — primeira versão pública revisada

Só poderá ser criada quando a revisão humana final estiver registrada.

### v1.x — correções

Correções posteriores que não alterem substancialmente o texto-base ou o método.

### v2.0 — revisão maior

Usar quando houver novo testemunho textual, alteração importante do texto-base ou retradução substancial.

## 5. Registro mínimo de aprovação

Antes da publicação, os metadados da unidade deverão conter:

```json
{
  "revisao_humana": {
    "responsavel": "NOME DO RESPONSÁVEL HUMANO",
    "data": "AAAA-MM-DD",
    "versao_aprovada": "v1.0",
    "aprovada": true
  }
}
```

Sem `aprovada: true`, nenhuma automação ou página deverá rotular o texto como versão revisada ou definitiva.

## 6. Registro de alterações

Toda mudança material deverá ser rastreável por Git e, a partir da v1.0, por um histórico editorial contendo:

- versão anterior;
- versão nova;
- data;
- responsável;
- natureza da alteração;
- trechos ou critérios afetados.

## 7. Publicação por unidades

O projeto poderá publicar conferências individualmente depois de aprovadas, mas a obra completa somente receberá o selo **TRADUÇÃO INTEGRAL v1.0** quando todas as unidades previstas estiverem concluídas e quando lacunas documentais estiverem claramente identificadas.

## 8. Bloqueio editorial

A existência de um rascunho no repositório não equivale a aprovação editorial. O HTML público deverá distinguir de forma visível:

- tradução em desenvolvimento;
- versão revisada;
- documento incompleto;
- nota ou fragmento autoral;
- material de terceiro.

---

**Regra final:** nenhuma velocidade de produção, inclusive com IA, substitui o ato humano de confrontar a tradução com o original e assumir responsabilidade editorial pela versão publicada.
