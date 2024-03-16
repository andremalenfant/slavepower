# SlavePower  synch the power status of a slave device to a master's power status
#
# Copyright (C) 2024 Andre Malenfant (andre@andremalenfant.com)
#
# This file may be distributed under the terms of the GNU GPLv3 license.


from __future__ import annotations
import logging

from typing import (
    Dict,
    Any,    
)

class SlavePower:
    def __init__(self, config):
        self.server = config.get_server()
        self.name = config.get_name()

        self.master = config.get("master")
        self.slave = config.get("slave")

        self.server.register_event_handler("power:power_changed", self._on_power_changed)
        
    def _on_power_changed(self, device_info: Dict[str, Any]) -> None:
        if device_info["device"] == self.master:
            power: PrinterPower = self.server.lookup_component("power")
            power.set_device_power(self.slave, device_info["status"])
            
def load_component(config):
    return SlavePower(config)