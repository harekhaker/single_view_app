import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from file_uploader import insert_new
from .config import *
import os




try:
    os.mkdir(WATCHED_DIR)

except FileExistsError:
        pass

for update_func in update_tor, update_anonymization, update_malicious, update_proxy:
    update_func()

patterns = "*"
ignore_patterns = ""
ignore_directories = False
case_sensitive = True
file_adding_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)


def on_created(event):
    insert_new(event.src_path)


file_adding_event_handler.on_created = on_created

go_recursively = True

music_observer = Observer()


music_observer.schedule(file_adding_event_handler, WATCHED_DIR, recursive=go_recursively)

music_observer.start()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    music_observer.stop()