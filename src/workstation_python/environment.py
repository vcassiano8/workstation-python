import platform
import sys


def python_environment() -> dict[str, str]:
    return {
        "python": sys.version,
        "executable": sys.executable,
        "platform": platform.platform(),
    }
