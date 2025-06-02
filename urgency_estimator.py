def estimate_urgency(sentiment_label, tags):
    emergency_keywords = {"flood", "fire", "earthquake", "cyclone", "injured", "collapsed", "stranded", "damage"}

    if any(tag.lower() in emergency_keywords for tag in tags):
        return "High"
    elif sentiment_label == "Negative":
        return "Medium"
    else:
        return "Low"
