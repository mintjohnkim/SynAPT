_, _, frames = next(os.walk(vid_path)) #load frames of a vid
frames.sort(key = lambda x: int(x[10:15]))

if not os.path.exists(output_path):  #designate an output path
    os.mkdir(output_path)

video_name = output_path + '/' + cur_vid_name + '0.mp4'
enc_video_name = output_path + '/' + cur_vid_name + '.mp4'

frame = cv2.imread(os.path.join(vid_path, frames[0]))
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'FMP4')
video = cv2.VideoWriter(video_name, fourcc, 30.0, (width,height))

for image in frames:
    video.write(cv2.imread(os.path.join(vid_path, image)))

cv2.destroyAllWindows()
video.release()

os.system('ffmpeg -i ' + video_name + ' -vcodec h264 ' + enc_video_name)
os.remove(video_name)

