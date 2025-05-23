import socket
import os
import mimetypes

HOST = '127.0.0.1'
PORT = 8080
WWW_DIR = 'www'

def get_mime_type(path):
    mime, _ = mimetypes.guess_type(path)
    return mime or 'application/octet-stream'

def handle_client(conn, addr):
    try:
        request = conn.recv(1024).decode()
        if not request:
            return
        request_line = request.split('\r\n')[0]
        method, path, _ = request_line.split()
        print(f"{addr} {method} {path}")

        if method != 'GET':
            response = "HTTP/1.1 405 Method Not Allowed\r\n\r\n"
            conn.sendall(response.encode())
            return

        if path == '/':
            path = '/index.html'
        file_path = os.path.join(WWW_DIR, path.lstrip('/'))

        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                content = f.read()
            mime_type = get_mime_type(file_path)
            headers = (
                "HTTP/1.1 200 OK\r\n"
                f"Content-Type: {mime_type}\r\n"
                f"Content-Length: {len(content)}\r\n"
                "Connection: close\r\n"
                "\r\n"
            )
            conn.sendall(headers.encode() + content)
        else:
            content = b"<h1>404 Not Found</h1>"
            headers = (
                "HTTP/1.1 404 Not Found\r\n"
                "Content-Type: text/html\r\n"
                f"Content-Length: {len(content)}\r\n"
                "Connection: close\r\n"
                "\r\n"
            )
            conn.sendall(headers.encode() + content)
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"Server running on http://{HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            handle_client(conn, addr[0])

if __name__ == "__main__":
    run_server()