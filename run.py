import sys
import PIL.ImageOps
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import argparse
import cv2
import os
import numpy

def break_captcha(out_image):
    # construct the argument parse and parse the arguments
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-i", "--image", required=True,
    #                 help="path to input image to be OCR'd")
    # _args = vars(ap.parse_args())

    # load the example image and convert it to RGB, invert it and adjust brightness
    image = Image.open(out_image).convert('RGB')
    image = PIL.ImageOps.invert(image)
    image = ImageEnhance.Brightness(image)
    image = image.enhance(2)
    imageArray = numpy.array(image)
    imageArray = imageArray[:, :, ::-1].copy()

    filename = "{}.png".format(os.getpid())
    image.save(filename)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    import ipdb; ipdb.set_trace()
    text = pytesseract.image_to_string(Image.open(filename))
    print(text)

    # os.remove(filename)
    # # # show the output images
    # cv2.imshow("Captcha", imageArray)
    # cv2.waitKey(0)


def prepare_image(img):
    """Transform image to greyscale and blur it"""
    img = img.filter(ImageFilter.SMOOTH_MORE)
    img = img.filter(ImageFilter.SMOOTH_MORE)
    if 'L' != img.mode:
        img = img.convert('L')
    return img


def remove_noise(img, pass_factor):
    for column in range(img.size[0]):
        for line in range(img.size[1]):
            value = remove_noise_by_pixel(img, column, line, pass_factor)
            img.putpixel((column, line), value)
    return img


def remove_noise_by_pixel(img, column, line, pass_factor):
    if img.getpixel((column, line)) < pass_factor:
        return (0)
    return (255)


if __name__ == "__main__":
    input_image = sys.argv[1]
    output_image = 'out_' + input_image
    pass_factor = int(sys.argv[2])

    img = Image.open(input_image)
    img = prepare_image(img)
    img = remove_noise(img, pass_factor)
    img.save(output_image)
    break_captcha(output_image)