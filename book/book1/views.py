from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .models import *
from .forms import RegistrationForm,rform,bookform

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
    name=name.upper()
    t = book2.objects.filter(Book_genre="Thriller")
    f = book2.objects.filter(Book_genre="Fiction")
    r = book2.objects.filter(Book_genre="Romance")
    f_count=f.count()
    f_rem=f_count%6
    f_con=f_count-f_rem
    f1=[]
    for i in range(0,f_con,6):
        k=i+6
        sf1=[]
        for j in range(i,k):
            sf1.append(f[j])
        f1.append(sf1)
    if f_rem != 0:
        sf1 = []
        for i in range(f_con, f_count):
            sf1.append(f[i])
        f1.append(sf1)

    r_count = r.count()
    r_rem = r_count % 6
    r_con = r_count - r_rem
    r1 = []
    for i in range(0, r_con, 6):
        k = i + 6
        rf1 = []
        for j in range(i, k):
            rf1.append(r[j])
        r1.append(rf1)
    if r_rem != 0:
        rf1 = []
        for i in range(r_con, r_count):
            rf1.append(r[i])
        r1.append(rf1)

    t_count = t.count()
    t_rem = t_count % 6
    t_con = t_count - t_rem
    t1 = []
    for i in range(0, t_con, 6):
        k = i + 6
        tf1 = []
        for j in range(i, k):
            tf1.append(t[j])
        t1.append(tf1)
    if t_rem != 0:
        tf1 = []
        for i in range(t_con, t_count):
            tf1.append(t[i])
        t1.append(tf1)

    con = {"s_t1": t1, "s_f1": f1, "s_r1": r1,"s_name":name}
    return render(request, 'book1/books.html', con)


def f8(request):
    if request.method == 'POST':
        context = {
            "error": ""
        }
        user = request.POST.get('username', '')
        psw = request.POST.get('password', '')
        if user =="admin" and psw =="admin":
            form= bookform()
            return render(request, 'book1/admin2.html', {"form":form})
        else:
            context={"error":"Please enter correct username and password."}
            return render(request, 'book1/admin.html', context)

    return render(request, 'book1/admin.html', {"a": "a"})

def admin(request):
    if request.method == 'POST':
        form = bookform(request.POST, request.FILES)
        if form.is_valid():
            bookname = request.POST.get('Book_name', '')
            if book2.objects.filter(Book_name=bookname).exists():
                context = {
                    "error": "Book already available.",
                    "form": form
                }
                return render(request, 'book1/admin2.html', context)
            else:
                form.save()
                context = {
                    "error": "File Uploaded Successfully",
                    "form": form
                }
                return render(request, 'book1/admin2.html', context)
        else:
            context = {
                "error": form.is_valid(),
                "form": form,
            }
            return render(request, 'book1/admin2.html', context)
    else:
        form = bookform()
        context={
            "form": form,
            "error":request.method
        }
    return  render(request,'book1/admin2.html',context)




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
            a=book2.objects.get(Book_name=i)
            c=c+a.Book_price
            s.append(a)

        context = {
        "user":c1.username.upper(), "items":s, "c":c
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
                        "x": username.upper()
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

















