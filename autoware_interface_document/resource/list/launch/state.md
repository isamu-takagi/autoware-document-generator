---
autoware_interface:
  method: notification
  type: autoware_adapi_v1_msgs/msg/AutowareLaunchState
---

# /api/autoware/launch/state

- Method: {{ autoware_interface.method }}
- Type: {{ autoware_interface.type | link_api_type }}

## Description

Get the launch state. For details, see the [launch state](../../../../features/launch-state.md).

## Message

| Name  | Type          | Description  |
| ----- | ------------- | ------------ |
| state | enum (uint32) | launch state |
