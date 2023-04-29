from PIL import Image, ImageFont, ImageDraw


def get_image(text):
    blank = Image.open("/Users/matvejdoroshenko/rendering_bot/tgbot/funcs/blank.png")
    font = ImageFont.truetype("/Users/matvejdoroshenko/rendering_bot/tgbot/funcs/tahoma-bold.ttf", 15)
    draw = ImageDraw.Draw(blank)
    W = 497
    w, h = font.getsize(text)
    draw.text((W - w - 10, 254), text, font=font, fill=(255, 255, 255, 255))
    font = ImageFont.truetype("/Users/matvejdoroshenko/rendering_bot/tgbot/funcs/tahoma.ttf", 15)
    w, h = font.getsize("Market")
    draw.text((W - w - 10, 278), "Market", font=font, fill=(255, 255, 255, 255))
    blank.save(f"/Users/matvejdoroshenko/rendering_bot/tgbot/funcs/drawn_image.png", "PNG")
    return open(f"/Users/matvejdoroshenko/rendering_bot/tgbot/funcs/drawn_image.png", "rb")
