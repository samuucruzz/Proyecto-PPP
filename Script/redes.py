#!/usr/bin/env python3

import subprocess
import socket

def ping(ip):
    resultado = subprocess.run(["ping", "-c", "4", ip], capture_output=True, text=True)
    print(resultado.stdout)
    return resultado.returncode == 0

def escanear_puertos(ip):
    puertos = [22, 80, 443, 2049, 8000, 8096, 8409, 112, 445]
    print("Puertos abiertos en", ip)
    for puerto in puertos:
        s = socket.socket()
        s.settimeout(0.5)
        if s.connect_ex((ip, puerto)) == 0:
            print(" -", puerto, "abierto")
        s.close()

try:
    ip = input("Indica dirección IP: ")
    puerto = int(input("Número de puerto: "))
    mascara = input("Máscara de red (ej. 255.255.255.0): ")
    latencia = float(input("Latencia en ms: "))
    servidor = input("¿Es un servidor? (sí/no): ")
except ValueError:
    print("Error: introduce bien los números")
    puerto = 0
    latencia = 0.0

print("\nDirección IP:", ip)
print("Puerto:", puerto)
print("Máscara de red:", mascara)
print("Latencia:", latencia, "ms")
print("Servidor:", servidor)

if ping(ip):
    escanear_puertos(ip)
else:
    print("El equipo no está dentro de la red")

print("\nInterfaces de red:")
subprocess.run(["ip", "addr", "show"])
print("\nTabla de rutas:")
subprocess.run(["ip", "route"])
