i = 0
FileCheck = False
while FileCheck == False:
    try:
        if i == 0:
            backupfile = open("/home/dita/.config/hypr/backup/hyprland.backup.conf","r")
        else: 
            backupfile = open(f"/home/dita/.config/hypr/backup/hyprland.backup.conf({i})","r")
        backupfile.close()
    except:
        FileCheck = True
        print("Passed")
        if i == 0:
            file = open("/home/dita/.config/hypr/backup/hyprland.backup.conf","w")
        else: 
            file = open(f"/home/dita/.config/hypr/backup/hyprland.backup.conf({i})","w")
        hyprconf = open("/home/dita/.config/hypr/hyprland.conf","r")

        file.write(hyprconf.read())
        hyprconf.close()
        file.close()
    else: 
        print("Failed")
        i += 1


    




print("Yup")