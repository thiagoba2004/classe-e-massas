#!/usr/bin/env python3

from pathlib import Path
from datetime import date
import html
import re
import unicodedata

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "templates" / "artigo.html"
ARTIGOS = ROOT / "artigos"


def perguntar(campo, padrao=None, obrigatorio=True):
    while True:
        rotulo = campo
        if padrao:
            rotulo += f" [{padrao}]"

        valor = input(f"{rotulo}: ").strip()

        if not valor and padrao:
            return padrao

        if valor or not obrigatorio:
            return valor

        print("Este campo é obrigatório.")


def criar_slug(texto):
    texto = unicodedata.normalize("NFKD", texto)
    texto = texto.encode("ascii", "ignore").decode("ascii")
    texto = texto.lower()
    texto = re.sub(r"[^a-z0-9]+", "-", texto)
    return texto.strip("-")


def escapar(texto):
    return html.escape(texto, quote=True)


def main():
    print()
    print("=" * 58)
    print("        GERADOR DE ARTIGOS — CLASSE E MASSAS")
    print("=" * 58)
    print()

    if not TEMPLATE.exists():
        raise SystemExit(f"ERRO: template não encontrado: {TEMPLATE}")

    titulo = perguntar("Título")
    subtitulo = perguntar("Subtítulo")
    descricao = perguntar(
        "Descrição para buscadores e compartilhamento",
        subtitulo
    )
    kicker = perguntar(
        "Kicker",
        "Campanha Salarial dos Bancários • 2026"
    )
    tipo = perguntar(
        "Tipo do documento",
        "Documento de intervenção e debate"
    )
    hoje = date.today()
    meses = (
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    )
    data_automatica = f"{hoje.day} de {meses[hoje.month - 1]} de {hoje.year}"

    data_publicacao = perguntar("Data", data_automatica)
    ano = perguntar("Ano da pasta", str(hoje.year))

    slug_sugerido = criar_slug(titulo)
    slug = perguntar("Nome do arquivo", slug_sugerido)

    if slug.endswith(".html"):
        slug = slug[:-5]

    slug = criar_slug(slug)

    if not slug:
        raise SystemExit("ERRO: nome de arquivo inválido.")

    apresentacao = perguntar(
        "Parágrafo de apresentação (opcional)",
        obrigatorio=False
    )

    destino_dir = ARTIGOS / ano
    destino_dir.mkdir(parents=True, exist_ok=True)

    destino = destino_dir / f"{slug}.html"

    if destino.exists():
        raise SystemExit(
            f"\nERRO: o arquivo já existe e não será sobrescrito:\n{destino}"
        )

    modelo = TEMPLATE.read_text(encoding="utf-8")

    apresentacao_html = ""
    if apresentacao:
        apresentacao_html = f"<p>{escapar(apresentacao)}</p>"

    substituicoes = {
        "{{TITULO}}": escapar(titulo),
        "{{DESCRICAO}}": escapar(descricao),
        "{{KICKER}}": escapar(kicker),
        "{{SUBTITULO}}": escapar(subtitulo),
        "{{APRESENTACAO}}": apresentacao_html,
        "{{TIPO}}": escapar(tipo),
        "{{DATA}}": escapar(data_publicacao),
        "{{CONTEUDO}}": (
            "<!-- ESCREVA O CONTEÚDO DO ARTIGO A PARTIR DAQUI -->\n\n"
            "<p>Conteúdo do artigo.</p>"
        ),
        "{{ESTILOS_EXTRAS}}": (
            "<!-- Estilos específicos deste artigo podem ser inseridos aqui. -->"
        ),
    }

    for marcador, valor in substituicoes.items():
        modelo = modelo.replace(marcador, valor)

    marcadores_restantes = re.findall(r"\{\{[^{}]+\}\}", modelo)

    if marcadores_restantes:
        raise SystemExit(
            "ERRO: existem marcadores não preenchidos no template: "
            + ", ".join(sorted(set(marcadores_restantes)))
        )

    destino.write_text(modelo, encoding="utf-8")

    print()
    print("=" * 58)
    print("ARTIGO CRIADO COM SUCESSO")
    print("=" * 58)
    print()
    print(f"Arquivo: {destino.relative_to(ROOT)}")
    print()
    print("O arquivo já contém:")
    print("  ✓ estrutura HTML")
    print("  ✓ metadados")
    print("  ✓ identidade do Classe e Massas")
    print("  ✓ CSS principal")
    print("  ✓ JavaScript principal")
    print("  ✓ Cloudflare Web Analytics")
    print()
    print("Agora edite apenas o conteúdo do novo artigo.")
    print()


if __name__ == "__main__":
    main()
