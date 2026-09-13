document.documentElement.classList.add("js");

(() => {
  const pathname = window.location.pathname;
  const projectMarker = "/classe-e-massas/";
  const base = pathname.includes(projectMarker) ? projectMarker : "/";

  const nav = document.querySelector("header .nav");
  if (nav) {
    const items = [
      { label: "Início", href: base, section: "home" },
      { label: "Notícias", href: `${base}noticias/`, section: "noticias" },
      { label: "Artigos", href: `${base}artigos/`, section: "artigos" },
      { label: "Observatório", href: `${base}observatorio/`, section: "observatorio" },
      { label: "Biblioteca", href: `${base}biblioteca/`, section: "biblioteca" },
      { label: "MPT", href: `${base}mpt/`, section: "mpt" }
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
              : "home";

    nav.classList.add("global-nav");
    nav.innerHTML = items.map(item => {
      const current = item.section === currentSection ? ' aria-current="page"' : "";
      return `<a href="${item.href}"${current}>${item.label}</a>`;
    }).join("");
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
})();
