# Router Firewall

## Overview

Welcome to the *Router Firewall*  project. This project involved creating an IPv4 topology with 11 hosts and 6 switches, following specific communication rules for hosts. This is because there is also a malicious host which is attempting to gain access to trusted hosts. The code files include final_skel.py (for assembling the topology) and finalcontroller_skel.py (for controlling the topology).

## Implementation

### Handling Packets

To manage packets, three helper functions were implemented: `drop` (to drop packets), `flood` (for ARP packets), and `sender` (to send packets through the appropriate switch port). The logic for handling packets involved checking for ARP or ICMP packets and applying the necessary actions.

## Prerequisites

To set up and run this project, make sure you have the following:

- Python installed on your system.
- Pox library installed (`pip install pox`).
- Mininet library installed (`pip install mininet`).

## Usage

1. **Clone the Repository:**
   - Clone this repository to your local machine.

2. **Create the Topology:**
   - Execute the final_skep Python script to create the topoology (`python finalcontroller_skel.py`).

3. **Create the Rules:**
   - Execute the finalcontroller_skel  script to create the rules (`python finalcontroller_skel.py`).
