from PIL import Image, ImageFont, ImageDraw


def get_image(text):
    blank = Image.open("/Users/matvejdoroshenko/rendering_bot/tgbot/funcs/blank.png")
    font_regular = ImageFont.truetype("/Users/matvejdoroshenko/rendering_bot/tgbot/funcs/tahoma.ttf", 15)
    font_bold = ImageFont.truetype("/Users/matvejdoroshenko/rendering_bot/tgbot/funcs/tahoma-bold.ttf", 15)
    draw = ImageDraw.Draw(blank)
    W = 497
    w, h = font_bold.getsize(text)
    draw.text((W - w - 10, 254), text, font=font_bold, fill=(255, 255, 255, 255))
    w, h = font_regular.getsize("Market")
    draw.text((W - w - 10, 278), "Market", font=font_regular, fill=(255, 255, 255, 255))
    blank.save(f"/Users/matvejdoroshenko/rendering_bot/tgbot/funcs/drawn_image.png", "PNG")
