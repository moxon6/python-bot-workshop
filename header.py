from browser import window, document as doc
from browser.html import *

trans_menu = {
    "menu_console": {"en": "Console", "es": "Consola", "fr": "Console"},
    "menu_editor": {"en": "Editor", "es": "Editor", "fr": "Editeur"},
    "menu_demo": {"en": "Demo", "es": "Demo", "fr": "DÃ©mo"},
    "menu_gallery": {"en": "Gallery", "es": "GalerÃ­a", "fr": "Galerie"},
    "menu_doc": {"en": "Documentation", "es": "DocumentaciÃ³n", "fr": "Documentation"},
    "menu_download": {"en": "Download", "es": "Descargas", "fr": "TÃ©lÃ©chargement"},
    "menu_dev": {"en": "Development", "es": "Desarrollo", "fr": "DÃ©veloppement"},
    "menu_groups": {"en": "Community", "es": "Comunidad", "fr": "CommunautÃ©"}
}
links = {"home": "index.html",
    "console": "tests/console.html",
    "demo": "demo.html",
    "editor": "tests/editor.html",
    "gallery": "gallery/gallery_{language}.html",
    "doc": "static_doc/{language}/intro.html",
    "download": "https://github.com/brython-dev/brython/releases",
    "dev": "https://github.com/brython-dev/brython",
    "groups": "groups.html"
}

def show(language=None):
    """Detect language, either from the key "lang" in the query string or
    from the browser settings."""
    has_req = False
    qs_lang = None

    prefix = "/"

    if language is None:
        qs_lang = doc.query.getfirst("lang") # query string
        if qs_lang and qs_lang in ["en", "fr", "es"]:
            has_req = True
            language = qs_lang
        else:
            lang = __BRYTHON__.language # browser setting
            if lang in ["en", "fr", "es"]:
                language = lang

    language = language or "en"

    _banner = doc["banner_row"]

    loc = window.location.href
    current = None
    for key in ["home", "console", "demo", "editor", "groups"]:
        if links[key] in loc:
            current = key
            break

    if current is None:
        if "gallery" in loc:
            current = "gallery"
        elif "static_doc" in loc:
            current = "doc"

    for key in ["console", "editor", "demo", "gallery", "doc", "download",
            "dev", "groups"]:
        if key in ["download","dev"]:
            href = links[key]
        else:
            href = prefix + links[key]
        if key in ["doc", "gallery"]:
            href = href.format(language=language)
        if key not in ["download", "dev"]:
            # add lang to href
            href += f"?lang={language}"
        if key == "home":
            img = IMG(src="/brython.svg", Class="logo")
            link = A(img, href=href)
            cell = TD(link, Class="logo")
        else:
            link = A(trans_menu[f"menu_{key}"][language], href=href,
                Class="banner")
            cell = TD(link)
            if key == current:
                link.classList.add("selected_header")
        if key in ["download", "dev"]:
            link.attrs["target"] = "_blank"
        _banner <= cell

    return qs_lang,language
