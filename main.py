import requests
import streamlit as st
from time import sleep as s

#url = 'http://187.95.124.224:7474/'
urls =[]
sistemas = ['esadmin','stp','scf','srh','stm']
with st.beta_expander("Cadastrar Url"):
    urls = st.text_input('Informe a Url')
    arquivo = open('urls.txt','a')
    arquivo.write(urls + "\n")
    arquivo.close()

if st.button("Verificar") :
    urls = open('urls.txt', 'r')
    for url in urls:
        for sistema in sistemas:
            print("Teste",url+sistema)
            resposta = requests.get(str(url)+sistema)
            if (resposta.status_code == 200):
                st.success("Sistema " + sistema.upper() + " no Ar.")
            else:
                st.error("Sistema " + sistema.upper() + " fora do Ar ou sem licença.")
