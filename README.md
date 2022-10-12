# SynAPT

This repository contains instructions needed to recreate the synthetic dataset for Synthetic Action Pre-training and Transfer (SynAPT) benchmark detailed in the paper *How Transferable are Video Representations Based on Synthetic Data?*


## Download Assets 
Visit the following links and download the three synthetic video datasets. 
- Eldersim: https://ai4robot.github.io/ElderSim/
- PHAV: http://adas.cvc.uab.es/phav/
- SURREACT: https://github.com/gulvarol/surreact

Note that it is possible to download the synthetic video rendering simulators for Eldersim and SURREACT, but it is sufficient to download SynADL for Eldersim and pre-rendered NTU and UESTC videos for SURREACT. Also, we only utilize the RGB data from Eldersim and SURREACT.
To download SynADL, sign the EULA and send a copy to the email address which can be found under the section Contact.


## Convert Frames/Videos

For consistency, you can either:
- Extract the frames from Eldersim and SURREACT videos, and place each group of frames under a folder named after the original video name.  
- Render frames of PHAV video into a video (e.g. mp4), and name the video output file after the original folder name. 


Refer to `frame_to_vid.py` and `vid_to_frame.py` for example scripts that extract frames from videos and render videos from frames, respectively, using `cv2` and `ffmpeg`. 


## Formatting
Place the downloaded assets in the following format:
``` 
-- SynAPT
---- createSynAPT.py
---- eldersim
------ video_0 (e.g. A001_P101_G008_C006.avi)
-------- 00001.jpg (if in frames format)
-------- 00002.jpg
-------- …
------ video_1 (e.g. A001_P101_G003_C020.avi)
-------- …
---- phav
------ class_name_0 (e.g. BrushHair)
-------- video_0 (e.g. b5009-Lake-Dawn-Clear-79_84-Civilian_Male04-....)
---------- 00001.jpg (if in frames format)
---------- 00002.jpg
---------- …
-------- video_1 (e.g. b5009-House-Dawn-Cloudy-79_84-MaleCharacter....)
---------- …
-------- …
------ …
---- surreact
------ video_0 (e.g. S017C003P016R001A011_v225_r00.mp4)
-------- 00001.jpg (if in frames format)
-------- 00002.jpg
-------- ...
------ video_1_folder (e.g. S017C003P016R001A011_v045_r00.mp4)
------ ... 
```


## Create SynAPT

Run `createSynAPT.py` to create the synthetic dataset. The dataset will be created in the root directory under `SynAPT_videos`.

## Models and Pre-trained Weights 

For our experiments with the various model architectures (TSN, I3D, R(2+1)), we used the IBM/action-recognition-pytorch GitHub repository (https://github.com/IBM/action-recognition-pytorch). 

TSN, I3D, and R(2+1)D models pretrained on the Synthetic data and Kinetics subset can be found here:
https://drive.google.com/drive/folders/1hAdtrwrSTKDlb0xBmDlMvawwqaiSnv6m?usp=sharing

## More Information
- You can find the 150 synthetic classes of SynAPT in `syn_labels.txt`. 
- You can find the 150 Kinetics classes used for comparison in `kinetics_labels.txt`, and the exact examples in `kinetics_total.txt`.
- To further clarify the SynAPT, we answered a set of questions listed on the *Datasheets for Datasets (Gebru et al., https://arxiv.org/pdf/1803.09010.pdf)*. Refer to `DataSheet.pdf`.
- Train/val splits used in the paper for Kinetics 150-class subset and the synthetic dataset can be found in `kinetics150_train.txt`, `kinetics150_val.txt`, `sim150_train.txt`, and `sim150_val.txt`.
















