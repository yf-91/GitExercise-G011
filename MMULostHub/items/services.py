from .models import Post

def create_post(post_data):

    post_type = post_data.get("post_type")
    location = post_data.get("post_location")

    if post_type == "found" and not location:
        raise ValueError("Location is required for found posts")

    

    new_post = Post.objects.create(
        post_type=post_type,
        post_datetime = post_data.get("post_datetime"),
        post_itemcategory=post_data.get("post_itemcategory"),
        post_location_id=post_data.get("post_location"),
        post_description=post_data.get("post_description"),
        post_user=post_data.get("post_user")
)

    return new_post