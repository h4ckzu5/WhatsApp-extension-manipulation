Greeatings To: @TeamWhoami @ElixSec @WitcheRHash @C0d3r17 

![imagen](https://github.com/user-attachments/assets/cc7b3468-e325-4e73-aa8e-1e90c5bdfd72)


El malware de Android (.apk) se puede difundir a través de un documento PDF falso manipulando la extensión de archivo en la aplicación WhatsApp. PoC está disponible en este repo

Paso 1: En primer lugar, cree una cuenta gratuita en ultramsg. Usaremos esto para gestionar la API
Paso 2: Haga clic en el botón "Añadir caso" y crear una nueva instancia.

![imagen](https://github.com/user-attachments/assets/fddac9ec-e8b7-4bc0-9360-33ae1ee7cd22)


Paso 3: Rellene los campos apropiados en wp.py con la información generada de la API e inicie sesión en su aplicación de WhatsApp usando el código QR encontrado bajo la información de instancia.

![imagen](https://github.com/user-attachments/assets/27c4fc6e-e7e9-406b-b637-2bd1d7d7f873)


Paso 4: Introduzca el número de destino en el campo "entrar en el número "entrar" y subir su archivo al servidor (esto puede ser un servidor de ngrok o pitón. Si estás probando localmente, puedes usar XAMPP).
Paso 5: Ejecute el archivo apk.py y vea el mensaje enviado.

usage: apk.py [-h] --to TO

options:

  -h, --help  show this help message and exit
  
  --to TO     Número de teléfono del destinatario con código de país, e.g., +52...


Descargo de responsabilidad
Este software se proporciona "tal cual", sin garantía de ningún tipo, expreso o implícito, incluyendo pero no limitado a las garantías de comerciabilidad, aptitud para un propósito particular, y sin infracción. En ningún caso los autores o titulares de derechos de autor serán responsables de cualquier reclamación, daños u otra responsabilidad, ya sea en una acción de contrato, responsabilidad civil, o de otra manera, derivada de, fuera o en conexión con el software o el uso u otros tratos en el software.
