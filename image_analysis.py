from PIL import Image
import random

def analyze_image(uploaded_file):
    try:
        image = Image.open(uploaded_file).convert("RGB")
    except Exception:
        return "Invalid image uploaded", []

    # Resize for faster processing
    image = image.resize((64, 64))
    pixels = list(image.getdata())

    # Count color presence to guess scene type
    red_count = sum(1 for r, g, b in pixels if r > 150 and g < 100 and b < 100)
    blue_count = sum(1 for r, g, b in pixels if b > 130 and g > 130 and r < 100)
    gray_count = sum(1 for r, g, b in pixels if abs(r - g) < 15 and abs(r - b) < 15 and r < 100)

    # Simulate tag logic
    if red_count > 500:
        caption = "The image appears to show fire or smoke."
        tags = ["fire", "smoke", "burning"]
    elif blue_count > 500:
        caption = "The image likely shows flooding or submerged areas."
        tags = ["flood", "water", "stranded"]
    elif gray_count > 500:
        caption = "The image may show rubble or damaged buildings or cyclone."
        tags = ["earthquake", "collapsed", "debris"]
    else:
        # Fallback random guess
        options = {
            "cyclone": ["cyclone", "wind", "storm"],
            "fire": ["fire", "smoke", "flames"],
            "flood": ["flood", "water", "submerged"],
            "earthquake": ["earthquake", "damage", "rubble"]
        }
        choice = random.choice(list(options.keys()))
        caption = f"The image might show a {choice} scene."
        tags = options[choice]

    return caption, tags
