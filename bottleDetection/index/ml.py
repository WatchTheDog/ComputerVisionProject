import os

import numpy as np
from sympy.printing.tests.test_tensorflow import tf
from tensorflow import keras
from keras.preprocessing import image
from keras.applications.mobilenet import preprocess_input
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def ml():
    test_image = image.load_img(os.path.join(BASE_DIR, 'media\\image.jpg'),
                                target_size=(224, 224))
    model = keras.models.load_model(os.path.join(BASE_DIR, 'model\\saved_model.pb'))
    if test_image is not None:
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        test_image = preprocess_input(test_image)
        result = model.predict(test_image)
        if result[0][3] > result[0][0] and result[0][3] > result[0][1] and result[0][3] > result[0][2]:
            prediction = 'not_beer'
            mlresult = False
        else:
            prediction = 'beer'
            mlresult = True
        print('Result=%s' % (result[0]) + ', Predicition=' + prediction)
        return mlresult
