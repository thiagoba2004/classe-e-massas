# Auditoria final — Sistema de UI Design do Classe e Massas

**Estratégia:** STRAT-CEM-20260917-010  
**Data:** 18/09/2026  
**Status:** CONCLUÍDA

## 1. Escopo

Auditoria final representativa após as nove fases do redesenho, cobrindo:

- Home;
- Notícias e Artigos;
- Observatório e documentos canônicos;
- Biblioteca;
- MPT;
- LAI;
- Fale Conosco;
- página 404;
- CSS global e JavaScript global.

## 2. Validações realizadas

Foram conferidos:

- viewport responsivo;
- carregamento de `css/style.css`;
- carregamento de `main.js`;
- navegação global e estado ativo;
- larguras de índice e de leitura;
- ausência de CSS dinâmico injetado por JavaScript;
- ausência de CSS local redundante em LAI, MPT, Fale Conosco e notícia auditada;
- skip link e navegação por teclado;
- tabelas e blocos `pre` em telas estreitas;
- formulários e estados ARIA;
- integridade de fechamento HTML;
- hierarquia visual dos documentos canônicos autônomos.

## 3. Regressões encontradas e corrigidas

### 3.1. Página 404
A página estava praticamente sem o sistema visual. Foi reconstruída com viewport, CSS global, cabeçalho, navegação, ações e `main.js`.

### 3.2. Confirmação do Fale Conosco
`fale-conosco/recebido.html` ainda continha CSS local. As regras foram migradas para `css/style.css`, preservando protocolo, confirmação, detalhes técnicos e comportamento JavaScript.

### 3.3. Documentos canônicos do Observatório
A hierarquia havia ficado invertida: o título principal do documento aparecia menor que os `h1` das seções. O tema autônomo foi corrigido para:

- título principal maior, serifado;
- seções `h1` internas menores, em sans serif e caixa alta;
- escala móvel correspondente.

## 4. Exceções intencionais

Os documentos HTML autônomos do Observatório mantêm dois blocos `<style>` por razões distintas:

1. o primeiro é o CSS técnico gerado pelo Pandoc, necessário para elementos como colunas, listas de tarefas e matemática;
2. o segundo é o tema visual autônomo do Classe e Massas.

Isso não é tratado como duplicação indevida.

## 5. Estado final

O site passa a operar com:

- design tokens globais;
- cabeçalho e navegação responsivos;
- tipografia e ritmo editorial padronizados;
- componentes canônicos;
- índices e páginas de leitura harmonizados;
- camada mobile e de acessibilidade;
- CSS global consolidado;
- exceções autônomas explicitamente documentadas.

## 6. Regra pós-estratégia

Novas páginas e alterações de interface devem reutilizar os componentes e tokens existentes em `css/style.css`.

Evitar:

- criar novos blocos `<style>` em páginas que carregam o CSS global;
- injetar CSS por JavaScript;
- criar variações locais de botão, card, nota, grid, formulário ou navegação quando já existir componente canônico;
- reintroduzir submenus móveis ou menus empilhados na Home.

Qualquer exceção deve ser justificada pela necessidade funcional do documento ou seção.
