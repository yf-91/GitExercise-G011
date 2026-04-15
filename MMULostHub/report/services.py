from .models import Feedback

def create_feedback(comments, image=None):
    feedback = Feedback(
        comments=comments,
        image=image
    )
    feedback.save()
    return feedback