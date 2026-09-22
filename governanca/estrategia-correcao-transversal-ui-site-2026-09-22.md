# Estratégia Corretiva Transversal de Interface — Site Classe e Massas

**Projeto:** PRJ-000001 — Classe e Massas  
**Estratégia:** EA-000001-000026 — Correção transversal de interface e arquitetura pública do Site Classe e Massas  
**Origem:** EA-000001-000025 — Auditoria integral de interface e coerência visual  
**Data:** 22/09/2026

## Objetivo

Eliminar as não conformidades sistêmicas identificadas na auditoria integral e consolidar um único sistema público de interface para o Classe e Massas, preservando sua identidade editorial própria e adotando os padrões funcionais comprovados em Ações Judiciais e Planejamento Financeiro sem copiar suas paletas ou linguagens visuais.

## Princípios obrigatórios

- identidade cromática própria: papel, tinta e vermelho;
- diferenciação de hiperlinks por superfícies derivadas da própria paleta, nunca por azul arbitrário;
- navegação simples não deve ser apresentada como botão preto;
- botões preenchidos ficam reservados a ações reais;
- cards clicáveis devem comunicar navegação pelo próprio card;
- títulos devem ser apenas moderadamente maiores que o texto corrente;
- menu global horizontal rolável em telas estreitas;
- Publicações permanece como hub de Notícias, Artigos, Vídeos e Observatório;
- HTML-fonte deve ser semanticamente correto sem depender do JavaScript para corrigir a arquitetura;
- Observatório público apresenta conhecimento, não roadmap, gates ou mecanismos internos;
- artefatos internos não devem integrar a superfície pública do Site.

## Plano de Fases

### FASE 01/08 [F-000001-000026-001] — Registro, arquitetura e guias canônicos
Criar o plano da estratégia, registrar o evento CREATED, atualizar o estado corrente e criar/normalizar `SITE_STYLE_GUIDE.md` e `SITE_ARCHITECTURE.md`.

**Gate:** padrões visuais, semânticos e arquiteturais explicitados antes das correções em massa.

### FASE 02/08 [F-000001-000026-002] — Fundação visual global
Refatorar tokens, escala tipográfica, cards clicáveis/estáticos, botões, navegação global e navegação contextual no CSS global.

**Gate:** nenhum componente global novo depende de cores arbitrárias; títulos e menus passam nos tamanhos-alvo.

### FASE 03/08 [F-000001-000026-003] — Coleções editoriais e semântica de navegação
Converter Notícias, Artigos e Vídeos para o padrão Coleção → Detalhe, com itens/card inteiramente clicáveis, retirando CTAs pretos redundantes.

**Gate:** navegação editorial simples não utiliza botão preenchido.

### FASE 04/08 [F-000001-000026-004] — Menu-fonte, rodapés e Mapa do Site
Sincronizar o menu global no HTML-fonte das páginas públicas, reduzir dependência do JS, criar Mapa do Site e normalizar a navegação auxiliar do rodapé.

**Gate:** fallback sem JavaScript mantém a arquitetura vigente.

### FASE 05/08 [F-000001-000026-005] — Observatório público
Reconstruir a Home do Observatório em torno de síntese, objetos de pesquisa, questões em aberto e acesso ao conhecimento público, removendo roadmap, gates e linguagem interna.

**Gate:** página pública não expõe mecanismos de governança interna.

### FASE 06/08 [F-000001-000026-006] — Legado, CSS embutido e separação público/interno
Reduzir estilos inline, consolidar componentes e estabelecer exclusões comprovadas para artefatos internos/rascunhos no pipeline do GitHub Pages.

**Gate:** artefatos internos têm regra explícita de não publicação e estilos legados críticos deixam de competir com o sistema global.

### FASE 07/08 [F-000001-000026-007] — Auditoria integral responsiva e semântica
Testar todas as famílias de páginas em 360 px, 390 px, 412 px e desktop; verificar menus, títulos, cards, links, botões, overflow e acessibilidade.

**Gate:** nenhuma não conformidade crítica ou alta permanece aberta.

### FASE 08/08 [F-000001-000026-008] — Deploy, verificação e fechamento
Versionar o conjunto final, verificar GitHub Pages, registrar o relatório corretivo e encerrar a estratégia.

**Gate:** build/deploy concluído com sucesso e estado documental sincronizado.

## Estado inicial

FASE 01/08 em execução.

## Próximo passo

Persistir os guias canônicos e, em seguida, iniciar a fundação visual global.
