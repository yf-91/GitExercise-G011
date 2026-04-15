from .models import post

def create_post(post_data):

    post_type = post_data.get("post_type")
    location = post_data.get("location")

    if post_type == "found" and not location:
        raise ValueError("Location is required for found posts")

    post = post.objects.create(
        post_type = post_type,
        post_datetime = post_data.get("post_datetime"),
        post_itemcategory = post_data.get("post_itemcategory"),
        post_location = location,
        post_description = post_data.get("post_description")
    )

    return post