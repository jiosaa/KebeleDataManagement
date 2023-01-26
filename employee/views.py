from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from.forms import UserCreationForm, KebeleEmployeeForm, ProfileForm, MessageForm
from .models import Employee, Profile
# Create your views here.
 


def index(request):
    
    return render(request, 'employee/index.html')
 


def loginEmployee(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method=='POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        
        try:
            user=User.objects.get(username=username)
        except: 
            messages.error(request, 'Username does not exist')
            
        user=authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'home') 
        else:
            messages.error(request, 'Username or password does not exist')
            
    return render(request, 'employee/login_register.html')



def logoutEmployee(request):
    logout(request)
    messages.error(request, 'User was logged out!')
    return redirect('index')


def registerEmployee(request):   
    page = 'register'
    if request.user.is_authenticated:
        return redirect('index') 
    form= UserCreationForm()
    
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request, "Account created!")
            
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Error occurred during registration")
    context={'page':page, 'form':form}
    return render(request, 'employee/login_register.html', context)

@login_required(login_url='login')
def employee_profile(request):
    profile = request.user.profile
    context = {'profile':profile}
    return render(request, 'employee/account.html', context)

 

def editProfile(request):
    profile  = request.user.profile

    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'You have successfully updated your profile')
            return redirect('index')
        else:
            messages.error(request,'There is an error while processing your in put')
    context = {'form':form}
    return render(request, 'employee/form.html',context)


# employee management
def manage_employee(request):
    employees = Employee.objects.all()
    context={'employees':employees}
    return render(request, 'employee/manage_employee.html', context)


def add_employee(request):
    form = KebeleEmployeeForm() 
    if request.method == 'POST':
        form = KebeleEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added employee')
            return redirect('manage-employee')  
        else:
            messages.warning(request, 'There was an error while adding the employee, please try again later!')
             
    context={'form':form} 
    return render(request, "employee/form.html", context)


def update_employee(request, id):
    employee = Employee.objects.get(pk=id)    
    form = KebeleEmployeeForm(instance=employee)
    if request.method == "POST":
        form = KebeleEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected employee')
            return redirect('home')
        else:
             messages.warning(request, 'There was an error while updating the employee, please try again later!')
    context = {'form': form}
    return render(request, 'employee/form.html', context)


def delete_employee(request, id):
    employee = Employee.objects.get(pk=id)  
    
    if request.method == "POST":
        if employee.delete():
            messages.success(request, 'You have successfully deleted the selected employee') 
            return redirect('home')
        else:
            messages.warning(request, 'There was an error during deletion of the selected employee')
    context = {'object': employee}
    return render(request, 'employee/delete.html', context)




def send_notification(request):
    pass


@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    kebele_employee = Employee.objects.get(employee=profile)
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context={'messageRequests':messageRequests, 'unreadCount':unreadCount}
    return render(request, 'employee/inbox.html', context)



@login_required(login_url='login')
def view_message(request, pk):
    profile = request.user.profile
    kebele_employee = Employee.objects.get(employee=profile)
    message = kebele_employee.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    context={'message':message}
    return render(request, 'employee/message.html', context)





def create_message(request, id):
    recipient = Employee.objects.get(id=id)
    form = MessageForm()
    
    try: 
        profile = request.user.profile
        kebele_employee = Employee.objects.get(employee=profile)
        sender = kebele_employee
    except:
        return HttpResponseRedirect("handler404")
        
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit = False)
            message.sender = sender
            message.recipient = recipient
            
            message.save()
            
            messages.success(request, 'Your message was successfully sent')
            return redirect('manage-employee')
    
    context={ 'form':form}

    return render(request, 'employee/form.html', context) 


def page_not_found(request, exception):
    return render(request, '404.html', status=404)

 
