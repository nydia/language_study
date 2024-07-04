import cv2
import numpy as np

# 读取图片
img = cv2.imread('C:/temp/1.jpg')

# 转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 使用阈值分割找到水印区域
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# 寻找轮廓
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 遍历每个轮廓并用背景填充
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    # 扩大边界以确保完全覆盖水印
    x, y, w, h = x-10, y-10, w+20, h+20
    roi = img[y:y+h, x:x+w]
    # 使用均值颜色填充
    mean_color = [int(c) for c in cv2.mean(roi)[:3]]
    img[y:y+h, x:x+w] = mean_color

# 保存结果
cv2.imwrite('C:/temp/2.jpg', img)