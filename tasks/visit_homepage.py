def visit_homepage(page, url):
    """
    Navega a la URL especificada usando la instancia de página de Playwright.

    Parámetros:
        page (playwright.sync_api.Page): Objeto de página de Playwright.
        url (str): URL a la que se desea navegar.
    """
    page.goto(url)
