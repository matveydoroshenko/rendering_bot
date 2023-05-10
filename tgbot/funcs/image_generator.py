from PIL import Image, ImageFont, ImageDraw


def get_image_1(text: list, user_id):
    W = 497
    blank = Image.open("/var/tgbot/photos/first_screen/blank.png")
    font = ImageFont.truetype("/var/tgbot/fonts/SF Pro Text/SF-Pro-Text-Regular.otf",
                              15)
    font_14 = ImageFont.truetype(
        "/var/tgbot/fonts/SF Pro Text/SF-Pro-Text-Regular.otf",
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
    blank.save(f"/var/tgbot/photos/first_screen/{user_id}_drawn_image.png", "PNG")


def get_image_2(text: list, user_id):
    W = 304
    blank = Image.open("/Users/matvejdoroshenko/rendering_bot/photos/second_screen/template_in_progress.png")
    font_11 = ImageFont.truetype(
        "/var/tgbot/fonts/SF Pro Text/SF-Pro-Text-Semibold.otf",
        11)
    font_12 = ImageFont.truetype(
        "/var/tgbot/fonts/SF Pro Text/SF-Pro-Text-Semibold.otf",
        12)
    font_15 = ImageFont.truetype(
        "/var/tgbot/fonts/SF Pro Text/SF-Pro-Text-Semibold.otf",
        15)
    font_14 = ImageFont.truetype(
        "/var/tgbot/fonts/SF Pro Text/SF-Pro-Text-Semibold.otf",
        14)
    draw = ImageDraw.Draw(blank)
    w, h = font_11.getsize(text[0].rsplit()[0])
    draw.text((W - w - 247, 11), text[0].rsplit()[0], font=font_11, fill=(255, 255, 255, 255))
    w, h = font_12.getsize(text[0].rsplit()[1])
    draw.text((W - w - 235, 24), text[0].rsplit()[1], font=font_12, fill=(255, 255, 255, 255))
    w, h = font_12.getsize(text[1])
    draw.text((W - w - 160, 18), text[1], font=font_12, fill=(255, 255, 255, 255))
    if text[2] == "sell" or text[2] == "Sell":
        direction = "down"
    elif text[2] == "buy" or text[2] == "Buy":
        direction = "up"
    arrow = Image.open(f"/Users/matvejdoroshenko/rendering_bot/photos/second_screen/arrows/arrow_{direction}.png")
    blank.paste(arrow, (166, 20), arrow)
    w, h = font_12.getsize(text[2])
    draw.text((W - w - 100, 18), text[2], font=font_12, fill=(255, 255, 255, 255))
    ticker_name = text[3].replace("/USD", "")
    ticker = Image.open(f"/var/tgbot/photos/second_screen/crypto_logos/{ticker_name.upper()}.png").convert("RGBA")
    ticker.resize((11, 11)).save(f"/var/tgbot/photos/second_screen/crypto_logos/{ticker_name.upper()}.png")
    ticker = Image.open(f"/var/tgbot/photos/second_screen/crypto_logos/{ticker_name.upper()}.png").convert("RGBA")
    blank.paste(ticker, (212, 20), ticker)
    w, h = font_12.getsize(text[3])
    if len(ticker_name) == 4:
        draw.text((W - w - 12, 18), text[3], font=font_12, fill=(255, 255, 255, 255))
    elif len(ticker_name) == 3:
        draw.text((W - w - 20, 18), text[3], font=font_12, fill=(255, 255, 255, 255))
    w, h = font_12.getsize(text[4])
    draw.text((W - w + 107, 18), text[4], font=font_12, fill=(88, 204, 105, 255))
    w, h = font_14.getsize(text[5])
    draw.text((W - w + 125, 60), text[5], font=font_14, fill=(255, 255, 255, 255))
    w, h = font_15.getsize(text[6])
    draw.text((W - w + 124, 82), text[6], font=font_15, fill=(255, 255, 255, 255))
    if text[7] == "USD":
        flag = Image.open("/var/tgbot/photos/second_screen/flags/usa_flag.png").convert("RGBA")
        flag.resize((18, 15)).save("/var/tgbot/photos/second_screen/flags/usa_flag.png")
    elif text[7] == "EUR":
        flag = Image.open("/var/tgbot/photos/second_screen/flags/eu_flag.png").convert(
            "RGBA")
        flag.resize((15, 15)).save("/var/tgbot/photos/second_screen/flags/eu_flag.png")
    blank.paste(flag, (383, 109), flag)
    w, h = font_15.getsize(text[7])
    draw.text((W - w + 128, 107), text[7], font=font_15, fill=(255, 255, 255, 255))
    w, h = font_15.getsize(text[8])
    draw.text((W - w + 125, 130), text[8], font=font_15, fill=(255, 255, 255, 255))
    w, h = font_15.getsize(text[9])
    draw.text((W - w + 125, 155), text[9], font=font_15, fill=(255, 255, 255, 255))
    w, h = font_14.getsize(text[10])
    draw.text((W - w + 125, 180), text[10], font=font_14, fill=(255, 255, 255, 255))
    w, h = font_14.getsize(text[11])
    draw.text((W - w + 125, 205), text[11], font=font_14, fill=(255, 255, 255, 255))
    w, h = font_14.getsize(text[12])
    draw.text((W - w + 125, 230), text[12], font=font_14, fill=(255, 255, 255, 255))
    w, h = font_14.getsize(text[13])
    draw.text((W - w + 125, 255), text[13], font=font_14, fill=(255, 255, 255, 255))
    w, h = font_15.getsize(text[14])
    draw.text((W - w + 125, 280), text[14], font=font_15, fill=(255, 255, 255, 255))
    blank.save(f"/var/tgbot/photos/second_screen/{user_id}_drawn_image.png", "PNG")
