import os
import ntpath
import time
import datetime
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from file_uploader import process_file
from django.conf import settings

for unprocessed_file in os.listdir(settings.MEDIA_ROOT):
    if not '.py' in unprocessed_file:
        unprocessed_file_path = os.path.join(settings.MEDIA_ROOT, unprocessed_file)
        process_file(unprocessed_file_path)
        process_file_name = unprocessed_file + datetime.datetime.now().isoformat()
        os.rename(unprocessed_file_path, os.path.join(settings.MEDIA_PROCESSED, process_file_name))


patterns = "*"
ignore_patterns = ""
ignore_directories = False
case_sensitive = True
file_adding_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)


def on_created(event):
    process_file(event.src_path)
    process_file_name = ntpath.basename(event.src_path) + datetime.datetime.now().isoformat()
    os.rename(event.src_path, os.path.join(settings.MEDIA_PROCESSED, process_file_name))


file_adding_event_handler.on_created = on_created

go_recursively = True

music_observer = Observer()

music_observer.schedule(file_adding_event_handler, settings.MEDIA_ROOT, recursive=go_recursively)

music_observer.start()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    music_observer.stop()