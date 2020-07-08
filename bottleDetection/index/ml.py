import numpy as np
from sympy.printing.tests.test_tensorflow import tf
from tensorflow import keras
from keras.preprocessing import image
from keras.applications.mobilenet import preprocess_input


def ml():
    test_image = image.load_img('C:\\Users\\Timo\\Source\\Repos\\freie-aufgabe\\bottleDetection\\media\\image.jpg',
                                target_size=(224, 224))
    model = keras.models.load_model('C:\\Users\\Timo\\Source\\Repos\\freie-aufgabe\\bottleDetection\\model\\saved_model.pb')
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
