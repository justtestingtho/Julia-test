import json
import re


def main():
    
    json_path = "ex.json"
    docker_path = "Dockerfile"
    
    try:
        j_file = open(json_path, "r")
        d_file = open(docker_path, "r")

        l_json = json.load(j_file)
        l_docker = d_file.readlines()

        package_list = l_json.get("Packages")

        pkg_commands = []
        counter = 0
        for pkg in package_list:
            if counter != len(package_list) - 1:
                cmd = f'    julia -e \'using Pkg; pkg"add {pkg}"; pkg"precompile"\' && \\\n'

            else:
                cmd = f'    julia -e \'using Pkg; pkg"add {pkg}"; pkg"precompile"\' \n'
            
            pkg_commands.append(cmd)
            counter += 1
 
        remove_pkgs = []

        existing_pkg_index = [i for i, s in enumerate(l_docker, start=0) if re.search('.*using Pkg', s)]

        for index, lines in enumerate(l_docker):

            if index not in existing_pkg_index:
                remove_pkgs.append(lines)

        RUN_index = [i for i, s in enumerate(l_docker, start=0) if re.search('.*RUN', s)]

        insert_at = RUN_index[0] + 1

        remove_pkgs[insert_at:insert_at] = pkg_commands

        store_updated = open("Dockerfile", "w")

        for update in remove_pkgs:
            store_updated.write(update)
    
        store_updated.close()
        
        print("Updated Docker File is stored. Please check...")
    
    except Exception as e:
        print("Exception :", e)
    

if __name__ == "__main__":
    
    main()


    
    

