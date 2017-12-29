from PIL import Image
import numpy as np


def ImgFunction1():
    b = np.zeros(shape=(2160, 3840, 3), dtype=np.uint8)
    b[:, :, 0] = 0
    b[:, :, 1] = 0
    b[:, :, 2] = 255
    im = Image.fromarray(b)
    im.save("D:/Resource/image/imgtest.bmp")


def ImgFunction2():
    filename = "D:/Resource/image/desktop.jpg"
    a = np.array(Image.open(filename))
    print(a.shape, a.dtype)
    c = (100 / 255) * a + 150
    im = Image.fromarray(c.astype(np.uint8))
    im.save("D:/Resource/image/imgtest.bmp")


def ImgFunction3():
    filename = "D:/Resource/image/desktop.jpg"
    a = np.array(Image.open(filename).convert('L'))
    b = 255 - a
    im = Image.fromarray(b.astype(np.uint8))
    im.save("D:/Resource/image/imgtest.bmp")


def ImgFunction4():
    filename = "D:/Resource/image/desktop.jpg"
    a = np.array(Image.open(filename).convert('L'))
    b = 255 * (a / 255) ** 1.5
    im = Image.fromarray(b.astype(np.uint8))
    im.save("D:/Resource/image/imgtest.bmp")


def ImgFunction5():
    filename = "D:/Resource/image/BodieLighthouse_EN-AU10541981640_1920x1080.jpg"
    a = np.array(Image.open(filename).convert('L')).astype('float')
    depth = 10.
    grad = np.gradient(a)
    grad_x, grad_y = grad
    grad_x = grad_x * depth / 100.
    grad_y = grad_y * depth / 100.
    A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)

    uni_x = grad_x / A
    uni_y = grad_y / A
    uni_z = 1. / A

    vec_el = np.pi / 2.2
    vec_az = np.pi / 4.
    dx = np.cos(vec_el) * np.cos(vec_az)
    dy = np.cos(vec_el) * np.cos(vec_az)
    dz = np.sin(vec_el)

    b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)
    b = b.clip(0, 255)

    im = Image.fromarray(b.astype(np.uint8))
    im.save("D:/Resource/image/imgtest.bmp")


a = np.array([[1, 2, 3, 4, 5],
              [2, 4, 6, 8, 10],
              [0, 0, 0 ,0, 0]])

x, y = np.gradient(a)
print('a=', a, 'x=', x, '\n', 'y=', y)
