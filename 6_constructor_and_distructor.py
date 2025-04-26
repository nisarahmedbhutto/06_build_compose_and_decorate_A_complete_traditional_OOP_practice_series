
class Logger:
    def __init__(self):
        print("logger created")

    def __del__(self):
        print("logger destroyed")

log = Logger()
print(log)