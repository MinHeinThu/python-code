from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Store users temporarily in memory (like a fake database)
users = []

class SimpleHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/':
            self.send_response(200) # 200 = ok
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<h1> Hello, Min! Backend has started.</h1>")
        
        elif self.path == '/hello':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"message": "Hello from plain backend"}')
        
        elif self.path == '/greet':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Greetings from ProfessorGPT!')

        elif self.path == '/users':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(users).encode())

        elif self.path == '/json':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            user_info= {
                "name": "someone",
                "goal": "Become a world-class software developer and hacker"
            }
            self.wfile.write(json.dumps(user_info).encode())
        
        else:
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'404 Not Found')

    def do_POST(self):
        if self.path == '/users':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode())
                name = data.get("name")
                email = data.get("email")

                if not name or not email:
                    raise ValueError("Missing name or email")
                
                user = {"id": len(users) + 1, "name": name, "email": email}
                users.append(user)

                self.send_response(201)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(user).encode())
            except Exception as e:
                self.send_response(400)
                self.send_header('content-type', 'application/json')
                self.end_headers()
                error = {"error": str(e)}
                self.wfile.write(json.dumps(error).encode())

        else:
            self.send_response(400)
            self.end_headers()

    def get_user_id_from_path(self):
        parts = self.path.strip("/").split("/")
        if len(parts) == 2 and parts[0] == "users":
            try:
                return int(parts[1])
            except ValueError:
                return None
        return None
    
    def do_PUT(self):
        user_id = self.get_user_id_from_path()
        if user_id is None:
            self.send_response(400)
            self.end_headers()
            return
        
        content_length = int(self.headers.get('Content-Length'), 0)
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data.decode())
            name = data.get("name")
            email = data.get("email")

            if not name or not email:
                raise ValueError("Missing name or email")
            
            for user in users:
                if user["id"] == user_id:
                    user["name"] == name
                    user["email"] == email
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.writable(json.dumps(user.encode()))
                    return
                
        except Exception as e:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
    
    def do_PATCH(self):
        user_id = self.get_user_id_from_path()
        if user_id is None:
            self.send_response(400)
            self.end_headers()
            return

        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data.decode())

            for user in users:
                if user["id"] == user_id:
                    user.update({k: v for k, v in data.items() if k in ["name", "email"]})
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(user).encode())
                    return

            self.send_response(404)
            self.end_headers()

        except Exception as e:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
        
    def do_DELETE(self):
        user_id = self.get_user_id_from_path()
        if user_id is None:
            self.send_response(400)
            self.end_headers()
            return

        for i, user in enumerate(users):
            if user["id"] == user_id:
                users.pop(i)
                self.send_response(204)  # No Content
                self.end_headers()
                return

        self.send_response(404)
        self.end_headers()



def run(server_class=HTTPServer, handler_calass = SimpleHandler, port=8000):
    print(f"Server running on http://localhost:{port}")
    server = server_class(('', port), handler_calass)
    server.serve_forever()

if __name__ == '__main__':
    run()