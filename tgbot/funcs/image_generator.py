from PIL import Image, ImageFont, ImageDraw


def get_image(text: list, user_id):
    print(text)
    W = 497
    blank = Image.open("/var/tgbot/tgbot/funcs/blank.png")
    font = ImageFont.truetype("/var/tgbot/tgbot/funcs/SF Pro Text/SF-Pro-Text-Regular.otf",
                              15)
    font_14 = ImageFont.truetype(
        "/var/tgbot/tgbot/funcs/SF Pro Text/SF-Pro-Text-Regular.otf",
        14)
    draw = ImageDraw.Draw(blank)
    w, h = font_14.getsize(text[0])
    draw.text((W - w - 410, 134), text[0], font=font_14, fill=(255, 255, 255, 255))
    w, h = font_14.getsize(text[1])
    draw.text((W - w - 300, 134), text[1], font=font_14, fill=(255, 255, 255, 255))
    w, h = font_14.getsize(text[2])
    if text[2] == "sell" or text[2] == "Sell":
        fill = (254, 95, 86, 255)
    elif text[2] == "buy" or text[2] == "Buy":
        fill = (88, 204, 105, 255)
    draw.text((W - w - 245, 134), text[2], font=font_14, fill=fill)
    w, h = font_14.getsize(text[3])
    draw.text((W - w - 155, 134), text[3], font=font_14, fill=(255, 255, 255, 255))
    w, h = font_14.getsize(text[4])
    if text[4].startswith("-"):
        fill = (254, 95, 86, 255)
    else:
        fill = (88, 204, 105, 255)
    draw.text((W - w - 39, 133), text[4], font=font_14, fill=fill)
    w, h = font.getsize(text[5])
    draw.text((W - w - 10, 182), text[5], font=font, fill=(255, 255, 255, 255))
    w, h = font.getsize("USD")
    draw.text((W - w - 10, 206), "USD", font=font, fill=(255, 255, 255, 255))
    draw.text((W - w - 10, 230), "USD", font=font, fill=(255, 255, 255, 255))
    w, h = font.getsize(text[6])
    draw.text((W - w - 10, 254), text[6], font=font, fill=(255, 255, 255, 255))
    w, h = font.getsize(text[7])
    draw.text((W - w - 10, 278), text[7], font=font, fill=(255, 255, 255, 255))
    w, h = font.getsize("Market")
    draw.text((W - w - 10, 302), "Market", font=font, fill=(255, 255, 255, 255))
    draw.text((W - w - 10, 326), "Market", font=font, fill=(255, 255, 255, 255))
    w, h = font.getsize(text[0])
    draw.text((W - w - 10, 350), text[0], font=font, fill=(255, 255, 255, 255))
    w, h = font.getsize(text[8])
    draw.text((W - w - 10, 374), text[8], font=font, fill=(255, 255, 255, 255))
    w, h = font.getsize(text[9])
    draw.text((W - w - 10, 398), text[9], font=font, fill=(255, 255, 255, 255))
    w, h = font.getsize(text[10])
    draw.text((W - w - 10, 422), text[10], font=font, fill=(255, 255, 255, 255))
    w, h = font.getsize(text[11])
    draw.text((W - w - 10, 448), text[11], font=font, fill=(255, 255, 255, 255))
    w, h = font.getsize(text[12])
    draw.text((W - w - 10, 472), text[12], font=font, fill=(255, 255, 255, 255))
    w, h = font.getsize(text[13])
    draw.text((W - w - 10, 496), text[13], font=font, fill=(255, 255, 255, 255))
    w, h = font.getsize(text[14])
    draw.text((W - w - 10, 520), text[14], font=font, fill=(255, 255, 255, 255))
    ratio = str(round(float(text[14].replace(" USD", "")) / float(text[6].replace(" USD", "")) * 100, 2)) + "%"
    w, h = font.getsize(ratio)
    draw.text((W - w - 10, 544), ratio, font=font, fill=(255, 255, 255, 255))
    w, h = font.getsize(text[15])
    draw.text((W - w - 10, 568), text[15], font=font, fill=(255, 255, 255, 255))
    blank.save(f"/Users/matvejdoroshenko/rendering_bot/tgbot/funcs/{user_id}_drawn_image.png", "PNG")
