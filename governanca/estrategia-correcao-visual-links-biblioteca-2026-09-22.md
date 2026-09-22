# Estratégia de Correção Visual dos Links da Biblioteca

**Projeto:** PRJ-000001 — Classe e Massas  
**Estratégia:** EA-000001-000028 — Correção visual dos acessos da Biblioteca  
**Origem:** regressão visual comprovada após EA-000001-000027  
**Data:** 22/09/2026

## Objetivo

Corrigir os acessos editoriais da Biblioteca que ficaram excessivamente claros após a regra global de semântica de links, restaurando uma superfície mais escura derivada da paleta canônica do Classe e Massas sem reintroduzir botões pretos de navegação.

## Plano de Fases

### FASE 01/04 [F-000001-000028-001] — Registro e diagnóstico
Registrar a estratégia e identificar os seletores/classes responsáveis pela regressão.

### FASE 02/04 [F-000001-000028-002] — Correção semântica e visual
Separar os links editoriais da Biblioteca da classe genérica de botão e aplicar superfície navegável canônica.

### FASE 03/04 [F-000001-000028-003] — Auditoria responsiva
Verificar Biblioteca em desktop/mobile por estrutura e CSS, inclusive hover, foco, contraste e ausência de regressão em outros componentes.

### FASE 04/04 [F-000001-000028-004] — Deploy e fechamento
Confirmar GitHub Pages, atualizar estado e encerrar a estratégia.

## Estado final

**CONCLUÍDA — 4/4 fases.**

- links dos rankings deixaram de usar classes `button` e `button secondary`;
- acessos superiores da Biblioteca deixaram de usar a classe genérica `button`;
- `.ranked-link` e `.library-nav-link` usam superfície navegável `#ebe4d8`, hover `#dfd3c3`, borda neutra e acento vermelho;
- mobile permite quebra de linha sem overflow;
- CSS validado com chaves balanceadas;
- GitHub Pages: run **35791589787 — success**.

## Próximo passo

Aguardar validação visual em dispositivo real. Qualquer divergência remanescente deve ser tratada como regressão localizada.
