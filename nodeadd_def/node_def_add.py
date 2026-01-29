cat node_add_def.py
#!/usr/bin/env python3

import subprocess
import sys
import readline

# -----------------------------
# Utility functions
# -----------------------------

def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return result.stdout.decode().strip()
    except subprocess.CalledProcessError as e:
        print(f"Command failed:\n{e.stderr.decode()}")
        sys.exit(1)


def get_user_input(prompt):
    try:
        return input(prompt)
    except EOFError:
        print("Input error.")
        sys.exit(1)


def define_prefix(node_number, prefix, digit_count):
    return f"{prefix}{str(node_number).zfill(digit_count)}"


def get_max_digit_count(start_node_no, last_node_no):
    return max(len(str(last_node_no)), 3)


def calculate_ip(base_ip, offset):
    """
    Correct IP rollover:
    - increments 4th octet
    - rolls over after 254
    - increments 3rd octet
    """
    o1, o2, o3, o4 = map(int, base_ip.split('.'))

    total = (o4 - 1) + offset
    third_octet = o3 + (total // 254)
    fourth_octet = (total % 254) + 1

    return f"{o1}.{o2}.{third_octet}.{fourth_octet}"


# -----------------------------
# User Inputs
# -----------------------------

subnet_prefix = int(get_user_input(
    "Enter The Subnet Prefix of Network (Valid range: 18-24): "
))
if subnet_prefix < 18 or subnet_prefix > 24:
    print("Invalid subnet prefix.")
    sys.exit(1)

node_type = get_user_input(
    "Enter The Node Type (compute, gpu, hm): "
)

pv_net_address = get_user_input(
    f"Enter Private Network Starting IP for {node_type}: "
)

bmc_net_address = get_user_input(
    f"Enter BMC Network Starting IP for {node_type}: "
)

ib_net_address = get_user_input(
    f"Enter IB Network Starting IP for {node_type}: "
)

prefix = get_user_input(
    f"Enter Node Prefix (rbcn, rpcn, rbgpu, etc): "
)

start_node_no = int(get_user_input(
    f"Enter Start {node_type} node number: "
))

last_node_no = int(get_user_input(
    f"Enter Last {node_type} node number: "
))

mac_file = get_user_input(
    f"Enter MAC file (one MAC per line): "
)

# -----------------------------
# MAC File Validation
# -----------------------------

try:
    with open(mac_file) as f:
        mac_addresses = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print(f"MAC file not found: {mac_file}")
    sys.exit(1)

required_mac_count = last_node_no - start_node_no + 1
if len(mac_addresses) < required_mac_count:
    print("Not enough MAC addresses in file.")
    sys.exit(1)

# -----------------------------
# Node Name Formatting
# -----------------------------

digit_count = get_max_digit_count(start_node_no, last_node_no)

# -----------------------------
# Main Loop
# -----------------------------

for index, node_number in enumerate(range(start_node_no, last_node_no + 1)):

    node_name = define_prefix(node_number, prefix, digit_count)
    mac = mac_addresses[index]

    offset = node_number - start_node_no

    pvt_ip = calculate_ip(pv_net_address, offset)
    bmc_ip = calculate_ip(bmc_net_address, offset)
    ib_ip  = calculate_ip(ib_net_address, offset)

    cmd = f"""
mkdef -f -t node "{node_name}" \
groups="{node_type},all" \
mgt=ipmi \
ip="{pvt_ip}" \
bmc="{bmc_ip}" \
bmcusername=root \
bmcpassword=0penBmc \
installnic=mac \
primarynic=mac \
mac="{mac}" \
nicips.ib0="{ib_ip}" \
nicnetworks.ib0=ib0 \
nictypes.ib0=Infiniband \
netboot=xnba \
postscripts="confignetwork -s,lustre.sh,ringbuf.sh"
"""

    run_command(cmd)
    print(f"✔ Node {node_name} added | IP={pvt_ip} | BMC={bmc_ip} | IB={ib_ip}")

# -----------------------------
print("\nAll nodes added successfully.")
