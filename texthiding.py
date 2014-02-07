from PIL import Image
import stepic

#encryption
im=Image.open("Lenna.png")
im1=stepic.encode(im,"hi friends")
im1.save('StegoLenna.jpg', 'JPEG')
im.show()
im1.show()

#decryption
s=stepic.decode()
data=s.decode()
print data
