import requests
from bs4 import BeautifulSoup


def hayEntradas():

    try:
        url = "https://venta.enterticket.es/buy/?id=23008&color=f32735"
        response = requests.get(url)
        html_content = response.text

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Select an object with the class 'class1' and 'class2'
        selected_object = soup.select('.list-group-item.text-center')[0]


        texto = selected_object.getText()

        if texto != "La venta de entradas online está cerrada.":
            print('HAY ENTRADAS')
            return True
        elif texto == "La venta de entradas online está cerrada.": 
            print('NO HAY ENTRADAS')
            return False
        else:  print('HA HABIDO UN ERROR')  
    except:
        print("An exception occurred")
        enviarEmail()
    # Retrieve the website's HTML content
      

def enviarEmail():
    import smtplib

    # Create a connection to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # Start the encryption
    server.starttls()

    # Login to the email account
    server.login("javiergracia.automation@gmail.com", "oxlxarktchdvypwm")

    # Create the email message
    message = """\
    Subject: ENTRADAS BACARRA

    HAY ENTRADAS DE BACARRA"""

    # Send the email
    server.sendmail("javiergracia.automation@gmail.com", "javiergracia2003@gmail.com", message)

    # Close the connection
    server.quit()


if hayEntradas():
    enviarEmail()

