from youtube import Youtube
from generative_ai import GenerativeAI
import urllib.parse
import http.server
# Define a custom handler that serves the HTML file
class ChapterGenerator(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'  # Replace 'index.html' with your HTML file's name
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == '/transcript':
            content_length = int(self.headers['Content-Length'])
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            url_encoded = self.rfile.read(content_length)
            decoded_url = urllib.parse.unquote(url_encoded)

            video_id = decoded_url.split("=")

            transcript = Youtube().get_transcript(video_id[2])
            
            msg = GenerativeAI().interact(prompt=transcript)

            self.wfile.write(msg.encode('utf-8'))