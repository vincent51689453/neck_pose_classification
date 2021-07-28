import cv2
import csv
import random
import os

# Config
num_data = 3339                                 # Total number of data
counter = 0                                     # Counter
index = 0                                       # Image index
training_counter = 0                            # Count training samples
training_fraction = 0.7                         # Fraction of training data
file_bank = []                                  # Record file processing record
source_path = './data/datset_28July2021/total/' # Source file
train_path = './data/dataset_28July2021/train/' # Training data
test_path = './data/dataset_28July2021/test/'   # Testing data
train_csv = train_path + 'train.csv'            # Training csv
test_csv = test_path + 'test.csv'               # Testing csv

training_size = int(num_data*training_fraction)

#Initial file bank (0 to num_data-1)
while(counter<num_data):
    # unprocessed files are labeled as 0
    file_bank.append(0)
    counter += 1


# The program will consider all images contain index (1 to num_data)
counter = 0
while(counter<=num_data):
    # Get a random file
    index = random.randint(1,num_data)

    # Move unprocessed file to training set
    if(file_bank[index-1] == 0)and(training_counter<=training_size):
        cmd1 = 'cp ./data/dataset_28July2021/total/img_' + str(index) + '.jpg '
        cmd2 = train_path
        os.system(cmd1 + cmd2)
        print("training:"+cmd1+cmd2)
        with open(train_csv, 'a') as csvfile:
                writer = csv.writer(csvfile)
                img_name = 'img_' + str(index) + '.jpg'
                # Define range of data in terms of classes
                if(((index >= 1)and(index <= 552))): 
                    writer.writerow([img_name,0])
                if(((index >= 553)and(index <= 1078))): 
                    writer.writerow([img_name,1])
                if(((index >= 1079)and(index <= 1680))): 
                    writer.writerow([img_name,2])
                if(((index >= 1681)and(index <= 2196))): 
                    writer.writerow([img_name,3])
                if(((index >= 2197)and(index <= 2780))): 
                    writer.writerow([img_name,4])
                if(((index >= 2781)and(index <= 3339))): 
                    writer.writerow([img_name,5])
        file_bank[index-1] = 1
        training_counter += 1
        counter += 1
    # Move unprocessed file to testing set
    elif (file_bank[index-1] == 0)and(training_counter>training_size):
        cmd1 = 'cp ./data/dataset_28July2021/total/img_' + str(index) + '.jpg '
        cmd2 = test_path
        os.system(cmd1 + cmd2)
        print("testing:"+cmd1+cmd2)
        with open(test_csv, 'a') as csvfile:
                writer = csv.writer(csvfile)
                img_name = 'img_' + str(index) + '.jpg'
                # Define range of data in terms of classes
                if(((index >= 1)and(index <= 552))): 
                    writer.writerow([img_name,0])
                if(((index >= 553)and(index <= 1078))): 
                    writer.writerow([img_name,1])
                if(((index >= 1079)and(index <= 1680))): 
                    writer.writerow([img_name,2])
                if(((index >= 1681)and(index <= 2196))): 
                    writer.writerow([img_name,3])
                if(((index >= 2197)and(index <= 2780))): 
                    writer.writerow([img_name,4])
                if(((index >= 2781)and(index <= 3339))): 
                    writer.writerow([img_name,5])
        file_bank[index-1] = 1
        training_counter += 1
        counter += 1
    else:
        p = 0

print("Dataset is ready...")
print("Number of training data:" + str(training_size))
print("Number of testing data:" + str(num_data-training_size))