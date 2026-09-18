document.documentElement.classList.add("js");

(() => {
  const pathname = window.location.pathname;
  const projectMarker = "/classe-e-massas/";
  const base = pathname.includes(projectMarker) ? projectMarker : "/";

  const main = document.querySelector("main");
  if (main) {
    if (!main.id) main.id = "conteudo-principal";
    main.setAttribute("tabindex", "-1");

    if (!document.querySelector(".skip-link")) {
      const skip = document.createElement("a");
      skip.className = "skip-link";
      skip.href = `#${main.id}`;
      skip.textContent = "Pular para o conteúdo principal";
      skip.addEventListener("click", event => {
        event.preventDefault();
        main.focus({ preventScroll: true });
        main.scrollIntoView({ block: "start" });
      });
      document.body.prepend(skip);
    }
  }

  const nav = document.querySelector("header .nav");
  if (nav) {
    if (!nav.hasAttribute("aria-label")) {
      nav.setAttribute("aria-label", "Navegação principal");
    }
    const items = [
      { label: "Início", href: base, section: "home" },
      { label: "Notícias", href: `${base}noticias/`, section: "noticias" },
      { label: "Artigos", href: `${base}artigos/`, section: "artigos" },
      { label: "Observatório", href: `${base}observatorio/`, section: "observatorio" },
      { label: "Biblioteca", href: `${base}biblioteca/`, section: "biblioteca" },
      { label: "MPT", href: `${base}mpt/`, section: "mpt" },
      { label: "LAI", href: `${base}lai/`, section: "lai" },
      { label: "Fale Conosco", href: `${base}fale-conosco/`, section: "fale-conosco" }
    ];

    const currentSection = pathname.includes("/noticias/")
      ? "noticias"
      : pathname.includes("/artigos/")
        ? "artigos"
        : pathname.includes("/observatorio/")
          ? "observatorio"
          : pathname.includes("/biblioteca/")
            ? "biblioteca"
            : pathname.includes("/mpt/")
              ? "mpt"
              : pathname.includes("/lai/")
                ? "lai"
                : pathname.includes("/fale-conosco/")
                  ? "fale-conosco"
                  : "home";

    nav.classList.add("global-nav");
    nav.innerHTML = items.map(item => {
      const current = item.section === currentSection ? ' aria-current="page"' : "";
      return `<a href="${item.href}"${current}>${item.label}</a>`;
    }).join("");

    const currentLink = nav.querySelector('[aria-current="page"]');
    const centerCurrentLink = () => {
      if (!currentLink || window.innerWidth > 700) return;
      const target = currentLink.offsetLeft - (nav.clientWidth - currentLink.offsetWidth) / 2;
      nav.scrollLeft = Math.max(0, target);
    };

    requestAnimationFrame(centerCurrentLink);
    window.addEventListener("resize", centerCurrentLink, { passive: true });
  }

  const portugueseVersions = new Map([
    [
      "https://www.marxists.org/history/international/iwma/documents/1864/rules.htm",
      "https://www.marxists.org/portugues/marx/1871/10/24.htm"
    ],
    [
      "https://www.marxists.org/archive/luxemburg/1918/russian-revolution/ch06.htm",
      "https://www.marxists.org/portugues/luxemburgo/1918/mes/40.pdf"
    ],
    [
      "https://www.marxists.org/archive/gramsci/1919/06/workers-democracy.htm",
      "https://www.marxists.org/portugues/gramsci/1919/06/21.htm"
    ],
    [
      "https://www.marxists.org/archive/trotsky/1936/revbet/ch05.htm",
      "https://www.marxists.org/portugues/trotsky/1936/revolucaotraida/index.htm"
    ],
    [
      "https://www.marxists.org/reference/archive/mao/selected-works/volume-1/mswv1_7.htm",
      "https://www.marxists.org/portugues/mao/1933/08/20.htm"
    ]
  ]);

  document.querySelectorAll("a[href]").forEach(link => {
    const translated = portugueseVersions.get(link.href);
    if (translated) {
      link.href = translated;
      link.dataset.language = "pt";
      link.title = "Versão em português";
    }
  });

  const laiArticle = "/artigos/2026/ano-eleitoral-aumento-real-banco-do-brasil.html";
  if (pathname.endsWith(laiArticle)) {
    const article = document.querySelector("main article");
    const nextHeading = article
      ? [...article.querySelectorAll("h2")].find(h => h.textContent.trim().startsWith("19."))
      : null;

    if (article && nextHeading && !document.getElementById("modelos-lai-no-artigo")) {
      const models = [
        ["Banco do Brasil", `${base}lai/banco-do-brasil.html`],
        ["MGI / SEST / CGPAR", `${base}lai/sest-cgpar.html`],
        ["Advocacia-Geral da União — AGU", `${base}lai/agu.html`],
        ["Ministério da Fazenda / PGFN", `${base}lai/ministerio-fazenda.html`],
        ["Tribunal Superior Eleitoral — TSE", `${base}lai/tse.html`],
        ["Tribunal de Contas da União — TCU", `${base}lai/tcu.html`],
        ["Procuradoria-Geral do Estado de São Paulo — PGE-SP", `${base}lai/pge-sp.html`],
        ["Outras estatais federais — modelo comparativo", `${base}lai/estatais-federais.html`]
      ];

      const style = document.createElement("style");
      style.id = "modelos-lai-artigo-style";
      style.textContent = `
        #modelos-lai-no-artigo{margin:34px 0 48px;padding:26px 0;border-top:2px solid currentColor;border-bottom:2px solid currentColor}
        #modelos-lai-no-artigo h3{font-size:1.35rem;margin:0 0 12px}
        #modelos-lai-no-artigo .lai-intro{line-height:1.7;margin-bottom:22px}
        #modelos-lai-no-artigo details{margin:12px 0;border:1px solid rgba(127,127,127,.35);border-radius:10px;overflow:hidden}
        #modelos-lai-no-artigo summary{cursor:pointer;padding:16px 18px;font-weight:800;line-height:1.35;background:rgba(127,127,127,.08)}
        #modelos-lai-no-artigo .lai-model-body{padding:18px}
        #modelos-lai-no-artigo pre{white-space:pre-wrap;overflow-wrap:anywhere;font:inherit;font-size:.94rem;line-height:1.58;margin:16px 0 0;padding:18px;border:1px solid rgba(127,127,127,.28);border-radius:8px;background:rgba(127,127,127,.06)}
        #modelos-lai-no-artigo .lai-actions{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
        #modelos-lai-no-artigo button,#modelos-lai-no-artigo a.lai-link{font:inherit;font-weight:800;padding:9px 13px;border:2px solid currentColor;border-radius:7px;background:transparent;color:inherit;text-decoration:none;cursor:pointer}
        #modelos-lai-no-artigo .lai-status{font-size:.92rem;opacity:.75}
        @media(max-width:700px){#modelos-lai-no-artigo .lai-model-body{padding:14px}#modelos-lai-no-artigo pre{padding:14px;font-size:.9rem}}
      `;
      document.head.appendChild(style);

      const section = document.createElement("section");
      section.id = "modelos-lai-no-artigo";

      const title = document.createElement("h3");
      title.textContent = "MODELOS COMPLETOS DE PEDIDOS DE ACESSO À INFORMAÇÃO";
      section.appendChild(title);

      const intro = document.createElement("p");
      intro.className = "lai-intro";
      intro.innerHTML = `Os modelos abaixo integram esta investigação. Eles foram redigidos para pedir <strong>documentos e registros preexistentes</strong>, evitando transformar a LAI em consulta jurídica abstrata. Abra o destinatário desejado, revise seus dados de identificação e copie o pedido. A <a href="${base}lai/">Central LAI</a> permanece disponível como versão independente.`;
      section.appendChild(intro);

      models.forEach(([label, url], modelIndex) => {
        const details = document.createElement("details");
        const summary = document.createElement("summary");
        summary.textContent = label;
        details.appendChild(summary);

        const body = document.createElement("div");
        body.className = "lai-model-body";
        const actions = document.createElement("div");
        actions.className = "lai-actions";

        const copy = document.createElement("button");
        copy.type = "button";
        copy.textContent = "Copiar pedido";
        copy.disabled = true;

        const open = document.createElement("a");
        open.className = "lai-link";
        open.href = url;
        open.textContent = "Abrir página própria";

        const status = document.createElement("span");
        status.className = "lai-status";
        status.id = `lai-model-status-${modelIndex}`;
        status.setAttribute("role", "status");
        status.setAttribute("aria-live", "polite");
        status.textContent = "Carregando modelo…";
        copy.setAttribute("aria-describedby", status.id);

        const pre = document.createElement("pre");
        pre.textContent = "Carregando modelo…";

        actions.append(copy, open, status);
        body.append(actions, pre);
        details.appendChild(body);
        section.appendChild(details);

        fetch(url)
          .then(response => {
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            return response.text();
          })
          .then(html => {
            const doc = new DOMParser().parseFromString(html, "text/html");
            const source = doc.querySelector("#text");
            if (!source) throw new Error("Modelo não localizado");
            pre.textContent = source.textContent.trim();
            copy.disabled = false;
            status.textContent = "Modelo carregado";
          })
          .catch(() => {
            pre.textContent = "Não foi possível carregar automaticamente este modelo. Use ‘Abrir página própria’.";
            status.textContent = "Falha no carregamento automático";
          });

        copy.addEventListener("click", async () => {
          const text = pre.textContent;
          const original = copy.textContent;
          try {
            await navigator.clipboard.writeText(text);
            copy.textContent = "Copiado";
          } catch {
            const range = document.createRange();
            range.selectNodeContents(pre);
            const selection = window.getSelection();
            selection.removeAllRanges();
            selection.addRange(range);
            copy.textContent = "Texto selecionado";
          }
          setTimeout(() => { copy.textContent = original; }, 1800);
        });
      });

      nextHeading.parentNode.insertBefore(section, nextHeading);
    }
  }
})();
