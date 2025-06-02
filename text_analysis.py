def analyze_text(text):
    text = text.lower()
    negative_keywords = ["flood", "fire", "earthquake", "cyclone", "injured", "stranded"]
    positive_keywords = ["rescued", "safe", "helped", "under control"]

    score = sum(word in text for word in positive_keywords) - sum(word in text for word in negative_keywords)

    if score > 0:
        label = "Positive"
    elif score < 0:
        label = "Negative"
    else:
        label = "Neutral"

    return score, label
