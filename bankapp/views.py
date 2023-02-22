from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Helpline
from random import choice
from django.contrib import messages
from django.contrib.auth import logout



def home(request):
    return render(request, './home.html')


def contact_us(request):
    return render(request, './contact_Us.html')



def registration(request):
    if request.method == ('GET'):
        return render(request, './registration_form.html')
    else:
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        company_name = request.POST.get("Company_name")
        address = request.POST.get("address")
        phone_number = request.POST.get("Phone_number")
        country = request.POST.get("Country")
        try:
            if CustomUser.objects.filter(Email=email).exists():
                messages.error(
                    request, 
                    'A user with this email already exist!'
                    )
                return render(request, './registration_form.html')
    
            admin_user = CustomUser.objects.create(
                Email = email,
                Password = password, 
                company_name = company_name, 
                Address = address,
                Phone_Number = phone_number,
                Country = country
            )
            print(admin_user)
            if not admin_user: 
                return HttpResponse("Registration failed")
            return redirect('login')
        except Exception as e:
            messages.error(request, e.message)
            return render(request, "./registration_form.html")
 



def forget_pass(request):
    if request.method =='GET':
        return render(request, './forget_pass.html')
    email_check = request.POST.get('email')
    request.session['email_id'] = email_check
    check_email = CustomUser.objects.filter(Email=email_check)
    if check_email:
        return redirect("forget_password")
    messages.error(request, 'No user matches that password!')
    return render(request, './forget_pass.html')



def forget_password(request):
    if request.method =='GET':
        return render(request, "./forget_password.html")
    else:
        user = CustomUser.objects.get(
            Email=request.session.get('email_id')
            )
        password = request.POST.get('Password')
        password2 = request.POST.get('confirm_password')
        if password !=password2:
            messages.error(request, "password must match")
            return render(request, './forget_password.html')
        user.Password = password
        user.save()
        context = {
            'pasword_validation': user
        }
        return render(request, "./login.html", context)




def login(request):
    if request.method=='GET':
      return render(request, './login.html')

    elif request.method =="POST":
        email = request.POST['Email']
        password = request.POST['Password']
        try:
            user = CustomUser.objects.get(Email= email)
            print(user.Password)
            if user.Password == password:
                return render(request, "./admin.html") 
            messages.error(request, 'Incorrect password!')
            return render(request, './login.html')
        except CustomUser.DoesNotExist:
            return render(request, "./not_found.html")



def customer_care_create(request):
    if request.method =='GET':
        return render(request, './admin.html')
    elif request.method=='POST':
        branch_name = request.POST.get('branch')
        phone_number =  request.POST.get('number')
        city =  request.POST.get('city')
        country =  request.POST.get('country')
        create_customer_care = Helpline.objects.create(
            Branch=branch_name, 
            City=city,
            Phone_number=phone_number,
            Country=country
            )
        if create_customer_care:
            messages.success(request, 'Customer care created successfully!')
            return render(request, './admin.html')
        messages.error(request, 'Registration unsuccessful!')
        return render(request, './admin.html')

    

def helpline(request):
    user_city= request.GET.get("city")
    user_country = request.GET.get("country")
    print(user_city, user_country)
    if user_city and user_country:
        try:
            centers_in_country = Helpline.objects.filter(
                Country=user_country, 
                City=user_city
            )
            if centers_in_country.exists():
                custom = choice(centers_in_country)
                customer_care = {
                    "country": custom.Country,
                    "branch": custom.Branch,
                    "city": custom.City,
                    "phone": custom.Phone_number
                }
                return render(
                    request, 
                    "./get_helpline.html", 
                    context=customer_care
                    )
        except Exception as e:
            return render (request, './contact_Us.html')     
    return render(request, './contact_Us.html')



@login_required(login_url='login')
def admin_page(request):
    return render(request, "./admin.html")



def logout_view(request):
    logout(request)
    return redirect('home')