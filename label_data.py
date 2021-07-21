import csv

# Training data
#source_file_path = 'data/train/train.csv'
#dest_file_path = 'data/train/train_new.csv'

# Testing data
source_file_path = 'data/test/test.csv'
dest_file_path = 'data/test/test_new.csv'

def find_index(file_name):
    return file_name.find('.')

with open(source_file_path,mode='r') as data:
    rows = csv.reader(data)   
    for row in rows:
        i = find_index(row[0])
        index = int(row[0][4:i])
        print("Index:",index)
        
        if(index>=1)and(index<=53):
            with open(dest_file_path, 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([row[0],0])

        if(index>=54)and(index<=103):
            with open(dest_file_path, 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([row[0],1])
        
        if(index>=104)and(index<=155):
            with open(dest_file_path, 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([row[0],2])

        if(index>=156)and(index<=194):
            with open(dest_file_path, 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([row[0],3])

        if(index>=195)and(index<=246):
            with open(dest_file_path, 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([row[0],4])

        if(index>=247)and(index<=298):
            with open(dest_file_path, 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([row[0],5])
