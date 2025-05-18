import time
import cv2
import os

from typing import Dict, Any
from vidgear.gears import CamGear

STREAMS: Dict[str, Dict[str, str]] = {
    "alpental_mid": {"url": "https://www.youtube.com/watch?v=c_XLrUYV8tk"}
}


def say(name: str, msg: str) -> None:
    print(f"[{name}] {msg}")


def init_streams() -> Dict[str, Dict[str, Any]]:
    ret = {}
    for k, v in STREAMS.items():
        say(k, "Initializing stream...")
        v["stream"] = CamGear(
            source=v["url"], y_tube=True, time_delay=1, stream_mode=True, logging=True
        ).start()
        ret[k] = v
    return ret


def capture(name: str, url: str, stream: Any) -> None:
    say(name, "Starting capture")
    stamp = int(time.time())
    frame = stream.read()
    if frame is not None:
        cv2.imwrite(f"./data/{name}-{stamp}.jpg", frame)
    else:
        say(
            name,
            "Failed to capture frame. Check the YouTube URL or network connection.",
        )
    stream.stop()


def main() -> None:
    streams = init_streams()
    while True:
        for k, v in streams.items():
            capture(k, v["stream"], v["url"])
            time.sleep(90)


if __name__ == "__main__":
    main()
