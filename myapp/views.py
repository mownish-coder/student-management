from django.shortcuts import render,redirect,get_object_or_404
from .models import details
from .forms import details_data

def details_list(request):
    tabel=details.objects.all()
    return render(request,'details_list.html',{'tabel':tabel})

def details_create(request):
    if request.method =="POST":
        form=details_data(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('details_list')
    else:
        form = details_data()
        return render(request,'details_create.html',{'form':form})

def details_update(request,id):
    update = get_object_or_404(details,id=id)
    if request.method == "POST":
        update_data = details_data(request.POST,instance=update)
        if update_data.is_valid():
            update_data.save()
            return redirect('details_list')
    else:
        update_data=details_data(instance=update)
    return render(request,'details_update.html',{'form':update_data})
        
     
def details_delete(request, id):
    delete_item = get_object_or_404(details, id=id)
    delete_item.delete()
    return redirect('details_list')
    

# hello 
# Create your views here.
