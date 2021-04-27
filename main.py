import requests
import streamlit as st
from time import sleep as s

#url = 'http://187.95.124.224:7474/'
url = st.text_input('Informe a Url')
sistemas = ['esadmin','stp','scf','srh','stm']

if st.button("Verificar") :

    for sistema in sistemas:

        resposta = requests.get(url+sistema)
        if (resposta.status_code == 200):
            st.success("Sistema " + sistema.upper() + " no Ar.")
        else:
            st.error("Sistema " + sistema.upper() + " fora do Ar ou sem licença.")
print()