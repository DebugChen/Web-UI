# import pytesseract
# from PIL import Image
#
#
# # 1、打开图片（生成一个图片对象）
# image = Image.open('1234.png')
#
# # 2、对文字进行提取
# text = pytesseract.image_to_string(image) #默认会识别成英文
# text_zh = pytesseract.image_to_string(image,lang='chi_sim')
# print(f'识别结果是:{text_zh}')

from pytesseract import *
from PIL import Image

image = Image.open('1234.png')  # Open image object using PIL
text = pytesseract.image_to_string(image)     # Run tesseract.exe on image
print(f'识别结果是:{text}')