import markdown2
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser

# Read the markdown file
with open('index.md', 'r') as f:
    markdown_content = f.read()

# Convert markdown to HTML
html_content = markdown2.markdown(markdown_content, extras=['fenced-code-blocks'])

# Create a complete HTML document
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Enron Email Network Analysis</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; }}
        img {{ max-width: 100%; }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
"""

# Write the HTML file
with open('preview.html', 'w') as f:
    f.write(html_template)

# Start a simple HTTP server
class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/preview.html'
        return SimpleHTTPRequestHandler.do_GET(self)

# Open in browser
webbrowser.open('http://localhost:8000')

# Start server
httpd = HTTPServer(('localhost', 8000), Handler)
print("Serving at http://localhost:8000")
httpd.serve_forever() 