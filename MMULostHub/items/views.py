from django.shortcuts import render

def mainPage(request):
    return render(request, 'items/mainpage.html')\
    

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
            })

            return redirect("/")

        except ValueError as e:
            return render(request, "create_post.html", {
                "error": str(e),
                "locations": MMULocation.objects.all()
            })

    return render(request, "createpost.html", {
        "locations": MMULocation.objects.all()
    })