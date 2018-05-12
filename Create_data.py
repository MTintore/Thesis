import pandas as pd

students_data=pd.read_csv("static/CSV/students.csv",sep=',', delimiter=None, header='infer', encoding='cp1252',engine='python')
hsyear=pd.read_csv("static/CSV/hsyear.csv",sep=',', delimiter=None, header='infer', encoding='cp1252',engine='python')
hsglobal=pd.read_csv("static/CSV/hsglobal.csv",sep=',', delimiter=None, header='infer', encoding='cp1252',engine='python')
pp=pd.read_csv("static/CSV/pubpri.csv",sep=',', delimiter=None, header='infer', encoding='cp1252',engine='python')

def st_data(sg=None):
    if sg != None:
        #remove the ones not coursed the subject
        sg_data=students_data[["GENDER","AC_YEAR","AC_GRADE",sg,"MEAN_CRED","STD","PASSED","FAILED","NUM_SUBJ","ALPHA"]]
    else:
        sg_data=students_data[["GENDER","AC_YEAR","AC_GRADE","MEAN_CRED","STD","PASSED","FAILED","NUM_SUBJ","ALPHA"]]
        passed_first_all(sg_data)
        alfa_access(sg_data)
        amean_access(sg_data)
        amean_year(sg_data)
    #llamar a todas las funciones de cada grafico para que escriban los csv
    histogram(sg_data)
    grade_year(sg_data)
    boxplot_year(sg_data)
    grade_access(sg_data)
    number_students(sg_data)

def hs_data(hs=None,sg=None):
    if hs != None:
        sg_data_hs=students_data[(students_data["HSCHOOL"]==hs)]
        sg_data_hs.drop(labels=["HSCHOOL"],axis=1,inplace=True)
        if sg != None:
            sg_data_hs=sg_data_hs[["GENDER","AC_YEAR","AC_GRADE",sg,"MEAN_CRED","STD","PASSED","FAILED","NUM_SUBJ","ALPHA"]]
            sg_data=students_data[["GENDER","AC_YEAR","AC_GRADE",sg,"MEAN_CRED","STD","PASSED","FAILED","NUM_SUBJ","ALPHA"]]
        else:
            sg_data_hs=sg_data_hs[["GENDER","AC_YEAR","AC_GRADE","MEAN_CRED","STD","PASSED","FAILED","NUM_SUBJ","ALPHA"]]
            sg_data=students_data[["GENDER","AC_YEAR","AC_GRADE","MEAN_CRED","STD","PASSED","FAILED","NUM_SUBJ","ALPHA"]]
            passed_first_all(sg_data_hs)
            alfa_access(sg_data_hs)
            amean_access(sg_data_hs)
            amean_year(sg_data_hs)
            amean_hs(sg_data,sg_data_hs)
            alpha_hs(sg_data,sg_data_hs)
        grade_year_hs(sg_data,sg_data_hs)
        boxplot_year(sg_data_hs)
        grade_access(sg_data_hs)
        number_students(sg_data_hs)
        #funciones especificas de hs
    #else:
        #hs_data=pp
        #if sg != None:
            #sg_data=hs_data[["AC_YEAR","TYPE","AC_GRADE",sg,"STD","PASSED","FAILED","NUM_SUBJ","ALPHA","RANKING","NUM_STUD","TOTAL_STUD","%"]]
            #i already have the number of students!!!! passed_first_sg(sg_data,sg)
        #else:
            #sg_data=hs_data[["AC_YEAR","TYPE","AC_GRADE","MEAN_CRED","STD","PASSED","FAILED","NUM_SUBJ","ALPHA","RANKING","NUM_STUD","TOTAL_STUD","%"]]
            #passed_first_all(sg_data)
            #alfa_access(sg_data)
            #amean_access(sg_data)
        #grade_year(sg_data)
        #grade_access(sg_data)

def grade_year(df):
    df=df[["AC_YEAR",(df.columns[3])]]
    df=df.dropna(axis=0, how='any')
    df=df.groupby(["AC_YEAR"])
    df=df.mean()
    df=df.reset_index()
    df=df.round(decimals=3)
    df.rename(index=str, columns={(df.columns[1]):"Mean"},inplace=True)
    df.to_csv("static/CSV/Chart_data/grade_year.csv", index=False)

def grade_year_hs(df,df_hs):
    df=df[["AC_YEAR",(df.columns[3])]]
    df=df.dropna(axis=0, how='any')
    df=df.groupby(["AC_YEAR"])
    df=df.mean()
    df=df.reset_index()
    df=df.round(decimals=3)
    df.rename(index=str, columns={"MEAN_CRED":"Mean"},inplace=True)
    df.rename(index=str, columns={(df.columns[1]):(df.columns[1])+" global"},inplace=True)

    df_hs=df_hs[["AC_YEAR",(df_hs.columns[3])]]
    df_hs=df_hs.dropna(axis=0, how='any')
    df_hs=df_hs.groupby(["AC_YEAR"])
    df_hs=df_hs.mean()
    df_hs=df_hs.reset_index()
    df_hs=df_hs.round(decimals=3)
    df_hs.rename(index=str, columns={"MEAN_CRED":"Mean"},inplace=True)

    df_total=pd.merge(df,df_hs,how='inner')
    df_total.to_csv("static/CSV/Chart_data/grade_year.csv", index=False)

def boxplot_year(df):
    df=df[["AC_YEAR",(df.columns[3])]]
    df = df.set_index([df.groupby('AC_YEAR').cumcount(), 'AC_YEAR'])[(df.columns[1])].unstack()
    df=df.round(decimals=3)
    df=df.dropna(axis=0, how='any')
    df.rename(index=str, columns={2010:"Y2010",2011:"Y2011",2012:"Y2012",2013:"Y2013",2014:"Y2014",2015:"Y2015"},inplace=True)
    df.to_csv("static/CSV/Chart_data/boxplot_year.csv", index=False)

def histogram(df):
    df=df[(df.columns[3])]
    df=df.round(decimals=1)
    df=df.rename("Subject")
    df.to_csv("static/CSV/Chart_data/histogram.csv", index=False, header=True)

def number_students(df):
    df=df[["GENDER","AC_YEAR",(df.columns[3])]]
    df=df.dropna(axis=0, how='any')
    df[(df.columns[2])]=(df[(df.columns[2])]>=5)
    df[(df.columns[2])].replace({False:0,True:1},inplace=True)
    s = df.groupby(["GENDER","AC_YEAR"]).size()
    df["NUM_STUD"] = df.set_index(["GENDER","AC_YEAR"]).index.map(s.get)
    df = df.groupby(["GENDER","AC_YEAR"]).agg({(df.columns[2]): 'sum','NUM_STUD':'mean'})
    df=df.reset_index()

    df1=df[["GENDER","AC_YEAR",(df.columns[2])]]
    df1=df1.pivot_table(index="AC_YEAR",columns="GENDER",values=(df.columns[2]))
    df1=df1.reset_index()
    df1.rename(index=str, columns={"H":"Passed men","D":"Passed women"},inplace=True)

    df2=df[["GENDER","AC_YEAR","NUM_STUD"]]
    df2=df2.pivot_table(index="AC_YEAR",columns="GENDER",values="NUM_STUD")
    df2=df2.reset_index()
    df2.rename(index=str, columns={"H":"Total men","D":"Total women"},inplace=True)

    df3=pd.merge(df1,df2,how='inner')
    df3.to_csv("static/CSV/Chart_data/number_students.csv", index=False)

def passed_first_all(df):
    df=df[["AC_YEAR","PASSED"]]
    df=df.groupby(["AC_YEAR"])
    df=df.mean()
    df=df.reset_index()
    df=df.round(decimals=2)
    df.to_csv("static/CSV/Chart_data/passed_first_all.csv", index=False)

def grade_access(df):
    df=df[["AC_GRADE",(df.columns[3])]]
    df=df.round(decimals=2)
    df.rename(index=str, columns={"AC_GRADE":"Access_grade"},inplace=True)
    df.to_csv("static/CSV/Chart_data/grades_access.csv", index=False)

def grade_access_hs(df,df_hs):
    df=df[["AC_GRADE",(df.columns[3])]]
    df=df.round(decimals=2)
    df.rename(index=str, columns={"AC_GRADE":"Access_grade",(df.columns[1]):(df.columns[1])+" global" },inplace=True)
    
    df=df[["AC_GRADE",(df.columns[3])]]
    df=df.round(decimals=2)
    df.rename(index=str, columns={"AC_GRADE":"Access_grade",(df.columns[1]):(df.columns[1])+" global" },inplace=True)
    
    df.to_csv("static/CSV/Chart_data/grades_access.csv", index=False)

def alfa_access(df):
    df=df[["AC_GRADE","ALPHA"]]
    df=df.round(decimals=2)
    df.to_csv("static/CSV/Chart_data/alpha_access.csv", index=False)

def amean_access(df):
    df=df[["AC_GRADE","MEAN_CRED","ALPHA"]]
    df["AC_GRADE"]=df["AC_GRADE"]*(10/14)
    df["A*MEAN"]=df["MEAN_CRED"]*df["ALPHA"]
    df=df.round(decimals=2)
    df.to_csv("static/CSV/Chart_data/amean_access.csv", index=False)

def amean_year(df):
    df=df[["AC_YEAR","MEAN_CRED","ALPHA"]]
    df["A*MEAN"]=df["MEAN_CRED"]*df["ALPHA"]
    df=df.groupby(["AC_YEAR"])
    df=df.mean()
    df=df.reset_index()
    df=df.round(decimals=2)
    df.rename(index=str, columns={"MEAN_CRED":"Mean","A*MEAN":"aMean","ALPHA":"a"},inplace=True)
    df.to_csv("static/CSV/Chart_data/amean_year.csv", index=False)

def amean_hs(df,df_hs):
    df=df[["AC_YEAR","MEAN_CRED","ALPHA"]]
    df["aMean global"]=df["MEAN_CRED"]*df["ALPHA"]
    df=df.groupby(["AC_YEAR"])
    df=df.mean()
    df=df.reset_index()
    df.drop(labels=["MEAN_CRED","ALPHA"],axis=1, inplace=True)
    df=df.round(decimals=2)

    df_hs=df_hs[["AC_YEAR","MEAN_CRED","ALPHA"]]
    df_hs["aMean"]=df_hs["MEAN_CRED"]*df_hs["ALPHA"]
    df_hs=df_hs.groupby(["AC_YEAR"])
    df_hs=df_hs.mean()
    df_hs=df_hs.reset_index()
    df_hs.drop(labels=["MEAN_CRED", "ALPHA"],axis=1, inplace=True)
    df_hs=df_hs.round(decimals=2)

    df_total=pd.merge(df,df_hs,how='inner')
    df_total.to_csv("static/CSV/Chart_data/amean.csv", index=False)

def alpha_hs(df,df_hs):
    df=df[["AC_YEAR","ALPHA"]]
    df=df.groupby(["AC_YEAR"])
    df=df.mean()
    df=df.reset_index()
    df=df.round(decimals=2)
    df.rename(index=str, columns={"ALPHA":"Alpha global"},inplace=True)

    df_hs=df_hs[["AC_YEAR","ALPHA"]]
    df_hs=df_hs.groupby(["AC_YEAR"])
    df_hs=df_hs.mean()
    df_hs=df_hs.reset_index()
    df_hs=df_hs.round(decimals=2)
    df_hs.rename(index=str, columns={"ALPHA":"Alpha"},inplace=True)

    df_total=pd.merge(df,df_hs,how='inner')
    df_total.to_csv("static/CSV/Chart_data/alpha.csv", index=False)

#def general_overall_year(df):
    #df=df[["AC_YEAR","MEAN_CRED","PASSED","FAILED","ALPHA"]]
    #df["A*MEAN"]=df["MEAN_CRED"]*df["ALPHA"]
    #df.drop(labels=["ALPHA"],axis=1,inplace=True)
    #df=df.groupby(["AC_YEAR"])
    #df=df.mean()
    #df=df.reset_index()
    #df=df.round(decimals=2)
    #df=df[["AC_YEAR","PASSED","FAILED","MEAN_CRED","A*MEAN"]]
    #df.rename(index=str, columns={"MEAN_CRED":"Mean","A*MEAN":"aMean","PASSED":"Passed","FAILED":"Failed"},inplace=True)
    #df.to_csv("static/CSV/Chart_data/general_overall_year.csv", index=False)

#def passed_first_sg(df,sg):
    #df=df[["AC_YEAR",(df.columns[3])]]
    #df=df.dropna(axis=0, how='any')
    #s = df.groupby(["AC_YEAR"]).size()
    #df["NUM_STUD"] = df.set_index(["AC_YEAR"]).index.map(s.get)
    #df[sg]=(df[sg]>=5)
    #df[sg].replace({False:0,True:1},inplace=True)
    #df = df.groupby(["AC_YEAR"]).agg({sg: 'sum','NUM_STUD':'mean'})
    #df=df.reset_index()
    #df["% Passed"]=(df[sg]/df["NUM_STUD"])*100
    ##df["Failed"]=100-df["Passed"]
    #df=df.round(decimals=2)
    #df=df[["AC_YEAR","% Passed"]]
    #df.to_csv("static/CSV/Chart_data/passed_first.csv", index=False)

#def ranking(df):