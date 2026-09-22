# Estratégia de Semântica Cromática da Ação Primária

**Projeto:** PRJ-000001 — Classe e Massas  
**Estratégia:** EA-000001-000029 — Semântica cromática da ação primária  
**Origem:** aprovação humana após revisão fundamentada pelo estado da arte de design systems e acessibilidade  
**Data:** 22/09/2026

## Objetivo

Substituir o botão preto residual do formulário Fale Conosco por uma ação primária coerente com a identidade do Classe e Massas e formalizar o papel semântico das cores de ação no sistema visual.

## Regra aprovada

- ação primária real: fundo `#9f2f2f`, texto branco;
- hover/foco da ação primária: `#7f2424`, texto branco;
- navegação editorial: link textual ou superfície de papel escurecida;
- ação secundária: tratamento tonal ou outlined derivado da paleta;
- preto permanece como tinta/estrutura e não como padrão automático de CTA.

## Plano de Fases

### FASE 01/04 [F-000001-000029-001] — Registro e normalização
Registrar a estratégia e atualizar o estado corrente.

### FASE 02/04 [F-000001-000029-002] — Implementação e norma visual
Aplicar o estilo ao botão de envio do Fale Conosco e atualizar o guia visual canônico.

### FASE 03/04 [F-000001-000029-003] — Auditoria semântica e responsiva
Verificar contraste estrutural, estados hover/foco/disabled, seletor restrito ao submit e ausência de regressão nos demais botões/links.

### FASE 04/04 [F-000001-000029-004] — Deploy e fechamento
Confirmar GitHub Pages, atualizar logs/estado e concluir a estratégia.
