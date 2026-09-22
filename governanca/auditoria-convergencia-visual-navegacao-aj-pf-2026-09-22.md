# Auditoria — convergência visual e navegacional AJ/PF

**Estratégia:** EA-000001-000024  
**Data:** 22/09/2026

## Referência comparativa

Ações Judiciais e Planejamento Financeiro utilizam navegação móvel horizontal rolável: a faixa de navegação permanece visível, usa `overflow-x:auto`, `flex-wrap:nowrap` e mantém os links como itens não flexíveis.

## Verificações no Classe e Massas

### Navegação
- `js/main.js` não contém mais `menu-toggle`, `nav-disclosure` ou `publicacoes-submenu`;
- o menu gerado possui **Início, Publicações, Biblioteca, MPT, LAI e Fale Conosco**;
- rotas de Notícias, Artigos, Vídeos e Observatório marcam **Publicações** como seção atual;
- no mobile, `css/style.css` usa `overflow-x:auto`, `flex-wrap:nowrap`, rolagem tátil e itens `flex:0 0 auto`;
- o overflow horizontal permanece restrito à navegação;
- o item atual continua destacado;
- **Publicações** permanece um destino próprio de primeiro nível e seu hub continua reunindo as quatro áreas editoriais.

### Cards MPT
- Guia Nacional, Modelo Nacional de Representação e Nota Técnico-Jurídica são links de bloco inteiro;
- cada um possui superfície e borda cromaticamente diferenciadas;
- foram removidos os CTAs pretos redundantes “Ler o Guia”, “Abrir o Modelo” e “Ler a Nota Técnica”;
- o card do caso concreto permanece informativo porque possui múltiplos destinos reais; suas ações são links textuais distintos.

### Norma
- `AGENTS.md` v2.8 substitui, para este Site, a regra recolhível da v2.7;
- o Gerador de Agents foi sincronizado pela EA-000002-000015 / versão 1.17, passando a admitir `HORIZONTAL_SCROLL` ou `COLLAPSIBLE_DISCLOSURE` por decisão arquitetural explícita.

## Deploy

GitHub Pages run **35784291957**  
Commit: `a8964898f0c3365a08f0771c934a685112f4420f`  
Estado: **completed / success**

## Gate

**APROVADO.** A implementação pública está coerente com o padrão solicitado e com a referência AJ/PF.
