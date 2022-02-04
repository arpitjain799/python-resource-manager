# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
#
# Generated code. DO NOT EDIT!
#
# Snippet for ListTagKeys
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-resourcemanager


# [START cloudresourcemanager_generated_resourcemanager_v3_TagKeys_ListTagKeys_sync]
from google.cloud import resourcemanager_v3


def sample_list_tag_keys():
    # Create a client
    client = resourcemanager_v3.TagKeysClient()

    # Initialize request argument(s)
    request = resourcemanager_v3.ListTagKeysRequest(
        parent="parent_value",
    )

    # Make the request
    page_result = client.list_tag_keys(request=request)
    for response in page_result:
        print(response)

# [END cloudresourcemanager_generated_resourcemanager_v3_TagKeys_ListTagKeys_sync]
