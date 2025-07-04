def test_titulo_tekus():
    """
    Prueba automatizada que verifica el título de la página principal de Tekus.

    Flujo:
        1. Abre el navegador usando Playwright.
        2. Navega a la página https://www.tekus.co/.
        3. Obtiene el título de la página y lo compara con el valor esperado.
        4. Cierra el navegador y detiene Playwright.
    """
    from abilities.open_browser import get_browser
    from tasks.visit_homepage import visit_homepage
    from questions.page_title import page_title

    browser, playwright = get_browser()
    page = browser.new_page()
    visit_homepage(page, "https://www.tekus.co/")
    assert page_title(page) == "Bienvenido a Tekus - Tekus"
    browser.close()
    playwright.stop()
