from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    title='weplay'
    profiles= Profile.objects.all()
    current_user = request.user
    images = Fitness_activities.objects.all()
    team = Team.objects.all()

    post = Events.objects.all()
    return render(request,'index.html',{'title':title,"profiles":profiles,"current_user":current_user,"images":images,"team":team,"post":post})

    chats=Chat.objects.all()
    return render(request,'index.html',{'title':title,"profiles":profiles,"current_user":current_user,"images":images,"team":team,"chat":chat})


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
def all_playgrounds(request,activities_id):
    images = Fitness_activities.get_images()
    playg = Fitness_activities.objects.get(id=activities_id)
    
    return render(request, 'index.html', {"images": images,"activities_id":activities_id})
def detail(request,image_id):
        image = Fitness_activities.objects.get(id = image_id)
        team = Team.objects.filter(ground=image_id)
        post = Events.objects.filter(poster=image_id)
        return render(request,"details.html", {"image":image, "team":team,"post":post})

def create_team(request,activities_id):
    current_user = request.user
    playg = Fitness_activities.objects.get(id=activities_id)
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            team = form.save(commit=False)
            team.ground = playg
            team.save()

        return redirect('detail', activities_id)


        return redirect('detail', playground_id)

    else:
        form = TeamForm()
        
    return render(request, 'team.html', {"form": form,"activities_id":activities_id})
def search_results(request):

    if 'activities' in request.GET and request.GET["activities"]:
        search_term = request.GET.get("activities")
        searched_activity = Fitness_activities.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"activitiess": searched_activity})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
def new_post(request,activities_id):
    current_user = request.user
    news= Fitness_activities.objects.get(id=activities_id)
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.posted_by = current_user
            post.poster = news
            post.save()
        return redirect('detail', activities_id)

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form, "activities_id": activities_id})


@login_required(login_url='/accounts/login/')
def chat(request):
    current_user = request.user
    teams= Team.objects.all()
    chats = Chat.objects.all()
    

    for team in teams:
        team.save()
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            team_id = int(request.POST.get("idteam"))
            team = Chat.objects.get(id = team_id)
            chat = form.save(commit=False)
            chat.username = request.user
            chat.team = team
            chat.save()
        return redirect('chat')

    else:
        form = ChatForm()
        return render(request,'chat.html',{"current_user":current_user,"chats":chats,"form":form,"teams":teams})


