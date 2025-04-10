#!/usr/bin/env python3

"""Create a directory with a UUID as its name.

This module provides functionality to create a directory with a UUID as its name.
It can create the directory in the current working directory, a specified path,
or a path defined by the 'MY_PROJECT_DIR' environment variable.

The module prints only the absolute path of the created directory to stdout
if successful, or raises an error otherwise.

Functions:
    main(): Parse arguments and create the UUID directory

Example usage:
    # Basic usage (creates in current directory)
    $ python make_uuid_dir.py

    # With specific path
    $ python make_uuid_dir.py --path /tmp

    # Using environment variable
    $ BLA=/var/tmp python make_uuid_dir.py
"""

import argparse
import os
import uuid
from pathlib import Path


def main():
    """Create a directory with a UUID as its name.

    Returns:
        None: Prints the absolute path of the created directory to stdout

    Raises:
        RuntimeError: If directory creation fails
    """
    parser = argparse.ArgumentParser(
        description="Create a directory with a UUID as name"
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=(
            os.environ.get("MY_PROJECT_DIR")
            if os.environ.get("MY_PROJECT_DIR")
            and Path(os.environ.get("MY_PROJECT_DIR")).exists()
            else None
        ),
        help="Path where UUID directory should be created",
    )

    args = parser.parse_args()

    directory_name = str(uuid.uuid4())
    base_path = args.path if args.path else Path.cwd()
    new_dir = base_path / directory_name

    try:
        new_dir.mkdir()
        print(new_dir.resolve())
    except Exception as e:
        raise RuntimeError(f"Failed to create directory: {e}")


if __name__ == "__main__":
    main()
