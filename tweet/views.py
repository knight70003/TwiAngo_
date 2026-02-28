from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm 
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required  
from django.contrib.auth import login
 


# Create your views here.
def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_edit(request,tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user = request.user
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

def tweet_delete(request, tweet_id):
    tweet=get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html', {'tweet': tweet})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

from django.shortcuts import render
from .models import Tweet # Replace YourModel with your actual model
from django.db.models import Q # Import Q object for complex lookups

def search_results(request):
    search_query = request.GET.get('search', '')  # Get the search term, default to empty string

    if search_query:
        # Filter your model based on the search query
        # Use __icontains for case-insensitive partial matches
        # Use Q objects for searching across multiple fields with OR logic
        results = Tweet.objects.filter(
            Q(field1_icontains=search_query) | Q(field2_icontains=search_query)
        ).order_by('field1') # Example ordering

    else:
        results = Tweet.objects.all() # Show all if no search query

    context = {
        'results': results,
        'search_query': search_query,
    }
    return render(request, 'search_results.html', context)


