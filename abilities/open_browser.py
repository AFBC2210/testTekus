from playwright.sync_api import sync_playwright

def get_browser():
    """
    Inicia Playwright y abre una instancia de navegador Chromium (Google Chrome).

    Retorna:
        tuple: (browser, playwright)
            browser (playwright.sync_api.Browser): Instancia del navegador Chromium.
            playwright (playwright.sync_api.Playwright): Instancia de Playwright para su posterior cierre.
    """
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, channel="chrome")
    return browser, playwright
