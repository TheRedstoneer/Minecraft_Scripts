from PIL import Image

COUNT = 10 #number of source-images, or frames (numbering starts at [NAME_PREFIX]1.png until [NAME_PREFIX][COUNT].png)
SIZE = 512 #size of image (must be quadratic!)
NAME_PREFIX = "" # prefix of the source-images
OUT_NAME = "gift_box" #name of the resulting image

#you can specify a (transparent) overlay with the same size as the source-images,
#which gets put ontop. this is helpful for not-animated text.
# if you don't want any overlay, set it to [None]
OVERLAY_IMG = "overlay.png"

img = Image.new("RGBA", (SIZE, COUNT*SIZE))
if OVERLAY_IMG:
    OVERLAY_IMG = Image.open(OVERLAY_IMG)

for i in range(COUNT):
    imgT = Image.open(NAME_PREFIX+str(i+1)+".png")
    img.paste(imgT, (0, i*SIZE))
    if OVERLAY_IMG:
        img.paste(OVERLAY_IMG, (0, i*SIZE),OVERLAY_IMG)

img.save(OUT_NAME+".png")
