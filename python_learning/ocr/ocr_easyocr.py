import easyocr

#设置识别中英文两种语言
reader = easyocr.Reader(['ch_sim','en'], gpu = False) # need to run only once to load model into memory
result = reader.readtext(r"c:/temp/images/2.png", detail = 0)
print(result)