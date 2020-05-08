import cv2 as cv
import sys
import random
import numpy

def main():
    src = cv.imread("/Users/henrypigg/documents/calpoly/year1/2020winter/cpe202/Laplacian_Edge_Detection/test3.jpg", cv.IMREAD_COLOR)
    if src is None:
        print('Error opening image')
        print('Program Arguments: [image_name -- default test.jpg')
        return -1
    laplate = laplacian_edge_detection(src, 3)
    laplate = cv.resize(laplate, (int(len(laplate[0]) * 3), int(len(laplate) * 3)), interpolation = cv.INTER_AREA)
    cv.imwrite('result6.jpg', dots(laplate))
    return 0

def dots(src):
    size = len(src) * len(src[0])
    test = src
    test[:] = 255
    
    for i in range(len(src)):
        for j in range(len(src[0])):
            test = i * len(src[0]) + j
            if test % 10000 == 0:
                #cv.imwrite('result1.jpg', src)
                print(str(round((test / size) * 100, 2)) + "%")
            rand = random.randint(0,30)
            if rand == 0:
                value = int(src[i][j])
                test = cv.circle(src, (j, i), int(((255 - value) / 255) * 2) + 4, max(min(255, value + 20) + 20, 255))
                test = cv.circle(src, (j, i), int(((255 - value) / 255) * 2) + 3, min(255, value + 20), -1)
            #elif src[i][j] != 0:
                #src[i][j] = 255
    return test

def laplacian_edge_detection(src, complexity):
    ddepth = cv.CV_16S
    kernel_size = complexity
    src = cv.GaussianBlur(src, (complexity, complexity), 0)
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    dst = cv.Laplacian(src_gray, ddepth, ksize=kernel_size)
    abs_dst = cv.convertScaleAbs(dst)
    abs_dst = (255-abs_dst)
    return abs_dst

if __name__ == "__main__":
    main()