# OBSERVATÓRIO CLASSE E MASSAS

## Diretriz Canônica de Arquitetura Documental, Formatos e Fonte de Verdade

**Versão:** 1.1  
**Data:** 12 de setembro de 2026  
**Status:** APROVADO  
**Projeto:** Classe e Massas / Observatório Classe e Massas  
**Natureza:** diretriz metodológica, editorial e computacional permanente

> Pesquisar. Estudar. Compreender. Organizar. Lutar.

## 1. Função deste documento

Esta diretriz estabelece quais formatos de arquivo devem ser utilizados pelo Observatório Classe e Massas, qual função pertence a cada formato e onde reside a fonte oficial de cada tipo de conhecimento produzido pelo projeto.

Seu objetivo é impedir que textos, dados e páginas públicas se multipliquem como versões independentes e contraditórias. A arquitetura deve permitir continuidade por pesquisadores, militantes, modelos de inteligência artificial e agentes de programação sem depender da memória das conversas que originaram cada decisão.

Esta diretriz altera expressamente as disposições anteriores que atribuíam ao DOCX função canônica ou institucional. Preserva, contudo, os princípios já aprovados de rastreabilidade, versionamento, separação entre evidência, dado e interpretação, preservação das fontes e publicação dos resultados no site Classe e Massas.

## 2. Decisão metodológica central

O Observatório adotará três famílias principais de formatos:

1. **Markdown (`.md`)** para documentos canônicos em linguagem humana;
2. **HTML (`.html`)** para publicação no site Classe e Massas;
3. **JSON e JSON Lines (`.json` e `.jsonl`)** para metadados, registros, relações e séries estruturadas.

O formato DOCX deixa de ser formato canônico do Observatório. Poderá existir apenas como legado histórico ou exportação excepcional destinada a uma finalidade externa específica.

A decisão pode ser resumida na seguinte regra:

> **Markdown fixa o texto oficial; JSON e JSONL fixam os dados estruturados; HTML publica os resultados.**

## 3. O que é um documento canônico

Documento canônico é o artefato editorial primário que fixa, em linguagem humana, uma decisão, identidade, objeto, conceito, classificação, método, regra de validação, limite de inferência ou programa de pesquisa do Observatório.

Um documento canônico pode conter:

- texto argumentativo;
- definições e distinções conceituais;
- perguntas de pesquisa;
- critérios de inclusão e exclusão;
- classificações e tipologias;
- tabelas explicativas;
- exemplos de aplicação;
- regras de codificação;
- decisões metodológicas ratificadas;
- referências às fontes;
- relações de precedência;
- histórico de versões.

O documento canônico não se confunde com o banco de dados. Arquivos JSON, JSONL, dicionários de dados, schemas, tabelas, índices e registros observacionais são artefatos estruturados que executam ou documentam o método, mas não substituem a formulação humana que o define.

## 4. Matriz canônica dos formatos

| Formato | Função principal | Condição no sistema | Edição |
|---|---|---|---|
| `.md` | Texto institucional, metodológico e analítico | Fonte canônica textual | Editado diretamente |
| `.html` | Página pública no site Classe e Massas | Representação publicada e derivada | Gerado ou sincronizado a partir do Markdown |
| `.json` | Metadados, catálogos, configurações, entidades e schemas | Fonte canônica de objetos estruturados | Editado ou gerado sob schema |
| `.jsonl` | Registros históricos, eventos e grandes séries | Fonte canônica de observações estruturadas | Acrescido e validado registro a registro |
| `.docx` | Legado ou exportação excepcional | Não canônico | Não utilizado como fonte de atualização |
| `.pdf` | Preservação de fonte ou exportação de leitura | Não canônico, salvo quando for a própria fonte original | Não utilizado como fonte de atualização |
| formato original | Documento recebido de fonte externa | Evidência primária preservada | Imutável; nova versão é novo arquivo |

## 5. Markdown como fonte canônica textual

### 5.1 Função

O Markdown será a fonte oficial dos documentos de fundação, diretrizes, metodologias, programas de pesquisa, dossiês narrativos e demais formulações destinadas à leitura humana.

### 5.2 Razões metodológicas

O Markdown é adotado porque:

- contém texto legível sem depender de programa proprietário;
- pode ser interpretado diretamente por modelos de inteligência artificial;
- permite comparação precisa de alterações no Git;
- favorece revisão humana linha a linha;
- pode ser editado no Termux, no Notebook, no Codex e em editores comuns;
- permite conversão automatizada para HTML;
- reduz códigos ocultos, formatação opaca e extrações defeituosas;
- permanece portátil e recuperável no longo prazo.

### 5.3 Regra de autoridade

Quando houver divergência entre o conteúdo de um arquivo Markdown e sua página HTML derivada, prevalecerá o Markdown da versão validada e publicada no repositório.

Toda mudança de conteúdo deve começar no Markdown. É proibido corrigir apenas o HTML quando a alteração modificar o sentido do documento.

### 5.4 Estrutura mínima

Todo documento canônico em Markdown deverá registrar, no próprio texto ou em metadados JSON relacionados:

- identificador estável;
- título;
- versão;
- data de aprovação ou revisão;
- status;
- função;
- documentos que complementa, altera ou supera;
- histórico das mudanças relevantes.

## 6. HTML como publicação oficial no site

### 6.1 Função

O HTML será a forma pública dos documentos no site Classe e Massas. Deve oferecer leitura acessível, identidade visual, navegação, sumário, referências, conexões com outros documentos e integração com mapas, tabelas e painéis.

### 6.2 Natureza derivada

O HTML não constitui uma segunda fonte textual autônoma. Ele representa publicamente o conteúdo aprovado no Markdown.

Elementos próprios da publicação — cabeçalho, menus, rodapé, classes CSS, metadados sociais, analytics e componentes de navegação — podem existir apenas no HTML ou nos templates do site. O conteúdo substantivo, porém, deve continuar rastreável até o Markdown.

### 6.3 Regra contra divergência

Não será admitida a manutenção manual de dois textos independentes, um em Markdown e outro em HTML. O fluxo de publicação deverá gerar, converter ou verificar o HTML a partir da fonte canônica.

Cada página deverá informar, sempre que possível:

- versão publicada;
- data de atualização;
- identificador do documento;
- situação metodológica dos resultados apresentados.

As fontes Markdown e os dados estruturados permanecem no repositório para versionamento, auditoria e processamento técnico, mas não integram a navegação pública do site. O catálogo e as páginas públicas oferecem somente as versões HTML destinadas à leitura.

## 7. JSON como memória de objetos estruturados

### 7.1 Função

O JSON será utilizado quando o conteúdo puder ser representado como um objeto estruturado ou conjunto limitado de objetos relacionados.

São usos próprios do JSON:

- catálogo dos documentos canônicos;
- metadados editoriais;
- cadastros de organizações, empresas, sindicatos e territórios;
- configurações de geração;
- dicionários de dados;
- schemas de validação;
- índices de fontes;
- relações entre documentos;
- resultados consolidados de tamanho controlável.

### 7.2 Requisitos

Todo conjunto JSON relevante deverá possuir definição de campos, identificadores estáveis, indicação de versão e procedimento de validação. Um campo não poderá assumir sentidos diferentes entre observatórios setoriais sem extensão formalmente documentada.

JSON não deve ser usado para imitar prosa longa. Conceitos, argumentos e justificativas pertencem ao documento Markdown; fatos e relações estruturáveis pertencem ao JSON ou JSONL.

## 8. JSON Lines como memória histórica e comparativa

### 8.1 Função

O JSON Lines, identificado pela extensão `.jsonl`, será utilizado para coleções extensas de registros independentes, especialmente quando houver crescimento contínuo, análise temporal ou comparação nacional.

São usos próprios do JSONL:

- assembleias;
- eleições;
- mandatos e diretorias;
- congressos e delegações;
- negociações coletivas;
- instrumentos coletivos;
- greves e eventos de luta;
- publicações sindicais;
- indicadores por período;
- registros de alterações territoriais;
- relações históricas entre organizações, empresas e grupos econômicos.

### 8.2 Razões para não concentrar tudo em um único JSON

Em JSONL, cada linha constitui uma unidade autônoma. Isso permite acrescentar, validar, comparar, filtrar e corrigir registros sem reescrever um grande arquivo composto por uma única matriz. Também reduz conflitos no Git e facilita processamento por scripts e modelos de inteligência artificial.

### 8.3 Unidade de observação

Cada linha deverá conter, conforme o schema aplicável:

- identificador do registro;
- identificadores das entidades relacionadas;
- período ou data;
- fonte e localização da evidência;
- estado epistemológico;
- data de coleta ou revisão;
- observações metodológicas necessárias.

## 9. Fontes originais

A adoção de Markdown, HTML e JSON não autoriza converter, substituir ou eliminar as fontes externas.

Estatutos, atas, editais, convenções, acordos, balanços, jornais, imagens, gravações, planilhas, páginas arquivadas, decisões judiciais e demais evidências devem ser preservados no formato em que foram obtidos.

Regras permanentes:

- a fonte original não será sobrescrita;
- uma nova versão será armazenada como novo arquivo ou nova versão identificada;
- conversões destinadas à pesquisa serão tratadas como derivados;
- texto extraído por OCR não substituirá a imagem ou o PDF de origem;
- todo dado relevante deverá apontar para a fonte que o sustenta;
- ausência de fonte pública não será preenchida por plausibilidade.

## 10. Cadeia canônica de produção do conhecimento

A cadeia geral do Observatório passa a ser:

```text
FONTE ORIGINAL PRESERVADA
        ↓
REGISTRO E METADADOS — JSON/JSONL
        ↓
DOCUMENTO CANÔNICO — MARKDOWN
        ↓
PUBLICAÇÃO — HTML
        ↓
ANÁLISE, MAPA, PAINEL, DOSSIÊ OU ARTIGO
```

Nem toda fonte produzirá imediatamente todas as camadas. Entretanto, qualquer afirmação pública relevante deverá possuir uma trilha que permita reconstruir sua origem, seu tratamento e sua condição documental.

## 11. Estados epistemológicos

Dados e afirmações deverão ser classificados, quando aplicável, segundo estados controlados:

| Estado | Significado |
|---|---|
| hipótese | proposição que orienta a investigação e não pode ser publicada como constatação |
| estimativa | cálculo dependente de premissas, método e margem de incerteza explícitos |
| provisório | dado documentado ainda sujeito a validação adicional |
| comprovado | afirmação sustentada por fonte adequada ao conteúdo declarado |
| controvertido | situação em que fontes relevantes ou interpretações fundamentadas divergem |
| desconhecido | inexistência de base suficiente; o campo não será preenchido por inferência plausível |

O estado epistemológico pertence ao registro estruturado e deve aparecer na publicação sempre que sua omissão puder induzir o leitor a considerar hipótese ou estimativa como fato.

## 12. Organização recomendada no repositório

```text
observatorio/
├── documentos/
│   ├── canonicos/          # fontes oficiais em Markdown
│   ├── publicados/         # HTML derivado para o site
│   └── legado-docx/        # documentos históricos preservados
├── dados/
│   ├── catalogos/          # JSON
│   ├── entidades/          # JSON
│   └── series/             # JSONL
├── esquemas/               # JSON Schema e dicionários
├── fontes/                 # documentos originais imutáveis
├── templates/              # estrutura visual e conversão para HTML
├── scripts/                # geração, validação e comparação
└── relatorios/             # resultados derivados aprovados
```

Essa árvore é uma orientação conceitual. Sua implementação física deverá respeitar a estrutura já existente no repositório e ser executada por migração documentada, sem apagar caminhos históricos silenciosamente.

## 13. Versionamento e fonte de verdade

O repositório GitHub `thiagoba2004/classe-e-massas` será a fonte compartilhada de versionamento do projeto.

Regras:

1. mudanças substantivas começam no arquivo canônico correspondente;
2. mudanças relevantes recebem commit descritivo;
3. o HTML publicado deve corresponder à versão Markdown aprovada;
4. arquivos JSON e JSONL devem ser validados antes de agregações ou publicação;
5. mudanças de schema exigem avaliação de compatibilidade histórica;
6. fontes originais e versões anteriores não serão eliminadas para simplificar a árvore;
7. toda correção preservará a possibilidade de auditar o estado anterior pelo Git ou pelo acervo histórico;
8. nenhuma conversa com IA será tratada como repositório final de uma decisão.

## 14. Regras para trabalho com inteligência artificial

Ao trabalhar com o Observatório, modelos de IA e agentes deverão:

- ler primeiro os documentos Markdown aplicáveis;
- consultar schemas e dados JSON/JSONL antes de comparar entidades;
- distinguir texto normativo, dado observado, cálculo, hipótese e interpretação;
- não extrair conclusões quantitativas apenas de prosa quando houver dado estruturado;
- não preencher campos desconhecidos com estimativas silenciosas;
- indicar incompatibilidades de conceito, período, território ou denominador;
- manter a rastreabilidade até as fontes;
- propor mudanças estruturais antes de implementá-las;
- atualizar a fonte Markdown antes do HTML substantivo;
- validar JSON e JSONL após qualquer alteração;
- registrar decisões duráveis no repositório, e não apenas na conversa.

## 15. Situação do DOCX e do PDF

### 15.1 Perda da função canônica

DOCX não é adequado como fonte principal do Observatório porque é um pacote binário de arquivos XML, produz diferenças pouco inteligíveis no Git, exige extração para análise, contém formatação e metadados que podem interferir na leitura e dificulta automação transparente.

PDF também não será fonte canônica textual porque privilegia a aparência final, fragmenta frequentemente a extração e não é apropriado para edição ou comparação de versões.

### 15.2 Usos residuais

DOCX ou PDF poderão ser produzidos quando houver finalidade externa concreta, como:

- formulário ou modelo jurídico destinado a preenchimento por terceiros;
- documento para protocolo em sistema que exija determinado formato;
- versão diagramada para impressão;
- arquivo de circulação solicitado por usuário ou entidade;
- preservação de documento recebido originalmente nesses formatos.

Nessas hipóteses, o arquivo será uma exportação ou fonte externa, não a origem da verdade canônica.

### 15.3 Preservação do legado

Os dois documentos canônicos bancários de 7 de setembro de 2026 e quaisquer DOCX já produzidos não serão apagados. Eles registram uma etapa histórica da arquitetura. Após a migração de seu conteúdo para Markdown e HTML, deverão ser classificados como legado e acompanhados de indicação clara de que não constituem a versão ativa.

## 16. Migração dos documentos existentes

A migração seguirá esta ordem:

1. inventariar os documentos existentes e atribuir identificadores estáveis;
2. converter o conteúdo integral para Markdown, preservando títulos, tabelas e relações de precedência;
3. revisar a conversão humana e metodologicamente;
4. registrar metadados e relações em um catálogo JSON;
5. produzir o HTML correspondente segundo o padrão visual do Classe e Massas;
6. verificar equivalência substantiva entre Markdown e HTML;
7. publicar as páginas aprovadas;
8. mover ou classificar os DOCX como legado sem apagar seu histórico;
9. registrar a migração em commit próprio.

Os sete novos documentos aprovados em 11 de setembro de 2026 deverão ser convertidos antes de ingressarem no repositório como documentos canônicos ativos. Seus DOCX poderão ser preservados como registro de elaboração, mas não serão utilizados como fonte futura de atualização.

## 17. Precedência e relação com documentos anteriores

Esta diretriz complementa os documentos de Fundação, Refundação, Observatórios Setoriais e Arquitetura Geral.

Em matéria de formatos, fonte de verdade, fluxo Markdown–HTML, função de JSON/JSONL e condição de DOCX/PDF, esta diretriz prevalece sobre disposições incompatíveis dos documentos anteriores.

Permanecem válidas as regras anteriores sobre:

- objeto e horizonte estratégico;
- independência de classe;
- democracia sindical e soberania das assembleias;
- unidade da classe trabalhadora;
- preservação de fontes;
- rastreabilidade;
- distinção entre fato, hipótese, estimativa e interpretação;
- validação antes da publicação;
- expansão gradual a partir do núcleo bancário;
- aprovação humana de mudanças estruturais.

## 18. Mandato permanente

O Observatório Classe e Massas deverá produzir conhecimento cumulativo, auditável e utilizável pela classe trabalhadora. Sua arquitetura documental deve servir simultaneamente à leitura humana, à análise por inteligência artificial, à comparação histórica, à publicação pública e à ação coletiva.

Nenhuma conveniência momentânea de edição poderá criar múltiplas fontes concorrentes, apagar a memória histórica ou romper a ligação entre documento, dado e evidência.

**Regra final:**

> **Escrever em Markdown. Estruturar em JSON e JSONL. Publicar em HTML. Preservar as fontes. Versionar no Git.**

## 19. Histórico de versões

| Versão | Data | Decisão |
|---|---|---|
| 1.0 | 12/09/2026 | Institui Markdown como fonte canônica textual, HTML como publicação derivada, JSON/JSONL como memória estruturada e DOCX/PDF como legado ou exportação excepcional. |
| 1.1 | 12/09/2026 | Separa a publicação pública em HTML dos arquivos Markdown e JSON mantidos no repositório, retirando estes últimos da navegação do site. |

