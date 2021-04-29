import requests
import streamlit as st
from time import sleep as s

#url = 'http://187.95.124.224:7474/'
urls =[]
urls = st.text_input('Informe a Url')
sistemas = ['esadmin','stp','scf','srh','stm']

arquivo = open('urls.txt','a')
arquivo.write(urls + "\n")
arquivo.close()

if st.button("Verificar") :

    for url in urls:
        print(url)
        for sistema in sistemas:
            resposta = requests.get(str(url)+sistema)
            if (resposta.status_code == 200):
                st.success("Sistema " + sistema.upper() + " no Ar.")
            else:
                st.error("Sistema " + sistema.upper() + " fora do Ar ou sem licença.")
