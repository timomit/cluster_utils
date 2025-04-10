# cluster_utils
Nice routines to work on a hpc cluster

## Installation

As of now, the package is not pubished on `PyPI` and most likely never will.
Therefore, a clone this repo and install it:

`cd cluster_utils` and `python -m pip install -e .`

## Modules

### 1. UUID Directory Creator

A simple Python module to create a directory with a UUID as its name. 
Useful to store simulation data at unique place.


#### Usage

You can use the package in the following ways:

#### Command Line

- Basic usage (creates in current directory): `uuid-dir`
- With specific path: `uuid-dir --path /tmp`
- Or set the environment variable `MY_PROJECT_DIR` to some existing path and run `uuid-dir`

#### In a Bash Script

```bash
#!/bin/bash
Capture the output only if successful

if UUID_DIR=$(uuid-dir); then
echo "Directory created successfully at: $UUID_DIR"
# Do something with the UUID_DIR variable
ls -la "$UUID_DIR"
else
echo "Failed to create directory"
exit 1
fi
```


#### As a Python Module

``` python
from cluster_utils.make_uuid_dir import main
Call the main function directly

main()
```


## License

MIT
