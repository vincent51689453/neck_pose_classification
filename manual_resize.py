import cv2
import csv
"""
This scipts helps to resize all the images from test_original or train_original to test and train.
"""

with open('./data/train_backup/train.csv',mode='r') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        name = row[0]
        complete_name = './data/train_backup/'+name
        img = cv2.imread(complete_name)
        img = cv2.resize(img,(720,480))
        save_path = './data/train/'+name
        cv2.imwrite(save_path,img)
        cv2.imshow("buffer",img)
        cv2.waitKey(1)
print("Done")

