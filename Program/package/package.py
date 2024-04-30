class package:
    @staticmethod
    def install_delete_package(bash):
        bash = bash.replace("pkg", "")
        bash = bash.replace(" ", "")
        if "install" in bash:
            bash = bash.replace("install", "")
            return bash
        elif "delete" in bash:
            bash = bash.replace("delete", "")
            return bash
        
print(package().install_delete_package("pkg install HUH"))