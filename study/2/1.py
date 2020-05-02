
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler): # BaseHTTPRequestHandler 를 상속받아
    # 원하는 로직으로 핸들러 클래스를 정의 
    # BaseHTTPRequestHandler : 핸들러를 만들기 위한 기반 클래스로, 
    # HTTP 프로토콜 처리 로직이 들어있음
    # 이 클래스를 상속받아, 자신의 로직 처리를 담당하는 핸들러 클래스를 만듦
    def do_GET(self):
        self.send_response(200, 'OK')
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello World')
        
if __name__ == '__main__':
    # 서버의 IP, PORT 및 핸들러 클래스를 인지로 하여 HTTPServer 객체를 생성함
    server = HTTPServer(('', 8888), MyHandler)
    # HTTPServer : 웹서버를 만들기 위한 클래스로, 서버 IP와 PORT를 바인딩 함
    # HTTPServer 객체 생성 시 핸들러 클래스 반드시 필요함 
    print('Started WebServer on port 8888...')
    print('Press ^C to quit WebServer.')
    server.serve_forever() # HTTPServer 객체의 serve_forever() 메소드 호출