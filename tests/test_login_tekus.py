from abilities.open_browser import get_browser
from tasks.visit_homepage import visit_homepage

def test_login_tekus():
    """
    Prueba automatizada que verifica el ingreso de usuario y contraseña en la página de login de Tekus.
    
    
    

    Flujo:
        1. Abre el navegador usando Playwright.
        2. Navega a la página https://qalab.invertebrado.co
        3. Obtiene el título de la página y lo compara con el valor esperado.
        4. Ingresa el usuario "qatester" en el campo correspondiente.
        5. Ingresa la contraseña "N9j^u9&Hm@dz2Kcs" en el campo correspondiente.
        6. Hace clic en el botón iniciar sesion
        7. Verifica que el texto 'Panel de Inicio' esté visible. despues del login
        8. Hace clic en 'Multimedia' en el menú lateral izquierdo.
        9. Verifica que el texto 'MD-5' esté visible.
        10. Verifica que el texto sobre el peso '1.02MB' esté visible.
        11. Verifica que el texto de la descripción de la imagen esté visible.
        12. Verifica que la imagen se previsualice correctamente.
        13. Cierra el navegador y detiene Playwright.
        
    
    
    """
    browser, playwright = get_browser()
    page = browser.new_page()
    visit_homepage(page, "https://qalab.invertebrado.co")

    #assert page.title() == "Tekus | login"

    # Usuario
    page.locator('input#mat-input-0').wait_for(state="visible")
    page.locator('input#mat-input-0').fill("qatester")

    # Contraseña
    page.locator('input#mat-input-1').wait_for(state="visible")
    page.locator('input#mat-input-1').fill("N9j^u9&Hm@dz2Kcs")

    # Click en el botón de login usando la clase única
    page.locator('button.btn.ark-btn.mat-mdc-raised-button').wait_for(state="visible")
    page.locator('button.btn.ark-btn.mat-mdc-raised-button').click()

    page.locator('h1.ark-h1').wait_for(state="visible")
    # Verifica que el título de la página sea el esperado después del login


    
    #Validando que el texto 'Panel de Inicio' esté visible...
    print("Validando que el texto 'Panel de Inicio' esté visible...")
    assert page.locator('h1.ark-h1').is_visible(), "El título del panel de inicio no es visible"

    #Validando que realice clic en 'Multimedia' en el menu lateral izquierdo
    print("Validando que realice clic en 'Multimedia' en el menu lateral izquierdo")
    page.locator('a[href="/screens/multimedia"]').click()

    #Validando que el texto 'MD-5' esté visible...
    print("Validando que el texto 'MD-5' esté visible...")
    page.locator('span.ark-card-content-id:has-text("MD-5")').wait_for(state="visible")
    assert page.locator('span.ark-card-content-id:has-text("MD-5")').text_content() == "MD-5"

    #Validando que el texto sobre el peso '1.02MB' esté visible...
    print("Validando que el texto sobre el peso '1.02MB' esté visible...")
    page.locator('span.ark-size-file:has-text("1.02MB")').wait_for(state="visible")
    assert page.locator('span.ark-size-file:has-text("1.02MB")').text_content() == "1.02MB"

    #Validando que el texto de la descripcion de la imagen esté visible...
    print("Validando que el texto de la descripcion de la imagen esté visible...")
    page.locator('a.ark-card-title:has-text("Tekus horizontal.png")').wait_for(state="visible")
    assert page.locator('a.ark-card-title:has-text("Tekus horizontal.png")').is_visible(), "El enlace 'Tekus horizontal.png' no es visible"

    #Validando que la imagen 1 se previsualice.......
    print("Validando que la imagen 1 se previsualice.......")
    page.locator('img[src="https://cdn.invertebrado.co/qalab/public/eee5e430-47db-48ce-a217-a61565f012ca.jpg"]').wait_for(state="visible")
    assert page.locator('img[src="https://cdn.invertebrado.co/qalab/public/eee5e430-47db-48ce-a217-a61565f012ca.jpg"]').is_visible(), "La imagen específica no es visible"


    browser.close()
    playwright.stop()