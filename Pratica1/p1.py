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




def searchInfo(texto):
    with open('index.dat','rb') as file:

        while True:
            len_name_bytes = file.read(4)
            if not len_name_bytes:
                break
            len_name = struct.unpack('I', len_name_bytes)[0]
            name_prod =  file.read(len_name).decode('utf-8')

            pos_bytes = file.read(8)
            pos = struct.unpack('Q',pos_bytes)[0]

            if name_prod.lower() == texto.lower():
                with open('inventario.txt','r') as data:
                    data.seek(pos)
                    info = data.readline().split('-')
                    name= info[0]
                    quantity = info[1]
                    price = info[2]
                    string = f"""Producto : {name} , Cantidad : {quantity} , Precio : {price}"""
                   
                    print(info)
                    st.write(string )
                    return
                 
        st.write("""Producto no encontrado""")


i = indexInfo


#TODO: Implementar la buscar en el .dat

st.write(
    """
# Practica 
    Busqueda de información en archivos txt
"""
)

text_input = st.text_input("Buscar", on_change=i) 

searchInfo(text_input)