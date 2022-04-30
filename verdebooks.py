from distutils.log import debug
from flask import Flask, render_template, request, redirect, url_for, session, make_response
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_session import Session
from datetime import datetime
import mysql.connector as mysql
from flask import jsonify
from flask_cors import CORS
from datetime import datetime
from datetime import timedelta
from datetime import date
import random
import pdfkit
import mimerender
import imgkit

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret123123'
app.config['SESSION_TYPE'] = 'filesystem'

db_name = "addatsco_verdebooks"
db_password = "sohaib023612"
db_user = "addatsco_sohaib"
db_host = "162.214.195.234"

# SETUP HEADERS

CORS(app)

# DATABASE INITIALIZATION

def database():
    db = mysql.connect(host=db_host, user=db_user, passwd=db_password, database=db_name)
    cursor=db.cursor(buffered=True)
    return db,cursor

# RUN PAYROLL

def calculate(values):
    record={}
    RegCurrent=values["payRate"]*values["regHours"]
    record["RegCurrent"]=RegCurrent
    YTD=RegCurrent+values["YTDPrev"]
    record["YTD"]=YTD
    OTHours=values["OTHours"]
    record["OTHours"]=OTHours
    OTRate=values["payRate"]*1.5
    record["OTRate"]=OTRate
    OTCurrent=values["OTHours"]*OTRate
    record["OTCurrent"]=OTCurrent
    OTYTD=OTCurrent+values["OTYTDPrev"]
    record["OTYTD"]=OTYTD
    VACCurrent=(RegCurrent+OTCurrent+values["stat"])*0.04
    record["VACCurrent"]=VACCurrent
    VACYTD=VACCurrent+values["VACYTDPrev"]
    record["VACYTD"]=VACYTD
    StatHours=values["stat"]
    record["StatHours"]=StatHours
    StatRate=values["statRate"]
    record["StatRate"]=StatRate
    StatCurrent=values["stat"]+values["payRate"]
    record["StatCurrent"]=StatCurrent
    StatYTD=StatCurrent+values["StatYTDPrev"]
    record["StatYTD"]=StatYTD
    IncomeTax=(RegCurrent+OTCurrent+VACCurrent+StatCurrent)*0.0505
    record["IncomeTax"]=IncomeTax
    IncomeTaxYTD=IncomeTax+values["IncomeTaxYTDPrev"]
    record["IncomeTaxYTD"]=IncomeTaxYTD
    EI=(RegCurrent+OTCurrent+VACCurrent+StatCurrent)*0.0158
    record["EI"]=EI
    EIYTD=EI+values["EIYTDPrev"]
    record["EIYTD"]=EIYTD
    CPP=(RegCurrent+OTCurrent+VACCurrent+StatCurrent)*0.0545
    record["CPP"]=CPP
    CPPYTD=CPP+values["CPPYTDPrev"]
    record["CPPYTD"]=CPPYTD
    TotalPayCurrent=RegCurrent+OTCurrent+VACCurrent+StatCurrent
    record["TotalPayCurrent"]=TotalPayCurrent
    TotalPayYTD=TotalPayCurrent+values["TotalPayYTDPrev"]
    record["TotalPayYTD"]=TotalPayYTD
    TotalTaxCurrent=IncomeTax+EI+CPP
    record["TotalTaxCurrent"]=TotalTaxCurrent
    TotalTaxYTD=TotalTaxCurrent+values["TotalTaxYTDPrev"]
    record["TotalTaxYTD"]=TotalTaxYTD
    NetPay=TotalPayCurrent-TotalTaxCurrent
    record["NetPay"]=NetPay
    return record
    
@app.route("/api/runPayRoll",methods=["GET","POST"])
def runPayRoll():
    db,cursor=database()
    data=request.form
    employees=data["employees"]
    employees=employees.split(",")
    print("employees",employees)
    regularPayHours=data["payHours"]
    regularPayHours=regularPayHours.split(",")
    print('regularPayHours',regularPayHours)
    otHours=data["otHours"]
    otHours=otHours.split(",")
    print('otHours',otHours)
    stat=data["stat"]
    stat=stat.split(",")
    print('stat',stat)
    memo=data["memo"]
    memo=memo.split(",")
    print('memo',memo)
    payDate=data["payDate"]
    week=data["week"]
    week=week.split(" - ")
    print('week',week)
    generateDate=str(datetime.today().strftime('%Y-%m-%d'))
    for i in range(len(employees)):
        query="select id from stubs where employeeId=%s and weekStart=%s and weekEnd=%s"
        values=(employees[i],week[0],week[1])
        cursor.execute(query,values)
        result=cursor.fetchall()
        if result:pass
        else:
            query1="select YTD,OTHours,OTYTD,VACYTD,StatYTD,EIYTD,CPPYTD,IncomeTaxYTD,TotalTaxYTD,TotalPayYTD,StatHours,StatRate from stubs where employeeId=%s order by id desc limit 1"
            cursor.execute(query1,(employees[i],))
            result1=cursor.fetchone()
            print("result1",result1)
            if result1:
                query2="select name,payRate from employee where id=%s"
                cursor.execute(query2,(employees[i],))
                result2=cursor.fetchone()
                print(result2)
                if result2:
                    temp={"payRate":float(result2[1]),"regHours":float(regularPayHours[i]),"YTDPrev":float(result1[0]),"OTHours":float(otHours[i]),"OTYTDPrev":float(result1[2]),
                    "stat":float(stat[i]),"VACYTDPrev":float(result1[3]),"payDate":payDate,"StatYTDPrev":float(result1[4]),"IncomeTaxYTDPrev":float(result1[7]),"EIYTDPrev":float(result1[5]),
                    "CPPYTDPrev":float(result1[6]),"TotalTaxYTDPrev":float(result1[8]),"TotalPayYTDPrev":float(result1[9]),"statRate":float(result1[10])}
                    record=calculate(temp)
                    record["name"]=result2[0]
                    record["employeeId"]=employees[0]
                    query3="insert into stubs(`generateDate`, `payDate`, `name`, `RegCurrent`, `YTD`, `OTHours`, `OTRate`, `OTCurrent`, `OTYTD`, `VACCurrent`, `VACYTD`, `StatHours`, `StatRate`, `StatYTD`, `IncomeTax`, `IncomeTaxYTD`, `EI`, `EIYTD`, `CPP`, `CPPYTD`, `TotalPayCurrent`, `TotalPayYTD`, `TotalTaxCurrent`, `TotalTaxYTD`, `NetPay`, `employeeId`, `status`,`weekStart`,`weekEnd`,`regHours`)  value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    values3=(generateDate, payDate, result2[0], record["RegCurrent"], record["YTD"], record["OTHours"], record["OTRate"], record["OTCurrent"], record["OTYTD"], record["VACCurrent"],
                    record["VACYTD"], record["StatHours"], record["StatRate"], record["StatYTD"], record["IncomeTax"], record["IncomeTaxYTD"], record["EI"], record["EIYTD"], record["EIYTD"],
                    record["CPPYTD"], record["TotalPayCurrent"], record["TotalPayYTD"], record["TotalTaxCurrent"],record["TotalTaxYTD"], record["NetPay"], employees[i], "original",week[0],week[1],regularPayHours[i])
                    cursor.execute(query3,values3)
                    db.commit()
    response=[]
    for i in range(len(employees)):
        query="select * from stubs where employeeId=%s and weekStart=%s and weekEnd=%s"
        values=(employees[i],week[0],week[1])
        cursor.execute(query,values)
        result=cursor.fetchone()
        if result:
            columns=("id", "generateDate", "payDate", "name", "RegCurrent", "YTD", "OTHours", "OTRate", "OTCurrent", "OTYTD", "VACCurrent", "VACYTD", "StatHours", "StatRate", "StatYTD", "IncomeTax", "IncomeTaxYTD", "EI", "EIYTD", "CPP", "CPPYTD", "TotalPayCurrent", "TotalPayYTD", "TotalTaxCurrent", "TotalTaxYTD", "NetPay", "employeeId", "status", "weekStart", "weekEnd", "regHours")
            temp={}
            for j in range(len(columns)):
                temp[columns[j]]=result[j]
            response.append(temp)
    return jsonify({"response":response})

#  FETCH EMPLOYEES

@app.route("/api/allEmployees",methods=['GET','POST'])
def allEmployees():
    db,cursor=database()
    query="select id,paymentMethod,name from employee"
    cursor.execute(query)
    result=cursor.fetchall()
    response=[]
    for row in result:
        temp={"id":row[0],"paymentMethod":row[1],"name":row[2]}
        response.append(temp)
    return jsonify({"response":response})

# ADD EMPLOYEE

@app.route("/api/addEmployee",methods=["GET","POST"])
def addEmployee():
    db,cursor=database()
    data=request.form
    query="INSERT INTO `employee`(`name`, `jobTitle`, `status`, `hireDate`, `dob`, `workingLocation`, `accountHolder`,`bankName`, `accountNumber`, `branchName`, `bankLocation`, `address`, `town`, `postalCode`, `phn`, `phn2`, `gender`, `notes`, `mi`, `payRate`, `payType`, `vacPolicy`, `deduction`, `paymentMethod`, `email`)  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values=( data["name"], data["jobTitle"], data["status"], data["hireDate"], data["dob"], data["workingLocation"], data["accountHolder"],data["bankName"],data["accountNumber"], data["branchName"], data["bankLocation"], data["address"], data["town"], data["postalCode"], data["phn"], data["phn2"],data["gender"], data["notes"], data["mi"], data["payRate"], data["payType"], data["vacPolicy"], data["deduction"], data["paymentMethod"], data["email"])
    cursor.execute(query,values)
    db.commit()
    query3="select id from employee order by id desc limit 1"
    cursor.execute(query3)
    result3=cursor.fetchone()
    query2="insert into stubs(`generateDate`, `payDate`, `name`, `RegCurrent`, `YTD`, `OTHours`, `OTRate`, `OTCurrent`, `OTYTD`, `VACCurrent`, `VACYTD`, `StatHours`, `StatRate`, `StatYTD`, `IncomeTax`, `IncomeTaxYTD`, `EI`, `EIYTD`, `CPP`, `CPPYTD`, `TotalPayCurrent`, `TotalPayYTD`, `TotalTaxCurrent`, `TotalTaxYTD`, `NetPay`, `employeeId`, `status`,`weekStart`,`weekEnd`,`regHours`)  value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    generateDate=str(datetime.today().strftime('%Y-%m-%d'))
    values2=(generateDate,0,data["name"],0,0,0,0,0,0,0,0,0,1.5,0,0,0,0,0,0,0,0,0,0,0,0,result3[0],'initial',0,0,0)
    cursor.execute(query2,values2)
    db.commit()
    return jsonify({"response":"done"})

# FETCH CHEQUE

@app.route("/api/employeeStubList/<data>", methods=["GET","POST"])
def employeeChequeList(data):
    db,cursor=database()
    query="select payDate,name,NetPay,id from stubs where employeeId=%s"
    value=(data,)
    cursor.execute(query,value)
    result=cursor.fetchall()
    response=[]
    for row in result:
        temp={"payDate":row[0],"name":row[1],"totalPay":row[2],"netPay":row[2],"paymentMethod":"bank","id":row[3]}
        response.append(temp)
    return jsonify({"response":response})

# FETCH EMPLOYEE DETAIL

@app.route("/api/employeeProfile/<data>",methods=["GET","POST"])
def employeeProfile(data):
    db,cursor=database()
    query="select * from employee where id=%s"
    cursor.execute(query,(data,))
    result=cursor.fetchone()
    print(len(result))
    print(result)
    response={"name":result[1],"jobTitle":result[2],"status":result[3],"hireDate":result[4],"dob":result[5],"workingLocation":result[6],"accountHolder":result[7],"bankName":result[8],"accountNumber":result[9],"branchName":result[10]
    ,"bankLocation":result[11],"address":result[12],"town":result[13],"postalCode":result[14],"phn":result[15],"phn2":result[16],"gender":result[17],"notes":result[18],"mi":result[19],"payRate":result[20],"payType":result[21],
    "vacPolicy":result[22],"deduction":result[23],"paymentMethod":result[24],"email":result[25]}
    return jsonify({"response":response})

# FETCH DATES

def numOfDays(date1, date2):
    return (date2-date1).days

@app.route("/api/getDates/<year>",methods=["GET","POST"])
def getDates(year):
    # Driver program
    start_date = date(2000,1,7)
    date2 = date.today()
    print(date2.year)
    days=numOfDays(start_date, date2)
    print(days)
    days=int(days/7)
    print(days)
    start_date=str(start_date)
    start_date=datetime.strptime(start_date, "%Y-%m-%d").strftime("%Y-%m-%d")
    fridays=[]
    dateRanges=[]
    count=0
    for i in range(days):
        previous=str(datetime.strptime(start_date, "%Y-%m-%d")+timedelta(days=1))
        friday=datetime.strptime(start_date, "%Y-%m-%d")+timedelta(days=7)
        generatedDate=str(friday)
        generatedDate=generatedDate[0:10]
        friday=datetime.strptime(str(friday.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
        start_date=friday
        dateRange=previous[0:10] +" - " + str(generatedDate)
        if dateRange=="":
            pass
        else:
            if year in str(generatedDate):
                fridays.append(str(generatedDate))
                dateRanges.append(dateRange)
                count=count+1
    print(fridays)
    print(dateRanges)
    return jsonify({"dateRanges":dateRanges,"count":count})

# LOGIN

@app.route("/api/login")
def login():
    db,cursor=database()
    data=request.form
    query="select id,password from usersData where email=%s"
    cursor.execute(query,(data["email"],))
    result=cursor.fetchone()
    response=""
    if result:
        if result[1]==data["password"]:
            response="Success"
        else:
            response="Invalid Password"
    else:
        response="Invalid Email or Password"
    return jsonify({"response":response})

# PRINT STUB

@app.route("/api/printStub/<data>",methods=["GET","POST"])
def printStub(data):
    db,cursor=database()
    query="select name,weekEnd,weekStart,payDate,NetPay,RegCurrent,RegCurrent,VACCurrent,VACYTD,statRate,TotalTaxCurrent,TotalTaxYTD,NetPay,TotalPayYTD,EI,EIYTD,CPP,CPPYTD,employeeId,YTD,StatYTD,IncomeTax,IncomeTaxYTD,regHours from stubs where id=%s"
    cursor.execute(query,(data,))
    result=cursor.fetchone()
    if result:
        query2="select address,town,payRate from employee where id=%s"
        cursor.execute(query2,(result[18],))
        result2=cursor.fetchone()
        sendData=[result[0],result[0],result2[0],result2[0],result2[1],result2[1],result[1],result[2],"PAY DATE: "+str(result[3]),result[3],"{:.2f}".format(float(result[4])),
        "$"+str(result[4]),"$"+str(result[4]),str(result[5]),str(result[6])+".00",str(result[6])+".00",str(result[6])+".00",str(result[7]),str(result[8])+".00",str(result[9])+".00 "+str(result[9])+".00",str(result[9])+".00",
        "{:.2f}".format(float(result[10])),"{:.2f}".format(float(result[11])),"{:.2f}".format(float(result[12])),"{:.2f}".format(float(result[13])),str("{:.2f}".format(float(result[14]))),
        "{:.2f}".format(float(result[15])),"{:.2f}".format(float(result[16])),"{:.2f}".format(float(result[17])),result2[2]+".00 "+result2[2]+".00",result[19],result[20],"{:.2f}".format(float(result[21])),"{:.2f}".format(float(result[22])),result[23]]
        print(sendData)
        return render_template("generateSlip.html",data=sendData)
    else:
        return jsonify({"response":"Invalid Id"})

# RUN APPLICATION

if __name__=="__main__":
    app.secret_key="Infiniti123"
    context=('addats.crt','addats.key')
    app.run(port=2211,debug=True,ssl_context=context,threaded=True,host='162.214.195.234')
