import os
import configparser
import requests
import json

class IPNotConfigured(Exception):
    pass

class ConfigFileNotFound(Exception):
    pass

class AutoRepr:
    def __repr__(self):
        otpt = ""
        for i in self.__dict__:
            otpt = otpt+f'{i}={self.__dict__[i]} ,'
        return f"{self.name}({otpt[:-2]})"



def Encode_Ord(s:str):
    otpt = ""
    for i in s:
        otpt = otpt + str(ord(i)) + " "
    return otpt[:-1]

def Decode_Ord(code:str):
    otpt = ""
    chars = code.split(" ")
    for i in chars:
        otpt = otpt + chr(int(i))
    return otpt

def ReadUserID():
    with open("USER.env" , "rb") as u:
        return str(Decode_Ord(str(u.read().decode())))


def ReadIP():
    if("host.ini" in os.listdir()):
        config = configparser.ConfigParser()
        config.read("host.ini")
        if("HOST" in config.sections()):
            try:
                ip = config["HOST"]["IP"]
                port = config["HOST"]["PORT"]
                return (ip,int(port))
            except:
                raise IPNotConfigured("IP not configured properly in host.ini")
        else:
            raise IPNotConfigured("IP not configured in host.ini")
    else:
        raise ConfigFileNotFound("host.ini not found in current directory.")

def ReadConfig():
    if("host.ini" in os.listdir()):
        otpt = {}

        config = configparser.ConfigParser()
        config.read("host.ini")
        for i in config.sections():
            otpt[i]={}
            for heading,value in config[i].items():
                otpt[i][heading]= value
        return(otpt)
    else:
        raise ConfigFileNotFound("host.ini not found in current directory.")


def PingServer(ip , port):
    try:
        r = requests.get(f"http://{ip}:{port}/ping")
        return(r.ok)
    except:
        return False

