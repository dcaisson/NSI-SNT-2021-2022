from PIL import Image


src = Image.open("lapin.jpg")

width, height = src.size
dst = Image.new(mode="RGBA",size=(width-2,height-2))
print(width,height)

seuil = 120

for i in range(width-2) :
   for j in range(height-2) :
       x = i + 1
       y = j + 1
       rougeN, vertN, bleuN = src.getpixel((x,y-1))
       rougeS, vertS, bleuS = src.getpixel((x,y+1))
       rougeW, vertW, bleuW = src.getpixel((x-1,y))
       rougeE, vertE, bleuE = src.getpixel((x+1,y))
       S = abs(rougeN-rougeS) + abs(vertN-vertS) + abs(bleuN-bleuS) + abs(rougeW-rougeE) + abs(vertW-vertE) + abs(bleuW-bleuE)
       if S > seuil:
          c = 0
       else:   
          c = 255   
       dst.putpixel((i,j),(c, c, c))

dst.show()
