import webbrowser
file_path = r"C:\Users\lukas\Documents\GitHub\NoNameOrga_LKL\NoNameOrga_MainSite.html"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print ("The file on {file_path}n was not found")
except Exception as e:
    print ("An error occured: {e}")

try:
    webbrowser.open_new_tab(r"file://" + file_path)
except Exception as e:
    print(f"An error has occured: {e}")