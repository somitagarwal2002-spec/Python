from flask import Flask,render_template,request
import requests

app=Flask(__name__)
API="https://api.dictionaryapi.dev/api/v2/entries/en/{}"

@app.route("/",methods=["GET","POST"])
def home():
    result=None
    word=""
    if request.method=="POST":
        word=request.form.get("word","").strip()
        if word:
            r=requests.get(API.format(word),timeout=20)
            if r.status_code==200:
                data=r.json()[0]
                meanings=[]
                for m in data.get("meanings",[]):
                    part=m.get("partOfSpeech","")
                    defs=[d["definition"] for d in m.get("definitions",[])[:2]]
                    meanings.append({"part":part,"defs":defs})
                result={"word":data["word"],"phonetic":data.get("phonetic",""),"meanings":meanings}
            else:
                result={"error":"Word not found."}
    return render_template("index.html",result=result,word=word)

if __name__=="__main__":
    app.run(debug=True)
