
import argparse
import time
from datetime import datetime


def countdown(seconds: int) -> None:
    deadline = time.monotonic() + seconds

    while True:
        remaining = max(0, int(deadline - time.monotonic() + 0.999))
        minutes, seconds_left = divmod(remaining, 60)
        print(f"\rTime remaining: {minutes:02}:{seconds_left:02}", end="", flush=True)

        if remaining == 0:
            break
        time.sleep(min(1, deadline - time.monotonic()))

    print("\nTime's upjjjjj!")


def main() -> None:
    parser = argparse.ArgumentParser(description="Show the current time or run a countdown.")
    parser.add_argument(
        "seconds",
        nargs="?",
        type=int,
        help="countdown duration in seconds (omit to show the current time)",
    )
    args = parser.parse_args()

    if args.seconds is None:
        print(datetime.now().strftime("%H:%M:%S"))
    elif args.seconds <= 0:
        parser.error("seconds must be a positive integer")
    else:
        countdown(args.seconds)


if __name__ == "__main__":
    main()
