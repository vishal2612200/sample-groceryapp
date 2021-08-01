
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

from .forms import AddGroceryForm
from .models import Grocery


def homepage(request):
	if request.method == "POST":
		date = request.POST['date']
		grocery_items = Grocery.objects.filter(added_date = date)
		
	else:
		grocery_items = Grocery.objects.all()
	return render(request, "index.html", context={"items": grocery_items})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("groceryapp:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request, "register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("groceryapp:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, "login.html", context={"login_form":form})
    

def add_form(request):

	if request.method == "POST":
		name = request.POST['name']
		quantity = request.POST['quantity']
		status = request.POST['status']
		date = request.POST['date']
		Grocery.objects.create(name = name, quantity = quantity,\
			                   status = status, added_date = date)
		# print(form)
		return redirect("groceryapp:homepage")
		
	
	return render(request, "add.html")



def update_form(request, grocery_id):

	if request.method == "POST":
		try: 
			name = request.POST['name']
			quantity = request.POST['quantity']
			status = request.POST['status']
			date = request.POST['date']
			
			Grocery.objects.filter(id = grocery_id).update(name = name, quantity = quantity,\
				status = status, added_date = date)
			return redirect("groceryapp:homepage")

		except Grocery.DoesNotExist:
			messages.error(request, "Item does not exist.")
		
	return render(request, "update.html")

def delete_form(request, grocery_id):
	Grocery.objects.get(id = grocery_id).delete()			
			
	messages.success(request, "Grocery Item successfully deleted")
	return redirect("groceryapp:homepage")


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("groceryapp:homepage")
