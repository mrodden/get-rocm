#!/usr/bin/env python3

# Copyright 2024 Mathew Odden <mathewrodden@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import ctypes
from ctypes import c_uint, c_int, POINTER, byref


def get_rocm_version(lib):
    c_uint_p = POINTER(c_uint)

    lib.getROCmVersion.argtypes = [c_uint_p, c_uint_p, c_uint_p]
    lib.getROCmVersion.res_type = c_int

    m = c_uint()
    n = c_uint()
    r = c_uint()

    res = lib.getROCmVersion(byref(m), byref(n), byref(r))

    if res != 0:
        raise Exception("getROCmVersion() returned res=%d" % res)

    return m.value, n.value, r.value


def main():
    path = "/opt/rocm/lib/librocm-core.so"
    rocm_core = ctypes.cdll.LoadLibrary(path)
    version = get_rocm_version(rocm_core)
    vstr = ".".join(map(str, version))
    print("Found rocm-core at %r, ROCm version %r" % (path, vstr))



if __name__ == "__main__":
    main()
