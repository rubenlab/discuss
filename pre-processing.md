# Server Network Configuration Documentation

This document provides an overview of the changes made to the network settings on the server, including modifications to Netplan configuration files, routing tables, and the creation of a systemd service file for applying custom routing rules.

## Netplan Configuration

- Added two configuration files located at `/etc/netplan/`. These files define the network interfaces and their settings, including IP addresses and routing preferences.

## Routing Table Modifications

- Modified the `/etc/iproute2/rt_tables` file to define custom routing tables. This allows for advanced routing policies that can specify different routing behaviors for different network interfaces or IP addresses.

## systemd Service for Custom Routing Rules

- Created a new systemd service file to apply custom routing rules at system startup. This ensures that the specified routing policies remain effective even after the system reboots.
  - **Service File Location**: The service file is located at `/etc/systemd/system/custom-routes.service`.
  - **Purpose**: This service executes `ip rule` and `ip route` commands to add custom routing rules based on the requirements. These rules are crucial for ensuring that outbound traffic from the server uses the appropriate source IP address, according to the custom routing policies.

## Conclusion

The above changes were implemented to refine the network behavior of the server, ensuring optimal routing and network interface configuration. By adjusting the Netplan settings, updating the routing tables, and ensuring the persistence of custom routing rules through a systemd service, the server's network configuration is tailored to meet specific operational requirements.
