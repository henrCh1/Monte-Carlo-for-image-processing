# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 13:20:55 2023

@author: 86319
"""

from PIL import Image
import random

# 打开图像文件并获取宽高信息
im = Image.open("C:/Users/86319/Desktop/xiaohui.png")
width, height = im.size
print("图片宽为：", width)
print("图片高为：", height)
print("图片大小为：", width * height)

# 统计非白色像素数目
white_pixels = 0
for x in range(width):
    for y in range(height):
        color = im.getpixel((x,y))
        #if im.getpixel((x,y)) == (255, 255, 255):
        if (240 <= color[0] <= 255) and (240 <= color[1] <= 255) and (240 <= color[2] <= 255):
            white_pixels += 1
print("实际非白色像素的面积为：",  width * height - white_pixels)
print("占比为：", (width * height - white_pixels) / (width * height))

# 使用蒙特卡洛方法估算非白色像素面积
num_samples = 1000000
count = 0
for i in range(num_samples):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    color = im.getpixel((x,y))
    #if im.getpixel((x,y)) == (255, 255, 255):
    if (240 <= color[0] <= 255) and (240 <= color[1] <= 255) and (240 <= color[2] <= 255):
        count += 1

area = (1 - count / num_samples) * width * height
print("蒙特卡洛求得的非白色像素的面积为：", area)
print("占比为：", area / (width * height))
