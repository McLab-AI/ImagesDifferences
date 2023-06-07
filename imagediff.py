from PIL import Image, ImageChops

#load images
img1, img2 = Image.open('1.jpg'),, Image.open('2.jpg')
dff = ImageChops.difference(img1,img2)

if diff.getbbox():
  diff.show()
else:
  print("No difference at all")
 
ImageChops.invert(img1)

