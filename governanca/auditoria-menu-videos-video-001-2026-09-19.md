# Auditoria estrutural — Menu Vídeos e Vídeo 001

**Projeto:** PRJ-000001 — Classe e Massas  
**Estratégia:** EA-000001-000021 — Menu Vídeos e primeiro filme cinematográfico  
**Data:** 19/09/2026  
**Estado do audiovisual:** EM PRODUÇÃO

## 1. Menu Vídeos

Criado:
- `videos/index.html`.

Ordem canônica do menu:
1. Início
2. Notícias
3. Artigos
4. Vídeos
5. Observatório
6. Biblioteca
7. MPT
8. LAI
9. Fale Conosco

A ordem foi verificada estaticamente em:
- `index.html`;
- `noticias/index.html`;
- `artigos/index.html`;
- `observatorio/index.html`;
- `biblioteca/index.html`;
- `mpt/index.html`;
- `lai/index.html`;
- `fale-conosco/index.html`.

O arquivo `js/main.js`, responsável por reconstruir o menu global em tempo de execução, também contém o item Vídeos e reconhece `/videos/` como seção própria.

O template `templates/artigo.html` e `404.html` foram atualizados para incluir Vídeos no fallback estático.

## 2. Vídeo 001

Criados:
- `videos/2026/quando-o-cliente-vira-fiscal-do-bancario.md`;
- `videos/2026/quando-o-cliente-vira-fiscal-do-bancario.html`;
- `videos/2026/quando-o-cliente-vira-fiscal-do-bancario.json`;
- `editorial/videos/2026/video-001-fiscalizacao-bancario-cliente.md`;
- `editorial/videos/2026/video-001-prompts-capcut.md`;
- `editorial/videos/2026/video-001-guia-producao-capcut.md`;
- `editorial/videos/2026/pesquisa-ferramenta-video-001.md`.

Verificações:
- página marcada como **EM PRODUÇÃO**;
- não existe elemento `<video>` nem `<iframe>` fingindo audiovisual final;
- menu global possui 9 itens na ordem canônica;
- nenhum ID HTML duplicado detectado na página;
- HTML fecha corretamente;
- metadados JSON registram `audiovisual_final: null`;
- blob SHA do HTML foi sincronizado no JSON;
- fonte editorial do artigo está registrada;
- dramatização ficcional está declarada;
- uso de banco real, pessoa real ou logotipo real está proibido pelo pacote de produção.

## 3. Governança

O AGENTS.md evoluiu para **v2.4** com:
- estados de produção audiovisual;
- distinção entre dramatização e fato documental;
- pacote canônico de produção;
- regras de direitos/licenças;
- proibição de player ou URL fictícia;
- posição permanente do Menu Vídeos.

## 4. Regressão corrigida

Durante a implantação foi identificado em `js/main.js` um componente dinâmico legado que ainda criava o botão **“Copiar pedido”** e o mantinha numa barra com outros elementos, contrariando o padrão vigente de Modelos.

A regressão foi corrigida:
- rótulo alterado para **COPIAR MODELO**;
- botão colocado em bloco próprio imediatamente antes do texto carregado;
- texto continua sendo o único alvo de cópia.

## 5. Ferramenta de produção

Ferramenta-base recomendada: **CapCut**.

Motivos e alternativas estão registrados em:
`editorial/videos/2026/pesquisa-ferramenta-video-001.md`.

## 6. Gate atual

### Estrutura do Site
**SATISFEITO.**

### Roteiro, prompts e guia de produção
**SATISFEITO.**

### Audiovisual final
**PENDENTE.**

O Modelo de IA desta sessão não possui ferramenta de geração de vídeo compatível com a produção final solicitada e não controla uma conta CapCut. Portanto, não pode declarar que o filme foi gerado.

## Próximo passo comprovado

Executar no CapCut as gerações dos oito planos definidos em `video-001-prompts-capcut.md`, montar o filme conforme o roteiro e guia de produção, exportar o arquivo real e então submetê-lo à revisão antes de alterar o estado público para `PUBLICADO`.
