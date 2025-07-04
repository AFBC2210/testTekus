def test_titulo_tekus():
    from abilities.open_browser import get_browser
    from tasks.visit_homepage import visit_homepage
    from questions.page_title import page_title

    browser, playwright = get_browser()
    page = browser.new_page()
    visit_homepage(page, "https://www.tekus.co/")
    assert page_title(page) == "Bienvenido a Tekus - Tekus"
    browser.close()
    playwright.stop()
