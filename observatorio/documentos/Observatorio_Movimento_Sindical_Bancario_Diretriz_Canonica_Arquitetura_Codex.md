# OBSERVATÓRIO DO MOVIMENTO SINDICAL BANCÁRIO

## Diretriz Canônica de Arquitetura, Dados e Execução no Codex

*Complemento e evolução do Documento Canônico de Fundação*

| **Versão**     | 2.0                                                                                  |
|----------------|--------------------------------------------------------------------------------------|
| **Data**       | 7 de setembro de 2026                                                                |
| **Status**     | Diretriz arquitetural aprovada para continuidade do projeto                          |
| **Projeto**    | Classe e Massas / Observatório do Movimento Sindical Bancário                        |
| **Finalidade** | Preservar decisões, orientar o Codex e impedir deriva arquitetural ou epistemológica |

# 1. Função deste documento

Este documento registra as decisões arquiteturais tomadas após a fundação do Observatório do Movimento Sindical Bancário e deve ser tratado como orientação persistente para qualquer modelo de IA, agente de programação ou colaborador que trabalhe no repositório.

Ele não substitui o Documento Canônico de Fundação, Objeto, Método e Programa de Pesquisa. Os dois documentos são complementares: o primeiro fixa missão, objeto, método e programa de pesquisa; este fixa a arquitetura digital, o padrão dos dossiês sindicais, a camada de dados e as regras de execução.

Regra de precedência: nenhuma implementação técnica pode alterar silenciosamente os princípios metodológicos ou epistemológicos do Documento Canônico de Fundação. Mudanças estruturais relevantes exigem decisão explícita e atualização da documentação canônica.

# 2. Decisão de ambiente: Notebook + Codex

A continuidade estrutural do Observatório deve ocorrer preferencialmente no Notebook, utilizando o Codex como ambiente principal de implementação, manutenção, automação, validação e evolução do repositório.

Justificativa: o Observatório deixou de ser apenas uma seção estática do site. Ele passa a combinar publicação web, acervo documental, dados históricos estruturados, geração padronizada de dossiês, validação de esquemas, análises intra-sindicais e comparações inter-sindicais. Esse conjunto caracteriza um projeto de software e dados de complexidade crescente.

- Chat/Projects: contexto, arquitetura, debate metodológico, decisões e documentação.

- Codex no Notebook: implementação, refatoração, scripts, validações, testes, automações e manutenção do repositório.

- Git/GitHub: fonte compartilhada de versionamento e sincronização entre dispositivos.

- Site Classe e Massas: camada pública de publicação dos resultados aprovados.

O Codex deve trabalhar sob versionamento Git e ler as diretrizes persistentes do repositório antes de editar arquivos. Recomenda-se criar, em etapa própria, um AGENTS.md na raiz adequada, resumindo as regras operacionais e apontando para estes documentos canônicos.

# 3. Princípio arquitetural central: três camadas

## 3.1 Fontes documentais

São os documentos originais ou cópias preservadas: estatutos, atas, editais, chapas, resultados eleitorais, teses, resoluções, jornais, boletins, editais de assembleia, atas de assembleia, instrumentos coletivos, documentos de registro sindical, páginas arquivadas e demais evidências.

## 3.2 Dados estruturados

Os fatos extraídos das fontes devem ser registrados em JSON Lines (.jsonl), com esquemas comuns, identificadores estáveis, datas, proveniência e estado documental. Essa camada é a memória computacional do Observatório.

## 3.3 Documentos canônicos e publicação

Os documentos canônicos destinados à leitura humana devem ser HTML. Eles sintetizam e interpretam os dados documentados, preservando rastreabilidade até os registros estruturados e as fontes originais.

Cadeia de rastreabilidade obrigatória: FONTE ORIGINAL → REGISTRO JSONL → DOCUMENTO CANÔNICO HTML → ANÁLISE COMPARATIVA / MAPA / ARTIGO.

# 4. Regra de formatos

| **Camada**                | **Formato principal**             | **Função**                        | **Regra**                                            |
|---------------------------|-----------------------------------|-----------------------------------|------------------------------------------------------|
| Publicação canônica       | .html                             | Leitura humana e publicação web   | Não usar Markdown como formato canônico dos dossiês. |
| Dados históricos          | .jsonl                            | Análise temporal e comparativa    | Mesmo esquema para todos os sindicatos.              |
| Fontes                    | formato original                  | Evidência e preservação           | Nunca sobrescrever versões históricas.               |
| Diretrizes institucionais | .docx + orientação no repositório | Memória arquitetural e governança | Mudanças relevantes devem ser documentadas.          |

# 5. Unidade fundamental: dossiê sindical padronizado

Cada sindicato pesquisado deve possuir um dossiê próprio, mas todos os dossiês devem nascer da mesma arquitetura. O objetivo é permitir leitura individual de uma entidade e, simultaneamente, comparação nacional entre entidades.

Exemplo de estrutura lógica para o Sindicato dos Bancários e Financiários de São Paulo, Osasco e Região:

observatorio/sindicatos/sao-paulo-osasco-regiao/

├── index.html

├── canonicos/

│ ├── identificacao-institucional.html

│ ├── estatuto-social.html

│ ├── base-territorial.html

│ ├── direcao-sindical.html

│ ├── eleicoes.html

│ ├── congressos-e-teses.html

│ └── historia.html

├── dados/

│ ├── identificacao-institucional.jsonl

│ ├── base-territorial.jsonl

│ ├── direcoes.jsonl

│ ├── eleicoes.jsonl

│ ├── congressos.jsonl

│ ├── teses.jsonl

│ ├── assembleias.jsonl

│ ├── negociacoes.jsonl

│ └── publicacoes.jsonl

└── fontes/

├── estatutos/

├── eleicoes/

├── congressos/

├── diretorias/

├── assembleias/

├── negociacoes/

├── publicacoes/

└── base-territorial/

# 6. Documentos canônicos específicos de cada sindicato

- Identificação institucional: nome jurídico, nome político, CNPJ, registro sindical, sede, filiações, abrangência e identificadores.

- Estatuto social: versões históricas, vigência, órgãos, competências, regras eleitorais, assembleares e de representação.

- Base territorial: municípios, categorias abrangidas, alterações históricas e documentação comprobatória.

- Direção sindical: composição por mandato, cargos, dirigentes e competências estatutárias.

- Eleições: cronologia, chapas, regras, eleitorado, participação, resultados, atas e controvérsias documentadas.

- Congressos e teses: congressos, delegações, teses, resoluções, correntes e posições políticas documentadas.

- História: reconstrução cronológica institucional, política, sindical e documental.

Documentos canônicos não substituem as fontes. Devem funcionar como sínteses auditáveis e historicamente versionáveis.

# 7. JSON Lines como espinha dorsal analítica

O JSONL é adotado como formato estrutural preferencial para séries históricas e análises comparativas. Cada linha deve representar uma unidade de observação suficientemente autônoma e conter identificadores que permitam ligação com sindicato, período, fonte e demais entidades.

Os esquemas não podem ser inventados isoladamente por sindicato. São esquemas nacionais do Observatório. O mesmo campo deve ter o mesmo significado em São Paulo, Bahia, Brasília, Rio de Janeiro ou qualquer outro dossiê.

- Identificador estável do sindicato (sindicato_id), independente de mudanças futuras no nome político ou jurídico.

- Datas em formato padronizado e possibilidade explícita de data desconhecida ou aproximada.

- Identificador de fonte (fonte_id) e proveniência obrigatória para afirmações documentais.

- Separação entre dado observado, cálculo derivado, hipótese e interpretação.

- Campos controlados para grau/status documental.

- Preservação de versões e correções sem apagar a história do dado.

- Validação automatizada antes de agregações nacionais.

# 8. Pasta nacional de esquemas e dados consolidados

A raiz do Observatório deve prever uma pasta esquemas/ para contratos de dados e uma pasta dados/ para conjuntos nacionais derivados. Os arquivos locais de cada sindicato permanecem em sindicatos/\<id\>/dados/.

observatorio/

├── esquemas/ \# definição dos contratos e campos JSONL

├── dados/ \# datasets nacionais consolidados/derivados

└── sindicatos/

└── \<sindicato_id\>/dados/ \# registros próprios da entidade

# 9. Gerador canônico de sindicatos

Deve existir uma Pasta Geradora capaz de criar automaticamente um novo dossiê sindical com todas as subpastas e arquivos exigidos pelo padrão do Observatório.

Estrutura proposta:

observatorio/gerador-sindicato/

├── criar-sindicato.sh (ou ferramenta equivalente multiplataforma)

├── templates/

│ ├── index.html

│ ├── canonicos/\*.html

│ └── dados/\*.jsonl

└── documentação de uso

O gerador deve receber ao menos um identificador estável e o nome oficial/político da entidade, criar a estrutura completa, preencher metadados iniciais e recusar sobrescrita de um sindicato já existente.

Objetivo estratégico: eliminar deriva estrutural. Sindicato B, C ou Z deve nascer segundo o mesmo contrato do Sindicato A.

# 10. Análise intra-sindical e inter-sindical

A arquitetura deve servir a dois eixos simultâneos.

## 10.1 Intra-sindical

Reconstruir a evolução de um mesmo sindicato no tempo: estatutos, mudanças territoriais, diretorias, permanência/renovação de dirigentes, eleições, congressos, participação, posições negociais, assembleias e publicações.

## 10.2 Inter-sindical

Comparar sindicatos sob os mesmos conceitos: tamanho da base, sindicalização quando disponível, participação eleitoral/assemblear, composição e renovação de direções, regras estatutárias, filiações, representação política, comportamento negocial e demais variáveis documentáveis.

Nenhuma comparação nacional deve misturar conceitos distintos. Trabalhadores na base territorial, sindicalizados e votantes/participantes são universos diferentes.

# 11. Regras epistemológicas obrigatórias

- Documentar antes de concluir.

- Nunca preencher lacunas com plausibilidade.

- Distinguir hipótese, estimativa, dado provisório e fato comprovado.

- Preservar versões históricas de documentos e dados.

- Registrar proveniência de toda afirmação relevante.

- Ausência de notícia ou documento público não prova descumprimento estatutário.

- Possível descumprimento só deve ser discutido com evidência positiva e análise jurídica.

- Revisões devem corrigir o conhecimento sem apagar a trilha histórica.

# 12. Direito Sindical como método de investigação

O Direito Sindical integra o núcleo metodológico. Constituição, CLT, jurisprudência STF/TST, estatutos, registros sindicais, instrumentos coletivos e regras assembleares devem ser usados para determinar quem representa quem, em qual território, com qual mandato, quem delibera, negocia e assina, e quais competências pertencem a cada órgão ou dirigente.

Matriz de fiscalização estatutária recomendada: Cargo → dirigente → competência estatutária → atos públicos identificados → documentos comprobatórios → período analisado.

Classificações prudenciais: cumprimento documentalmente identificado; cumprimento parcialmente documentado; documentação pública insuficiente para avaliação.

# 13. Mapas nacionais e hipóteses de concentração

O Observatório pretende construir o Mapa do Poder Sindical Bancário (Top 1, Top 3, Top 10 e Top 20) e o Mapa da Representação Política. As estimativas discutidas durante a fundação — por exemplo, concentração aproximada em determinados grupos de sindicatos ou participação reduzida de sindicatos dirigidos por oposições — são hipóteses de pesquisa, não fatos publicados.

Nenhum percentual desse tipo deve ser apresentado como fato antes de definição do denominador nacional, identificação das bases, documentação das fontes e validação dos cálculos.

# 14. Governança para o Codex

- Antes de alterar arquitetura, ler os documentos canônicos e a orientação persistente do repositório.

- Não criar novos formatos ou nomenclaturas quando já existir padrão aprovado.

- Não transformar hipóteses em dados.

- Não alterar esquemas JSONL sem avaliar compatibilidade histórica e comparativa.

- Não sobrescrever fontes ou versões históricas.

- Fazer mudanças estruturais em etapas pequenas, auditáveis e versionadas.

- Executar validações/testes antes de commit quando houver scripts ou dados estruturados.

- Apresentar mudanças relevantes para aprovação humana antes de consolidá-las.

- Manter Git como trilha de auditoria das alterações.

# 15. Estado de transição Android → Notebook

O trabalho realizado no Android/Termux pertence ao mesmo repositório Git Classe e Massas. Tudo que já foi commitado e enviado (push) ao remoto GitHub pode ser recuperado no Notebook por clone ou atualização do repositório.

Atenção: alterações apenas locais no Android não existem ainda no GitHub. No momento desta diretriz, a nova árvore observatorio/ foi criada localmente e o DOCX de fundação foi copiado para observatorio/documentos/, mas essas mudanças precisam ser verificadas, adicionadas ao Git, commitadas e enviadas ao remoto antes da migração segura.

Diretórios vazios não são rastreados pelo Git. Portanto, a simples existência local de subpastas vazias não garante sua presença no GitHub; elas precisam conter arquivos rastreados ou ser recriadas pelo gerador.

# 16. Fluxo de migração recomendado

- No Android: revisar git status e decidir exatamente quais arquivos do Observatório serão preservados.

- Adicionar arquivos necessários, fazer commit e push para origin/main.

- No Notebook: atualizar ou clonar o mesmo repositório a partir do GitHub.

- Confirmar commit/hash e árvore antes de iniciar mudanças no Codex.

- Criar a camada persistente de orientação do Codex (AGENTS.md) apontando para a documentação canônica.

- Projetar e validar esquemas JSONL antes de povoar grandes volumes de dados.

- Implementar o gerador de sindicatos somente depois de congelado o primeiro contrato arquitetural.

- Gerar o primeiro dossiê real como teste de referência e validar a arquitetura antes de escalar ao Top 20.

# 17. Estrutura-alvo conceitual da raiz

observatorio/

├── index.html

├── documentos/

├── metodologia/

├── esquemas/

├── dados/

├── gerador-sindicato/

├── mapas/

├── sindicatos/

├── representacao-politica/

├── direito-sindical/

├── fontes/

├── pesquisas/

└── downloads/

# 18. Critério de sucesso

O Observatório será arquiteturalmente bem-sucedido quando qualquer novo sindicato puder ser incorporado sem improvisação estrutural; qualquer dado comparativo puder ser rastreado até sua fonte; qualquer documento canônico puder ser reconstruído a partir de evidências; e análises históricas nacionais puderem ser executadas sobre dados homogêneos sem apagar as particularidades de cada entidade.

# 19. Decisões que permanecem abertas

- Definição final dos campos e schemas de cada família JSONL.

- Convenção definitiva de fonte_id e demais identificadores.

- Política de versionamento dos dados e documentos canônicos.

- Linguagem/ferramenta final do gerador (shell, Python ou combinação).

- Quais arquivos serão publicados no site e quais permanecerão apenas como infraestrutura de pesquisa.

- Primeiro conjunto de sindicatos do Top 20 após levantamento empírico.

- Procedimento de validação automática e geração dos datasets nacionais.

Esses pontos não devem ser preenchidos por conveniência do agente. Devem ser propostos, discutidos, testados e aprovados.

# 20. Mandato final ao agente de IA

Ao trabalhar neste projeto, trate o Observatório como infraestrutura de pesquisa histórica, jurídica, sindical e computacional de longo prazo. Preserve a distinção entre evidência, dado e interpretação; prefira estruturas comparáveis e auditáveis; não sacrifique memória histórica por conveniência técnica; não faça mudanças silenciosas de arquitetura; e mantenha cada decisão suficientemente documentada para que outro agente, pesquisador ou desenvolvedor possa continuar o trabalho sem depender da memória da conversa que o originou.
