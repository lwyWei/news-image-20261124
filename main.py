# A working news-image-daily entry (Python 3.13, standard library only):
# its image is the entry.png beside this file, and the program copies it
# to /output/entry.png. The gate takes a whole PNG or JPEG of at most
# 1 MiB and 1024 by 1024 pixels, and the judge sees exactly the bytes copied.
# The output is left readable by every user (mode 0644): make.fun collects
# the outputs as another user than the one the program runs as.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "entry.png"
shutil.copyfile(src, out_path)
os.chmod(out_path, 0o644)
