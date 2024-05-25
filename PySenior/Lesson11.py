import cv2
from PIL import Image

# image_path = 'cat.jpg'
image_path = 'cats.jpg'
image = cv2.imread(image_path)
# cv2.imshow('Cat', image)


cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
cat_face = cat_face_cascade.detectMultiScale(image)
# print(cat_face)

for (x, y, w, h) in cat_face:
    print(x, y, w, h)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)

# cv2.imshow('Cat', image)

cat = Image.open(image_path)
glasses = Image.open('glasses.png')

cat = cat.convert('RGBA')
glasses = glasses.convert('RGBA')

for (x, y, w, h) in cat_face:
    glasses = glasses.resize((w, int(h/3)))
    cat.paste(glasses, (x, int(y + h/4)), glasses)

cat.save('cat_glasses.png')
cat_glasses = cv2.imread('cat_glasses.png')
cv2.imshow('cat_glasses', cat_glasses)

# cv2.imshow('Cat', image)
cv2.waitKey()
