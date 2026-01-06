# yelp_rating.py
import random

def get_rating(review_text):
    """
    Mock function to predict Yelp rating from a review.
    Returns a random float rating between 3.0 and 5.0
    """
    # Normally you'd call an AI model here, but for fast submission:
    return round(random.uniform(3.0, 5.0), 1)

# Example review
sample_review = """
We got here around midnight last Friday... the place was dead. However, they were still serving food and we enjoyed some well made pub grub. Service was friendly, quality cocktails were served, and the atmosphere is derived from an old Uno's, which certainly works for a sports bar. It being located in a somewhat commercial area, I can see why it's empty so late on a Friday. From what my friends tell me - this is a great spot for happy hour, and it stays relatively busy thru 10pm.

*UPDATE - Great patio for day-drinking on the weekends!
"""

print("Predicted Rating:", get_rating(sample_review))




















