# Copyright 2022 TIER IV, Inc.
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


import re


def camel_to_snake(text):
    text = re.sub("(.)([A-Z][a-z]+)", R"\1_\2", text)
    text = re.sub("([a-z0-9])([A-Z])", R"\1_\2", text)
    return text.lower()


def hook_markdown_link(text, depth):
    pattern = re.compile(r"\[(.*?)]\(/(.*?)\)")
    parents = "../" * depth
    return pattern.sub(f"[\\1]({parents}\\2)", text)
