import streamlit as st
from io import BytesIO
import base64

def main():
    st.title("Criar Landing Page  com Streamlit")
    
    # Campo de texto para o usuário digitar o contato
    contato = st.text_area("Digite seu contato (email e telefone):", height=50)

    # Campo de texto para o usuário digitar o texto da página
    texto_inicio = st.text_area("Conteúdo   da página inicial:", height=150)
    texto_sobre_nos = st.text_area("Conteúdo da página sobre nós:", height=150)
    
    # Campo de texto para o usuário digitar o link do mapa incorporado
    link_mapa = st.text_input("Cole o link do mapa incorporado:", "")

    # Campo de texto para o usuário digitar o link da foto de fundo para o parallax
    link_foto_parallax = st.text_input("Cole o link da foto de fundo para o parallax:", "")

    if st.button("Gerar Landing Page"):
        # Gerar o arquivo HTML com o conteúdo da Landing Page
        gerar_landing_page(texto_inicio, texto_sobre_nos, contato, link_mapa, link_foto_parallax)

def gerar_landing_page(texto_inicio, texto_sobre_nos, contato, link_mapa, link_foto_parallax):
    # Obtendo a cor do título "Sobre Nós"
    cor_sobre_nos = "#007bff"

    # Estrutura HTML da Landing Page com rodapé
    landing_page = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Landing Page</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f9f9f9;
                color: #333;
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            .container {{
                max-width: 1200px;
                margin: auto;
                padding: 0 20px;
            }}
            .header {{
                padding: 50px 0;
                text-align: center;
            }}
            .header h1 {{
                font-size: 48px;
                font-weight: bold;
                margin-bottom: 20px;
            }}
            .header p {{
                font-size: 18px;
                line-height: 1.6;
            }}
            .section {{
                padding: 100px 0;
                text-align: center;
            }}
            .section h2 {{
                font-size: 36px;
                font-weight: bold;
                margin-bottom: 20px;
                color: {cor_sobre_nos}; /* Usando a mesma cor de "Sobre Nós" */
            }}
            .section p {{
                font-size: 18px;
                line-height: 1.6;
            }}
            .contact {{
                padding: 100px 0;
                text-align: center;
                background-color: #f9f9f9; /* Fundo branco */
                color: #333;
            }}
            .contact h2 {{
                font-size: 36px;
                font-weight: bold;
                margin-bottom: 20px;
                color: {cor_sobre_nos}; /* Usando a mesma cor de "Sobre Nós" */
            }}
            .contact p {{
                font-size: 18px;
                line-height: 1.6;
            }}
            nav {{
                background-color: #333;
                color: #fff;
                padding: 20px 0;
                text-align: center;
                position: fixed;
                width: 100%;
                top: 0;
                z-index: 9999;
            }}
            nav a {{
                color: #fff;
                text-decoration: none;
                padding: 0 20px;
                font-size: 18px;
            }}
            nav a:hover {{
                color: #007bff;
            }}
            .parallax {{
                background-image: url('{link_foto_parallax}');
                min-height: 500px;
                background-attachment: fixed;
                background-position: center;
                background-repeat: no-repeat;
                background-size: cover;
                padding: 100px 0;
                text-align: center;
            }}
            .parallax-text {{
                font-size: 36px;
                color: white;
            }}
            footer {{
                background-color: #333;
                color: #fff;
                padding: 20px 0;
                text-align: center;
                position: fixed;
                width: 100%;
                bottom: 0;
            }}
            footer p {{
                margin: 0;
            }}
        </style>
    </head>
    <body>
        <nav>
            <a href="#inicio">Início</a>
            <a href="#sobre-nos">Sobre Nós</a>
            <a href="#contato">Contato</a>
            <a href="#como-chegar">Como Chegar</a> <!-- Adicionado link para a seção "Como Chegar" -->
        </nav>
        <div class="container">
            <div class="parallax">
                <div class="parallax-text"></div>
            </div>
            <div class="header">
                <h1>Sua Empresa</h1>
                <p>Uma descrição breve sobre o que sua empresa faz.</p>
            </div>
            <div id="inicio" class="section">
                <h2>Início</h2>
                <p>{texto_inicio}</p>
            </div>
            <div id="sobre-nos" class="section">
                <h2>Sobre Nós</h2>
                <p>{texto_sobre_nos}</p>
            </div>
            <!-- Seção Contato -->
            <div id="contato" class="contact">
                <h2>Contato</h2>
                <p>{contato}</p>
            </div>
            <!-- Seção Como Chegar -->
            <div id="como-chegar" class="section">
                <h2>Como Chegar</h2>
                <p>Aqui está o mapa:</p>
                <!-- Mapa do Google Maps -->
                {link_mapa}
            </div>
        </div>

        <!-- Rodapé -->
        <footer>
            <div class="container">
                <p>© 2024 Sua Empresa. Todos os direitos reservados.</p>
            </div>
        </footer>
    </body>
    </html>
    """

    # Salvar o conteúdo em um arquivo HTML
    with open("landing_page.html", "w", encoding="utf-8") as file:
        file.write(landing_page)

    # Ler o conteúdo do arquivo HTML
    with open("landing_page.html", "rb") as file:
        html_bytes = file.read()

    # Converter o conteúdo do arquivo HTML para base64
    encoded_html = base64.b64encode(html_bytes).decode()

    # Gerar um link de download para o arquivo HTML
    href = f'<a href="data:text/html;base64,{encoded_html}" style="color: green;" download="landing_page.html">Clique aqui para baixar a Landing Page</a>'

    st.success("Landing Page gerada com sucesso! Clique no link abaixo para baixar.")
    st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
