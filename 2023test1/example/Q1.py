# pillow库官网：https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes

from PIL import Image
import cv2
import numpy as np
image = Image.open('2023校模1/example/example.jpg')

# print(image.filename)
# print(image.format)
# print(image.mode)#如RGB
# print(image.size)#分辨率大小
# print(image.info)#基本信息

# # img = cv2.imread('2023校模1/example/example.jpg')
# # img_np = img.flatten()
# # print(img_np)

im = Image.open('2023校模1/example/example.jpg').convert('L')#转换灰度图像
pix = im.load()
width = im.size[0]
height = im.size[1]
for x in range(width):
    for y in range(height):
        value = pix[x, y]
print(pix[50,50])

# print(image.getpixel((120,120)))#获取某点RGB

## 图像变换
# #1位像素图
# image.convert('1').save('2023校模1/example/img1_pixel.png',quality=100)
# #8位灰度图
# image.convert('L').save('2023校模1/example/imgL_grayscale.png',quality=100)
# #8位彩图
# image.convert('P').save('2023校模1/example/imgP_8_bit_colors.png',quality=100)

# #图片剪切：开始点x1,y1，结束点x2,y2
# image.crop((40,40,160,120)).save('2023校模1/example/img_crop.png')

# #图片旋转
# image.rotate(30).save('2023校模1/example/img_rotate_30.png')
# image.rotate(-30).save('2023校模1/example/img_rotate_-30.png')
# image.rotate(30,Image.NEAREST,True).save('2023校模1/example/img_rotate_expand.png')#如果超过原大小，true图片大小进行扩展

# # 指定大小
# image_resize = image.resize((160,200),Image.NEAREST)
# image_resize.save('2023校模1/example/img_resize_1.png')
# #宽高取半
# image_resize = image.resize((int(image.width/2),int(image.height/2)),Image.NEAREST)
# image_resize.save('2023校模1/example/img_resize_2.png')
