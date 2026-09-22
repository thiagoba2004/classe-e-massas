# Arquitetura Pública do Site — Classe e Massas

## Objetivo

Definir a estrutura pública canônica do Site Classe e Massas e separar navegação editorial, conteúdo público e governança interna.

## Menu global canônico

1. **Início**
2. **Publicações**
3. **Biblioteca**
4. **MPT**
5. **LAI**
6. **Fale Conosco**

O menu global deve permanecer semanticamente presente no HTML-fonte. JavaScript pode acrescentar acessibilidade e comportamento, mas não deve ser necessário para corrigir a arquitetura.

## Publicações

`/publicacoes/` é o hub editorial que reúne:

- `/noticias/` — atualidade, apuração e documentos;
- `/artigos/` — análise, interpretação e intervenção;
- `/videos/` — produção audiovisual;
- `/observatorio/` — pesquisa cumulativa e sínteses públicas.

Essas áreas não são itens autônomos do menu global.

## Biblioteca

`/biblioteca/` organiza leitura, autores, traduções, formação e acervo de estudo.

## MPT

`/mpt/` reúne guias, modelos e materiais relacionados ao Ministério Público do Trabalho. Navegação para um destino único deve preferir card clicável ou link editorial; botões ficam reservados a ações.

## LAI

`/lai/` funciona como central pública de pedidos e modelos de Lei de Acesso à Informação. Modelos mantêm botão **COPIAR MODELO** imediatamente acima do texto copiável.

## Fale Conosco

`/fale-conosco/` reúne contato e participação. Envio de formulário é ação real e pode usar botão preenchido.

## Mapa do Site

Criar `/mapa-do-site/` como índice de navegação auxiliar e referenciá-lo no rodapé público.

## Rodapé

O rodapé deve conter, no mínimo:
- identificação do projeto;
- link para Mapa do Site;
- quando aplicável, link para Fale Conosco.

Não deve expor arquivos de governança.

## Observatório público

A Home do Observatório é uma página editorial de conhecimento. Deve mostrar:
- escopo;
- objetos de observação;
- sínteses disponíveis;
- perguntas em aberto;
- fontes e produtos públicos.

Devem permanecer fora da superfície pública:
- roadmap;
- gates;
- fases internas;
- arquivos de estratégia;
- logs;
- PROJECT_STATE;
- instruções de produção;
- referências a Markdown/JSON como processo interno.

## Conteúdo público x interno

### Público
- Homes e índices editoriais;
- notícias;
- artigos;
- vídeos publicados ou claramente marcados como em produção;
- modelos e guias destinados ao visitante;
- páginas de síntese do Observatório;
- Mapa do Site.

### Interno
- `AGENTS.md`;
- `PROJECT_STATE.json`;
- `REQUEST_LOG.jsonl`;
- `STRATEGY_LOG.jsonl`;
- `governanca/`;
- rascunhos editoriais;
- planos de fases;
- relatórios de auditoria;
- documentos canônicos de produção não destinados ao visitante.

O pipeline de publicação deve excluir a camada interna por configuração comprovada, não apenas por ausência de links.

## Padrão Coleção → Detalhe

Listagens com um único destino por item devem usar o item/card inteiro como hiperlink. Evitar a composição:
`título não clicável + resumo + botão Ler/Ver/Acessar`.

## Responsividade

- menu global horizontal rolável em telas estreitas;
- navegação contextual horizontal rolável quando necessário;
- nenhuma pilha de grandes caixas de menu no mobile;
- títulos em escala moderada;
- ausência de overflow estrutural.

## Fonte da verdade

Este arquivo define a arquitetura pública. Mudanças estruturais de menu, hub, rodapé ou superfície pública devem atualizá-lo antes ou junto da implementação.
