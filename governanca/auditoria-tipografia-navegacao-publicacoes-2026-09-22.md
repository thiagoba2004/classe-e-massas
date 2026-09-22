# Auditoria — tipografia e arquitetura de navegação do Site Classe e Massas

**Estratégia:** EA-000001-000022  
**Data:** 22/09/2026  
**Escopo:** Home, navegação global, hub Publicações e integração das quatro áreas editoriais.

## Resultado

### Tipografia da Home
- regra anterior da Home: até `6.8rem` no desktop e até `5rem` no mobile, com influência de `18vw`;
- regra atual: `clamp(2.8rem, 7vw, 4.6rem)`;
- mobile: `clamp(2.35rem, 11vw, 3.2rem)`;
- identidade serifada e caráter jornalístico preservados;
- texto de apresentação reduzido e mantido legível.

### Navegação global
Primeiro nível implantado:

```text
Início · Publicações · Biblioteca · MPT · LAI · Fale Conosco
```

No mobile:
- `flex-wrap: wrap`;
- `overflow: visible`;
- nenhuma dependência de rolagem horizontal para descobrir itens posteriores.

### Hub Publicações
Criados:
- `publicacoes/index.md`;
- `publicacoes/index.html`.

Subáreas:
- Notícias;
- Artigos;
- Vídeos;
- Observatório.

As URLs históricas das quatro áreas foram preservadas.

### Integração
- `js/main.js` trata Notícias, Artigos, Vídeos, Observatório e o próprio hub como seção `publicacoes`, mantendo **Publicações** ativo no menu global.
- Home e template editorial atualizados.
- Índices de Notícias, Artigos, Vídeos e Observatório apontam para o hub.
- Observatório passou de “Voltar à publicação” para “Voltar a Publicações”.
- `AGENTS.md` atualizado para v2.6 com a arquitetura canônica.

## Verificação
Auditoria de repositório:
- Home contém o menu reduzido;
- hub contém as quatro áreas;
- JS não contém mais Notícias, Artigos, Vídeos e Observatório como itens globais separados;
- CSS móvel usa quebra de linhas e não `overflow-x:auto` no menu;
- regras antigas de título gigante foram substituídas.

GitHub Pages:
- workflow run: **35771021125**;
- commit auditado: `fd690074f80fd49fdac92eae52c4f8294d3e843f`;
- build: **success**;
- deploy: **success**.

A ferramenta de pesquisa pública desta sessão não conseguiu abrir diretamente o domínio GitHub Pages; por isso, a verificação externa foi feita pelo pipeline oficial do GitHub Pages e a verificação estrutural diretamente no repositório, sem representar acesso visual público não realizado.

## Gate
**APROVADO.**
