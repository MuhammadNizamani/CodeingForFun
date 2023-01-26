import subprocess


class Main():
    def __init__(self) -> None:
        self.allWifiNames = []
        self.wifiNames = []
        self.paswords = []
        self.wifiNamesWithPasword = {}
        self.NoOFPasswordNotFound = 0

        self.meta_data = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profiles'])
        # decoding meta data
        self.data = self.meta_data.decode('utf-8', errors="backslashreplace")
        # splitting data by line by line
        self.data = self.data.split('\n')

        self.profileGetter()
        self.passwordGetter()
        # print(self.wifiNamesWithPasword)

        if self.NoOFPasswordNotFound == 0:
            print("Sir, I have sucessfully found passwords for all wifi networks")
        else:
            found = len(list(self.wifiNamesWithPasword.keys()))
            notFound = self.NoOFPasswordNotFound
            print(
                f"Sir, I have found passwords of {found} networks out of {found+notFound}  ")

    def profileGetter(self):
        newL = []
        # Getting all the names of wifi
        for i in self.data:
            if "All User Profile" in i:
                newL.append(i)
        # Stripping whitspaces and unnecessary things from names
        for p in newL:
            name = ""
            startAppending = False
            for q in p:
                if startAppending:
                    name += str(q)
                if q == ":":
                    startAppending = True
                if q == "\\":
                    startAppending = False
            self.allWifiNames.append(name)
        self.wifiNames = []
        for name in self.allWifiNames:
            name = name.rstrip()
            newName = name.replace(" ", "", 1)
            self.wifiNames.append(newName)
            if newName == "Python":
                self.wifiNames.append('PTCL-BB')


    def passwordGetter(self):
        for i in self.wifiNames:
            try:
                # Getting password of all wifi networks
                wifiName = i
                print('Trying to get password for = "{0}"'.format(i))
                meta_data_password = subprocess.check_output(
                    ['netsh', 'wlan', 'show', 'profile', f"{wifiName}", 'key=clear'])
                meta_data_password = meta_data_password.decode("UTF-8")
                meta_data_password = meta_data_password.split("\n")

                # Checking if the wifi is open or it has password
                isWifiOpen = None
                for i in meta_data_password:
                    if "Authentication" in i:
                        if "Open" in i:
                            isWifiOpen = True
                        else:
                            isWifiOpen = False

                # Stripping whitspaces and unnecessary things from password
                password = ""
                if not isWifiOpen:
                    for p in meta_data_password:
                        if "Key Content" in p:
                            name = ""
                            startAppending = False
                            for q in p:
                                if startAppending:
                                    name += str(q)
                                if q == "\\":
                                    startAppending = False
                                if q == ":":
                                    startAppending = True
                            password = name
                    password = password.rstrip()
                    password = password.replace(" ", "")
                else:
                    password = "WIFI IS OPEN"
                self.wifiNamesWithPasword[wifiName] = password

            # Handling any error if it arises
            except Exception as e:
                self.NoOFPasswordNotFound += 1


a = Main()
# print(a.NoOFPasswordNotFound)
print(a.wifiNamesWithPasword)
