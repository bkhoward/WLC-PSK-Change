# ---------------------------------------------------------------------------------------------------------------#
# host[] is a list of dictionaries containing the following key value pairs for each host
    # ip:ip_address for mgmt access
    # hostname:hostname of device
    # device_type:used to find the template file in ntc_templates
# ---------------------------------------------------------------------------------------------------------------#
# host_list = [['CSI-2504', '192.168.1.9', '5508', 'grep include "System Name" "show sysinfo"']]

host = [
    {'ip': '10.252.17.31', 'hostname': 'US-TX-MDL-4451-vWLC', 'device_type': 'cisco_ios'}
    #{'ip': '10.225.232.26', 'hostname': 'RP-WLC-5508-1', 'device_type': 'cisco_wlc_ssh'},
    # {'ip': '10.241.0.30', 'hostname': 'US-TX-KRC-WLC', 'device_type': 'cisco_wlc_ssh'},
    # {'ip': '10.240.40.30', 'hostname': 'US-TX-MDL-vWLC', 'device_type': 'cisco_wlc_ssh'},
    # {'ip': '10.54.202.30', 'hostname': 'Q93-WLC-5508-A', 'device_type': 'cisco_wlc_ssh'},
    # {'ip': '10.32.11.180', 'hostname': 'GP-WLC-5508-A', 'device_type': 'cisco_wlc_ssh'},
    # {'ip': '10.32.11.230', 'hostname': 'DC-WLC-5508-A', 'device_type': 'cisco_wlc_ssh'}

    # {'ip': '10.243.67.22', 'hostname': 'US-OK-OKA-vWLC', 'device_type': 'cisco_ios'},
    # {'ip': '10.243.75.22', 'hostname': 'US-OK-OKC-vWLC', 'device_type': 'cisco_ios'},
    # {'ip': '10.243.71.22', 'hostname': 'US-OK-FOS-vWLC', 'device_type': 'cisco_ios'},
    # {'ip': '10.243.79.22', 'hostname': 'US-ND-WFC-vWLC', 'device_type': 'cisco_ios'},
    # {'ip': '10.243.86.22', 'hostname': 'US-UT-ROS-vWLC', 'device_type': 'cisco_ios'},
    # {'ip': '10.243.30.15', 'hostname': 'US-TX-TWL-WLC-9800', 'device_type': 'cisco_ios'},
#     {'ip': '10.231.201.15', 'hostname': 'US-CO-FTST-WLC-9800', 'device_type': 'cisco_ios'}

#     {'ip': '10.231.248.42', 'hostname': 'US-CO-FTST-EIA-WLC-9800', 'device_type': 'cisco_ios'},
#     {'ip': '10.54.8.42', 'hostname': 'CA-AB-Q93-EIA-WLC-9800', 'device_type': 'cisco_ios'},
#     {'ip': '10.54.202.21', 'hostname': 'CA-AB-Q93-WLC-9800', 'device_type': 'cisco_ios'},
]
