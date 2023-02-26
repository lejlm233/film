from PIL import Image
from pillow_lut import load_cube_file
from pillow_lut import rgb_color_enhance

# lut的使用
def lutUse(cube_file, image):
    lut_3d = load_cube_file(cube_file)  # .cube文件
    filtered_image = image.filter(lut_3d)  # 图片加载lut
    return filtered_image  # 返回处理后的图片

# 参数细节调整
def rgbUse(image):
    # rgb_color_enhance(source, brightness=0, exposure=0, contrast=0, warmth=0, saturation=0, vibrance=0, hue=0, gamma=1.0, linear=False, cls=<class 'PIL.ImageFilter.Color3DLUT'>)
    lut = rgb_color_enhance(
        11, exposure=0.2, contrast=0.1, vibrance=0.5, gamma=1.3)
    filtered_image = image.filter(lut)  # 图片加载参数调整lut
    return filtered_image  # 返回处理后的图片
"""
    参数：	
    source – 可能是将被修改的源查找表， 或者只是新标识表的大小，从 2 到 65。 性能可以显著降低更大的尺寸。
    亮度 – 所有通道一个值，或三个值的元组 从 -1.0 到 1.0。使用以获得更好的效果。exposure
    曝光 – 所有通道一个值，或三个值的元组 从 -5.0 到 5.0。
    对比度 – 所有通道一个值，或三个值的元组 从 -1.0 到 5.0。
    温暖 – 从 -1.0 到 1.0 的一个值。
    饱和度 – 所有通道一个值，或三个值的元组 从 -1.0 到 5.0。
    活力 – 所有通道的一个值，或三个值的元组 从 -1.0 到 5.0。
    色调 – 从 0 到 1.0 的一个值。
    gamma – 从 0 到 10.0 的一个值。默认值为 1.0。
    线性 – 布尔值。将值从 sRGB 转换为线性颜色空间 在操纵之前，在之后返回。默认值为 False。 大多数参数在此模式下更敏感。 """



if __name__=="__main__":
    image = Image.open("FUJI0237.jpg")
    lut="2.cube"
    lutout=lutUse(lut,image)
    lutout.save("4.jpg")
    #rgbUse(lutout).save("4.jpg")
    
    pass
