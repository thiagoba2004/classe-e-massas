# Estratégia de Saneamento Residual de Semântica e Publicação — Site Classe e Massas

**Projeto:** PRJ-000001 — Classe e Massas  
**Estratégia:** EA-000001-000027 — Saneamento residual de links, botões e separação público/interno  
**Origem:** auditoria ampliada posterior ao fechamento da EA-000001-000026  
**Data:** 22/09/2026

## Objetivo

Sanar lacunas residuais não cobertas pelos gates anteriores: hiperlinks simples ainda estilizados como botões de ação, resíduos de componentes legados no MPT e exposição pública direta de arquivo canônico interno usado como Linha Editorial.

## Princípios

- botão preenchido somente para ação real: copiar, enviar, confirmar, baixar ou executar comando;
- navegação simples deve usar link textual/contextual, card clicável ou navegação estrutural;
- downloads podem permanecer visualmente como ação;
- a Linha Editorial continua acessível ao público, mas por página editorial pública própria;
- arquivos canônicos internos permanecem fora do GitHub Pages;
- nenhuma correção desta estratégia reabre ou reescreve a EA-000001-000026.

## Plano de Fases

### FASE 01/05 [F-000001-000027-001] — Registro e delimitação residual
Registrar a estratégia, vincular o pedido de continuidade e documentar as lacunas comprovadas.

**Gate:** escopo residual separado do histórico concluído da EA-000001-000026.

### FASE 02/05 [F-000001-000027-002] — Semântica de links e botões
Converter hiperlinks de navegação simples estilizados como botões em links contextuais. Preservar aparência de ação somente em downloads e comandos reais.

**Gate:** nenhum link de navegação simples depende de botão preenchido como pista de acesso.

### FASE 03/05 [F-000001-000027-003] — Separação Linha Editorial pública x documento canônico
Criar página pública de Linha Editorial em `noticias/`, atualizar o acesso no índice de Notícias e excluir `editorial/documentos/` do pipeline público.

**Gate:** Linha Editorial permanece acessível; documento canônico interno deixa de integrar a superfície pública.

### FASE 04/05 [F-000001-000027-004] — Saneamento CSS e auditoria integral
Eliminar regras legadas sem uso relacionadas a botões de navegação e repetir a auditoria das páginas publicáveis, incluindo semântica de links, menu, rodapé, estilos embutidos e responsividade.

**Gate:** nenhuma não conformidade crítica ou alta residual permanece aberta.

### FASE 05/05 [F-000001-000027-005] — Deploy, verificação e fechamento
Versionar, verificar GitHub Pages, registrar relatório residual e sincronizar PROJECT_STATE/REQUEST_LOG/STRATEGY_LOG.

**Gate:** build/deploy success e estado documental coerente.
