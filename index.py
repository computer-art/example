# coding=utf-8

# ========================================
#   Modules
# ========================================

# importing the os module
import os

# importing the Pillow module
from PIL import Image, ImageDraw, ImageFilter

# ========================================
#   User defined values
# ========================================

# some constants
kBackgrounds = 4
kBodies = 12
kFaces = 12

# to get the current script directory
kDirectory = os.path.dirname(os.path.realpath(__file__))

# create outputs if not exists
if not os.path.exists(kDirectory + '/outputs'):
    os.makedirs(kDirectory + '/outputs')

# ========================================
#   Go go go!
# ========================================

# loop through each background
for index_background in range(1, kBackgrounds + 1):

    # loop through each body
    for index_body in range(1, kBodies + 1):

        # loop through each face
        for index_face in range(1, kFaces + 1):

            # the combination
            index_combination = f'{index_background:03}' + "-" + f'{index_body:03}' + "-" + f'{index_face:03}'

            # the files
            background = kDirectory + '/images/backgrounds/' +  f'{index_background:02}' + '.png'
            body = kDirectory + '/images/bodies/' +  f'{index_body:02}' + '.png'
            face = kDirectory + '/images/faces/' +  f'{index_face:02}' + '.png'
            output = kDirectory + '/outputs/' + index_combination + '.png'

            # some validations
            if not os.path.exists(background):
                print("file not exists", background)
                exit(-1)

            if not os.path.exists(body):
                print("file not exists", body)
                exit(-1)

            if not os.path.exists(face):
                print("file not exists", face)
                exit(-1)

            # load the images
            im1 = Image.open(background)
            im2 = Image.open(body)
            im3 = Image.open(face)

            # paste body into background
            im1.paste(im2, (540, 1970), mask=im2)
            im1.paste(im3, (456, 370), mask=im3)

            # save!
            im1.save(output)

            # update status!
            print(output, "was successfully created.")



            