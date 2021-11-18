from PIL import Image

image = Image.open("lapin.jpg")

width, height = image.size

for x in range(width) :
   for y in range(height) :
       rouge, vert, bleu = image.getpixel((x,y))
       moyenne = round((rouge+vert+bleu)/3)
       image.putpixel((x,y),(moyenne, moyenne, moyenne))

image.show()
