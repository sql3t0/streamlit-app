import streamlit as st
from http.server import HTTPServer, SimpleHTTPRequestHandler
st.title("🎈 My new app")

httpd = HTTPServer(('localhost', 8501), SimpleHTTPRequestHandler)
httpd.serve_forever()

# filec = open('/etc/passwd').read()
# #print(filec)

# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )
# st.write(
#     f"{filec}"
# )
