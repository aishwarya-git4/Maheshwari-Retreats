from django.shortcuts import render,HttpResponse
from .forms import *
from .import views
from .models import *
import json
from datetime import datetime, timedelta
def index(request):
    fb=Feedbackmodel.objects.all().order_by('?')[:5]
    if request.method=='POST':
        feedback=Feedbackform(request.POST)
        feedback2=Feedbackform()
        if feedback.is_valid():
            feedback.save()
            return render(request,'index.html',{'form':feedback2,'recs':fb})
        else:
            return render(request,'index.html',{'form':feedback,'recs':fb})
    else:
        feedback=Feedbackform()
    
        return render(request,'index.html',{'form':feedback,'recs':fb})
def search(request):
    l=[]
    query=request.GET.get("search")
    for rec in Storage.objects.all():
        if query.lower() in rec.name.lower() or query.lower() in rec.place.lower():
            l.append(rec)
    return render(request,'searchbar.html',{'results':l})


            
    
def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'service.html')
def package(request):
    return render(request,'package.html')

def booking(request):
    if request.method=='POST':
        details=Bookingform(request.POST)
        if details.is_valid():
            flag=0
            if details.cleaned_data.get('have_you_availed_membership')=='Yes':
                recs=Membershipmodel.objects.all()
                for rec in recs:
                    if rec.name==details.cleaned_data.get('name') and rec.email==details.cleaned_data.get('email'):
                        if checkbook(request,details.cleaned_data.get('destination'),details.cleaned_data.get('type_of_room'),details.cleaned_data.get('check_in_date'),details.cleaned_data.get('check_out_date')):
                            return render(request,'backtohomepage.html')
                        else:
                            return HttpResponse('Please choose another date!')
                        
                else:
                    details._errors['have_you_availed_membership']=details.error_class(['You are not a member'])
                    return render(request,'booking.html',{'form':details})
            else:
                recs=Membershipmodel.objects.all()#all instances of Membership model
                for rec in recs:
                    if rec.name==details.cleaned_data.get('name') and rec.email==details.cleaned_data.get('email'):
                        details._errors['have_you_availed_membership']=details.error_class(['You are a member'])
                        return render(request,'booking.html',{'form':details})
                if checkbook(request,details.cleaned_data.get('destination'),details.cleaned_data.get('type_of_room'),details.cleaned_data.get('check_in_date'),details.cleaned_data.get('check_out_date')):
                    request.session['form_data2'] = details.cleaned_data
                    (t,gt)=amount(details.cleaned_data.get('type_of_room'),details.cleaned_data.get('check_in_date'),details.cleaned_data.get('check_out_date'))
                    return render(request,'payment2.html',{'t':t,'gt':gt})
                else:
                    return HttpResponse('Please choose another date!')
        else:
            return render(request,'booking.html',{'form':details})
    else:
        form=Bookingform(None)
        return render(request,'booking.html',{'form':form})

def amount(room,ind,outd):
    date_format="%Y-%m-%d"
    indd=datetime.strptime(ind,date_format)
    outdd=datetime.strptime(outd,date_format)
    n=outdd-indd
    if room=='S':
        return (5000*n.days,5000+0.2*5000*n.days)
    elif room=='1':
        return (7500*n.days,7500+0.2*7500*n.days)
    elif room=='2':
        return (10000*n.days,10000+0.2*10000*n.days)
        









def checkbook(request,place,roomt,checkin,checkout):
    date_format="%Y-%m-%d"
    in_date=datetime.strptime(checkin,date_format)
    out_date=datetime.strptime(checkout,date_format)
    avail_list=[]
    booking_list=Bookingmodel.objects.filter(destination=place,type_of_room=roomt)
    if roomt=='S':
        for i in range(100,106):
            studios=booking_list.filter(room_num=i)
            for book in studios:
                recindate=datetime.strptime(book.check_in_date,date_format)
                recoutdate=datetime.strptime(book.check_out_date,date_format)
                if recindate>out_date or in_date>recoutdate:
                    avail_list.append(True)
                else:
                    avail_list.append(False)
            if all(avail_list):
                request.session['room']=i
                return 1
        else:
            return 0
    elif roomt=='1':
        for i in range(106,111):
            onebed=booking_list.filter(room_num=i)
            for book in onebed:
                recindate=datetime.strptime(book.check_in_date,date_format)
                recoutdate=datetime.strptime(book.check_out_date,date_format)
                if recindate>out_date or in_date>recoutdate:
                    avail_list.append(True)
                else:
                    avail_list.append(False)
            if all(avail_list):
                request.session['room']=i
                return 1
        else:
            return 0
    elif roomt=='2':
        for i in range(111,116):
            twobed=booking_list.filter(room_num=i)
            for book in twobed:
                recindate=datetime.strptime(book.check_in_date,date_format)
                recoutdate=datetime.strptime(book.check_out_date,date_format)
                if recindate>out_date or in_date>recoutdate:
                    avail_list.append(True)
                else:
                    avail_list.append(False)
            if all(avail_list):
                request.session['room']=i
                return 1
        else:
            return 0
                
'''
            rooms=Roomsmodel.objects.all()
            for room in rooms:
                if room.name==details.cleaned_data.get('destination'):
                    if details.cleaned_data.get('type_of_room')=='S' and room.studio==0:
                        details._errors['type_of_room']=details.error_class(['Booking studiofull'])
                        return render(request,'booking.html',{'form':details})
                    elif details.cleaned_data.get('type_of_room')=='1' and room.onebed==0:
                        details._errors['type_of_room']=details.error_class(['Booking onebedfull'])
                        return render(request,'booking.html',{'form':details})
                    elif details.cleaned_data.get('type_of_room')=='2' and room.twobed==0:
                        details._errors['type_of_room']=details.error_class(['Booking twobedfull'])
                        return render(request,'booking.html',{'form':details})
                    else:
                        request.session['form_data2'] = details.cleaned_data
                        if flag==0:
                            return render(request,'payment2.html')
                        else:
                            return HttpResponse(request,'Booking successful')
        else:
            return render(request,'booking.html',{'form':details})
    else:
        form=Bookingform(None)
        return render(request,'booking.html',{'form':form})'''

def bookingpaid(request):
    details=request.session.get('form_data2')
    details1=Bookingform(details)
    if details1.is_valid():
        post=details1.save(commit=False)#post is an instance of model
        post.save()
        #json_data=post.to_json()  #Serialize the model instance to JSON
        #json_data_dict=json.loads(json_data)
    rooms=Bookingmodel.objects.filter(name=details1.cleaned_data.get('name'),email=details1.cleaned_data.get('email'),check_in_date=details1.cleaned_data.get('check_in_date'))
    for room in rooms:
        room.room_num=request.session.get('room')
        room.save()
    '''for room in rooms:
        if room.name==details1.cleaned_data.get('destination'):
            if details1.cleaned_data.get('type_of_room')=='S':
                room.studio-=1
                room.save()
            elif details1.cleaned_data.get('type_of_room')=='1':
                room.onebed-=1
                room.save()
            elif details.cleaned_data.get('type_of_room')=='2':
                room.twobed-=1
                room.save()'''
    #return (JsonResponse(json_data_dict),HttpResponse("Booking confirmed"))
    return render(request,'backtohomepage.html')
def error(request):
    return render(request,'error.html')
def northindia(request):
    return render(request,'northindia.html')
def southindia(request):
    return render(request,'southindia.html')
def international(request):
    return render(request,'international.html')
def asia(request):
    return render(request,'asia.html')
def europe(request):
    return render(request,'europe.html')
def india(request):
    return render(request,'india.html')

def membership(request):
    if request.method=='POST':
        details=Membershipform(request.POST)
        if not details.is_valid():
            return render(request,'membership.html',{'form':details})
        else:
            request.session['form_data'] = details.cleaned_data
            return render(request,'payment.html')
    else:
        form=Membershipform(None)
        return render(request,'membership.html',{'form':form})
def membershippaid(request):
    details=request.session.get('form_data')
    details1=Membershipform(details)
    post=details1.save(commit=False)
    post.save()
    return HttpResponse("data submitted")
    
def testimonial(request):
    return render(request,'testimonial.html')
def contact(request):
    return render(request,'contact.html')
def kanatal(request):
    return render(request,'kanatal.html')
def mussoorie(request):
    return render(request,'mussoorie.html')
def shimla(request):
    return render(request,'shimla.html')
def janjehli(request):
    return render(request,'janjehli.html')
def poovar(request):
    return render(request,'poovar.html')
def munnar(request):
    return render(request,'munnar.html')
def ooty(request):
    return render(request,'ooty.html')
def kodaikanal(request):
    return render(request,'kodaikanal.html')

# Create your views here.
