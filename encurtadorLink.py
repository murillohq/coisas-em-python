import pyshorteners

url = "https://www.mercadolivre.com.br/notebook-gamer-acer-nitro-v-anv15-51-57ws-intel-core-i5-13420h-13geraco-512ssd-8gb-nvidia-geforce-rtx-3050-gddr6-linux-gutta-156/p/MLB37396835"

s = pyshorteners.Shortener()

link_encurtado = s.tinyurl.short(url)

print(f'Link encurtado: {link_encurtado}')
