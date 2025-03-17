import cv2, os, time

raw_dataset_dir = "dataset/raw"

files = os.listdir(raw_dataset_dir)


for video in files:
    # recreate video path, opens with vidcap, creates save name 
    video_path = os.path.join(raw_dataset_dir, video)
    cap = cv2.VideoCapture(video_path)
    video_name = video.split(".")[0]

    # output folder to store frames
    output_folder = f'./dataset/{video_name}'
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
        print(f"Folder '{output_folder}' created.")
    else:
        print(f"Folder '{output_folder}' already exists.")

    # set capture framerate
    fps = cap.get(cv2.CAP_PROP_FPS)
    capture_fps = 30 #NOTE: this is the minimum i think we should increase but idk dataset fps
    frame_interval = 1 / capture_fps

    # loop frames
    curr_frame = 0
    prev_time = time.time()

    while cap.isOpened():
        ret,frame = cap.read()
        if not ret:
            print("Error reading frame. Exiting...")
            break

        curr_time = time.time()
        if (curr_time - prev_time) >= frame_interval:
            frame_name = f'{video_name}_{curr_frame}.jpg' #NOTE: idk if high enough quality// can change if u want
            cv2.imwrite(frame_name, frame)
            curr_frame += 1
            prev_time = curr_time

cap.release()
cv2.destroyAllWindows()




    

