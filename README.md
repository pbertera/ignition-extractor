# Core OS Ignition extractor

Most of the code is a copy-paste from [omg](https://github.com/kxr/o-must-gather).

```bash
$ Usage: extractor.py [OPTIONS]

Options:
  -h, --help     show this help message and exit
  -d             perform a diff between two ignition files
  -c             show content of the diff
  -f FILES       file to load, use "-" for stdin.
  -o OUTPUT_DIR  outout directory where the ignition file should be extracted
  -s SYNTAX      syntax of the files (json or yaml)
  -m             the loaded content is a MachineConfig
```

## Extract from a Machine Config

```bash
$ oc get mc 00-master -o json | ./extractor.py -f - -m -d masters
$ tree masters
masters/
├── storage
│   ├── etc
│   │   ├── containers
│   │   │   └── storage.conf
│   │   ├── kubernetes
│   │   │   ├── apiserver-url.env
│   │   │   ├── ca.crt
│   │   │   ├── kubelet-ca.crt
│   │   │   ├── kubelet-plugins
│   │   │   │   └── volume
│   │   │   │       └── exec
│   │   │   ├── manifests
│   │   │   │   └── apiserver-watcher.yaml
│   │   │   └── static-pod-resources
│   │   │       └── configmaps
│   │   │           └── cloud-config
│   │   │               └── ca-bundle.pem
│   │   ├── mco
│   │   │   └── proxy.env
│   │   ├── modules-load.d
│   │   │   └── iptables.conf
│   │   ├── NetworkManager
│   │   │   └── conf.d
│   │   │       ├── 99-keyfiles.conf
│   │   │       ├── hostname.conf
│   │   │       └── sdn.conf
│   │   ├── pki
│   │   │   └── ca-trust
│   │   │       └── source
│   │   │           └── anchors
│   │   │               └── openshift-config-user-ca-bundle.crt
│   │   ├── ssh
│   │   │   └── sshd_config.d
│   │   │       └── 10-disable-ssh-key-dir.conf
│   │   ├── sysctl.d
│   │   │   ├── forward.conf
│   │   │   └── inotify.conf
│   │   ├── systemd
│   │   │   ├── system
│   │   │   │   └── kubelet.service.d
│   │   │   │       └── 20-logging.conf
│   │   │   └── system.conf.d
│   │   │       ├── 10-default-env-godebug.conf
│   │   │       └── kubelet-cgroups.conf
│   │   └── tmpfiles.d
│   │       ├── cleanup-cni.conf
│   │       └── nm.conf
│   ├── opt
│   │   └── libexec
│   │       └── openshift-gcp-routes.sh
│   ├── usr
│   │   └── local
│   │       ├── bin
│   │       │   ├── configure-ovs.sh
│   │       │   └── recover-kubeconfig.sh
│   │       └── sbin
│   │           └── set-valid-hostname.sh
│   └── var
│       └── lib
│           └── kubelet
│               └── config.json
└── systemd
    ├── crio.service.d
    │   ├── 10-mco-default-env.conf
    │   ├── 10-mco-default-madv.conf
    │   └── 10-mco-profile-unix-socket.conf
    ├── docker.socket.d
    │   ├── gcp-hostname.service
    │   └── mco-disabled.conf
    ├── gcp-routes.service.d
    │   └── mco-disabled.conf
    ├── kubelet.service.d
    │   ├── 10-mco-default-env.conf
    │   ├── 10-mco-default-madv.conf
    │   ├── etc-NetworkManager-system\x2dconnections\x2dmerged.mount
    │   ├── machine-config-daemon-firstboot.service
    │   ├── machine-config-daemon-pull.service
    │   ├── nodeip-configuration.service.disabled
    │   ├── node-valid-hostname.service
    │   ├── openshift-gcp-routes.service
    │   └── ovs-configuration.service
    ├── ovsdb-server.service.d
    │   └── 10-ovsdb-restart.conf
    ├── ovs-vswitchd.service.d
    │   └── 10-ovs-vswitchd-restart.conf
    ├── pivot.service.d
    │   └── 10-mco-default-env.conf
    ├── rpm-ostreed.service.d
    │   └── mco-controlplane-nice.conf
    └── zincati.service.d
        └── mco-disabled.conf
```

## Extract from an ignition file

```bash
$ ./extractor.py -f ign.json -o ign-root
Storage: ign-root/storage/etc/containers/registries.conf
Storage: ign-root/storage/etc/ignition-machine-config-encapsulated.json
Storage: ign-root/storage/etc/motd
[...]
Storage: ign-root/storage/opt/openshift/tls/root-ca.crt
Systemd unit: ign-root/systemd/approve-csr.service
[...]
Systemd unit: ign-root/systemd/systemd-journal-gatewayd.service.d/systemd-journal-gatewayd.socket
User: ign-root/passwd/core

$ tree ign-root
ign-root
├── passwd
│   └── core
├── storage
│   ├── etc
│   │   ├── containers
│   │   │   └── registries.conf
│   │   ├── ignition-machine-config-encapsulated.json
│   │   ├── motd
│   │   ├── pki
│   │   │   └── ca-trust
│   │   │       └── source
│   │   │           └── anchors
│   │   │               └── ca.crt
[...]
│               └── report-progress.sh
└── systemd
    ├── approve-csr.service
    ├── bootkube.service
    ├── chown-gatewayd-key.service
    ├── crio-configure.service
    ├── kubelet.service
    ├── progress.service
    ├── release-image.service
    └── systemd-journal-gatewayd.service.d
        ├── certs.conf
        └── systemd-journal-gatewayd.socket
```

## Diff between two MachineConfig

```bash
$ ./extractor.py -d -f rendered-infra-52a886f905663a424954dd22c3116e3d.txt -f rendered-infra-5010f1247f65a4aff09cb78a66f7781a.txt -s yaml -m -c
```
