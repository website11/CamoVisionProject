import cv2
import numpy as np

def start_cam():
    # Turn on the webcam and snap an image
    webcam = cv2.VideoCapture(0)
    ret, img = webcam.read()

    # Convert the image to RGB
    rgb_ver = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Get unique colors
    unique_colors = np.unique(rgb_ver.reshape(-1, 3), axis=0)
    print("Unique Colors:")
    for color in unique_colors:
        print(tuple(color))
      
    cap.release()
    return unique_colors

if __name__ == "__main__":
  start_cam()




