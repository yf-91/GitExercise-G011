from django.shortcuts import render
from .models import CATEGORY_CHOICES, Post

def mainPage(request):
    post_box = Post.objects.all().order_by('-id')  # 最新在上
    return render(request, 'items/mainPage.html', {
        'posts': post_box
    })
    

from django.shortcuts import redirect
from .models import MMULocation
from .services import create_post


def create_post_view(request):
    if request.method == "POST":
        try:
            create_post({
                "post_type": request.POST.get("post_type"),
                "post_datetime": request.POST.get("post_datetime"),
                "post_itemcategory": request.POST.get("post_itemcategory"),
                "post_location": request.POST.get("post_location") or None,
                "post_description": request.POST.get("post_description"),
                "post_user": request.user
        }, request.user)
            return redirect("mainPage")

        except ValueError as e:
            return render(request, "items/createpost.html", {
                "error": str(e),
                "category_choices": CATEGORY_CHOICES,
                "locations": MMULocation.objects.all()
            })
        
    return render(request, "items/createpost.html", {
        "category_choices": CATEGORY_CHOICES,
        "locations": MMULocation.objects.all()
    })