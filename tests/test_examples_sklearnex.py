# ==============================================================================
# Copyright 2023 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import os
import subprocess
import sys
import unittest

import pytest

test_path = os.path.abspath(os.path.dirname(__file__))
unittest_data_path = os.path.join(test_path, "unittest_data")
examples_path = os.path.join(os.path.dirname(test_path), "examples", "sklearnex")


@pytest.mark.parametrize(
    "file",
    [
        f
        for f in os.listdir(examples_path)
        if f.endswith(".py") and "spmd" not in f and "dpnp" not in f and "dpctl" not in f
    ],
)
def test_generator(file):
    # Run the script and capture its exit code
    process = subprocess.run(
        [sys.executable, os.path.join(examples_path, file)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )  # nosec
    exit_code = process.returncode

    # Assert that the exit code is 0
    if exit_code:
        pytest.fail(
            pytrace=False,
            reason=f"Example has failed, the example's output:\n{process.stdout.decode()}\n{process.stderr.decode()}",
        )
