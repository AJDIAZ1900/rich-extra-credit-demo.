import emoji

samples = [
    ":fire:", ":rocket:", ":thumbs_up:", ":clinking_beer_mugs:",
    ":red_heart:", ":smiling_face_with_sunglasses:"
]

for s in samples:
    print(f"{s} -> {emoji.emojize(s)}")
