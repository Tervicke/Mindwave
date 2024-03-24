import os
import pkg_resources

# List of module names to exclude
EXCLUDED_MODULES = ["EditorWidget", "MenuBar", "SideMenu", "app_settings"]

def get_package_version(package_name):
    try:
        return pkg_resources.get_distribution(package_name).version
    except pkg_resources.DistributionNotFound:
        return None

def main():
    project_dir = 'src/'
    packages = set()
    for root, dirs, files in os.walk(project_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                with open(file_path, 'r') as f:
                    for line in f:
                        if line.startswith("import ") or line.startswith("from "):
                            parts = line.split(" ")
                            if len(parts) >= 2:
                                package = parts[1].split(".")[0].strip()
                                if package not in EXCLUDED_MODULES:
                                    packages.add(package)

    with open('requirements.txt', 'w') as req_file:
        for package in sorted(packages):
            version = get_package_version(package)
            if version:
                req_file.write(f"{package}=={version}\n")
            else:
                req_file.write(f"{package}\n")

if __name__ == "__main__":
    main()

