from jinja2 import Environment, FileSystemLoader
import libvirt

def main():

  # Set jinja environment and set template file to use
  environment = Environment(loader=FileSystemLoader("templates/"))
  template = environment.get_template("default.xml")

  # variables to read from user
  name        = input("Enter the VMs name.                           (Default will be 'Test')\n") or 'Test'
  description = input("Enter a description.                          (Default will be 'Testing 123')\n") or 'Testing 123'
  memory      = input("How much memory? In MiB E.g. 4096             (Default will be 4096)\n") or 4096
  vcpus       = input("How many virtual CPUs E.g. 2                  (Default will be 4)\n") or 4
  path        = input("What is the absolute path for the QCOW image? (Default will be '/var/lib/libvirt/images/centos8'\n") or '/var/lib/libvirt/images/centos8'
  iso         = input("What is the absolute path for the Linux ISO   (Default will be '/var/lib/libvirt/images/CentOS-Stream-9-latest-x86_64-dvd1.iso'\n") or '/var/lib/libvirt/images/CentOS-Stream-9-latest-x86_64-dvd1.iso'
  
  filename = f"virt-xml.xml"
  content = template.render(
      name=name,
      description=description,
      memory=memory,
      vcpus=vcpus,
      path=path,
      iso=iso
  )
  with open(filename, mode="w", encoding="utf-8") as message:
    message.write(content)
    print(f"Created file {filename}")

  with open(filename) as fp:
    xmlconfig = fp.read()

  conn = libvirt.open('qemu:///system')
  instance = conn.defineXML(xmlconfig)

  instance.create()
  instance.isActive()

main()