
# Sara Kazemi
# Lab6

# Run the main method
# change output directory to desired path on your machine

## Output directory
dir = "/Documents/CST205/Lab6/output/"

## main method
#def main():
  #writePict(removeRedEye(getPic(),877, 981, 300, 450), dir + "noredeye.jpg")
  #writePict(artify(getPic()), dir + "artybike.jpg")



# Returns the picture given a directory
def getPic():
  return makePicture(pickAFile())

# Writes a picture to a file  
def writePict(pict,name):
  file=getMediaPath(name)
  writePictureTo(pict,file)
  
############################################
# Warmup: Remove red-eye
############################################
def removeRedEye(pic, x1, x2, y1, y2):
  for x in range (x1, x2):
    for y in range(y1, y2):
      p = getPixel(pic, x, y)
      if distance(red, getColor(p)) < 180:
        setColor(p, black)
  show(pic)
  return pic


############################################
# Problem 1: Convert picture to sepia tones
############################################
def sepia(pic):
  betterBnW(pic)
  setColorWrapAround(0)
  for p in getPixels(pic):
    r = getRed(p)
    b = getBlue(p)
    #lowlights
    if r < 63:
      myRed = r * 1.1
      myBlue = b * 0.9
    
    #midtones
    if r > 62 and r < 192:
      myRed = r * 1.15
      myBlue = b * 0.85 
    
    #highlights
    if r > 191:
      myRed = r * 1.08
     # if myRed > 255:
      #  myRed = 255
      myBlue = b * .93
    #set new color values
    setRed(p, myRed)
    setBlue(p, myBlue)
  show(pic)
  return pic
      


 
# improved grayscale function using weights  
def betterBnW(pic):
   pixels = getPixels(pic)
   for p in pixels:
      # Find opposite of color by subtracting from max and multiply by weight
      newColor =  ((getRed(p) * 0.299) + (getGreen(p) * 0.587) + (getBlue(p) * 0.114))
      setColor(p, makeColor(newColor, newColor, newColor))
  # show(pic)
   return pic

############################################
# Problem 2: Posterize a picture
############################################

def artify(pic):
  for p in getPixels(pic):
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    #reds
    if r < 64:
      myRed = 31
    elif r > 63 and r < 128:
      myRed = 95
    elif r > 127 and r < 192:
      myRed = 159
    elif r > 191 and r < 256:
      myRed = 223
    
    #greens
    if g < 64:
      myGreen = 31
    elif g > 63 and g < 128:
      myGreen = 95
    elif g > 127 and g < 192:
      myGreen = 159
    elif g > 191 and g < 256:
      myGreen = 223
      
    #Blues
    if b < 64:
      myBlue = 31
    elif b > 63 and b < 128:
      myBlue = 95
    elif b > 127 and b < 192:
      myBlue = 159
    elif b > 191 and b < 256:
      myBlue = 223
      
    
    #set new color values
    setColor(p, makeColor(myRed, myGreen, myBlue))
  show(pic)
  return pic
  
############################################
# Problem 3: Implement chromakey
############################################
  
def chromaKey(pic, back):
  for x in range (0, getWidth(pic)):
    for y in range(0, getHeight(pic)):
      pic_p = getPixel(pic, x, y)
      back_p = getPixel(back, x, y)
      if distance(green, getColor(pic_p)) < 160:
        setColor(pic_p, getColor(back_p))
  show(pic)
  return pic
      