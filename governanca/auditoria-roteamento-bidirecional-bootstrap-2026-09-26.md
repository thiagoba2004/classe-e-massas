# Auditoria — EA-000001-000033 — Roteamento bidirecional com o Bootstrap

**Data:** 26/09/2026  
**Resultado:** APROVADO

## Gates

- [x] AGENTS local contém ponteiro explícito para `/Governanca-Geral-Modelos-IA/00_BOOTSTRAP_COORDENADOR_GERAL.md`;
- [x] consulta ao Bootstrap é condicional, não aplicada mecanicamente a pedidos inequivocamente locais;
- [x] regra anti-loop explicitada;
- [x] ausência de acesso à Biblioteca não autoriza invenção do conteúdo global;
- [x] governança global permanece externa ao repositório e não foi duplicada;


## Fluxos verificados

1. entrada global → Bootstrap → Projeto/Gerador;
2. entrada direta por Projeto/Gerador → AGENTS local → Bootstrap apenas quando houver dúvida de roteamento, repercussão transversal, governança global ou potencial de novo Projeto;
3. após a classificação, o AGENTS local reassume o trabalho, evitando circularidade.

## Conclusão

A ponte reduz o risco de um Modelo iniciar diretamente em um repositório e ignorar a metagovernança, sem impor o custo de carregar a governança global em tarefas locais.
