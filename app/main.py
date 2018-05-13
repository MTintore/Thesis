import pandas as pd
from flask import Flask,render_template,request
from objeto import Objeto
import Create_data as cd

registered=pd.read_csv("static/CSV/registered.csv",sep=',', delimiter=None, header='infer', encoding='cp1252',engine='python',dtype={"HSCHOOL":str,"HS_CODE":str})
grades=pd.read_csv("static/CSV/grades.csv",sep=',', delimiter=None, header='infer', encoding='cp1252',engine='python')

app=Flask(__name__)

registered=registered.sort_values(by=["HSCHOOL"],ascending=True)  
hsch=registered["HSCHOOL"].unique()

subjects=["Basic Mechanics","Calculus I","Chemistry I","Fundamentals of Informatics","Linear Algebra","Basic Thermodynamics","Calculus II","Chemistry II","Engineering Drawing","Geometry"]
group_sub=["Maths","Physics","Chemistry","Informatics"]
objeto = Objeto(hsch=hsch,subj=subjects,group=group_sub)

@app.route("/")
@app.route("/project")
def index():
    objeto.sname=None
    objeto.gsname=None
    objeto.hsname=None
    objeto.pubpri=False
    objeto.general=False
    return render_template("index.html",objeto=objeto)

@app.route("/students")
def students():
    objeto.sname=None
    objeto.gsname=None
    objeto.hsname=None
    objeto.pubpri=False
    objeto.general=False
    return render_template("students.html",objeto=objeto)

@app.route("/hschool")
def hschool():
    objeto.sname=None
    objeto.gsname=None
    objeto.hsname=None
    objeto.pubpri=False
    objeto.general=False
    return render_template("hschool.html",objeto=objeto)

@app.route("/me")
def me():
    objeto.sname=None
    objeto.gsname=None
    objeto.hsname=None
    objeto.pubpri=False
    objeto.general=False
    return render_template("me.html",objeto=objeto)

#/students
@app.route("/subject", methods=["POST"])
def subject():
    objeto.gsname=None
    objeto.hsname=None
    objeto.pubpri=False
    objeto.general=False
    objeto.sname = request.form.get("sname")
    cd.st_data(objeto.sname)
    return render_template("students.html", objeto=objeto)
@app.route("/group_s", methods=["POST"])
def group_s():
    objeto.hsname=None
    objeto.pubpri=False
    objeto.sname=None
    objeto.general=False
    objeto.gsname = request.form.get("gsname")
    cd.st_data(objeto.gsname)
    return render_template("students.html", objeto=objeto)
@app.route("/overall", methods=["POST"])
def overall():
    objeto.hsname=None
    objeto.pubpri=False
    objeto.sname=None
    objeto.gsname =None
    objeto.general=True
    cd.st_data()
    return render_template("students.html", objeto=objeto)

#/hschool
@app.route("/hsname", methods=["POST"])
def hsname():
    objeto.gsname=None
    objeto.sname=None
    objeto.general=False
    objeto.pubpri=False
    objeto.hsname = request.form.get("hsname")
    return render_template("hschool.html", objeto=objeto)
@app.route("/pubpri", methods=["POST"])
def pubpri():
    objeto.gsname=None
    objeto.sname=None
    objeto.general=False
    objeto.pubpri=True
    return render_template("hschool.html", objeto=objeto)
@app.route("/hs_subject", methods=["POST"])
def hs_subject():
    objeto.gsname=None
    objeto.general=False
    objeto.sname = request.form.get("sname")
    cd.hs_data(objeto.hsname,objeto.sname)
    return render_template("hschool.html", objeto=objeto)
@app.route("/hs_group_s", methods=["POST"])
def hs_group_s():
    objeto.sname=None
    objeto.general=False
    objeto.gsname = request.form.get("gsname")
    cd.hs_data(objeto.hsname,objeto.gsname)
    return render_template("hschool.html", objeto=objeto)
@app.route("/hs_overall", methods=["POST"])
def hs_overall():
    objeto.sname=None
    objeto.gsname =None
    objeto.general=True
    cd.hs_data(objeto.hsname)
    return render_template("hschool.html", objeto=objeto)


if __name__=="__main__":
    app.debug=True
    app.run()