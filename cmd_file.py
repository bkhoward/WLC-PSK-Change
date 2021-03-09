# 	- 5508 Series 'config wlan security wpa akm psk set-key ascii {psk} {wlan_id}'
# 	- vWLC Series '	wlan ONEguest_Midland
# 	 				 security wpa psk set-key ascii 0 Returntodemand21!'
#

cmd = {
    ###### AIREOS COMMANDS ######
    # change PSK syntax 'config wlan security wpa akm psk set-key ascii {psk} {wlan_id}'
    'aireos_psk': 'config wlan security wpa akm psk set-key ascii',
    'aireos_ap': 'show ap summary',
    'get_wlan': 'show wlan sum',
    # disable wlan syntax 'config wlan disable {wlan_id}'
    'aireos_wlan_disable': 'config wlan disable',
    # enable wlan syntax 'config wlan enable {wlan_id}'
    'aireos_wlan_enable': 'config wlan enable',
    'aireos_save': 'save config',
    'aireos_yes': ' y ',

    ###### IOS COMMANDS ######
    'ios_psk': 'security wpa psk set-key ascii 0',
    'ios_save': 'copy run start',
    'ios_config': 'config t',
    'ios_shutdown': 'shutdown',
    'ios_no_shutdown': 'no shutdown',
    'get_wlan': 'show wlan sum'
}
