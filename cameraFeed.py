# get the necessary library that has the video
import cv2

# define the video capture object
# video capture things start here
# think like its src in the scanner from java ithink
vid = cv2.VideoCapture(0)

# set up infinite loop that breaks when an action is performed
while(True):
    # capture the video frame by frame
    ret, frame = vid.read()

    # display the resulting frame
    cv2.imshow('frame', frame)
    # yes, it can probably update this per frame
    # ithink thats really fun
    """cv2.imwrite('images\capture.png', frame)"""

    # caputre one frame of the feed
    # store it as an image somewhere
    if cv2.waitKey(1) & 0xFF == ord('c'):
        # make a file in the directory
        cv2.imwrite('images\capture.png', frame)
        # from here it should be possible to do some fancy stuff like do verification and all that

    # set q as the quitting button
    # breaks the loop when the user desires
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video capture object after the loop ends
vid.release()
# destroy all windows
cv2.destroyAllWindows()