from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# from django.http import HttpResponse
# from appTwo.models import User
from appTwo.forms import ClientDefaultInfoForm, ClientInfoForm,BookingForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'appTwo/base.html')

# sigup page, validation,commiting to databse and creation of a user
def clients(request):
    registered = False

    if request.method == "POST":
        client_form1 = ClientDefaultInfoForm(data=request.POST)
        client_form2 = ClientInfoForm(data=request.POST)

        if client_form1.is_valid() and client_form2.is_valid():
            client = client_form1.save() #grabbing data and saving it to the db
            client.set_password(client.password) #hashing the password_validation
            client.save()

            form2 = client_form2.save(commit=False)
            form2.client = client

            if 'client_form2' in request.POST:
                form2.client_form2 = request.POST['client_form2']
            form2.save()
            registered = True
        else:
            print(client_form1.errors, client_form2.errors)
    else:
        client_form1 = ClientDefaultInfoForm()
        client_form2 = ClientInfoForm()

    return render(request,'appTwo/registration.html',{'client_form1':client_form1,
                                                    'client_form2':client_form2,
                                                    'registered':registered})
# view function for the login, authentication, validation, password hashing
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        client = authenticate(username=username, password=password)

        if client: #this condition checks if the user has bee authenticated
            login(request,client)

            return HttpResponseRedirect(reverse('index'))

        else:
            print("Someone tried to login and failed")
            print("username {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'appTwo/login.html')

#Using the decorator to condition the status of the user
@login_required # It has to be above the function
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
#using the decorator to condition the status of the user
@login_required # you have to log in to be able to be decorated by this
def special(request):
    return HttpResponse("You're logged-in!")


# view function for the booking page
def book(request):
    bookform = BookingForm()

    if request.method == "POST":
        bookform = BookingForm(request.POST)

        if bookform.is_valid():
            bookform.save(commit=True)
            return index(request) #This is how the homepage is return when validated
        else:
            print('ERROR FORM INVALID')
# rendering from book.html
    return render(request,'appTwo/book.html',{'bookform':bookform})
