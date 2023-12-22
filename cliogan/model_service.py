import numpy as np
import requests
import tensorflow as tf
import keras
from PIL import Image
from rembg import remove
from io import BytesIO

data_path = 'predict/'
data_path_ser = 'Data71/'
image_resolution = (256, 256, 1)
step = 3
image_path = 'result' + str(step) + '/'


def load_model(numb):
    return keras.models.load_model(f"resources/models/gen31/{numb}/gen/")


def image_to_image(gen: keras.Model, image):
    return gen.predict(tf.expand_dims(image, axis=0))


def load_image_url(url, remove_bg=True):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))

    if remove_bg:
        image = remove(image)
        jpg_image = Image.new("RGB", image.size, (255, 255, 255))
        jpg_image.paste(image, (0, 0), image)
        image = jpg_image
    image = tf.convert_to_tensor(np.array(image))
    image = tf.image.resize(image, image_resolution[:2])
    image = tf.image.rgb_to_grayscale(image)
    image.set_shape(image_resolution)
    image /= 255.0
    return image


def load_image(image_path, remove_bg=False):
    image = Image.open(image_path)
    if remove_bg:
        image = remove(image)
        jpg_image = Image.new("RGB", image.size, (255, 255, 255))
        jpg_image.paste(image, (0, 0), image)
        image = jpg_image
    image = tf.convert_to_tensor(image)
    image = tf.image.resize(image, image_resolution[:2])
    image = tf.image.rgb_to_grayscale(image)
    image.set_shape(image_resolution)
    image /= 255.0
    return image
