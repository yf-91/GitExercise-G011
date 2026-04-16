from .models import Feedback

def create_feedback(comments, image=None):

    #a service function specifically responsible for saving feedback data to the database
    feedback = Feedback(
        comments=comments,
        image=image
    )
    feedback.save()
    return feedback