from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ProfileForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    title='weplay'
    profiles= Profile.objects.all()
    current_user = request.user
    return render(request,'index.html',{'title':title,"profiles":profiles,"current_user":current_user})

@login_required(login_url='/accounts/login/')
def profile(request,id):
    user_object = request.user
    current_user = Profile.objects.get(username__id=request.user.id)
    user = Profile.objects.get(username__id=id)

    return render(request, "profile.html", {"current_user":current_user,"user":user,"user_object":user_object})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user=request.user
    user_edit = Profile.objects.get(username__id=current_user.id)
    if request.method =='POST':
        form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()

        return redirect("home")               
    else:
        form=ProfileForm(instance=request.user.profile)
     
    return render(request,'edit_profile.html',locals())
def all_playgrounds(request):
    images = Playground.get_images()
    return render(request, 'welcome.html', {"images": images})