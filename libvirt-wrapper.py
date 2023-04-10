import configparser
import subprocess


if __name__ == "__main__":
    # Read config file
    config = configparser.ConfigParser()
    config.read("config/vm.ini")
    defaults = config["DEFAULT"]

    # configparser variables from vm.ini
    name = defaults["name"]
    description = defaults["description"]
    ram = defaults["ram"]
    vcpus = defaults["vcpus"]
    ks_path = defaults["ks_path"]
    os_variant = defaults["os_variant"]
    disk_path = defaults["disk_path"]
    disk_size = defaults["disk_size"]
    location = defaults["location"]
    network_bridge = defaults["network_bridge"]

    # Construct the command as a list of arguments
    cmd = [
        "virt-install",
        f"--name={name}",
        f"--ram={ram}",
        f"--vcpus={vcpus}",
        f"--disk=path={disk_path},size={disk_size}",
        f"--os-variant={os_variant}",
        "--graphics=none",
        f"--network=bridge={network_bridge}",
        f"--location={location}",
        f"--initrd-inject={ks_path}",
        "--extra-args", "inst.ks=file:/ks.cfg console=tty0 console=ttyS0,115200n8",
        "--check=all=on",
        f"--cpu=host",
    ]

    # Execute the command
    subprocess.run(cmd, check=True)
