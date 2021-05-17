#!/usr/bin/python
# -*- coding: utf-8 -*-
# This code comes from the omg project
# https://github.com/kxr/o-must-gather/ 

import os
import yaml
import json
import sys
from base64 import b64decode
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from urllib.parse import unquote

def decode_content(content):
    """
    Decodes url/bas64 encoded content found in machine-configs
    Certificate data is also converted to human readable format
    """
    split = content.split(",", 1)
    head = split[0]
    data = split[1]
    if head.startswith("data:"):
        if len(data) == 0:
            return ""
        form = head[5:].split(";")
        if "base64" in form:
            charset = next((x[8:] for x in form if x[0:8] == "charset="), "utf-8")
            dec_data = b64decode(data).decode(charset)
        else:
            dec_data = unquote(data)

        if dec_data.startswith("-----BEGIN CERTIFICATE-----"):
            certs = []
            cert = []
            for cert_line in dec_data.splitlines():
                if cert_line != "-----END CERTIFICATE-----":
                    cert.append(cert_line)
                else:
                    cert.append(cert_line)
                    certs.append("\n".join(cert))
                    cert = []
            dec_certs = []
            for c in certs:
                dec_cert = []
                parse_cert = x509.load_pem_x509_certificate(
                    str.encode(c), default_backend()
                )
                dec_cert.append("~~~~~BEGIN CERTIFICATE~~~~~")
                dec_cert.append("SUBJECT    : " + parse_cert.subject.rfc4514_string())
                dec_cert.append("ISSUER     : " + parse_cert.issuer.rfc4514_string())
                dec_cert.append("SERIAL     : " + str(parse_cert.serial_number))
                dec_cert.append(
                    "NOT BEFORE : " + parse_cert.not_valid_before.isoformat()
                )
                dec_cert.append(
                    "NOT AFTER  : " + parse_cert.not_valid_after.isoformat()
                )
                dec_cert.append("~~~~~END CERTIFICATE~~~~~")
                dec_certs.append("\n".join(dec_cert))
            return "\n".join(dec_certs)
        else:
            return dec_data
    else:
        print('[Warning] Unable to recognize content (not starting with "data:")')
        return content

def write_unit(systemd_path, unit):
    os.makedirs(systemd_path, exist_ok=True)
    name = unit["name"]
    if "enabled" in unit:
        if unit["enabled"] is not True:
            name += ".disabled"
    if "contents" in unit:
        abs_fil = os.path.join(systemd_path, name)
        with open(abs_fil, "w") as fh:
            print("Systemd unit: " + abs_fil)
            fh.write(unit["contents"])


def extract(dest_dir, ignition_file = None):
    if ignition_file:
        ign_file = open(ignition_file)
        ign_json = json.load(ign_file)
        ign_file.close()
    else:
        ign_json = json.load(sys.stdin)
    os.makedirs(dest_dir, exist_ok=True)
    storage_path = os.path.join(dest_dir, 'storage')
    os.makedirs(storage_path, exist_ok=True)
    
    storage = systemd = passwd = {}
    if "storage" in ign_json:
        storage = ign_json['storage']
    if "files" in storage:
        for fi in storage["files"]:
            path = fi["path"]
            rel_fil = path[1:]
            rel_dir = os.path.dirname(rel_fil)
            abs_dir = os.path.join(storage_path, rel_dir)
            abs_fil = os.path.join(storage_path, rel_fil)
            os.makedirs(abs_dir, exist_ok=True)
            with open(abs_fil, "w") as fh:
                print("Storage: " + abs_fil)
                if "contents" in fi:
                  fh.write(decode_content(fi["contents"]["source"]))
                else:
                  fh.write('') 
    # TODO directories, links, disks, raid, filesystems
    # systemd
    if "systemd" in ign_json:
        systemd = ign_json['systemd']
        systemd_path = os.path.join(dest_dir, "systemd")
    if "units" in systemd:
        for unit in systemd["units"]:
            if "dropins" in unit:
                systemd_path = os.path.join(
                    dest_dir, "systemd/" + unit["name"] + ".d"
                )
                for unit in unit["dropins"]:
                    write_unit(systemd_path, unit)
            else:
                write_unit(systemd_path, unit)
    # passwd
    if "passwd" in ign_json:
        passwd = ign_json["passwd"]
        passwd_path = os.path.join(dest_dir, "passwd")
    if "users" in passwd:
        for user in passwd["users"]:
            os.makedirs(passwd_path, exist_ok=True)
            name = user["name"]
            abs_fil = os.path.join(passwd_path, name)
            with open(abs_fil, "w") as fh:
                print("User: " + abs_fil)
                fh.write(yaml.dump(user))
    # TODO groups
    # TODO networkd

if __name__ == '__main__':
    if len(sys.argv) == 3:
        dest_dir = sys.argv[1]
        file = sys.argv[2]
        extract(dest_dir, file)
    if len(sys.argv) == 2:
        dest_dir = sys.argv[1]
        extract(dest_dir)
    else:
        print('Usage: %s extract-dir <ignition-file>' % sys.argv[0])
        sys.exit(-1)
