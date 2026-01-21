import http.server
import socketserver
from task import Task

PORT = 8000


class Handler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. Lire la taille du message
        content_length = int(self.headers["Content-Length"])
        # 2. Lire le contenu (le JSON)
        post_data = self.rfile.read(content_length)

        # 3. Désérialiser et Traiter la tâche
        task = Task.from_json(post_data.decode("utf-8"))
        print(f"Processing task {task.identifier} (size: {task.size})")
        task.work()

        # 4. Renvoyer la réponse
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(task.to_json().encode("utf-8"))


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
