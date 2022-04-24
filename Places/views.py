from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from .models import Contact, TouristSpot, Comment, TravelAgencie, Hotel
from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'index.html')


class contacts(View):
    def get(self, request):
        messages = None
        return render(request, 'contact.html', {'message': messages})

    def post(self, request):
        messages = None
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        messages = "Thanks for contacting us, we'll reach out you soon."
        msg = EmailMessage(
        "Somebody Contacted us!",
        "Name: "+name + ", Email: "+email + ", Message: "+message,
        settings.EMAIL_HOST_USER,
        ["sidharthv605@gmail.com"],
        )
        msg.send(fail_silently=False)
        return render(request, 'contact.html', {'message': messages})


class forts(View):
    def get(self, request):
        forts = TouristSpot.objects.filter(category="Forts")
        return render(request, 'forts.html', {'forts': forts})


class wildlife(View):
    def get(self, request):
        wildlifes = TouristSpot.objects.filter(category="Wildlife")
        return render(request, 'wildlife.html', {'wildlifes': wildlifes})


class lake(View):
    def get(self, request):
        lakes = TouristSpot.objects.filter(category="Lakes")
        return render(request, 'lake.html', {'lakes': lakes})


class museum(View):
    def get(self, request):
        museums = TouristSpot.objects.filter(category="Museum")
        return render(request, 'museum.html', {'museums': museums})


class religiousplace(View):
    def get(self, request):
        religiousplaces = TouristSpot.objects.filter(
            category="Religious Places")
        return render(request, 'religiousplace.html', {'religiousplaces': religiousplaces})


class placeview(View):
    def get(self, request, myid):
        place = TouristSpot.objects.filter(id=myid)
        reviews = Comment.objects.filter(place=myid)
        hotel = Hotel.objects.filter(place=myid)
        print(hotel)
        context = {'place': place[0], 'reviews': reviews, 'hotel':hotel}
        return render(request, 'placeview.html', context)


class addcomment(View):
    def post(self, request, myid):
        message = None
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        rating = request.POST.get('rate')
        placeinstance = TouristSpot.objects.get(id=myid)

        comment = Comment(place=placeinstance, name=name, comments=comment, rate=rating)
        comment.save()
        message = "Thank you for your valuable review!"

        place = TouristSpot.objects.filter(id=myid)
        reviews = Comment.objects.filter(place=myid)
        # print(reviews)
        context = {'place': place[0], 'reviews': reviews, 'message':message}

        return render(request, 'placeview.html', context)
        

class travelagency(View):
    def get(self, request):
        travelagent = TravelAgencie.objects.all()
        return render(request, 'travelagency.html', {'travelagent':travelagent})


class travelagencyview(View):
    def get(self, request, myid):
        travelagent = TravelAgencie.objects.filter(id=myid)
        context = {'travelagent': travelagent[0]}
        return render(request, 'travelagencyview.html', context)