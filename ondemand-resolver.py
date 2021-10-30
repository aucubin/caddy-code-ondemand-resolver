from http.server import BaseHTTPRequestHandler, HTTPServer
import getopt
import os
import sys
import re

domain = ''
regex = ''

class ResolverServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if(self.path.startswith("/domain")):
            pathArgs = self.path.split('?')
            if(len(pathArgs) == 2):
                queryArgs = pathArgs[1].split('=')
                if(len(queryArgs) == 2 and queryArgs[0] == 'domain'):
                    match = re.search(regex, queryArgs[1])
                    if match:
                        self.send_response(200)
                        self.end_headers()
                        return
                    else:
                        self.send_response(404)
                        self.end_headers()
                        return
            self.send_response(400)
            self.end_headers()
        else:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(bytes("Undefined Endpoint", "utf-8"))

if __name__ == "__main__":
    hostName = ''
    serverPort = -1

    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:p:d:", ["server=","port=", "domain="])

        for opt, arg in opts:
            if opt in ['-s']:
                hostName = arg
            elif opt in ['-p']:
                serverPort = int(arg)
            elif opt in ['-d']:
                domain = arg

    except getopt.GetoptError:
        print(getopt.GetoptError)
        print('ondemand-resolver.py -p <port> -s <server> -d <domain>')
        sys.exit(2)

    regex = '\d.{}'.format(domain)

    webServer = HTTPServer((hostName, serverPort), ResolverServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
