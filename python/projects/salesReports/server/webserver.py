from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
# import os
# import functools

class helloHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        SimpleHTTPRequestHandler.__init__(self, *args, directory = '../ui', **kwargs)

##    def do_GET(self):
##        self.path = '../ui/salesReports.html'
##        self.path = '../ui'
##       
##        try:
##            files = '../ui'
##            fileToOpen = open(self.path).read()
##            for filename in os.listdir(files):
##                with open(os.path.join(files, filename), 'r') as f:
##                    self.send_response(200)
##                    text = f.read()
##                    print(text)
##                    print(filename)
##        except:
##            fileToOpen = "File not found"
##            self.send_response(404)
##        self.end_headers() # to close headers once all headers are listed
##        self.wfile.write(fileToOpen.encode()) # can't send strings in http request, so encode to bytes

def main():
    PORT = 8000
##    simpleHandler = SimpleHTTPRequestHandler(directory = '../ui')
##    simpleHandler = functools.partial(SimpleHTTPRequestHandler, directory='../ui')
##    server = HTTPServer( ("", PORT), simpleHandler)
    server = HTTPServer( ('', PORT), helloHandler) # blank name because local host
    print('Server running on port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main() # run directly, not imported
    pass
