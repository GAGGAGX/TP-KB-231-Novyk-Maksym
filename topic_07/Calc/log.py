import os
from datetime import datetime

class Logger:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), "log.log")

    def log_operation(self, a, b, tool, res, elapsed):
        act_time = datetime.now().strftime("%A %Y-%m-%d %H:%M:%S")
        with open(self.file_path, "a") as file:
            file.write(f"{act_time} | {a} {tool} {b} = {res} | Elapsed: {elapsed:.9f} seconds\n")
