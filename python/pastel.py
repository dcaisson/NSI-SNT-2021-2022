from PIL import Image

image = Image.open("lapin.jpg")

width, height = image.size

step = 64
for x in range(width) :
   for y in range(height) :
       rouge, vert, bleu = image.getpixel((x,y))
       rouge = (rouge // step) * step + step//2;
       bleu = (bleu // step) * step + step//2;
       vert = (vert // step) * step + step//2;
       image.putpixel((x,y),(rouge, vert, bleu))

image.show()
