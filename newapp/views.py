from django.shortcuts import render,redirect
from newapp.forms import empregform
from newapp.models import empregmodel,empanotherdatamodel
import pdfkit
from django.http import HttpResponse
# Create your views here.
def empreg(request) :
    return render (request ,'empreg.html')


def empregsave(request) :
    if request.method == 'POST' :
        form = empregform (request.POST)
        # return HttpResponse(form)
        if form.is_valid ( ) :
            try :
                form.save ( )
                return redirect ('/empshow')
            except :
                return HttpResponse ('except block')
        else :
            return HttpResponse ("fail")


def empshow(request) :
    data = empregmodel.objects.all ( )
    dataa= empanotherdatamodel.objects.all()
    # return HttpResponse(dataa)
    return render (request , "empshow.html" , { 'data' : data,'dataa':dataa})


def empedit(request , id) :
    data = empregmodel.objects.get (id = id)
    return render (request , 'empedit.html' , { 'data' : data })


def empupdate(request , id) :
    data = empregmodel.objects.get (id = id)
    form = empregform (request.POST , instance = data)
    if form.is_valid ( ) :
        form.save ( )
        return redirect ("/empshow")
    return render (request , 'empedit.html' , { 'data' : data })


def empdestroy(request , id) :
    data = empregmodel.objects.get (id = id)
    data.delete ( )
    return redirect ("/empshow")

def total(request , id) :
    total = empregmodel.objects.get (id = id)
    # return HttpResponse(total.id)
    id = total.id
    emp_name = total.emp_name
    emp_address = total.emp_address
    emp_gender = total.emp_gender
    emp_number = total.emp_number
    emp_salary = total.emp_salary
    empemail = total.empemail
    emp_photo = total.emp_photo
    emp_joindate = total.emp_joindate

    dataa = empanotherdatamodel.objects.get(emp_name=emp_name)
    emp_namee=dataa.emp_name
    # return HttpResponse(dataa)
    emp_color=dataa.emp_color
    # return HttpResponse (emp_color)
    emp_height = dataa.emp_height
    emp_ofc=dataa.emp_ofc
    # return HttpResponse(emp_joindate)
    htmlpage = "<html><head></head><body><a href='/empshow'>total emp list</a><h1 style='color:red'>SINGLE EMP DETAILS</h1>empid:" + str (
        id) + "<br>emp_name:" + str (emp_name) + "<br>emp_address:" + str (emp_address) + "<br>emp_gender:" + str (
        emp_gender) + "<br>emp_number:" + str (emp_number) + "<br>emp_salary:" + str (
        emp_salary) + "<br>empemail:" + str (empemail) + "<br>emp_photo:" + str (
        emp_photo) + "<br>emp_joindate:" + str (emp_joindate) + "<br><hr>emp_namee:"+str(emp_namee)+"<br>emp_color:"+str(emp_color)+"<br>emp_height:"+str(emp_height)+"<br>emp_ofc:"+str(emp_ofc)+"</body></html>"
    return HttpResponse (htmlpage)


