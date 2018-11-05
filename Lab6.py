
# Ryan Dorrity
# Team SCSI Logic - Cody Young, Sara Kazemi, Nathan Warren-Acord, Ryan Dorrity
# Lab 6
# Date 11/4/2018


# Run the main method
# change output directory to desired path on your machine

## Output directory
dir = "/Documents/GitHub/Lab6/output/"

## main method
def main():
  writePict(removeRedEye(getPic(), 322, 995, 385, 465), dir + "noredeye.jpg")
  writePict(sepia(getPic()), dir + "sepia.jpg")
  writePict(artify(getPic()), dir + "artify2.jpg")
  writePict(chromaKey(getPic(), getPic()), dir + "greenscreen2.png")
  
  



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
   #Convert image to grayscale
   betterBnW(pic)
   pixels = getPixels(pic)
   for p in pixels:
     r = getRed(p)
     b = getBlue(p)
     #Adjust lowlights of picture
     if(r < 63):
       setRed(p, r * 1.1)
       setBlue(p, b * 0.9)
     #Adjust mid tones of picture  
     elif(r < 192):
       setRed(p, r * 1.15)
       setBlue(p, b * 0.85)
     #Adjust highlights of picture  
     else:
       setColorWrapAround(false)
       setRed(p, r * 1.08)
       setBlue(p, b * 0.93)
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
    #Red adjustment
    if r < 64:
      setRed(p, 31)
    elif r < 128:
      setRed(p, 95)
    elif r < 192:
      setRed(p, 159)
    else:
      setRed(p, 223)
    #Green adjustment
    if g < 64:
      setGreen(p, 31)
    elif g < 128:
      setGreen(p, 95)
    elif g < 192:
      setGreen(p, 159)
    else:
      setGreen(p, 223)
    #Blue adjustment
    if b < 64:
      setBlue(p, 31)
    elif b < 128:
      setBlue(p, 95)
    elif b < 192:
      setBlue(p, 159)
    else:
      setBlue(p, 223)
    
  show(pic)
  return pic
  
############################################
# Problem 3: Implement chromakey
############################################
# Parameters: pic is a greenscreen image, back is 
# the background image. 
def chromaKey(pic, back):
  for x in range (0, getWidth(pic)):
    for y in range(0, getHeight(pic)):
      pic_p = getPixel(pic, x, y)
      back_p = getPixel(back, x, y)
      if distance(makeColor(110, 181, 125), getColor(pic_p)) < 75:
        setColor(pic_p, getColor(back_p))
  show(pic)
  return pic
      