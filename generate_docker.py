import json
import re
import os


def main():
    
    json_path = "training_config.json"
    file_path = "Dockerfile"

    
    try:
        j_file = open(json_path, "r")
        l_json = json.load(j_file)
        package_list = l_json.get("Packages")

        pkg_commands = []
        l_size = len(package_list)
        f = open("Dockerfile", 'w')
        f.write("#!/bin/bash")
        f.write("\n")
        f.write("FROM julia:latest")
        f.write("\n")
        f.write("\n")
        f.write("RUN julia -e 'import Pkg; Pkg.update()' && \\")
        f.write("\n")
        for pkg in package_list:
            if pkg != package_list[-1]:
                cmd = f'    julia -e \'using Pkg; pkg"add {pkg}"; pkg"precompile"\' && \\\n'
                f.write(cmd)

            else:
                cmd = f'    julia -e \'using Pkg; pkg"add {pkg}"; pkg"precompile"\' \n'
                f.write(cmd)

        f.write("\n")            
        f.write("ENV PATH='/opt/program:${PATH}'")
        f.write("\n")
        f.write("COPY . /opt/program")
        f.write("\n")
        f.write("ENTRYPOINT [ 'julia', './algo/train' ]")
        f.close()
        print("Updated Docker File is stored")
        l_json["IMG_URI"] = os.environ['IMAGE_REPO_NAME']
        l_json["IMG_TAG"] = os.environ['IMAGE_TAG']
        out_file = open('training_config.json','w')
        out_file.write(json.dumps(l_json))
        out_file.close()
        print("Image URI and Tag fields updated in JSON")
    
    except Exception as e:
        print("Exception :", e)
    

if __name__ == "__main__":
    
    main()


    
    

