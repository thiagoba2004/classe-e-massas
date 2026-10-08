# Auditoria final — piloto local de recuperação lexical

**Estratégia:** EA-000001-000036  
**Projeto:** PRJ-000001 — Classe e Massas  
**Classificação:** S0 público  
**Gate terminal:** `PRJ000001_LEXICAL_RETRIEVAL_PILOT_VERIFIED`

## 1. Resultado executivo

O piloto foi aprovado. A decisão é **adotar a recuperação lexical BM25 exact-first como capacidade local complementar** do projeto Classe e Massas.

O novo mecanismo não substitui `governanca/KNOWLEDGE_INDEX.jsonl`. O índice anterior continua responsável pela descoberta factual e de metadados; o piloto acrescenta recuperação textual por unidades de evidência com proveniência e hashes.

## 2. Escopo efetivamente testado

- 40 documentos Markdown públicos e canônicos;
- 556 unidades de evidência;
- coleções: artigos, notícias, LAI, MPT, Observatório e vídeos;
- exclusão comprovada de governança, logs, pauta editorial, formulários, credenciais, configurações e conteúdo S1+;
- nenhum HTML duplicado foi indexado.

Manifesto do corpus: `15baf0c2f8e10d7ce8d7ae31be3a64586e40f1689de321d619c7bddcfe275408`.

## 3. Implementação auditada

- normalização Unicode NFD, remoção de marcas combinantes e minúsculas;
- tokenização determinística por `[a-z0-9]+(?:[-_.:/][a-z0-9]+)*`;
- buckets exatos por título e caminho/slug antes do ranking;
- BM25 com `k1=1.2` e `b=0.75`;
- ordenação estável e desempate por caminho e sequência;
- proveniência por documento, unidade, cabeçalhos e hashes SHA-256;
- data de geração explícita para reconstrução byte a byte.

## 4. Benchmark

O goldset contém 20 consultas: 14 exact-first, 5 BM25 e 1 negativa.

| Métrica | Resultado | Limiar | Estado |
|---|---:|---:|---|
| Recall@5 | 1,0000 | 1,0000 | passou |
| MRR | 0,9737 | 0,9500 | passou |
| nDCG@5 | 0,9806 | 0,9500 | passou |
| Evidence hit rate | 1,0000 | 1,0000 | passou |
| Exact-first rate | 1,0000 | 1,0000 | passou |
| Negative pass rate | 1,0000 | 1,0000 | passou |

O caso BM25 “mapas trabalho capital relações força” posicionou a fonte esperada em segundo lugar; os demais casos positivos localizaram evidência dentro do corte. Isso explica MRR e nDCG inferiores a 1, sem violar os limiares.

## 5. Integridade e reprodutibilidade

- documentos: IDs únicos e hashes das fontes válidos;
- unidades: IDs únicos, vínculo documental válido e hashes textuais válidos;
- contagens do contrato e do índice reconciliadas;
- duas reconstruções consecutivas produziram bytes idênticos;
- SHA-256 reprodutível:
  - documentos: `967a30ddf0eb17273554c58bd19b66c0d2990e7f354eb951ebac8f49b8e6e4d4`;
  - unidades: `738b7642f3208b1b13b3fd79c608c7bf1c1e52baa243b6e8df51bc7a8c7efa90`;
  - índice: `a4901173343668152370a98e5cc9a6f90cf0dd33226883011acbbbb463466c3c`.

## 6. Limitações

1. O goldset é pequeno e foi construído para este corpus.
2. O piloto avalia recuperação lexical; não compara embeddings, busca híbrida ou geração aumentada.
3. As métricas avaliam caminhos relevantes e presença de evidência, não julgamento editorial do trecho por avaliadores independentes.
4. Não houve alteração da interface pública nem implantação de uma caixa de busca no site.
5. Crescimento substancial do corpus exigirá observar tamanho do índice, tempo de construção e necessidade de fragmentação.

## 7. Decisão e operação

Adoção aprovada no âmbito local, com estas condições:

- reconstruir o índice quando qualquer fonte do manifesto mudar;
- executar `tools/test_lexical_retrieval.py` antes de aceitar uma nova versão;
- bloquear a publicação do índice se integridade, determinismo ou qualquer limiar falhar;
- manter `KNOWLEDGE_INDEX.jsonl` e o índice lexical com responsabilidades distintas;
- não ampliar para embeddings ou arquitetura híbrida sem estratégia própria e nova avaliação.

## 8. Fechamento

Todos os artefatos previstos estão persistidos, o benchmark passou e a decisão de adoção está registrada. O gate `PRJ000001_LEXICAL_RETRIEVAL_PILOT_VERIFIED` está satisfeito.

