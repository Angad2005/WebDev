from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Feedback
from .forms import FeedbackForm
import requests

# Create your views here.
def home(request):
    return render(request, 'home.html')

def tuf(request):
    product = 'tuf'
    feedbacks = Feedback.objects.filter(product=product).order_by('-created_at')
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fb = form.save(commit=False)
            fb.user = request.user
            fb.product = product
            fb.save()
            try:
                response = requests.post('http://localhost:5000/analyze', json={'text': fb.message})
                if response.status_code == 200:
                    sentiment = response.json().get('sentiment', 'neutral')
                    fb.sentiment = sentiment
                    fb.save(update_fields=['sentiment'])
            except requests.exceptions.RequestException:
                pass
            return redirect('tuf')
    else:
        form = FeedbackForm(initial={'product': product})
    return render(request, 'tuf.html', {'form': form, 'feedbacks': feedbacks})

# @login_required
# def tuf(request):
#     product = 'tuf'
#     feedbacks = Feedback.objects.filter(product=product).order_by('-created_at')

#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             fb = form.save(commit=False)
#             fb.user = request.user
#             fb.product = product  # Redundant with hidden field but safe
#             fb.save()
#             return redirect('tuf')
#     else:
#         form = FeedbackForm(initial={'product': product})

#     return render(request, 'tuf.html', {'form': form, 'feedbacks': feedbacks})



# @login_required
# def strix(request):
#     product = 'strix'
#     feedbacks = Feedback.objects.filter(product=product).order_by('-created_at')

#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             fb = form.save(commit=False)
#             fb.user = request.user
#             fb.product = product  # Redundant with hidden field but safe
#             fb.save()
#             return redirect('strix')
#     else:
#         form = FeedbackForm(initial={'product': product})

#     return render(request, 'strix.html', {'form': form, 'feedbacks': feedbacks})

from django.contrib.auth.decorators import login_required
import requests

@login_required
def strix(request):
    product = 'strix'
    feedbacks = Feedback.objects.filter(product=product).order_by('-created_at')

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fb = form.save(commit=False)
            fb.user = request.user
            fb.product = product
            fb.save()
            try:
                response = requests.post('http://localhost:5000/analyze', json={'text': fb.message})
                if response.status_code == 200:
                    sentiment = response.json().get('sentiment', 'neutral')
                    fb.sentiment = sentiment
                    fb.save(update_fields=['sentiment'])
            except requests.exceptions.RequestException:
                pass
            return redirect('strix')
    else:
        form = FeedbackForm(initial={'product': product})

    return render(request, 'strix.html', {'form': form, 'feedbacks': feedbacks})



# @login_required
# def zenbook(request):
#     product = 'zenbook'
#     feedbacks = Feedback.objects.filter(product=product).order_by('-created_at')

#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             fb = form.save(commit=False)
#             fb.user = request.user
#             fb.product = product  # Redundant with hidden field but safe
#             fb.save()
#             return redirect('zenbook')
#     else:
#         form = FeedbackForm(initial={'product': product})

#     return render(request, 'zenbook.html', {'form': form, 'feedbacks': feedbacks})

@login_required
def zenbook(request):
    product = 'zenbook'
    feedbacks = Feedback.objects.filter(product=product).order_by('-created_at')

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fb = form.save(commit=False)
            fb.user = request.user
            fb.product = product
            fb.save()
            try:
                response = requests.post('http://localhost:5000/analyze', json={'text': fb.message})
                if response.status_code == 200:
                    sentiment = response.json().get('sentiment', 'neutral')
                    fb.sentiment = sentiment
                    fb.save(update_fields=['sentiment'])
            except requests.exceptions.RequestException:
                pass
            return redirect('zenbook')
    else:
        form = FeedbackForm(initial={'product': product})

    return render(request, 'zenbook.html', {'form': form, 'feedbacks': feedbacks})


#@login_required
#def strix(request):
 #   return render(request, 'strix.html')

# @login_required
# def zephyrus(request):
#     product = 'zephyrus'
#     feedbacks = Feedback.objects.filter(product=product).order_by('-created_at')

#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             fb = form.save(commit=False)
#             fb.user = request.user
#             fb.product = product  # Redundant with hidden field but safe
#             fb.save()
#             return redirect('zephyrus')
#     else:
#         form = FeedbackForm(initial={'product': product})

#     return render(request, 'zephyrus.html', {'form': form, 'feedbacks': feedbacks})

@login_required
def zephyrus(request):
    product = 'zephyrus'
    feedbacks = Feedback.objects.filter(product=product).order_by('-created_at')

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fb = form.save(commit=False)
            fb.user = request.user
            fb.product = product
            fb.save()
            try:
                response = requests.post('http://localhost:5000/analyze', json={'text': fb.message})
                if response.status_code == 200:
                    sentiment = response.json().get('sentiment', 'neutral')
                    fb.sentiment = sentiment
                    fb.save(update_fields=['sentiment'])
            except requests.exceptions.RequestException:
                pass
            return redirect('zephyrus')
    else:
        form = FeedbackForm(initial={'product': product})

    return render(request, 'zephyrus.html', {'form': form, 'feedbacks': feedbacks})


# @login_required
# def vivobook(request):
#     return render(request, 'vivobook.html')

# @login_required
# def vivobook(request):
#     product = 'vivobook'
#     feedbacks = Feedback.objects.filter(product=product).order_by('-created_at')

#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             fb = form.save(commit=False)
#             fb.user = request.user
#             fb.product = product  # Redundant with hidden field but safe
#             fb.save()
#             return redirect('vivobook')
#     else:
#         form = FeedbackForm(initial={'product': product})

#     return render(request, 'vivobook.html', {'form': form, 'feedbacks': feedbacks})

@login_required
def vivobook(request):
    product = 'vivobook'
    feedbacks = Feedback.objects.filter(product=product).order_by('-created_at')

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fb = form.save(commit=False)
            fb.user = request.user
            fb.product = product
            fb.save()
            try:
                response = requests.post('http://localhost:5000/analyze', json={'text': fb.message})
                if response.status_code == 200:
                    sentiment = response.json().get('sentiment', 'neutral')
                    fb.sentiment = sentiment
                    fb.save(update_fields=['sentiment'])
            except requests.exceptions.RequestException:
                pass
            return redirect('vivobook')
    else:
        form = FeedbackForm(initial={'product': product})

    return render(request, 'vivobook.html', {'form': form, 'feedbacks': feedbacks})


from .forms import FeedbackForm
from .models import Feedback


def feedback_page(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = FeedbackForm(request.POST)
            if form.is_valid():
                fb = form.save(commit=False)
                fb.user = request.user
                fb.save()
                return redirect('feedback')
        else:
            return redirect('login')
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form, 'feedbacks': feedbacks})

from django.shortcuts import get_object_or_404
from django.contrib import messages

@login_required
def delete_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)

    if feedback.user != request.user:
        messages.error(request, "You can't delete someone else's feedback.")
        return redirect('home')  # Or wherever you want

    if request.method == 'POST':
        feedback.delete()
        messages.success(request, "Feedback deleted successfully.")
        return redirect(request.META.get('HTTP_REFERER', 'home'))

    return render(request, 'confirm_delete.html', {'feedback': feedback})



#for sentiments
@login_required
def feedback_page(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = FeedbackForm(request.POST)
            if form.is_valid():
                fb = form.save(commit=False)
                fb.user = request.user
                fb.save()
                try:
                    response = requests.post('http://localhost:5000/analyze', json={'text': fb.message})
                    if response.status_code == 200:
                        sentiment = response.json().get('sentiment', 'neutral')
                        fb.sentiment = sentiment
                        fb.save(update_fields=['sentiment'])
                except requests.exceptions.RequestException:
                    pass
                return redirect('feedback')
        else:
            return redirect('login')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form, 'feedbacks': feedbacks})

@login_required
def delete_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)
    if feedback.user != request.user:
        messages.error(request, "You can't delete someone else's feedback.")
        return redirect('home')
    if request.method == 'POST':
        feedback.delete()
        messages.success(request, "Feedback deleted successfully.")
        return redirect(request.META.get('HTTP_REFERER', 'home'))
    return render(request, 'confirm_delete.html', {'feedback': feedback})