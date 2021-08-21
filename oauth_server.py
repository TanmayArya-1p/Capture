
import os
from flask import Flask, redirect, url_for , render_template
from flask_discord import DiscordOAuth2Session, requires_authorization, Unauthorized
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager
import threading
from util import *
import csv
from flask import request
from capture import *
from config import *

IP,PORT = ReadIP()

app = Flask(__name__)
app.secret_key = b"auth"
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"   
app.config["DISCORD_CLIENT_ID"] = 872003233734877226    # Discord client ID.
app.config["DISCORD_CLIENT_SECRET"] = DC_CLIENT_SECRET        # Discord client secret.
app.config["DISCORD_REDIRECT_URI"] = f"http://{IP}:{PORT}/redirecturi"                 # URL to your callback endpoint.
app.config["DISCORD_BOT_TOKEN"] = BOT_SECRET                  # Required to access BOT resources.


discord = DiscordOAuth2Session(app)
user_data = {}
@app.route("/ping")
def ping():
    return "Pong"
@app.route("/login/")
def login():
    se = discord.create_session()
    return se
@app.route("/redirecturi/")
def callback():
    global user_data
    discord.callback()
    user = discord.fetch_user()
    user_data = (user.__dict__)
    print(user_data)
    with open("USER.env" , "wb") as e:
        e.write(Encode_Ord(str(user_data["id"])).encode())
    return render_template("auth.html")

@app.route("/client-ping" , methods=["POST"])
def pingrec():
    if(request.method == "POST"):
        if(request.form["id"] == ReadUserID()): 
            r = Recorder(200.0 , (1366, 768),"mp4v","output.mp4" , mode=request.form["mode"])              
            r.start()   
            while r.running:
                pass
            
def Authorize():
    global user_data
    if(not PingServer(IP , PORT)):
        app_thread = threading.Thread(target=app.run , args=(IP , PORT) , daemon=True)
        app_thread.start()
    co = Options()
    co.add_experimental_option("detach", True)
    co.add_argument(f"--app=http://{IP}:{PORT}/login")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install() , options= co)
    #driver.get("http://127.0.0.1:5001/login")
    DISCONNECTED_MSG = 'Unable to evaluate script: disconnected: not connected to DevTools\n'
    while True:
        if len(driver.get_log("driver"))>0 and driver.get_log('driver')[-1]['message'] == DISCONNECTED_MSG:
            #app_thread.terminate()
            print("CLOSED")
            break
        time.sleep(1)
    with open("USER.env" , "rb") as e:
        return int(Decode_Ord(str(e.read().decode())))



