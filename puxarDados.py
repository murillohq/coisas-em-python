import requests

resposta = requests.get("https://ipinfo.io/json?token=").json()

print("🌐 IP:      ", resposta.get("ip"))
print("🏳️  País:    ", resposta.get("country"))
print("📍 Estado:  ", resposta.get("region"))
print("🏙️  Cidade:  ", resposta.get("city"))
print("📮 CEP:     ", resposta.get("postal"))
print("🗺️  Loc:     ", resposta.get("loc"))
print("🏢 Org:     ", resposta.get("org"))