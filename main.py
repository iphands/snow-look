import cv2
from vidgear.gears import CamGear

URL = "https://www.youtube.com/watch?v=c_XLrUYV8tk"


def capture(url: str) -> None:
    stream = CamGear(
        source=URL, y_tube=True, time_delay=1, stream_mode=True, logging=True
    ).start()
    frame = stream.read()
    if frame is not None:
        print(frame)
        cv2.imwrite("frame.jpg", frame)
        print("Frame captured successfully as frame.jpg")
    else:
        print("Failed to capture frame. Check the YouTube URL or network connection.")
    stream.stop()


if __name__ == "main":
    main()
