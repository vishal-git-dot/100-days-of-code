from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


#Login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("contact_list")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


#Logout
def logout_view(request):
    logout(request)
    return redirect("login")


#View + Search Contacts
@login_required
def contact_list(request):
    query = request.GET.get("q")
    contacts = Contact.objects.all()

    if query:
        contacts = contacts.filter(name__icontains=query)

    return render(request, "contact_list.html", {
        "contacts": contacts,
        "query": query
    })


#Add Contact
@login_required
def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact added successfully!")
            return redirect("contact_list")
    else:
        form = ContactForm()

    return render(request, "contact_edit.html", {"form": form})


#Edit Contact
@login_required
def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact updated successfully!")
            return redirect("contact_list")
    else:
        form = ContactForm(instance=contact)

    return render(request, "contact_edit.html", {"form": form})


#Delete Contact
@login_required
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    messages.success(request, "Contact deleted successfully!")
    return redirect("contact_list")
