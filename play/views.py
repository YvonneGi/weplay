from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    title='weplay'
    profiles= Profile.objects.all()
    current_user = request.user
    images = Fitness_activities.objects.all()
    team = Team.objects.all()
    sectors = Sector.objects.all()
    post = Events.objects.all()
    blog = Blog.objects.all()
    locations = Location.objects.all()
    return render(request,'index.html',{'title':title,"profiles":profiles,"current_user":current_user,"images":images,"team":team,
    "post":post,"locations":locations,"blog":blog})

    chats=Chat.objects.all()
    return render(request,'index.html',{'title':title,"profiles":profiles,"current_user":current_user,"images":images,"team":team,"post":post,"locations":locations, "chat":chat, "sectors":sectors})

    # chats=Chat.objects.all()
    # return render(request,'index.html',{'title':title,"profiles":profiles,"current_user":current_user,"images":images,"team":team,"chat":chat})


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

# def all_events(request):
#     events = Events.objects.all()
    
#     return render(request, 'details.html', {"events": events})


def detail(request,image_id):
        image = Fitness_activities.objects.get(id = image_id)
        team = Team.objects.filter(ground=image_id)
        post = Events.objects.all()
        blog = Blog.objects.filter(poster=image_id)
       
        return render(request,"details.html", {"image":image, "team":team,"post":post,"blog":blog})

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
def search_sector(request):
    sectors = Sector.objects.all() 
    fitness = Fitness_activities.objects.all()
    if 'sectors' in request.GET and request.GET["sectors"]:
        
        search_term = request.GET.get("sectors")
        searched_sector = Fitness_activities.search_by_sector(search_term)

        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched_sector": searched_sector,"fitness":fitness ,"sectors":sectors})

    else:

        message = "You haven't searched for any Sector"
        return render(request, 'search.html',{"message":message})
    
def new_post(request,activities_id):
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message,'locations':locations})

# def new_post(request,activities_id):
#     current_user = request.user
#     news= Fitness_activities.objects.get(id=activities_id)
#     if request.method == 'POST':
#         form = NewPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.posted_by = current_user
#             post.poster = news
#             post.save()
#         return redirect('detail', activities_id)

#     else:
#         form = NewPostForm()
#     return render(request, 'new_post.html', {"form": form, "activities_id": activities_id})

def new_blog(request,activities_id):
    current_user = request.user
    news= Fitness_activities.objects.get(id=activities_id)
    if request.method == 'POST':
        form = NewBlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.posted_by = current_user
            blog.poster = news
            blog.save()
        return redirect('detail', activities_id)

    else:
        form = NewBlogForm()
    return render(request, 'new_blog.html', {"form": form, "activities_id": activities_id})


def page_location(request,sector):
    sectors = Sector.objects.all()
    categories = Category.objects.all()
    title = f"{sector}"
    location_results = Fitness_activities.filter_sector(sector)
    return render(request,'search.html',{'all_images':location_results,'sectors':sectors,'categories':categories, 'title':title})

@login_required(login_url='/accounts/login/')
def chat(request,team_id):
    current_user = request.user
    teams= Team.objects.all()
    team = Team.objects.get(id = team_id)
    chats = Chat.objects.filter(team=team.id)
    
    for team in teams:
        team.save()
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.username = request.user
            chat.team = team
            chat.save()
        return redirect('chat',team_id)

    else:
        form = ChatForm()
        return render(request,'chat.html',{"current_user":current_user,"chats":chats,"form":form,"teams":teams,"team_id":team_id})


def message(request):
    message = request.POST.get('your_message') 
    recipient = MessageRecipients(message=message)
    recipient.save()
    # send_welcome_email(name, email)
    data = {'success': 'Your message is sent'}
    return JsonResponse(data)


# @login_required(login_url='/accounts/login/')
# def comment(request,activities_id):
#     current_user = request.user
#     comments = Fitness_activities.objects.get(id=activities_id)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             activities_id = int(request.POST.get("idpost"))
#             post = Fitness_activities.objects.get(id = activities_id)
#             comment = form.save(commit=False)
#             comment.username = request.user
#             comment.post = post
#             comment.save()
#         return redirect('detail')

#     else:
#         form = CommentForm()

#     return render(request,'details.html',{"comments":comments,"current_user":current_user})

# @login_required(login_url='/accounts/login/')
# def comment(request,activities_id):
#     current_user = request.user
#     activitiess = Fitness_activities.objects.all()
#     activities = Fitness_activities.objects.get(id = activities_id)
#     comments = Comments.objects.filter(activity=activities.id)
    
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.username = request.user
#             comment.activity = activity
#             comment.save()
#         return redirect('detail',activities_id)

#     else:
#         form = CommentForm()
#     return render(request,'detail.html',{"current_user":current_user,"comments":comments,"form":form,"activities_id":activities_id,"activitiess":activitiess})
