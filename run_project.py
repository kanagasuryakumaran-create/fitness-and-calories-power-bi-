import http.server
import socketserver
import webbrowser
import subprocess
import os
import sys
import json

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class ProjectHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == '/open-powerbi':
            try:
                # Trigger Power BI Desktop (Store App or Executable)
                subprocess.Popen(["powershell", "-Command", "Start-Process shell:AppsFolder\\Microsoft.MicrosoftPowerBIDesktop_8wekyb3d8bbwe!Microsoft.MicrosoftPowerBIDesktop"])
                response = {"status": "success", "message": "Power BI Desktop is launching!"}
            except Exception as e:
                response = {"status": "error", "message": str(e)}

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
            return
        
        return super().do_GET()

def start_server():
    os.chdir(DIRECTORY)
    print("=" * 65)
    print(" FITNESS & CALORIE ANALYTICS PROJECT RUNNER")
    print("=" * 65)
    print(f"Project directory: {DIRECTORY}")
    print(f"Starting local server at http://localhost:{PORT}")
    print("Opening interactive dashboard in your default browser...")
    print("Press Ctrl+C to stop the server at any time.")
    print("=" * 65)

    webbrowser.open(f"http://localhost:{PORT}")

    with socketserver.TCPServer(("", PORT), ProjectHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server. Goodbye!")

if __name__ == '__main__':
    start_server()
