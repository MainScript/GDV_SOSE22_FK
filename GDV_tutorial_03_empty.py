import numpy as np
import cv2

# TODO capture webcam image
webcam = cv2.VideoCapture(0)

# TODO get camera image parameters from get()
width = int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)
# TODO create a window for the video
cv2.namedWindow('An interesting title', cv2.WINDOW_FREERATIO)

# TODO start a loop
running = True
while running:

    # TODO (in loop) read a camera frame and check if that was successful
    ret, frame = webcam.read()

    if not ret:
        print('Getting Frame was unsuccessful')
        running = False
        break

    # TODO (in loop) create four flipped tiles of the image
    result = np.zeros(frame.shape, np.uint8)
    small = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    result[:height//2, :width//2] = small
    result[height//2:, :width//2] = cv2.flip(small, 0)
    result[height//2:, width//2:] = cv2.flip(small, -1)
    result[:height//2, width//2:] = cv2.flip(small, 1)

    # TODO (in loop) display the image
    cv2.imshow('An interesting title', result)

    # TODO (in loop) press q to close the window and exit the loop
    if cv2.waitKey(10) == ord('q'):
        break


# TODO release the video capture object and window
webcam.release()
cv2.destroyAllWindows()