# Estratégia — Submenus do Menu Notícias

**ID:** STRAT-CEM-20260917-008  
**Data:** 17/09/2026  
**Status:** EM EXECUÇÃO

## Objetivo

Separar a listagem de matérias jornalísticas dos conteúdos institucionais que hoje aparecem como cards no índice de Notícias, convertendo estes conteúdos em submenus do item global **Notícias**.

## Escopo

Submenus:
1. **Participe da pauta** — aponta para o formulário já existente em `/fale-conosco/`.
2. **Linha editorial** — aponta para a diretriz editorial canônica já existente.
3. **Princípio síntese** — passa a ter página própria sob `/noticias/`.

## Plano de fases

### Fase 1 — Separação editorial
Remover os três cards institucionais de `noticias/index.html`, deixando a página principal dedicada às matérias publicadas.

### Fase 2 — Navegação
Implementar submenu acessível e reutilizável no menu global **Notícias**, via `js/main.js` e `css/style.css`, com funcionamento em desktop e dispositivos móveis.

### Fase 3 — Princípio síntese e validação
Criar página própria para o Princípio síntese; validar links, estado ativo da navegação, responsividade e ausência de regressões.

## Critério de conclusão

- índice de Notícias contém apenas matérias;
- os três conteúdos institucionais estão acessíveis pelo submenu de Notícias;
- nenhuma informação é perdida;
- submenu funciona por teclado, toque e mouse;
- links são válidos e coerentes.
