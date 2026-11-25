#!/usr/bin/env python3
"""Build-time gallery cards for the README (not used by the entry itself).

Renders the tournament winner and the three runners-up as captioned
quote cards with Pillow, which exists on the build machine only —
main.py never touches it.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (18, 20, 28)
FG = (240, 238, 230)
ACCENTS = {
    "winner": (255, 176, 32),
    "finalist": (64, 190, 200),
}

CARDS = [
    (
        "card-winner.png",
        "WINNER — THE ROBOTS ARE WAITING",
        "winner",
        "The CAPTCHA asked me to prove I'm not a robot by finding traffic "
        "lights, and I failed twice. Somewhere a machine is doing my job "
        "flawlessly while I sit here, a human, unable to identify a bus. "
        "The robots aren't coming. They're waiting for me to finish the test.",
        "261 characters · tournament score 19/20",
    ),
    (
        "card-finalist-cart.png",
        "FINALIST — THE WHEEL TESTIFIES",
        "finalist",
        "Every shopping cart has one wheel that has seen things. It doesn't "
        "roll, it testifies. It points at a crime scene only it remembers "
        "while the other three pretend this is a vehicle. I am pushing a "
        "witness protection program with a handle.",
        "237 characters · tournament score 19/20",
    ),
    (
        "card-finalist-checkout.png",
        "FINALIST — THE BAG CHECK",
        "finalist",
        "The self-checkout trusts me to scan forty items but not to buy one "
        "bag. I have a mortgage, Deborah. I have buried relatives. But sure, "
        "call an attendant — clearly the plastic bag is where my criminal "
        "career begins.",
        "214 characters · tournament score 18/20",
    ),
    (
        "card-finalist-courier.png",
        "FINALIST — WE MISSED YOU",
        "finalist",
        "The courier wrote 'we missed you' while I sat six feet from the "
        "door holding my breath like a hostage. Missed me? You didn't knock, "
        "you didn't ring, you achieved speeds the military would envy. You "
        "missed me the way I miss my ex: deliberately, and with paperwork.",
        "263 characters · tournament score 17/20",
    ),
]


def font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)


def wrap(draw, text, fnt, width):
    words, lines, line = text.split(), [], ""
    for word in words:
        trial = f"{line} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            line = trial
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def render(filename, title, kind, text, footer):
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    accent = ACCENTS[kind]
    draw.rectangle([0, 0, W, 14], fill=accent)
    draw.text((60, 52), title, font=font(40, bold=True), fill=accent)
    body = font(37)
    lines = wrap(draw, text, body, W - 120)
    y = 150
    for line in lines:
        draw.text((60, y), line, font=body, fill=FG)
        y += 52
    draw.text((60, H - 70), footer, font=font(26), fill=(150, 152, 160))
    img.save(filename)
    print("wrote", filename)


if __name__ == "__main__":
    for card in CARDS:
        render(*card)
