# Contrato de recuperação lexical — EA-000001-000036

## 1. Finalidade

Este contrato define a representação reprodutível do corpus público usado pelo piloto local de recuperação lexical do projeto Classe e Massas.

## 2. Escopo

- Classificação permitida: `S0_PUBLICO`.
- Fonte canônica: Markdown editorial público.
- Regra de seleção: arquivo Markdown sob `artigos/`, `noticias/`, `lai/`, `mpt/`, `observatorio/` ou `videos/` que possua HTML irmão no snapshot registrado em `F1_BASELINE.json`.
- O HTML irmão não é indexado para evitar duplicidade.
- Governança, logs, pauta editorial, formulários, credenciais, configurações e qualquer conteúdo S1+ ficam excluídos.

## 3. Documento

Cada linha de `RETRIEVAL_DOCUMENTS.jsonl` contém:

- `doc_id`: identificador estável derivado do caminho;
- `sequence`: ordem lexicográfica do corpus;
- `source_path`: caminho Markdown canônico;
- `source_sha256`: hash do conteúdo-fonte;
- `title`: primeiro título H1 do documento, com fallback para o nome do arquivo;
- `unit_count`: número de unidades derivadas;
- `classification`: sempre `S0_PUBLICO`;
- `canonical_format`: sempre `MARKDOWN`.

## 4. Unidade de evidência

Cada linha de `RETRIEVAL_UNITS.jsonl` contém:

- `unit_id`: identificador estável dentro do documento;
- `doc_id` e `sequence`: vínculo e ordem;
- `source_path` e `title`: proveniência legível;
- `heading_path`: hierarquia de títulos ativa;
- `text`: texto editorial preservado, sem marcação ornamental;
- `text_sha256`: hash do texto da unidade;
- `token_count`: comprimento da representação pesquisável;
- `classification`: sempre `S0_PUBLICO`.

Parágrafos consecutivos sob o mesmo caminho de títulos são agrupados até o limite determinístico de 350 tokens. Mudança de título abre nova unidade.

## 5. Normalização e ordenação

- Unicode NFD com remoção de marcas combinantes;
- conversão para minúsculas;
- tokens por `[a-z0-9]+(?:[-_.:/][a-z0-9]+)*`;
- caminhos de entrada, termos e listas serializados em ordem estável;
- JSON canônico para artefatos indexáveis;
- `generated_at` explícito para reconstrução byte a byte.

## 6. Invariantes

1. Nenhum documento sem classificação S0 pode entrar no corpus.
2. Todo documento deve apontar para uma fonte existente cujo SHA-256 coincida.
3. Toda unidade deve apontar para um documento válido e conservar seu próprio SHA-256.
4. IDs de documentos e unidades são únicos.
5. Duas reconstruções com as mesmas entradas e o mesmo `generated_at` devem produzir bytes idênticos.
6. O índice lexical complementa, mas não substitui, `KNOWLEDGE_INDEX.jsonl`.

