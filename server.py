
# Importáljuk a szükséges modulokat
import http.server
import socketserver
import webbrowser

# A szerver portja, amelyen a kéréseket fogadni fogjuk
PORT = 8080

# Az aktuális munkakönyvtár megadása
Handler = http.server.SimpleHTTPRequestHandler

# Szerver indítása az adott porton
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("A szerver fut a http://localhost:" + str(PORT) + " címen...")
    # A böngésző automatikus megnyitása
    webbrowser.open_new_tab("http://localhost:" + str(PORT))
    # A szerver végtelen ciklusban futtatása
    httpd.serve_forever()
