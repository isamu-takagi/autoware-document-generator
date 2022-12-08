---
autoware_interface:
  method: function call
  type: autoware_adapi_v1_msgs/srv/AutowareLaunchCommand
---

# /api/autoware/launch/command

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Launch or terminate Autoware. This API changes the [launch state](../../../../features/launch-state.md).

## Request

| Name    | Type          | Description    |
| ------- | ------------- | -------------- |
| command | enum (uint32) | launch command |

## Response

None
