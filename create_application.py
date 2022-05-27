import shutil
import subprocess
import sys
import zipapp

shutil.copytree("src", "build/src", dirs_exist_ok=True)


subprocess.check_call(
    [
        sys.executable,
        "-m",
        "pip",
        "install",
        "-r",
        "requirements.txt",
        "--target",
        "build",
    ]
)


zipapp.create_archive("build", "app.pyz", main="src.cli:app")
