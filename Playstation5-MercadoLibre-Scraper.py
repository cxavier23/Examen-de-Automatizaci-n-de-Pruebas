from playwright.sync_api import sync_playwright
import time

def buscar_playstation5():
    try:
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        # Navegar a Mercado Libre
        page.goto("https://www.mercadolibre.com/")
        time.sleep(3)

        # Seleccionar México como país
        page.click("text=México", timeout=10000)
        time.sleep(3)

        # Cerrar el banner de cookies (si aparece)
        try:
            banner = page.locator("div[class*='cookie-consent-banner']")
            if banner.is_visible():
                page.click("button:has-text('Entendido')")
                print("Banner de cookies cerrado.")
        except Exception:
            print("El banner de cookies no se mostró o ya estaba cerrado.")

        # Buscar "playstation5"
        search_box = page.locator("input[type='text']")
        search_box.fill("playstation5")
        search_box.press("Enter")
        time.sleep(5)
        print("Búsqueda realizada con éxito.")

        # Filtro: Nuevos
        nuevos_selector = "//li[contains(@class, 'ui-search-filter') and .//span[text()='Nuevo']]"
        page.locator(nuevos_selector).click()
        time.sleep(5)
        print("Filtro 'Nuevos' aplicado.")

        # Filtro: Ciudad de México
        cdmx_selector = "//li[contains(@class, 'ui-search-filter') and .//span[text()='Ciudad de México']]"
        cdmx_locator = page.locator(cdmx_selector)
        if cdmx_locator.count() > 0:
            cdmx_locator.click()
            time.sleep(5)
            print("Filtro 'Ciudad de México' aplicado.")
        else:
            print("El filtro 'Ciudad de México' no está disponible.")

        # Obtener los 5 primeros productos
        productos = page.locator(".ui-search-layout__item")
        total_productos = productos.count()

        if total_productos == 0:
            print("No se encontraron productos en la búsqueda.")
            return

        print(f"Se encontraron {total_productos} productos. Mostrando los primeros 5:")
        for idx in range(min(5, total_productos)):  # Limitar a los primeros 5
            try:
                producto = productos.nth(idx)
                producto.wait_for(state="visible", timeout=10000)

                # Extraer el título del producto
                titulo_locator = producto.locator("h2")
                if not titulo_locator.is_visible():
                    print(f"El título del producto {idx + 1} no está visible.")
                    continue
                nombre = titulo_locator.text_content(timeout=5000)

                # Extraer el precio del producto (probar múltiples selectores)
                precio = "N/A"  # Valor predeterminado si no se encuentra el precio
                precio_selectores = [
                    ".price-tag-fraction",  # Precio estándar
                    ".price-tag-text-sr-only",  # Precio accesible para lectores de pantalla
                    ".price-tag-whole"  # Precio alternativo
                ]
                for selector in precio_selectores:
                    precio_locator = producto.locator(selector)
                    if precio_locator.is_visible():
                        precio = precio_locator.text_content(timeout=5000)
                        break

                if precio == "N/A":
                    print(f"El precio del producto {idx + 1} no está visible.")

                print(f"{idx + 1}. {nombre} - ${precio}")

            except Exception as e:
                print(f"Error obteniendo el producto {idx + 1}:", e)

        # Cerrar el navegador
        browser.close()
        playwright.stop()

    except Exception as e:
        print("Error general:", e)

if __name__ == "__main__":
    buscar_playstation5()
