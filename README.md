# Core OS Ignition extractor

```
$ ./extractor.py ign.json ign-root
Storage: ign-root/storage/etc/containers/registries.conf
Storage: ign-root/storage/etc/ignition-machine-config-encapsulated.json
Storage: ign-root/storage/etc/motd
Storage: ign-root/storage/etc/pki/ca-trust/source/anchors/ca.crt
Storage: ign-root/storage/etc/profile.d/proxy.sh
Storage: ign-root/storage/etc/systemd/system.conf.d/10-default-env-godebug.conf
Storage: ign-root/storage/etc/systemd/system.conf.d/10-default-env.conf
Storage: ign-root/storage/root/.docker/config.json
Storage: ign-root/storage/usr/local/bin/approve-csr.sh
Storage: ign-root/storage/usr/local/bin/bootkube.sh
Storage: ign-root/storage/usr/local/bin/crio-configure.sh
Storage: ign-root/storage/usr/local/bin/installer-gather.sh
Storage: ign-root/storage/usr/local/bin/installer-masters-gather.sh
Storage: ign-root/storage/usr/local/bin/kubelet-pause-image.sh
Storage: ign-root/storage/usr/local/bin/release-image-download.sh
Storage: ign-root/storage/usr/local/bin/release-image.sh
Storage: ign-root/storage/usr/local/bin/report-progress.sh
Storage: ign-root/storage/opt/openshift/manifests/04-openshift-machine-config-operator.yaml
Storage: ign-root/storage/opt/openshift/manifests/cloud-controller-uid-config.yml
Storage: ign-root/storage/opt/openshift/manifests/cloud-provider-config.yaml
Storage: ign-root/storage/opt/openshift/manifests/cluster-config.yaml
Storage: ign-root/storage/opt/openshift/manifests/cluster-dns-02-config.yml
Storage: ign-root/storage/opt/openshift/manifests/cluster-infrastructure-02-config.yml
Storage: ign-root/storage/opt/openshift/manifests/cluster-ingress-02-config.yml
Storage: ign-root/storage/opt/openshift/manifests/cluster-ingress-default-ingresscontroller.yaml
Storage: ign-root/storage/opt/openshift/manifests/cluster-network-01-crd.yml
Storage: ign-root/storage/opt/openshift/manifests/cluster-network-02-config.yml
Storage: ign-root/storage/opt/openshift/manifests/cluster-proxy-01-config.yaml
Storage: ign-root/storage/opt/openshift/manifests/cluster-scheduler-02-config.yml
Storage: ign-root/storage/opt/openshift/manifests/cvo-overrides.yaml
Storage: ign-root/storage/opt/openshift/manifests/etcd-ca-bundle-configmap.yaml
Storage: ign-root/storage/opt/openshift/manifests/etcd-client-secret.yaml
Storage: ign-root/storage/opt/openshift/manifests/etcd-metric-client-secret.yaml
Storage: ign-root/storage/opt/openshift/manifests/etcd-metric-serving-ca-configmap.yaml
Storage: ign-root/storage/opt/openshift/manifests/etcd-metric-signer-secret.yaml
Storage: ign-root/storage/opt/openshift/manifests/etcd-namespace.yaml
Storage: ign-root/storage/opt/openshift/manifests/etcd-service.yaml
Storage: ign-root/storage/opt/openshift/manifests/etcd-serving-ca-configmap.yaml
Storage: ign-root/storage/opt/openshift/manifests/etcd-signer-secret.yaml
Storage: ign-root/storage/opt/openshift/manifests/kube-cloud-config.yaml
Storage: ign-root/storage/opt/openshift/manifests/kube-system-configmap-root-ca.yaml
Storage: ign-root/storage/opt/openshift/manifests/machine-config-server-tls-secret.yaml
Storage: ign-root/storage/opt/openshift/manifests/openshift-config-secret-pull-secret.yaml
Storage: ign-root/storage/opt/openshift/manifests/openshift-kubevirt-infra-namespace.yaml
Storage: ign-root/storage/opt/openshift/openshift/99_cloud-creds-secret.yaml
Storage: ign-root/storage/opt/openshift/openshift/99_kubeadmin-password-secret.yaml
Storage: ign-root/storage/opt/openshift/openshift/99_role-cloud-creds-secret-reader.yaml
Storage: ign-root/storage/opt/openshift/openshift/openshift-install-manifests.yaml
Storage: ign-root/storage/opt/openshift/openshift/99_openshift-cluster-api_master-user-data-secret.yaml
Storage: ign-root/storage/opt/openshift/openshift/99_openshift-machineconfig_99-master-ssh.yaml
Storage: ign-root/storage/opt/openshift/openshift/99_openshift-machineconfig_99-worker-ssh.yaml
Storage: ign-root/storage/opt/openshift/openshift/99_openshift-cluster-api_worker-user-data-secret.yaml
Storage: ign-root/storage/opt/openshift/openshift/99_openshift-cluster-api_worker-machineset-0.yaml
Storage: ign-root/storage/opt/openshift/openshift/99_openshift-cluster-api_worker-machineset-1.yaml
Storage: ign-root/storage/opt/openshift/openshift/99_openshift-cluster-api_worker-machineset-2.yaml
Storage: ign-root/storage/opt/openshift/auth/kubeconfig
Storage: ign-root/storage/opt/openshift/auth/kubeconfig-kubelet
Storage: ign-root/storage/opt/openshift/auth/kubeconfig-loopback
Storage: ign-root/storage/opt/openshift/tls/admin-kubeconfig-ca-bundle.crt
Storage: ign-root/storage/opt/openshift/tls/aggregator-ca.key
Storage: ign-root/storage/opt/openshift/tls/aggregator-ca.crt
Storage: ign-root/storage/opt/openshift/tls/aggregator-ca-bundle.crt
Storage: ign-root/storage/opt/openshift/tls/aggregator-client.key
Storage: ign-root/storage/opt/openshift/tls/aggregator-client.crt
Storage: ign-root/storage/opt/openshift/tls/aggregator-signer.key
Storage: ign-root/storage/opt/openshift/tls/aggregator-signer.crt
Storage: ign-root/storage/opt/openshift/tls/apiserver-proxy.key
Storage: ign-root/storage/opt/openshift/tls/apiserver-proxy.crt
Storage: ign-root/storage/opt/openshift/tls/etcd-ca-bundle.crt
Storage: ign-root/storage/opt/openshift/tls/etcd-metric-ca-bundle.crt
Storage: ign-root/storage/opt/openshift/tls/etcd-metric-signer.key
Storage: ign-root/storage/opt/openshift/tls/etcd-metric-signer.crt
Storage: ign-root/storage/opt/openshift/tls/etcd-metric-signer-client.key
Storage: ign-root/storage/opt/openshift/tls/etcd-metric-signer-client.crt
Storage: ign-root/storage/opt/openshift/tls/etcd-signer.key
Storage: ign-root/storage/opt/openshift/tls/etcd-signer.crt
Storage: ign-root/storage/opt/openshift/tls/etcd-client.key
Storage: ign-root/storage/opt/openshift/tls/etcd-client.crt
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-lb-ca-bundle.crt
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-lb-server.key
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-lb-server.crt
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-internal-lb-server.key
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-internal-lb-server.crt
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-lb-signer.key
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-lb-signer.crt
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-localhost-ca-bundle.crt
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-localhost-server.key
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-localhost-server.crt
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-localhost-signer.key
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-localhost-signer.crt
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-service-network-ca-bundle.crt
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-service-network-server.key
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-service-network-server.crt
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-service-network-signer.key
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-service-network-signer.crt
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-complete-server-ca-bundle.crt
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-complete-client-ca-bundle.crt
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-to-kubelet-ca-bundle.crt
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-to-kubelet-client.key
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-to-kubelet-client.crt
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-to-kubelet-signer.key
Storage: ign-root/storage/opt/openshift/tls/kube-apiserver-to-kubelet-signer.crt
Storage: ign-root/storage/opt/openshift/tls/kube-control-plane-ca-bundle.crt
Storage: ign-root/storage/opt/openshift/tls/kube-control-plane-kube-controller-manager-client.key
Storage: ign-root/storage/opt/openshift/tls/kube-control-plane-kube-controller-manager-client.crt
Storage: ign-root/storage/opt/openshift/tls/kube-control-plane-kube-scheduler-client.key
Storage: ign-root/storage/opt/openshift/tls/kube-control-plane-kube-scheduler-client.crt
Storage: ign-root/storage/opt/openshift/tls/kube-control-plane-signer.key
Storage: ign-root/storage/opt/openshift/tls/kube-control-plane-signer.crt
Storage: ign-root/storage/opt/openshift/tls/kubelet-bootstrap-kubeconfig-ca-bundle.crt
Storage: ign-root/storage/opt/openshift/tls/kubelet-client-ca-bundle.crt
Storage: ign-root/storage/opt/openshift/tls/kubelet-client.key
Storage: ign-root/storage/opt/openshift/tls/kubelet-client.crt
Storage: ign-root/storage/opt/openshift/tls/kubelet-signer.key
Storage: ign-root/storage/opt/openshift/tls/kubelet-signer.crt
Storage: ign-root/storage/opt/openshift/tls/kubelet-serving-ca-bundle.crt
Storage: ign-root/storage/opt/openshift/tls/machine-config-server.key
Storage: ign-root/storage/opt/openshift/tls/machine-config-server.crt
Storage: ign-root/storage/opt/openshift/tls/service-account.key
Storage: ign-root/storage/opt/openshift/tls/service-account.pub
Storage: ign-root/storage/opt/openshift/tls/journal-gatewayd.key
Storage: ign-root/storage/opt/openshift/tls/journal-gatewayd.crt
Storage: ign-root/storage/opt/openshift/tls/root-ca.crt
Systemd unit: ign-root/systemd/approve-csr.service
Systemd unit: ign-root/systemd/bootkube.service
Systemd unit: ign-root/systemd/chown-gatewayd-key.service
Systemd unit: ign-root/systemd/crio-configure.service
Systemd unit: ign-root/systemd/kubelet.service
Systemd unit: ign-root/systemd/progress.service
Systemd unit: ign-root/systemd/release-image.service
Systemd unit: ign-root/systemd/systemd-journal-gatewayd.service.d/certs.conf
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
│   │   ├── profile.d
│   │   │   └── proxy.sh
│   │   └── systemd
│   │       └── system.conf.d
│   │           ├── 10-default-env.conf
│   │           └── 10-default-env-godebug.conf
│   ├── opt
│   │   └── openshift
│   │       ├── auth
│   │       │   ├── kubeconfig
│   │       │   ├── kubeconfig-kubelet
│   │       │   └── kubeconfig-loopback
│   │       ├── manifests
│   │       │   ├── 04-openshift-machine-config-operator.yaml
│   │       │   ├── cloud-controller-uid-config.yml
│   │       │   ├── cloud-provider-config.yaml
│   │       │   ├── cluster-config.yaml
│   │       │   ├── cluster-dns-02-config.yml
│   │       │   ├── cluster-infrastructure-02-config.yml
│   │       │   ├── cluster-ingress-02-config.yml
│   │       │   ├── cluster-ingress-default-ingresscontroller.yaml
│   │       │   ├── cluster-network-01-crd.yml
│   │       │   ├── cluster-network-02-config.yml
│   │       │   ├── cluster-proxy-01-config.yaml
│   │       │   ├── cluster-scheduler-02-config.yml
│   │       │   ├── cvo-overrides.yaml
│   │       │   ├── etcd-ca-bundle-configmap.yaml
│   │       │   ├── etcd-client-secret.yaml
│   │       │   ├── etcd-metric-client-secret.yaml
│   │       │   ├── etcd-metric-serving-ca-configmap.yaml
│   │       │   ├── etcd-metric-signer-secret.yaml
│   │       │   ├── etcd-namespace.yaml
│   │       │   ├── etcd-service.yaml
│   │       │   ├── etcd-serving-ca-configmap.yaml
│   │       │   ├── etcd-signer-secret.yaml
│   │       │   ├── kube-cloud-config.yaml
│   │       │   ├── kube-system-configmap-root-ca.yaml
│   │       │   ├── machine-config-server-tls-secret.yaml
│   │       │   ├── openshift-config-secret-pull-secret.yaml
│   │       │   └── openshift-kubevirt-infra-namespace.yaml
│   │       ├── openshift
│   │       │   ├── 99_cloud-creds-secret.yaml
│   │       │   ├── 99_kubeadmin-password-secret.yaml
│   │       │   ├── 99_openshift-cluster-api_master-user-data-secret.yaml
│   │       │   ├── 99_openshift-cluster-api_worker-machineset-0.yaml
│   │       │   ├── 99_openshift-cluster-api_worker-machineset-1.yaml
│   │       │   ├── 99_openshift-cluster-api_worker-machineset-2.yaml
│   │       │   ├── 99_openshift-cluster-api_worker-user-data-secret.yaml
│   │       │   ├── 99_openshift-machineconfig_99-master-ssh.yaml
│   │       │   ├── 99_openshift-machineconfig_99-worker-ssh.yaml
│   │       │   ├── 99_role-cloud-creds-secret-reader.yaml
│   │       │   └── openshift-install-manifests.yaml
│   │       └── tls
│   │           ├── admin-kubeconfig-ca-bundle.crt
│   │           ├── aggregator-ca-bundle.crt
│   │           ├── aggregator-ca.crt
│   │           ├── aggregator-ca.key
│   │           ├── aggregator-client.crt
│   │           ├── aggregator-client.key
│   │           ├── aggregator-signer.crt
│   │           ├── aggregator-signer.key
│   │           ├── apiserver-proxy.crt
│   │           ├── apiserver-proxy.key
│   │           ├── etcd-ca-bundle.crt
│   │           ├── etcd-client.crt
│   │           ├── etcd-client.key
│   │           ├── etcd-metric-ca-bundle.crt
│   │           ├── etcd-metric-signer-client.crt
│   │           ├── etcd-metric-signer-client.key
│   │           ├── etcd-metric-signer.crt
│   │           ├── etcd-metric-signer.key
│   │           ├── etcd-signer.crt
│   │           ├── etcd-signer.key
│   │           ├── journal-gatewayd.crt
│   │           ├── journal-gatewayd.key
│   │           ├── kube-apiserver-complete-client-ca-bundle.crt
│   │           ├── kube-apiserver-complete-server-ca-bundle.crt
│   │           ├── kube-apiserver-internal-lb-server.crt
│   │           ├── kube-apiserver-internal-lb-server.key
│   │           ├── kube-apiserver-lb-ca-bundle.crt
│   │           ├── kube-apiserver-lb-server.crt
│   │           ├── kube-apiserver-lb-server.key
│   │           ├── kube-apiserver-lb-signer.crt
│   │           ├── kube-apiserver-lb-signer.key
│   │           ├── kube-apiserver-localhost-ca-bundle.crt
│   │           ├── kube-apiserver-localhost-server.crt
│   │           ├── kube-apiserver-localhost-server.key
│   │           ├── kube-apiserver-localhost-signer.crt
│   │           ├── kube-apiserver-localhost-signer.key
│   │           ├── kube-apiserver-service-network-ca-bundle.crt
│   │           ├── kube-apiserver-service-network-server.crt
│   │           ├── kube-apiserver-service-network-server.key
│   │           ├── kube-apiserver-service-network-signer.crt
│   │           ├── kube-apiserver-service-network-signer.key
│   │           ├── kube-apiserver-to-kubelet-ca-bundle.crt
│   │           ├── kube-apiserver-to-kubelet-client.crt
│   │           ├── kube-apiserver-to-kubelet-client.key
│   │           ├── kube-apiserver-to-kubelet-signer.crt
│   │           ├── kube-apiserver-to-kubelet-signer.key
│   │           ├── kube-control-plane-ca-bundle.crt
│   │           ├── kube-control-plane-kube-controller-manager-client.crt
│   │           ├── kube-control-plane-kube-controller-manager-client.key
│   │           ├── kube-control-plane-kube-scheduler-client.crt
│   │           ├── kube-control-plane-kube-scheduler-client.key
│   │           ├── kube-control-plane-signer.crt
│   │           ├── kube-control-plane-signer.key
│   │           ├── kubelet-bootstrap-kubeconfig-ca-bundle.crt
│   │           ├── kubelet-client-ca-bundle.crt
│   │           ├── kubelet-client.crt
│   │           ├── kubelet-client.key
│   │           ├── kubelet-serving-ca-bundle.crt
│   │           ├── kubelet-signer.crt
│   │           ├── kubelet-signer.key
│   │           ├── machine-config-server.crt
│   │           ├── machine-config-server.key
│   │           ├── root-ca.crt
│   │           ├── service-account.key
│   │           └── service-account.pub
│   ├── root
│   └── usr
│       └── local
│           └── bin
│               ├── approve-csr.sh
│               ├── bootkube.sh
│               ├── crio-configure.sh
│               ├── installer-gather.sh
│               ├── installer-masters-gather.sh
│               ├── kubelet-pause-image.sh
│               ├── release-image-download.sh
│               ├── release-image.sh
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
