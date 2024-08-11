import requests

# Cloudflare API údaje
api_token = "TYJTTcIqEPDX8NuHaWkjvfWV25ifi6hqqc4SCdUd"
zone_id = "17bc825db3e90a62e08ba1b21a6937e8"

# Hlavičky pre autentifikáciu
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json",
}

# Získanie zoznamu všetkých DNS záznamov
list_dns_url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
response = requests.get(list_dns_url, headers=headers)

if response.status_code == 200:
    dns_records = response.json().get("result", [])
    for record in dns_records:
        record_id = record["id"]
        record_name = record["name"]
        
        # Mazanie DNS záznamu
        delete_url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"
        delete_response = requests.delete(delete_url, headers=headers)
        
        if delete_response.status_code == 200:
            print(f"DNS záznam {record_name} bol úspešne zmazaný.")
        else:
            print(f"Chyba pri mazaní záznamu {record_name}: {delete_response.status_code}")
else:
    print(f"Chyba pri načítaní DNS záznamov: {response.status_code}")
