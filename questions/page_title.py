def page_title(page):
    """
    Devuelve el título de la página web actual.

    Parámetros:
        page (playwright.sync_api.Page): Objeto de página de Playwright sobre el que se realiza la consulta.

    Retorna:
        str: Título de la página web.
    """
    return page.title()
