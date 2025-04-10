#!/usr/bin/env python3

import io
import sys
from pathlib import Path

import pytest  # noqa

from cluster_utils.make_uuid_dir import main


def test_create_in_temp_dir(tmp_path, monkeypatch):
    # Set up the command line arguments
    monkeypatch.setattr(sys, "argv", ["uuid-dir", "--path", str(tmp_path)])

    # Capture stdout
    captured_output = io.StringIO()
    monkeypatch.setattr(sys, "stdout", captured_output)

    # Run the main function
    main()

    # Get the printed path
    output = captured_output.getvalue().strip()
    printed_path = Path(output)

    # Check that the directory exists
    assert printed_path.exists()
    assert printed_path.is_dir()

    # Check that it's in the temp directory
    assert (
        tmp_path in printed_path.parents
    ), f"Expected directory to be created in {tmp_path}, but it was created at {printed_path}"  # noqa
