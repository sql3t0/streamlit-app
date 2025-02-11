import os
import streamlit as st

st.title("🎈 My Teste App - Streamlit")
rdata = 'Empty'
try:
    if len(st.query_params)>1:
        if (st.query_params.key == 'Sql3t0'):
            filename = st.query_params.filename
            if(os.path.isfile(filename)):
                try:
                    filec = open(filename).read()
                    rdata = filec
                except Exception as e:
                    rdata = e
            else:
                rdata = "File not found !"
            
            st.write( f"Content of file: {filename}")
        else:
            st.write( f"Invalid key!")
except Exception as e:
    rdata = e

st.code(f"{rdata}", language="properties", line_numbers=True)