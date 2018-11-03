#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)
from timeit import timeit
import os

# Setup
imread_options = [
    {
        "name": "Pillow",
        "import_name": "PIL",
        "setup": "from PIL import Image",
        "test_fun": "image=Image.open(\"{filename}\").load(); x=image[3,3]",
    },
    {
        "name": "OpenCV",
        "import_name": "cv2",
        "setup": "from cv2 import imread",
        "test_fun": "image=imread(\"{filename}\"); x=image[3,3]",
    },
    {
        "name": "Matplotlib",
        "import_name": "matplotlib",
        "setup": "from matplotlib.image import imread",
        "test_fun": "image=imread(\"{filename}\"); x=image[3,3]",
    },
    {
        "name": "SciPy",
        "import_name": "scipy",
        "setup": "from scipy.misc import imread",
        "test_fun": "image=imread(\"{filename}\"); x=image[3,3]",
    },
    {
        "name": "SciKit-Image",
        "import_name": "skimage",
        "setup": "from skimage.io import imread",
        "test_fun": "image=imread(\"{filename}\"); x=image[3,3]",
    }
]

# Test
# Check that the test directories exist
test_image_directory = os.path.join(os.path.dirname(__file__), '..', 'images')
if not os.path.exists(test_image_directory):
    raise IOError(
        'The test image directory does not exist. '
        'This is most likely because the test data is not installed. '
        'You may need to install pysss from source to get the '
        'test data.')
filenames = [os.path.join(test_image_directory, "squirrel.jpg"),
             os.path.join(test_image_directory, "clouds.png")]

def imread_eval(filenames=filenames, times=100):
    speeds={}
    logging.info('\t`imread` performance test:')
    for this_option in imread_options:
        try:
            __import__(this_option["import_name"])
        except ImportError:
            logging.info('\t\t%s is not installed.', this_option["name"])
            continue
        speeds[this_option["name"]] = 0
        for image in filenames:
            speeds[this_option["name"]] = timeit(
                this_option["test_fun"].format(filename=image),
                setup=this_option["setup"],
                number=times) + speeds[this_option["name"]]
        logging.info('\t\t%s time: %s.', this_option["name"], speeds[this_option["name"]])

    # Scoring
    optimum = sorted(speeds.items(), key=lambda kv: kv[1])[0][0]
    logging.info('\t\t\t%s is the fastest.\n', optimum)
    return optimum

default_number = 10
optimum = imread_eval(filenames = filenames, times=default_number)

# Proxy
if optimum == "Pillow":
    from PIL import Image
    def imread(filename):
        return Image.open(filename).load()
elif optimum == "OpenCV":
    from cv2 import imread
elif optimum == "Matplotlib":
    from matplotlib.image import imread
else:
    from PIL import Image
    def imread(filename):
        return Image.open(filename).load()
