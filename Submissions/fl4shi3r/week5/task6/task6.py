#use python 2 
from PIL import Image
import stepic
image = Image.open('/home/shivendra/universe.png')
data = stepic.decode(image)
image_o = open('/home/shivendra/hidden_universe.png','wb')
image_o.write(data)
image_o.close()
