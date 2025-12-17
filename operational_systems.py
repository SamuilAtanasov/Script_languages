os_type = input("Enter operational system(W for Windows, L for Linux):").strip().upper()
path = input("Enter path:").strip()

def is_windows_path(p):
    return "\\" in p or (len(p) > 2 and p[1:3] == ":\\")

def is_linux_path(p):
    return p.startswith("/") and "\\" not in p

if os_type == "W":
    if is_windows_path(path):
        print("The path is valid for Windows.")
    else:
        print("The path is not valid for Windows.")

elif os_type == "L":
    if is_linux_path(path):
        print("The path is valid for Linux.")
    else:
        print("The path is not valid for Linux.")

else:
    print("Invalid choice of operational system.")