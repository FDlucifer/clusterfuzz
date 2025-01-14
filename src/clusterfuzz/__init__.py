# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""libClusterfuzz package."""

import os

if not os.getenv('ROOT_DIR'):
  # If ROOT_DIR isn't set by the time we import this, assume we're
  # libClusterFuzz.
  this_dir = os.path.dirname(os.path.abspath(__file__))
  os.environ['CONFIG_DIR_OVERRIDE'] = os.path.join(this_dir, 'lib-config')
  os.environ['ROOT_DIR'] = os.path.dirname(os.path.dirname(this_dir))
  os.environ['LIB_CF'] = 'True'

  from ._internal.system import environment
  environment.set_default_vars()
