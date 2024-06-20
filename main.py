import discord
import requests
import json

# Remplacez par votre jeton de bot Discord ici
TOKEN = 'VOTRE_TOKEN_ICI'

def get_user_info(user_id):
    url = f'https://discord.com/api/v10/users/{user_id}'
    headers = {
        'Authorization': f'Bot {TOKEN}'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        return user_data
    else:
        print(f"Erreur lors de la récupération des informations: {response.status_code}")
        return None

def main():
    print("""
   _______    __         _____  __________    
  /  _/ _ \  / /____    /  _/ |/ / __/ __ \   
 _/ // // / / __/ _ \  _/ //    / _// /_/ /   
/___/____/  \__/\___/ /___/_/|_/_/  \____/    
                                            
    """)
    
    user_id = input("Entrez l'ID de l'utilisateur Discord: ")
    user_info = get_user_info(user_id)

    if user_info:
        print("\nInformations de l'utilisateur:")
        print(json.dumps(user_info, indent=4))

if __name__ == "__main__":
    main()
