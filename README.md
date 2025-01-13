# Proyecto de Búsqueda de Playstation 5 en Mercado Libre

Este proyecto tiene como objetivo automatizar la búsqueda de productos de **Playstation 5** en el sitio web de Mercado Libre, aplicando filtros como "Nuevo" y "Ciudad de México", y mostrando los primeros 5 resultados con su precio.

## Requisitos

- Python 
- Playwright para Python

## Instalación

Para ejecutar este proyecto, sigue los siguientes pasos:

1. Clona este repositorio:
   ```
   git clone https://github.com/tu_usuario/nombre_del_repositorio.git
   ```

2. Instala las dependencias:
   ```
   pip install playwright
   ```

3. Ejecuta el siguiente comando para instalar los navegadores necesarios para Playwright:
   ```
   python -m playwright install
   ```

## Uso

Para ejecutar el script, simplemente corre el siguiente comando:
```
python buscar_playstation5.py
```

El script realizará las siguientes acciones:
1. Navegará al sitio web de Mercado Libre.
2. Aplicará los filtros: "Nuevo" y "Ciudad de México".
3. Buscará el término "playstation5".
4. Extraerá el título y el precio de los primeros 5 productos que se muestren.

## Soluciones

Durante el desarrollo del código, se encontraron varios problemas comunes que fueron resueltos de la siguiente manera:

- **Sincronización de la página**: Se utilizó `wait_for()` de Playwright en lugar de `time.sleep()` para mejorar la sincronización y hacer el código más eficiente y menos propenso a fallos.
  - **Fuente**: [Playwright Docs: Esperar por Elementos](https://playwright.dev/docs/wait-for-element)

- **Manejo de errores**: El código fue ajustado para capturar excepciones durante la obtención de datos, especialmente al obtener el precio o nombre de los productos.
  - **Fuente**: [Python Docs: Manejo de Errores y Excepciones](https://docs.python.org/3/tutorial/errors.html)

- **Selectores**: Se utilizaron múltiples selectores para asegurar que el precio de los productos se pueda obtener, independientemente del tipo de presentación en la página.
  - **Fuente**: [Playwright Docs: Localización de Elementos](https://playwright.dev/docs/selectors)





