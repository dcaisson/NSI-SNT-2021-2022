from PIL import Image

def flou(src):
   width, height = src.size
   dst = Image.new(mode="RGB",size=(width-2,height-2))
  
   for i in range(width-2) :
      for j in range(height-2) :
          x = i + 1
          y = j + 1
          rouge,vert,bleu = src.getpixel((x,y))
          rougeN, vertN, bleuN = src.getpixel((x,y-1))
          rougeS, vertS, bleuS = src.getpixel((x,y+1))
          rougeW, vertW, bleuW = src.getpixel((x-1,y))
          rougeE, vertE, bleuE = src.getpixel((x+1,y))
          rouge = (4 * rouge + rougeN + rougeS + rougeW + rougeE)//8
          vert = (4 * vert + vertN + vertS + vertW + vertE)//8
          bleu = (4 * bleu + bleuN + bleuS + bleuW + bleuE)//8
          dst.putpixel((i,j),(rouge, vert, bleu))
   return(dst)

def contour(src,seuil):
   width, height = src.size
   dst = Image.new(mode="RGB",size=(width-2,height-2))
  
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
   return(dst)

src = Image.open("lapin.jpg")
img1 = flou(flou(flou(src)))
img1.show()
img2 = contour(img1,100)
img2.show()
