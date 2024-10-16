# get-rocm
Helper script for downloading and installing ROCm for various Linux environments

Inspired by [get-pip.py](https://github.com/pypa/get-pip)


# Usage

```
$ curl -sSL https://raw.githubusercontent.com/mrodden/get-rocm/refs/heads/master/get-rocm.py -o get-rocm.py
$ python get-rocm.py --rocm-version 6.0.3
```


# Github Action Usage

`get-rocm` now provides a Github Action that can be used to install ROCm at a specific version in your Github Workflows

```
name: Install ROCm
on: push

jobs:
  install-rocm:
    runs-on: ubuntu-latest
    steps:
      # checks out files from your GH repo
      - uses: actions/checkout@v4

      # get-rocm requires python3
      - uses: actions/setup-python@v5

      # Github workers have limited disk space, so freeing space is recommended before install
      - uses: jlumbroso/free-disk-space@v1.3.1

      # install ROCm (rocm_version is optional and defaults to "latest")
      - uses: mrodden/get-rocm@v1
        with:
          rocm_version: 6.2.2
```
