   vid_path = os.path.join(datasetpath, vid_name) #path to vid
vidcap = cv2.VideoCapture(vid_path)
dest_vid_path = os.path.join(outputdatasetpath, vid_name)
if not os.path.isdir(dest_vid_path):
    os.mkdir(dest_vid_path)
success,image = vidcap.read()
count = 1
while success:
    cv2.imwrite(dest_vid_path + '/{:05d}.jpg'.format(count), image)     # save frame as JPEG file      
    success,image = vidcap.read()
    # print('Read a new frame: ', success)
    count += 1
print('Converted ', vid_name)