import webview
import threading
from app import app

def start_server():
    app.run(port=5000)
    app.debug = True

if __name__ == '__main__':
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()

    webview.create_window('Pressao_',
                          'http://localhost:5000')
    webview.start()