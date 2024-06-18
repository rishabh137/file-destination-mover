import os
import shutil
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

"""
Directory name we want to access
"""
target_dir = "/home/rishabh/Downloads"
dir_music = "/home/rishabh/Music"
dir_video = "/home/rishabh/Videos"
dir_image = "/home/rishabh/Pictures"
dir_document = "/home/rishabh/Documents"


"""
Move files from source to destination using shutil
"""
def move(dest, entry):
    shutil.move(entry, dest)


"""
Define the file format
"""
class ChangeFileDir(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(target_dir) as entries:
            for entry in entries:
                name = entry.name
                dest = target_dir

                if name.endswith(".mp3"):
                    dest = dir_music
                    move(dest, entry)
                elif name.endswith(".mp4"):
                    dest = dir_video
                    move(dest, entry)
                elif (
                    name.endswith(".jpg")
                    or name.endswith(".png")
                    or name.endswith(".jpeg")
                ):
                    dest = dir_image

                    move(dest, entry)

                elif name.endswith(".pdf") or name.endswith(".docx"):
                    dest = dir_document

                    move(dest, entry)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    """
    Set path variable to the directory we want to track
    """
    path = target_dir
    event_handler = ChangeFileDir()

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
