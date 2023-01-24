from jinja2 import Environment, FileSystemLoader

def main():

  # Set jinja environment and set template file to use
  environment = Environment(loader=FileSystemLoader("templates/"))
  template = environment.get_template("default.xml")

  # variables to read from user
  name        = input("Enter the VMs name. - ")
  description = input("Enter a description. - ")
  memory      = input("How much memory? In MB E.g. 4096 - ")
  vcpus       = input("How many virtual CPUs E.g. 2 - ")
  path        = input("What is the absolute path for the QCOW image? - ")
  iso         = input("What is the absolute path for the Linux ISO - ")
  
  filename = f"message_{test.lower()}.xml"
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
    print(f"... wrote {filename}")

main()