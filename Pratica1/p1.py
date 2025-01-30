import streamlit as st
import struct
import os
#Archivo (producto-cantidad-precio)

index ={}
def indexInfo():
    with open('inventario.txt','r') as file:
        pos = 0
        while True:
            line = file.readline()
            if not line:
                break
            prod = line.split('-')[0]
            index[prod] = pos
            pos = file.tell()
    with open('index.dat','wb') as f:
        for key,val in index.items():
            key_bytes = key.encode('utf-8')
            f.write(struct.pack('I',len(key_bytes)))
            f.write(key_bytes)
            f.write(struct.pack('Q',val))
    print('Indexación terminada')


i = indexInfo

#TODO: Implementar la buscar en el .dat

st.write(
    """
# Practica 
    Busqueda de información en archivos txt
"""
)

st.text_input("Buscar", on_change=i)


