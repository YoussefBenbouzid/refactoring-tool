import requests
import base64

def estrai_file_da_repository(url):
    response = requests.get(url)
    if response.status_code == 200:
        lista_file = response.json()
        for item in lista_file:
            # Controllo se è un file Python, Java, JavaScript, C o C++
            if item['type'] == 'file' and item['path'].endswith('.py') or item['path'].endswith('.java') or item['path'].endswith('.js') or item['path'].endswith('.c') or item['path'].endswith('.cpp'):
                url_file = item['url']
                file_response = requests.get(url_file)
                if file_response.status_code == 200:
                    file_content = file_response.json()
                    if 'content' in file_content:
                        codice = base64.b64decode(file_content['content']).decode('utf-8')
                        print(f"Contenuto di {item['path']}:\n")
                        print(codice)
                    else:
                        print(f"Errore nel recupero di {item['path']}")
            elif item['type'] == 'dir':
                estrai_file_da_cartella(item['url'])