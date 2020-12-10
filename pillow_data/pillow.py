# !/usr/bin/python3
import os   # Utilities 相关函式库
import matplotlib.pyplot as plt     # 图像处理/展现的相关函数库
from PIL import Image

'''
安装注意事项：
1,pip install Pillow
2,如果编译错误 则可能需要安装指定版本的 numpy: pip install numpy==1.19.3
3,其他需要安装的模块: pip install matplotlib, PIL, pillow
'''

'''
一些说明：
1,plt.imshow()函数负责对图像进行处理，并显示其格式，但是不能显示。其后跟着plt.show（）才能显示出来
2,cmap即colormaps,图谱
3,matplotlib.cm是matplotlib库中内置的色彩映射函数
4,
'''

# 根目录路径
root_dir = os.getcwd()
print(root_dir)

# 训练/验证用的资料目录
data_path = os.path.join(root_dir, 'images')

# 测试用的图像
test_image = os.path.join(data_path, 'heben.jpg')

# 载入图像
image = Image.open(test_image)

# 存储图像并转换格式(jpg->png)
# image.save(os.path.join(data_path, 'new_image.png'))
# plt.imshow(image)

# 将图像逆时针旋转 18 度
# img_rotate_18 = image.rotate(18)
# plt.imshow(img_rotate_18)

# 要扩展让旋转图像的尺寸以适应整个图像，可以将第二个参数传递给rotate()，如下所示
img_rotate_18 = image.rotate(18, expand=True)
plt.imshow(img_rotate_18)

# 对图片进行 左右翻转
# image_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
# plt.imshow(image_flip)

# 对图片进行 上下翻转
# image_flip = image.transpose(Image.FLIP_TOP_BOTTOM)
# plt.imshow(image_flip)

# 将彩色转换成灰阶
# greyscale_image = image.convert('L')
# plt.imshow(greyscale_image, cmap='gray')

plt.show()

使用Pillow来进行图像处理: https://zhuanlan.zhihu.com/p/53732081
plt.imshow(): https://www.jianshu.com/p/08f4ecac9eef
