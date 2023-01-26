import sys
from jinja2 import Environment, FileSystemLoader
import libvirt
import configparser
import http.server
import socketserver


# HTTP server for serving kickstart file
def start_server():
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", 80), Handler) as httpd:
        print("serving at port", 80)
        httpd.serve_forever()



if __name__ == "__main__":

    # Set jinja environment and set template file to use
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("default.xml.jinja")

    # Read config file
    config = configparser.ConfigParser()
    config.read('config/vm.ini')
    defaults = config['DEFAULT']

    # configparser variables from vm.ini
    name          = defaults['name']
    description   = defaults['description']
    memory        = defaults['memory']
    vcpus         = defaults['vcpus']
    path          = defaults['path']
    iso           = defaults['iso']
    kickstart     = defaults['kickstart']

    content = template.render(
        name=name,
        description=description,
        memory=memory,
        vcpus=vcpus,
        path=path,
        iso=iso,
        kickstart=kickstart
    )

    filename = "virt-xml.xml"
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
        print("Created file", {filename})

    with open(filename, encoding="utf-8") as vm_xml:
        xmlconfig = vm_xml.read()

    conn = libvirt.open('qemu:///system')
    if conn is None:
        print('Failed to connect to the hypervisor')
        sys.exit(1)

    instance = conn.defineXML(xmlconfig)
    if instance is None:
        print('Failed to define the instance')
        sys.exit(1)


    instance.create()
    start_server()





