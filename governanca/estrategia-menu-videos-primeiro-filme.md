# Estratégia Autônoma EA-000001-000021 — Menu Vídeos e primeiro filme cinematográfico

**Projeto:** PRJ-000001 — Classe e Massas  
**Origem:** REQ-20260919-024  
**Escopo:** arquitetura pública do Site / audiovisual / primeiro vídeo do Projeto.

## Objetivo

Criar o Menu **Vídeos** como nova área estrutural do Site Classe e Massas, definir um padrão audiovisual coerente com a identidade de jornal operário contemporâneo e preparar o primeiro vídeo realista, com linguagem cinematográfica, sobre o caso da fiscalização pública da produtividade do bancário por cliente.

O primeiro vídeo deve derivar do artigo publicado:
`artigos/2026/quando-o-cliente-vira-fiscal-do-trabalhador.html`.

## Princípios audiovisuais

1. Realismo social contemporâneo, sem estética publicitária corporativa.
2. Fotografia cinematográfica sóbria, naturalista e documental.
3. Personagens ficcionais; não representar pessoas reais sem autorização.
4. Não reproduzir logotipos ou identidade de banco real na dramatização.
5. Diferenciar claramente dramatização ficcional, fatos/documentos e análise editorial.
6. Não dramatizar como fato aquilo que não esteja documentalmente comprovado.
7. Priorizar cenas curtas, coerência de personagem, continuidade espacial e legibilidade em celular.
8. Todo vídeo deve possuir roteiro, plano de cenas, prompts, ficha técnica, fontes e estado de produção versionados.

## Plano de Fases

### FASE 01/06 [F-000001-000021-001] — Registro e pesquisa de ferramenta
Pesquisar ferramentas gratuitas atuais para geração de vídeo realista/cinematográfico, verificando limites relevantes para publicação.

### FASE 02/06 [F-000001-000021-002] — Arquitetura do Menu Vídeos
Criar `videos/index.html`, definir padrão de cards, estados (EM PRODUÇÃO / PUBLICADO), metadados e integração ao menu global.

### FASE 03/06 [F-000001-000021-003] — Roteiro e linguagem cinematográfica do vídeo 001
Criar argumento, roteiro, narração, estrutura temporal, plano de cenas e direção de fotografia.

### FASE 04/06 [F-000001-000021-004] — Pacote de geração
Produzir prompts por plano/cena, referências de continuidade, instruções de som, legendas e montagem para uso na ferramenta escolhida.

### FASE 05/06 [F-000001-000021-005] — Implantação estrutural
Propagar o item Vídeos ao menu global das páginas públicas aplicáveis e publicar a página do vídeo 001 em estado compatível com a produção real.

### FASE 06/06 [F-000001-000021-006] — Auditoria e fechamento
Auditar navegação, metadados, links, acessibilidade e integridade; o vídeo só poderá ser marcado PUBLICADO após existir arquivo/URL real do audiovisual final.

## Regra de verdade operacional

Enquanto o arquivo audiovisual final não existir, a página do vídeo 001 deve permanecer **EM PRODUÇÃO**. É proibido criar player falso, URL fictícia ou afirmar que um vídeo foi gerado quando apenas roteiro/prompts existirem.
