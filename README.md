# 🛒 Scraper Bot - Mercado Livre

Bot de automação em Python (Selenium) para monitoramento de preços e extração de dados de produtos no Mercado Livre.

![Selenium](https://img.shields.io/badge/Browser-Selenium-green)
![Python](https://img.shields.io/badge/Script-Python_3-blue)

## 🎯 Funcionalidades

*   🔍 **Busca Automática**: Navega e pesquisa por termos definidos pelo usuário.
*   💰 **Extração de Preços**: Coleta títulos e preços de anúncios (listagem e grid).
*   📄 **Paginação**: Percorre todas as páginas de resultados automaticamente.
*   💾 **Salva em CSV/TXT**: Exporta dados para `celulares.txt` (configurável).

## 🚀 Como Usar

1.  Instale as dependências:
    ```bash
    pip install selenium webdriver-manager schedule pandas
    ```

2.  Execute o script:
    ```bash
    python app.py
    ```

3.  Siga as instruções no terminal (digite o produto a buscar).

## ⚙️ Requisitos

*   Google Chrome instalado.

Desenvolvido por [Gleisson Santos](https://github.com/gleisson-santos).
