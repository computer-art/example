# Computer Art

> There is no must in art because art is free.


## Introduction

The following tutorial exaplains how to generate `computer art` based on a series of predefined `digital images`.
Our `script` will combinate all the `digital images` generating an specific `image collection`

## Example Case

We will use the following `digital assets`:

- `4 x backgrounds images`
- `12 x bodies images`
- `12 x faces images`

## Expected Results

Our script will generate `576 new images` as a result of combinate `4 x 12 x 12` (backgrounds, bodies, and faces).

![Example](https://i.ibb.co/CpLnRrB/all.jpg)

## Environment

The script was `successfully tested` with:

- `Python 3.8.5`
- `Pip 21.2.4`
- `Pillow 8.3.2`

## Digital Assets

There is an `images` folder with `3 sub-folders`

- `/images/backgrounds`
- `/images/bodies`
- `/images/faces`

Inside `each sub-folder` there is a few `transparent png files` named with `2-left pad zero` strategy, for example: `01.png`, `02.png`, `...`, `11.png`

## Script Strategy

### 1. Import Pillow Module

```python
# importing the Pillow module
from PIL import Image, ImageDraw, ImageFilter
```

### 2. Define how many digital assets will combine

```python
# my primary source :D
kBackgrounds = 4
kBodies = 12
kFaces = 12
```

### 3. Loop in order

```python
for index_background in range(1, kBackgrounds + 1):
    for index_body in range(1, kBodies + 1):
        for index_face in range(1, kFaces + 1):
```

### 4. Load the 3 images that will generate the current new image

```python
            im1 = Image.open(/path/to/index_background.png)
            im2 = Image.open(/path/to/index_body.png)
            im3 = Image.open(/path/to/index_face.png)
```

### 5. Paste `img2` and `img3` into `img1` in the right position

![Example](https://i.ibb.co/nzDw233/example.jpg)

The magic happens because all the bodies and all the faces have the same `canvas/size`!

```python
            # paste body into background
            im1.paste(im2, (540, 1970), mask=im2)
            # paste face into background
            im1.paste(im3, (456, 370), mask=im3)
```

### 6. Save & continue the loop with the next combination!

```python
            # save!
            im1.save(/path/to/new-image.png)

            # update status!
            print(/path/to/new-image.png, "was successfully created.")
```

## Bye!

![Example](https://i.ibb.co/x7H5dMb/003-008-011.png)
