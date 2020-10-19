import numpy as np
import cv2 as cv


def av_pix(img_, circles, size):
    av_value = []
    for coords in circles[0, :]:
        col = np.mean(img_[coords[1] - size:coords[1] + size,
                      coords[0] - size:coords[0] + size])
        # print(img[coords[1] - size:coords[1] + size,
        #       coords[0] - size:coords[0] + size])
        av_value.append(col)
    return av_value


def get_radius(circles):
    radius = []
    for coord in circles[0, :]:
        radius.append(coord[2])
    return radius


img = cv.imread('coins.png', cv.IMREAD_GRAYSCALE)
original_img = cv.imread('coins.png', 1)
img = cv.GaussianBlur(img, (5, 5), 0)
circle = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 0.9, 120, param1=50,
                         param2=27, minRadius=60, maxRadius=120)
circle = np.uint16(np.around(circle))
print(circle)
count = 1
for i in circle[0, :]:
    """
    i[0],i[1] are the center of the circle,(x,y).
    i[2] is the radius 
    """
    # draw the outer circle
    cv.circle(original_img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv.circle(original_img, (i[0], i[1]), 2, (0, 0, 255), 3)
    # Text
    # cv.putText(original_img, str(count), (i[0], i[1]),
    #            cv.FONT_HERSHEY_SIMPLEX,
    #            2, (0, 0, 0), 2)
    count += 1
radii = get_radius(circle)
print(radii)

bright_values = av_pix(img, circle, 20)
bright_values = np.uint16(np.around(bright_values))
print(f'Bright colors {bright_values}')

values = []
for a, b in zip(bright_values, radii):
    if a > 150 and b > 110:
        values.append(10)
    elif a > 150 and b <= 110:
        values.append(5)
    elif a < 150 and b > 110:
        values.append(2)
    elif a < 150 and b < 110:
        values.append(1)

print(values)
count2 = 0
for i in circle[0, :]:
    cv.putText(original_img, str(values[count2]) + 'p', (i[0], i[1]),
               cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)
    count2 += 1
cv.putText(original_img, 'ESTIMATED TOTAL VALUE' + 'p', (200, 100),
           cv.FONT_HERSHEY_SIMPLEX, 1.3, 255)

cv.imshow('Detected Coins', original_img)
cv.waitKey(0)
cv.destroyAllWindows()
