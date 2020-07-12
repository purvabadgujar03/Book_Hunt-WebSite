from django.shortcuts import render
from .models import *
from .forms import RegistrationForm

# Create your views here.
a = recommendation.objects.all()
a1, a2 = [], []
for i in range(0, 4):
    a1.append(a[i])
for i in range(4, 8):
    a2.append(a[i])


def f1(request):
    if cutomers.objects.filter(login="true").exists():
        c=cutomers.objects.get(login="true")
        #for i in c:
        c.login= "false"
        c.save()
    con = {"a1": a1, "a2": a2}
    return render(request, 'book1/welcome.html', con)


def f2(request , name):
    t = book2.objects.filter(disc="Thriller")
    f = book2.objects.filter(disc="Fiction")
    r = book2.objects.filter(disc="Romance")
    f1, f2, r1, r2, t1, t2 = [], [], [], [], [], []
    for i in range(0, 6):
        f1.append(f[i])
        r1.append(r[i])
        t1.append(t[i])
    for i in range(6, 12):
        f2.append(f[i])
        r2.append(r[i])
        t2.append(t[i])
    con = {"s_t1": t1, "s_t2": t2, "s_f1": f1, "s_r1": r1, "s_f2": f2, "s_r2": r2,"s_name":name}
    return render(request, 'book1/books.html', con)


def f4(request):
    return render(request, 'book1/authors.html', {"a": "a"})


def f7(request):
    return render(request, 'book1/about.html', {"a": "a"})

def f5(request):
    context = {
        "a1": a1, "a2": a2
    }
    return render(request, 'book1/home.html', context)

def f6(request):
    if cutomers.objects.filter(login="true").exists():
        c1 = cutomers.objects.get(login="true")

    if request.method == 'POST':
        user = request.POST.get('user', '')
        items = request.POST.get('items', '')
        x,y,z=[],[],[]
        s=[]
        x=list(items)
        for i in x:
            if i==",":
                s1=""
                for j in z:
                    s1=s1+j
                y.append(str(s1))
                z=[]
            else:
                z.append(i)
        c=0
        for i in y:
            a=book2.objects.get(name=i)
            c=c+a.price
            s.append(a)

        context = {
        "user":c1.username, "items":s, "c":c
        }
        return render(request, 'book1/cart.html', context)

    context = {
        "error": request.method
    }
    return render(request, 'book1/cart.html', context)


def f3(request):
    form1 = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            emailid = request.POST.get('email', '')
            password = request.POST.get('password', '')
            if emailid == "":
                u=cutomers.objects.get(username=username)
                if u.password ==password:
                    u.login="true"
                    u.save()
                    context = {
                        "a1": a1, "a2": a2,
                        "x": username
                    }

                    return render(request, 'book1/home.html', context)

                else:
                    context={"error":"Please enter correct username and password"}
                    return render(request, 'book1/login-registration.html', context)


            else:
                if cutomers.objects.filter(username=username).exists():
                    context = {"error": "You have already registered. Please login."}
                    return render(request, 'book1/login-registration.html', context)

                else:

                    u = cutomers(username=username, login="true", emailid=emailid, password=password)
                    u.save()
                    context = {
                        "a1":a1,"a2":a2,
                        "x": username
                    }
                    return  render(request, 'book1/home.html', context)
        else:
            context = {
                "form": form1,
                "error":"nooooo"
            }
            return render(request, 'book1/login-registration.html', context)

    context = {
        "form": form1
    }
    return render(request, 'book1/login-registration.html', context)

















