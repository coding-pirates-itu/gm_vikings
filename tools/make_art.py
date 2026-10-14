"""Draws all Vikings sprites as pixel art. Output: <out>/<sprite>/<n>.png"""
import math, os, random, sys
from PIL import Image, ImageDraw

OUT = sys.argv[1]
T = (0, 0, 0, 0)

def new(w, h):
    return Image.new("RGBA", (w, h), T)

def save(name, frames):
    d = os.path.join(OUT, name)
    os.makedirs(d, exist_ok=True)
    for i, f in enumerate(frames):
        f.save(os.path.join(d, f"{i}.png"))

def rect(d, x0, y0, x1, y1, c):
    d.rectangle([x0, y0, x1, y1], fill=c)

def flip(img):
    return img.transpose(Image.FLIP_LEFT_RIGHT)

# ------------------------------------------------------------ palette
OUTL = (30, 22, 20, 255)
SKIN = (240, 190, 140, 255)
SKIN_D = (200, 140, 100, 255)
STEEL = (180, 186, 196, 255)
STEEL_D = (110, 116, 128, 255)
HORN = (240, 232, 210, 255)
HORN_D = (190, 176, 150, 255)
WOOD = (150, 96, 50, 255)
WOOD_D = (100, 62, 32, 255)
WOOD_L = (190, 130, 72, 255)
EYE = (20, 20, 20, 255)

# ------------------------------------------------------------ walls
def wall():
    img = Image.new("RGBA", (32, 32), (52, 52, 64, 255))
    d = ImageDraw.Draw(img)
    rnd = random.Random(5)
    for row in range(2):
        y0 = row * 16
        off = 0 if row == 0 else -8
        for col in range(-1, 3):
            x0 = off + col * 16
            g = rnd.choice([96, 104, 112])
            rect(d, x0 + 1, y0 + 1, x0 + 14, y0 + 14, (g, g, g + 10, 255))
            d.line([x0 + 1, y0 + 1, x0 + 14, y0 + 1], fill=(g + 40, g + 40, g + 50, 255))
            d.line([x0 + 1, y0 + 1, x0 + 1, y0 + 14], fill=(g + 25, g + 25, g + 35, 255))
            d.line([x0 + 1, y0 + 14, x0 + 14, y0 + 14], fill=(g - 30, g - 30, g - 20, 255))
            for _ in range(3):
                px, py = x0 + rnd.randrange(3, 13), y0 + rnd.randrange(3, 13)
                if 0 <= px < 32:
                    img.putpixel((px, py), (g - 20, g - 20, g - 10, 255))
    return img

def arrow_hole():
    img = wall()
    d = ImageDraw.Draw(img)
    rect(d, 6, 12, 31, 19, (20, 16, 18, 255))
    rect(d, 6, 12, 31, 12, (10, 8, 10, 255))
    d.polygon([(20, 13), (28, 15), (28, 16), (20, 18)], fill=(60, 40, 30, 255))  # arrow tip waiting
    return img

# ------------------------------------------------------------ devices
def button(on):
    img = new(32, 32)
    d = ImageDraw.Draw(img)
    rect(d, 8, 8, 23, 23, STEEL_D)
    rect(d, 9, 9, 22, 22, (70, 74, 84, 255))
    d.line([8, 8, 23, 8], fill=STEEL)
    for (x, y) in [(10, 10), (21, 10), (10, 21), (21, 21)]:
        img.putpixel((x, y), STEEL)
    if on:
        rect(d, 12, 12, 19, 19, (60, 200, 80, 255))
        rect(d, 13, 13, 16, 14, (160, 255, 170, 255))
    else:
        rect(d, 12, 11, 19, 18, (210, 50, 40, 255))
        rect(d, 12, 19, 19, 20, (120, 20, 20, 255))
        rect(d, 13, 12, 16, 13, (255, 150, 130, 255))
    return img

def plate(down):
    img = new(32, 32)
    d = ImageDraw.Draw(img)
    rect(d, 2, 29, 29, 31, STEEL_D)
    if down:
        rect(d, 4, 28, 27, 29, (60, 200, 80, 255))
    else:
        rect(d, 4, 25, 27, 28, (230, 190, 40, 255))
        d.line([4, 25, 27, 25], fill=(255, 235, 120, 255))
    return img

def door(open_):
    img = new(32, 64)
    d = ImageDraw.Draw(img)
    rect(d, 0, 0, 31, 63, (40, 34, 36, 255))          # dark doorway
    rect(d, 0, 0, 3, 63, STEEL_D); rect(d, 28, 0, 31, 63, STEEL_D)  # frame
    if open_:
        rect(d, 4, 0, 27, 5, WOOD_D)   # door pulled up into the ceiling
        rect(d, 4, 4, 27, 5, (60, 60, 66, 255))
    else:
        rect(d, 4, 0, 27, 63, WOOD)
        for x in (10, 16, 22):
            d.line([x, 0, x, 63], fill=WOOD_D)
        for y in (8, 30, 52):
            rect(d, 4, y, 27, y + 3, STEEL_D)
            d.line([4, y, 27, y], fill=STEEL)
            for x in (7, 15, 23):
                img.putpixel((x, y + 2), STEEL)
    return img

def trapdoor(open_):
    img = new(32, 32)
    d = ImageDraw.Draw(img)
    rect(d, 0, 0, 1, 7, STEEL_D); rect(d, 30, 0, 31, 7, STEEL_D)
    if open_:
        rect(d, 2, 0, 6, 26, WOOD)          # plank hangs down from the hinge
        d.line([4, 0, 4, 26], fill=WOOD_D)
        rect(d, 2, 0, 6, 2, STEEL_D)
    else:
        rect(d, 2, 0, 29, 7, WOOD)
        d.line([2, 0, 29, 0], fill=WOOD_L)
        for x in (9, 16, 23):
            d.line([x, 1, x, 7], fill=WOOD_D)
        rect(d, 2, 3, 6, 4, STEEL_D)
    return img

def ladder():
    img = new(32, 32)
    d = ImageDraw.Draw(img)
    rect(d, 5, 0, 8, 31, WOOD); rect(d, 23, 0, 26, 31, WOOD)
    d.line([5, 0, 5, 31], fill=WOOD_L); d.line([23, 0, 23, 31], fill=WOOD_L)
    for y in (4, 12, 20, 28):
        rect(d, 9, y, 22, y + 2, WOOD)
        d.line([9, y, 22, y], fill=WOOD_L)
    return img

def ladder_rolled():
    img = new(32, 32)
    d = ImageDraw.Draw(img)
    rect(d, 3, 0, 28, 3, (90, 70, 50, 255))   # hook
    d.ellipse([4, 2, 27, 17], fill=WOOD, outline=WOOD_D)
    d.ellipse([10, 6, 21, 13], fill=WOOD_D)
    d.ellipse([13, 8, 18, 11], fill=WOOD_L)
    rect(d, 14, 16, 17, 22, (200, 180, 120, 255))  # rope end
    return img

def laser(i):
    img = new(32, 32)
    d = ImageDraw.Draw(img)
    w = [3, 4, 3][i]
    glow = [(255, 60, 60, 70), (255, 80, 80, 100), (255, 60, 60, 60)][i]
    rect(d, 16 - w - 3, 0, 15 + w + 3, 31, glow)
    rect(d, 16 - w, 0, 15 + w, 31, (255, 40, 40, 255))
    rect(d, 15, 0, 16, 31, (255, 220, 220, 255))
    return img

def laser_emitter():
    img = new(32, 32)
    d = ImageDraw.Draw(img)
    rect(d, 4, 0, 27, 7, STEEL_D)
    d.line([4, 0, 27, 0], fill=STEEL)
    rect(d, 11, 8, 20, 11, (70, 74, 84, 255))
    rect(d, 13, 11, 18, 12, (200, 40, 40, 255))
    return img

def spikes():
    img = new(32, 32)
    d = ImageDraw.Draw(img)
    rect(d, 0, 28, 31, 31, STEEL_D)
    for i in range(4):
        x = i * 8
        d.polygon([(x, 28), (x + 4, 15), (x + 7, 28)], fill=STEEL)
        d.line([x + 4, 15, x + 7, 28], fill=STEEL_D)
        img.putpixel((x + 4, 15), (255, 255, 255, 255))
    return img

def exit_door(i):
    img = new(64, 64)
    d = ImageDraw.Draw(img)
    # stone arch
    d.rectangle([0, 8, 63, 63], fill=(90, 90, 104, 255))
    d.ellipse([0, 0, 63, 30], fill=(90, 90, 104, 255))
    glow = [(255, 210, 90, 255), (255, 240, 150, 255)][i]
    d.rectangle([8, 16, 55, 63], fill=glow)
    d.ellipse([8, 8, 55, 32], fill=glow)
    d.rectangle([12, 24, 51, 63], fill=[(255, 240, 180, 255), (255, 250, 210, 255)][i])
    # rune / sign
    d.rectangle([22, 2, 41, 11], fill=WOOD, outline=WOOD_D)
    d.line([26, 4, 26, 9], fill=(255, 230, 120, 255)); d.line([26, 4, 30, 6], fill=(255, 230, 120, 255))
    d.line([33, 4, 37, 9], fill=(255, 230, 120, 255)); d.line([37, 4, 33, 9], fill=(255, 230, 120, 255))
    return img

def arrow():
    img = new(24, 6)
    d = ImageDraw.Draw(img)
    d.line([2, 3, 19, 3], fill=WOOD_L)
    d.polygon([(19, 0), (23, 3), (19, 5)], fill=STEEL)
    d.line([0, 1, 4, 3], fill=(230, 230, 230, 255)); d.line([0, 5, 4, 3], fill=(230, 230, 230, 255))
    return img

def stone():
    img = new(12, 12)
    d = ImageDraw.Draw(img)
    d.ellipse([1, 1, 10, 10], fill=(130, 126, 120, 255), outline=(60, 56, 54, 255))
    d.point([(4, 3), (3, 4), (4, 4)], fill=(200, 196, 190, 255))
    return img

def slime(i):
    img = new(32, 24)
    d = ImageDraw.Draw(img)
    h = [14, 12, 10, 12][i]
    w = [11, 12, 14, 12][i]
    top = 23 - h
    d.ellipse([16 - w, top, 15 + w, 23 + h // 2], fill=(80, 200, 60, 230), outline=(30, 110, 30, 255))
    d.rectangle([16 - w, 23, 15 + w, 23], fill=(30, 110, 30, 255))
    rect(d, 16 - w // 2 - 2, top + 3, 16 - w // 2, top + 4, (200, 255, 190, 255))  # shine
    # eyes
    rect(d, 11, top + 5, 13, top + 8, (255, 255, 255, 255)); rect(d, 18, top + 5, 20, top + 8, (255, 255, 255, 255))
    rect(d, 12, top + 6, 13, top + 8, EYE); rect(d, 19, top + 6, 20, top + 8, EYE)
    img = img.crop((0, 0, 32, 24))
    return img

def marker(i):
    img = new(16, 12)
    d = ImageDraw.Draw(img)
    y = i
    d.polygon([(1, y), (14, y), (8, y + 9)], fill=(255, 220, 40, 255), outline=(150, 100, 0, 255))
    return img

def poof(i):
    img = new(48, 48)
    rnd = random.Random(20 + i)
    r = [6, 12, 17, 20, 21, 20][i]
    alpha = [255, 255, 240, 200, 140, 70][i]
    for _ in range(9):
        a = rnd.random() * math.tau
        dist = r * 0.5
        cx, cy = 24 + math.cos(a) * dist, 24 + math.sin(a) * dist
        rr = r * 0.55
        ImageDraw.Draw(img).ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=(235, 235, 240, alpha))
    for _ in range(5):
        a = rnd.random() * math.tau
        cx, cy = 24 + math.cos(a) * r * 0.8, 24 + math.sin(a) * r * 0.8
        ImageDraw.Draw(img).ellipse([cx - 2, cy - 2, cx + 2, cy + 2], fill=(255, 220, 80, alpha))
    return img

# ------------------------------------------------------------ vikings (facing right)
def helmet(d, x, y, w, horns, horn_len):
    # dome
    d.rectangle([x, y + 2, x + w - 1, y + 6], fill=STEEL)
    d.rectangle([x + 2, y, x + w - 3, y + 1], fill=STEEL)
    d.line([x, y + 6, x + w - 1, y + 6], fill=STEEL_D)
    d.rectangle([x + w // 2 - 1, y, x + w // 2, y + 6], fill=STEEL_D)
    if horns:
        # horns curve up on both sides
        d.polygon([(x, y + 4), (x - horn_len, y - 1), (x - horn_len, y - 5), (x + 1, y + 1)], fill=HORN)
        d.polygon([(x + w - 1, y + 4), (x + w - 1 + horn_len, y - 1), (x + w - 1 + horn_len, y - 5), (x + w - 2, y + 1)], fill=HORN)
        d.point([(x - horn_len, y - 5), (x + w - 1 + horn_len, y - 5)], fill=HORN_D)

def bjorn(pose, step):
    """pose: idle / walk / climb. 40x48, feet at y=47, centre x=20, faces right."""
    img = new(40, 48)
    d = ImageDraw.Draw(img)
    bob = 1 if (pose == "idle" and step == 1) or (pose == "walk" and step in (1, 3)) else 0
    top = 6 + bob
    beard = (200, 80, 30, 255)
    tunic = (170, 40, 40, 255)
    tunic_d = (120, 26, 26, 255)
    belt = (80, 50, 30, 255)
    if pose == "climb":
        # back view
        helmet(d, 12, top, 16, True, 5)
        rect(d, 12, top + 7, 27, top + 14, beard)              # hair from behind
        rect(d, 9, top + 15, 30, top + 30, tunic)
        rect(d, 9, top + 27, 30, top + 29, belt)
        up = step == 0
        rect(d, 5, top + (8 if up else 14), 8, top + (20 if up else 26), SKIN)   # arms up
        rect(d, 31, top + (14 if up else 8), 34, top + (26 if up else 20), SKIN)
        # round shield on the back
        d.ellipse([12, top + 14, 27, top + 29], fill=WOOD, outline=WOOD_D)
        d.ellipse([18, top + 20, 21, top + 23], fill=STEEL)
        rect(d, 11, top + 31, 17, 47 - (2 if up else 0), (90, 70, 50, 255))
        rect(d, 22, top + 31, 28, 47 - (0 if up else 2), (90, 70, 50, 255))
        return img
    helmet(d, 12, top, 16, True, 5)
    rect(d, 12, top + 7, 27, top + 12, SKIN)                       # face
    rect(d, 22, top + 8, 23, top + 9, EYE)
    rect(d, 26, top + 10, 27, top + 11, SKIN_D)                    # nose
    rect(d, 11, top + 12, 28, top + 20, beard)                     # big beard
    rect(d, 13, top + 18, 26, top + 22, beard)
    rect(d, 8, top + 15, 30, top + 31, tunic)                      # body
    rect(d, 8, top + 15, 10, top + 31, tunic_d)
    rect(d, 8, top + 27, 30, top + 29, belt)
    rect(d, 18, top + 27, 20, top + 29, (220, 180, 60, 255))       # buckle
    # legs
    if pose == "walk":
        spread = [0, 3, 0, 3][step]
        front = step < 2
        a, b = (11 - spread, 22 + spread) if front else (11 + spread, 22 - spread)
    else:
        a, b = 11, 22
    rect(d, a, top + 32, a + 6, 44, (90, 70, 50, 255))
    rect(d, b, top + 32, b + 6, 44, (90, 70, 50, 255))
    rect(d, a - 1, 45, a + 7, 47, OUTL)
    rect(d, b - 1, 45, b + 8, 47, OUTL)
    # back arm
    rect(d, 5, top + 16, 8, top + 27, SKIN)
    # shield in front (right side)
    sy = top + 13
    d.ellipse([27, sy, 39, sy + 20], fill=WOOD, outline=WOOD_D)
    d.line([33, sy + 1, 33, sy + 19], fill=WOOD_D)
    d.ellipse([31, sy + 8, 35, sy + 12], fill=STEEL)
    d.arc([27, sy, 39, sy + 20], 270, 90, fill=STEEL_D)
    return img

def kaj(pose, step):
    """32x36, feet at y=35, centre x=16, faces right."""
    img = new(32, 36)
    d = ImageDraw.Draw(img)
    bob = 1 if (pose == "idle" and step == 1) or (pose == "walk" and step in (1, 3)) else 0
    top = 6 + bob
    hair = (250, 210, 80, 255)
    tunic = (60, 150, 70, 255)
    tunic_d = (40, 100, 50, 255)
    if pose == "climb":
        helmet(d, 10, top, 12, True, 3)
        rect(d, 10, top + 7, 21, top + 11, hair)
        rect(d, 9, top + 12, 22, top + 22, tunic)
        up = step == 0
        rect(d, 6, top + (6 if up else 11), 8, top + (15 if up else 20), SKIN)
        rect(d, 23, top + (11 if up else 6), 25, top + (20 if up else 15), SKIN)
        rect(d, 10, top + 23, 14, 35 - (2 if up else 0), (110, 80, 50, 255))
        rect(d, 17, top + 23, 21, 35 - (0 if up else 2), (110, 80, 50, 255))
        return img
    helmet(d, 10, top, 12, True, 3)
    rect(d, 10, top + 7, 21, top + 12, SKIN)
    rect(d, 9, top + 7, 11, top + 13, hair)                        # hair at the back
    rect(d, 18, top + 8, 19, top + 9, EYE)
    rect(d, 17, top + 11, 19, top + 11, (170, 80, 60, 255))
    rect(d, 9, top + 13, 22, top + 22, tunic)
    rect(d, 9, top + 13, 10, top + 22, tunic_d)
    rect(d, 9, top + 20, 22, top + 21, (80, 50, 30, 255))
    # legs
    if pose == "jump":
        rect(d, 10, top + 23, 14, top + 26, (110, 80, 50, 255)); rect(d, 9, top + 27, 14, top + 28, OUTL)
        rect(d, 17, top + 23, 21, top + 27, (110, 80, 50, 255)); rect(d, 17, top + 28, 23, top + 29, OUTL)
        rect(d, 22, top + 8, 25, top + 15, SKIN)                   # arm up
        rect(d, 6, top + 14, 8, top + 19, SKIN)
        # stone pouch
        rect(d, 7, top + 18, 10, top + 21, (140, 100, 60, 255))
        return img
    if pose == "walk":
        spread = [0, 2, 0, 2][step]
        front = step < 2
        a, b = (10 - spread, 17 + spread) if front else (10 + spread, 17 - spread)
    else:
        a, b = 10, 17
    rect(d, a, top + 23, a + 4, 33, (110, 80, 50, 255))
    rect(d, b, top + 23, b + 4, 33, (110, 80, 50, 255))
    rect(d, a - 1, 34, a + 5, 35, OUTL)
    rect(d, b - 1, 34, b + 6, 35, OUTL)
    swing = [0, 2, 0, -2][step] if pose == "walk" else 0
    rect(d, 6, top + 14 + max(0, swing), 8, top + 20 + max(0, swing), SKIN)
    rect(d, 23, top + 14 + max(0, -swing), 25, top + 20 + max(0, -swing), SKIN)
    rect(d, 7, top + 18, 10, top + 21, (140, 100, 60, 255))        # stone pouch
    return img

save("s_Wall", [wall()])
save("s_ArrowHole", [arrow_hole()])
save("s_Button", [button(False), button(True)])
save("s_Plate", [plate(False), plate(True)])
save("s_Door", [door(False), door(True)])
save("s_Trapdoor", [trapdoor(False), trapdoor(True)])
save("s_Ladder", [ladder()])
save("s_LadderRolled", [ladder_rolled()])
save("s_Laser", [laser(i) for i in range(3)])
save("s_LaserEmitter", [laser_emitter()])
save("s_Spikes", [spikes()])
save("s_Exit", [exit_door(0), exit_door(1)])
save("s_Arrow", [arrow()])
save("s_Stone", [stone()])
save("s_Slime", [slime(i) for i in range(4)])
save("s_Marker", [marker(0), marker(2)])
save("s_Poof", [poof(i) for i in range(6)])
save("s_BjornIdle", [bjorn("idle", i) for i in range(2)])
save("s_BjornWalk", [bjorn("walk", i) for i in range(4)])
save("s_BjornClimb", [bjorn("climb", i) for i in range(2)])
save("s_KajIdle", [kaj("idle", i) for i in range(2)])
save("s_KajWalk", [kaj("walk", i) for i in range(4)])
save("s_KajClimb", [kaj("climb", i) for i in range(2)])
save("s_KajJump", [kaj("jump", 0)])

# preview sheet
names = sorted(n for n in os.listdir(OUT) if os.path.isdir(os.path.join(OUT, n)))
sheet = Image.new("RGBA", (8 * 70 + 160, len(names) * 70), (34, 30, 40, 255))
d = ImageDraw.Draw(sheet)
for r, n in enumerate(names):
    d.text((4, r * 70 + 30), n, fill=(255, 255, 255, 255))
    files = sorted(os.listdir(os.path.join(OUT, n)), key=lambda f: int(f.split(".")[0]))
    for c, f in enumerate(files):
        sheet.alpha_composite(Image.open(os.path.join(OUT, n, f)), (160 + c * 70, r * 70 + 2))
sheet.resize((sheet.width * 2, sheet.height * 2), Image.NEAREST).save(os.path.join(os.path.dirname(OUT.rstrip("/")), "preview.png"))
