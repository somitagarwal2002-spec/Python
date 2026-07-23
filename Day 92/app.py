from flask import Flask,render_template,request
from PIL import Image
import numpy as np
from collections import Counter
import os

app=Flask(__name__)
UPLOAD_PHOTO="Day 92/static"
app.config["UPLOAD_FOLDER"]=UPLOAD_PHOTO

def rgb_to_hex(rgb):
    return "#{:02X}{:02X}{:02X}".format(*rgb)

@app.route("/",methods=["GET","POST"])
def home():
    colors=[]
    image=None
    if request.method=="POST":
        f=request.files["image"]
        path=os.path.join(app.config["UPLOAD_FOLDER"],f.filename)
        f.save(path)
        image=f.filename
        img=Image.open(path).convert("RGB").resize((200,200))
        arr=np.array(img).reshape(-1,3)
        common=Counter(map(tuple,arr)).most_common(10)
        colors=[{"rgb":c,"hex":rgb_to_hex(c),"count":n} for c,n in common]
    return render_template("index.html",colors=colors,image=image)

if __name__=="__main__":
    app.run(debug=True)
