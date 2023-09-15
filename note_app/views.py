from django.shortcuts import render,redirect
from note_app.forms import NewItemForm
from note_app.models import Note
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'note_app/index.html')

def about(request):
    return render(request,'note_app/about.html')

def create(request):
    form = NewItemForm()
    
    if request.method == 'POST':
        form = NewItemForm(request.POST)
        if form.is_valid():

            t = form.cleaned_data['title']
            d =form.cleaned_data['description']

            item = Note(title=t,description=d)
            item.save()

            print("\n Valid Form")
            messages.success(request,"Ye kam pura karoge toh aur milega :) !")
            #return index(request)
            return redirect("view")
        else:
            print("Form is invalid")

    return render(request,'note_app/create_todo.html',context={'form':form})

def view(request):
    # query set
    all = Note.objects.all()
    # raw query set
    all = Note.objects.raw("SELECT * FROM note_app_Note ORDER BY id DESC;")
    paginator = Paginator(all,4)
    page = request.GET.get('page')
    page_track = paginator.get_page(page)

    context={'page_track':page_track,'all_todos':all}

    return render(request,'note_app/view_todo.html',context=context)


    # paginator = Paginator(all,2)
    # page = request.GET.get('page',1)
    # # page_obj = paginator.get_page(page_number)
    # page_track = paginator.get_page(page)
    
    # try:
    #     all = paginator.page(page)
    # except PageNotAnInteger:
    #     all = paginator.page(1)
    # except EmptyPage:
    #     all = paginator.page(paginator.num_pages)

    # all_todo_list = {'all_todos':all,"page_track":page_track}

    # return render(request,'note_app/view_todo.html',context=all_todo_list)


def delete(request,id):
    task = Note.objects.get(pk=id)
    print()
    print(f"Task : {task}")
    print(f"ID : {id}")
    
    task.delete()
    
    #messages.info(request, "item removed !!!")
    messages.success(request,"Khatam , tata ,bye-bye , GAYA !")
    #return redirect("index") 
    return redirect("view")

def update(request,id):
    obj = Note.objects.get(pk=id)
    form = NewItemForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        messages.info(request,"Ekdum se inhone waqt badal diya jasbat badal diye..")
        return redirect("view")

    return render(request,'note_app/update.html',context={'obj':obj,'form':form})