from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Contact
from django.db.models import Q
from .forms import ContactForm
from django.core.paginator import Paginator

def intro_view(request):
    return render(request,'intro.html')

def home(request):
    data=Contact.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        data=Contact.objects.filter(Q(name__icontains=q)|Q(phno__icontains=q)|Q(email__icontains=q))
    paginator=Paginator(data,10)
    page_number=request.GET.get('page',10)
    data=paginator.get_page(page_number)
    return render(request,'home.html',{'data':data})

# Add Contact
def addContact(request):
    form=ContactForm
    if request.method=='POST':
        saveForm=ContactForm(request.POST)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request,'Data has been added.')
    return render(request,'add-contact.html',{'form':form})

# Update Contact
def updateContact(request,id):
    contact=Contact.objects.get(id=id)
    if request.method=='POST':
        saveForm=ContactForm(request.POST,instance=contact)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request,'Data has been updated.')
    form=ContactForm(instance=contact)
    return render(request,'update-contact.html',{'form':form})

# Delete Contact
def deleteContact(request,id):
    Contact.objects.filter(id=id).delete()
    return redirect('/home')

