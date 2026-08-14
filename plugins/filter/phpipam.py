# Copyright (c) 2020 Christian Meißner
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


import ipaddress

DOCUMENTATION = r'''
  name: is_subnet
  author: Christian Meißner
  version_added: '1.2.0'
  short_description: Check if a subnet belongs to another
  description:
    - First argument is a subnet  second another. If the first subnet belongs to second
  positional: _input, parent
  options:
    _input:
      description: Subnet in cidr format which should belongs to parent
      type: string
      required: true
    parent:
      description: Subnet where input should belongs to
      type: string
      required: true
'''

EXAMPLES = r'''
  192.0.2.0/25 | codeaffen.phpipam.is_subnet(192.0.2.0/24)
'''

RETURN = r'''
  _value:
    description: True if children belongs to parent and false if not or both networks are the same.
    type: bool
'''


class FilterModule(object):
    """Define useful filter in collection."""

    def filters(self):
        """Export filter for ansible.

        :return: return a dictionary of filters
        :rtype: dict
        """
        return {
            'is_subnet': is_subnet,
        }


def is_subnet(children, parent):
    """Check if a subnet belongs to another.

    First argument is a subnet  second another. If the first subnet belongs to second

    :param children: First subnet in cidr format which should belongs to parent
    :type children: string
    :param parent: Second subnet where children should belongs to
    :type parent: string
    :return: True if children belongs to parent and false if not or both networks are the same.
    :rtype: bool
    """
    c = ipaddress.ip_network(children)
    p = ipaddress.ip_network(parent)

    if not c.subnet_of(p) or c == p:
        return False
    else:
        return c.subnet_of(p)
