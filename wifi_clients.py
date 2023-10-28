import subprocess
import socket

def display_banner():
    print("Welcome to A-STAR Tool")
    print("Auteur : Léon Meizou, Specialiste sur les questions de Cyber Sécurité")

def get_ip_info():
    try:
        result = subprocess.check_output("ipconfig", shell=True, universal_newlines=True)
        return result
    except Exception as e:
        return str(e)

def get_wifi_clients():
    try:
        result = subprocess.check_output("arp -a", shell=True, universal_newlines=True)
        lines = result.split('\n')

        client_info = []

        for line in lines:
            if line:
                parts = line.split()
                if len(parts) == 3 and not parts[1].startswith(('ff-ff-ff', '01-00-5e')):
                    ip_address = parts[0]
                    mac_address = parts[1]
                    try:
                        host_name, _, _ = socket.gethostbyaddr(ip_address)
                    except socket.herror:
                        host_name = "N/A"
                    client_info.append({"Adresse IP": ip_address, "MAC Address": mac_address, "Nom d'hôte": host_name})

        return client_info
    except Exception as e:
        return str(e)

def display_menu():
    print("Menu :")
    print("1. Obtenir les informations IP")
    print("2. Obtenir la liste des clients connectés au réseau Wi-Fi")
    print("3. Quitter")

def display_ip_info(ip_info):
    print("\nInformations IP :")
    print(ip_info)

def display_client_info(client_info):
    if client_info:
        print("\nListe des clients connectés :")
        for client in client_info:
            nom_hote = client.get("Nom d'hote", "N/A")
            print("Adresse IP: {}, MAC: {}, Nom d'hôte: {}".format(client['Adresse IP'], client['MAC Address'], nom_hote))
    else:
        print("Aucun client Wi-Fi trouvé.")

# ...


def main():
    while True:
        display_menu()
        choice = input("Sélectionnez une option : ")

        if choice == "1":
            ip_info = get_ip_info()
            display_ip_info(ip_info)
        elif choice == "2":
            client_info = get_wifi_clients()
            display_client_info(client_info)
        elif choice == "3":
            break
        else:
            print("Option invalide. Veuillez sélectionner une option valide.")

if __name__ == "__main__":
    main()
