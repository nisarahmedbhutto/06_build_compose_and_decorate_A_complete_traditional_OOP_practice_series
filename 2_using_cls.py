class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Objects Created : {cls.count}")


tracking1 = Counter()
tracking2 = Counter()
tracking3 = Counter()

Counter.show_count()
