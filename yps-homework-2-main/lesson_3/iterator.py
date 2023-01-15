#!venv/bin/python


def generator_function(start: int = 0, end: int = 100):
    print("generator_function started")
    while start < end:
        print(f"Will return start={start}")
        yield start
        print(f"Continue from here with start={start}")
        start += 10
        print(f"Add 10 to start. Now start={start}")


if __name__ == "__main__":
    generator = generator_function(80)
    print(generator)
    for i in generator:
        print(i)
