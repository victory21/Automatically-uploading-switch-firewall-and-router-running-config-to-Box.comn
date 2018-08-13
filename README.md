# uploading-running-config-to-Box.comn

the program uploads switch, router, and firewall running configurations onto Box.com

Switches and Routers running Cisco Catalyst and Nexus OS, respectively

Firewall running CheckPoint Next Gen 5 OS

input a spreadsheet file with name of device, and ip address along with more specific login details

uses the netmiko module to SSH to the various IP addresses of the devices that are requested and excecute the commands to obtain the running configuration

first trials used the paramiko for its SSH function but it was quite lacking

uses JWT authentication, i.e. JSON Web Tokens, to be able to dynamiacly login and interact with the Box.com server from anycomputer that has the matching RSA Private Key and private Key passphrase.

uses boxsdk module to interact and upload files to specific directories on the Box.com server so that the user may access them later

is able to have the authentication information on an "importable" file so abit more security

can easily be changed to upload other information from the network devices to Box.com

