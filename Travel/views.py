

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Destination, Ppd,Hotels,TransactionHistory
from accounts import views
import datetime
from django.conf import settings
import uuid

# Create your views here.from django.http import HttpResponse
dests= Destination.objects.all()
def index(request):
    d1= Destination.objects.filter(name="Mumbai").values()
    d1=list(d1)
    print(d1)
   
    # dests= Destination.objects.all()
    populars= Ppd.objects.all()
    return render(request, 'index.html', {"dests": d1, "placess": populars })
def destinationview(request,id):
    objid=id
    ob=Destination.objects.filter(id=objid).values()
    obj=list(ob)
    img=obj[0]['img']
    img="/media/"+img
    n=obj[0]['name']
    print(img)
    hotel_obj= Hotels.objects.filter(location=n).values()
    hotel_ob= list(hotel_obj)
    print(hotel_ob)
    
    return render(request, "destination_details.html", {'d': ob, 'h': hotel_ob, 'img': img, 'media_url':settings.MEDIA_URL} )
def aboutpage(request):
    return render(request, 'about.html')    
def search(request):
    q= request.GET['query']
    s= q.capitalize()
    print(s)
    # s=Destination.objects.filter(name=q).exists()
    if Destination.objects.filter(name=s).exists():
        d= Destination.objects.filter(name=s).values()
        d= list(d)  
        # print(x)
        return render(request, "result.html", {'results': "yes", 'somelist': d})
    else:
         "There is no such result for the query."
         return render(request, "result.html", {'m': "There is no such result for the query."}) 
def traveldest(request):
    d=dests
    print(d)
    return render(request, "travel_destination.html", {'dests': dests})     
def booking(request):
    if request.method== 'POST':
        objId = request.GET.get('id')
        personname= request.POST['username']
        card_number = request.POST['cardnumber']
        # card_type = request.POST['cardtype']
        bId = uuid.uuid4().hex
        bId= bId[0:15]
        check_in = request.POST['in']
        check_out = request.POST['out']
        a=datetime.datetime.strptime(check_in,'%Y-%m-%d')
        b=datetime.datetime.strptime(check_out,'%Y-%m-%d')

        days= (b-a).days
        u=  request.user.get_username()
        bookdate = datetime.datetime.today().strftime('%Y-%m-%d')
        today= datetime.datetime.strptime(bookdate,'%Y-%m-%d')
        obj = Hotels.objects.filter(id = objId).values()
        obj=list(obj)
        cost= days*obj[0]['cost']
        hotel_name= obj[0]['hotel_name']
        addrss= obj[0]['location']
        case_1= TransactionHistory.objects.filter(companyName=hotel_name, check_in=a, check_out=a).exists()
        case_2= TransactionHistory.objects.filter(companyName=hotel_name, check_in=b, check_out=b).exists()
        case_3= TransactionHistory.objects.filter(companyName=hotel_name, check_in=a, check_out=b).exists()
        if a<today:
            messages.error(request, "Check-in date must start from current date that is from today")
            return redirect('book')  
        else:        
            if a<b:
                if case_1 or case_2 or case_3:
                    messages.error(request, "Rooms of hotel are booked of these dates")
                    return redirect('book') 
                else:     
                    new_transaction = TransactionHistory.objects.create(username=u, bookdate=bookdate, check_in=check_in, paymentAmount=cost, paymentCardNo=card_number, companyName=hotel_name, location=addrss, bookperson=personname, check_out=check_out, bookingId=bId, dummy_check_in=check_in, dummy_check_out=check_out )
                    new_transaction.save()
                    return render(request, 'bookingconfirm.html', { 'obj': obj,'msg': ' Your Booking is successful'})
            else:
                messages.error(request, "Check-out date must be after check-in date")
                return redirect('book')   

    else:   
        objid= request.GET.get('id')
        obj=Hotels.objects.filter(id=objid).values()
        obj=list(obj)
        print(obj)
       
        return render(request, "booking.html", {'obj': obj})  

def mybookings(request):
    u= request.user.get_username()
    obj= TransactionHistory.objects.filter(username=u).values()
    if (len(list(obj))==0):
        return render(request, "confirmedbookings.html", {'msg': "You have'nt booked any hotels yet."})
    else:
        return render(request, "confirmedbookings.html", {'obj': obj})

def cancel_booking(request):
    objId= request.GET.get('id')
    c_Id = uuid.uuid4().hex
    c_Id= c_Id[0:15]
    TransactionHistory.objects.filter(id=objId).update(cancelled=True, cancel_Id=c_Id, check_in=None, check_out=None)
    return redirect('bookinghistory')

def booking_details(request):
    objId= request.GET.get('id')
    b_detail=TransactionHistory.objects.filter(id=objId).values()
    return render(request, 'bookingDetails.html', {'details':b_detail})

