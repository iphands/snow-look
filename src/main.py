import time
import cv2
import os

from typing import Dict, Any
from vidgear.gears import CamGear

STREAMS: Dict[str, str] = {
    "alpental_mid": "https://www.youtube.com/watch?v=c_XLrUYV8tk",
    "central_express": "https://www.youtube.com/watch?v=0_LK8swEqzc",
}


def say(name: str, msg: str) -> None:
    print(f"[{name}] {msg}")


def init_streams() -> Dict[str, Dict[str, Any]]:
    ret = {}
    for k, v in STREAMS.items():
        say(k, "Initializing stream...")
        stream = CamGear(
            source=v, y_tube=True, time_delay=1, stream_mode=True, logging=True
        ).start()
        ret[k] = {
            "url": v,
            "stream": stream,
        }
    return ret


# def capture(name: str, stream: Any) -> None:
def capture(name: str, url: str) -> None:
    say(name, "Starting capture")
    stream = CamGear(
        source=url, y_tube=True, time_delay=1, stream_mode=True, logging=True
    ).start()
    stamp = int(time.time())
    frame = stream.read()
    if frame is not None:
        cv2.imwrite(f"./data/{name}/{stamp}.jpg", frame)
    else:
        say(
            name,
            "Failed to capture frame. Check the YouTube URL or network connection.",
        )
    stream.stop()


def main() -> None:
    for k in STREAMS.keys():
        os.makedirs(f"data/{k}", exist_ok=True)
    # streams = init_streams()
    while True:
        for k, v in STREAMS.items():
            capture(k, v)
        time.sleep(300)


if __name__ == "__main__":
    main()
