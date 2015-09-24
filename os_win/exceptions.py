# Copyright 2015 Cloudbase Solutions Srl
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Utility class for VM related operations on Hyper-V.
"""

from os_win._i18n import _


class OSWinException(Exception):
    msg_fmt = '%(message)s'

    def __init__(self, message=None, **kwargs):
        self.kwargs = kwargs

        if not message:
            message = self.msg_fmt % kwargs

        self.message = message
        super(OSWinException, self).__init__(message)


class HyperVException(OSWinException):
    pass


# TODO(alexpilotti): Add a storage exception base class
class VHDResizeException(HyperVException):
    msg_fmt = _("Exception encountered while resizing the VHD %(vhd_path)s."
                "Reason: %(reason)s")


class HyperVAuthorizationException(HyperVException):
    msg_fmt = _("The Windows account running nova-compute on this Hyper-V "
                "host doesn't have the required permissions to perform "
                "Hyper-V related operations.")


class HyperVVMNotFoundException(HyperVException):
    msg_fmt = _("VM not found: %(vm_name)s")


class SMBException(OSWinException):
    pass
