from PIL import Image
import os

dirt = os.getcwd()
files = os.listdir(dirt + '/images')

for i in files:
    img = Image.open('images/' + i)
    img.thumbnail((500, 2500))
    img.save('new_' + i)
    
# img = Image.open('images/photo1.jpg')  # 오픈시 흑백변환.convert('L')
# img.thumbnail((300, 500))
# # img = img.crop((50, 50, 150, 150))
# img.save('PIL/new_photo1.jpg', quality=95)

