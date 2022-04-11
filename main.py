import argparse
import os
import sys

import uvicorn


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--workers", type=int, default=None)
    parser.add_argument("--reload", action="store_true")
    return parser.parse_args()


def main():
    print(f"""
___________                __     _____ __________.___ 
\_   _____/____    _______/  |_  /  _  \ ______   \   |
 |    __) \__  \  /  ___/\   __\/  /_\  \|     ___/   |
 |     \   / __ \_\___ \  |  | /    |    \    |   |   |
 \___  /  (____  /____  > |__| \____|__  /____|   |___|
     \/        \/     \/               \/              
    """)

    args = parse_args()

    if sys.platform == "win32":
        workers = 1
    else:
        workers = args.workers or min(os.cpu_count() + 1, 32)

    uvicorn.run("src.fastapi_template.main:app", host=args.host, port=args.port, workers=workers, reload=args.reload)


if __name__ == "__main__":
    main()
