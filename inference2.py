import cv2
import torch
from torch import nn
from torchvision import transforms
from torch.autograd import Variable

# Name of model (please confirm)
model_name = 'neck_pose_net_v2'

# Video source
video_input_path = 'data/dataset_28July2021/videos/man_2.avi'
capture = cv2.VideoCapture(video_input_path)

# Load network with CUDA support
network_save_path = 'models/' + model_name +'.pt'
pose_CNN = torch.load(network_save_path)
print(pose_CNN)
if torch.cuda.is_available():       
    pose_CNN = pose_CNN.cuda()  

transformer = transforms.ToTensor()

while (capture.isOpened()):
    # Load video frames
    ret,frame = capture.read()

    # Resize frame
    #frame = cv2.resize(frame,(720,480))

    # np array to tensor
    # # Expand dimensions from [3,480,720] to [1,3,480,720]
    image_tensor = transformer(frame)   
    image_tensor = torch.unsqueeze(image_tensor,0)
    if torch.cuda.is_available():
            image_tensor = Variable(image_tensor).cuda()

    # Inference and search for max probability
    direction = pose_CNN(image_tensor)
    _,predicted = torch.max(direction.data,1)
    pose_label = predicted.item()
    print("Pose label:",pose_label)

    # Message Visualization
    if(pose_label==0):
        cv2.putText(frame, 'End of range poking chin', (10, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (204, 0, 204), 2, cv2.LINE_AA)
    elif(pose_label==1):
        cv2.putText(frame, 'Second worst poking chin', (10, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (204, 0, 204), 2, cv2.LINE_AA)
    elif(pose_label==2):
        cv2.putText(frame, 'The limit of acceptable poking chin', (10, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (204, 0, 204), 2, cv2.LINE_AA)
    elif(pose_label==3):
        cv2.putText(frame, 'Upright head position', (10, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (204, 0, 204), 2, cv2.LINE_AA)
    elif(pose_label==4):
        cv2.putText(frame, 'The limit of acceptable neck extension', (10, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (204, 0, 204), 2, cv2.LINE_AA)
    elif(pose_label==5):
        cv2.putText(frame, 'The end of range of neck extension', (10, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (204, 0, 204), 2, cv2.LINE_AA)
    else:
        cv2.putText(frame, 'UNKOWN', (10, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (204, 0, 204), 2, cv2.LINE_AA)

    # Display
    cv2.imshow('Output',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
