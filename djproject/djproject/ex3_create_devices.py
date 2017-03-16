#!/usr/bin/env python

from net_system.models import NetworkDevice
import django

def main():
    django.setup()
    ip_addr = raw_input('Enter IP address: ')

    test_rtr1 = NetworkDevice(
        device_name='test-rtr1',
        device_type='cisco_ios',
        ip_address=ip_addr,
        port=5022,
    )
    test_rtr1.save()

    test_rtr2 = NetworkDevice.objects.get_or_create(
        device_name='test-rtr2',
        device_type='cisco_ios',
        ip_address=ip_addr,
        port=1022,
    )

    # verify devices that currently exist
    print
    devices = NetworkDevice.objects.all()
    for a_device in devices:
        print a_device
        print a_device.ip_address
    print


if __name__ == '__main__':
    main()
