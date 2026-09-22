# EA-000001-000022 — Revisão da tipografia e arquitetura de navegação do Site Classe e Massas

**Status:** CONCLUÍDA  
**Origem:** REQ-20260922-001.

## Objetivo
Reavaliar a escala tipográfica da Home e a navegação global do Site Classe e Massas, reduzindo excesso visual em telas móveis e alinhando a camada editorial ao padrão de hub Publicações adotado no Gerador.

## Plano de Fases
1. **FASE 01/04 [F-000001-000022-001] — Diagnóstico do estado atual** — CONCLUÍDA.
2. **FASE 02/04 [F-000001-000022-002] — Decisão arquitetural e especificação** — CONCLUÍDA.
3. **FASE 03/04 [F-000001-000022-003] — Implementação pública e sincronização normativa** — CONCLUÍDA.
4. **FASE 04/04 [F-000001-000022-004] — Auditoria responsiva, navegação e deploy** — CONCLUÍDA.

## Diagnóstico comprovado
- A Home usa `.home-main h1{font-size:clamp(3.4rem,10vw,6.8rem)}`.
- Em telas de até 700 px, a regra sobe a influência relativa para `clamp(3.1rem,18vw,5rem)`, produzindo título muito dominante no celular.
- O menu móvel usa faixa horizontal com `overflow-x:auto`, o que torna itens posteriores parcialmente ocultos e exige rolagem lateral.
- O menu global expõe separadamente Notícias, Artigos, Vídeos e Observatório.
- O Gerador 1.15 recomenda, para Sites editoriais densos, um hub global **Publicações** com subáreas Notícias, Artigos e Observatório; a decisão de incluir Vídeos deve considerar sua função editorial e a densidade do menu.

## Gate da Fase 02
Definir:
1. escala tipográfica alvo da Home;
2. itens de primeiro nível;
3. escopo de Publicações;
4. comportamento móvel sem depender de descoberta por rolagem horizontal.

## Especificação implementada
- Home: título reduzido para escala responsiva contida, preservando identidade jornalística.
- Mobile: menu global quebra em linhas e não depende de rolagem horizontal.
- Primeiro nível: Início · Publicações · Biblioteca · MPT · LAI · Fale Conosco.
- Publicações: Notícias · Artigos · Vídeos · Observatório.
- URLs editoriais históricas preservadas.
- AGENTS atualizado para v2.6.

## Fechamento

Auditoria aprovada. Home com escala tipográfica contida; Publicações implantado como hub de Notícias, Artigos, Vídeos e Observatório; menu móvel sem dependência de rolagem horizontal; URLs históricas preservadas; AGENTS v2.6; GitHub Pages run `35771021125` com build e deploy em success.
