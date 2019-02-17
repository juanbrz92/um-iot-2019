# IoT UM - 2019
Deployment de una plataforma de IoT en KUbernetes

Create cluster using gcloud cli (for demo purpose 6 standard nodes are going to be deployed for cluster pods). Select from the list above validMasterVersions that is higher than 1.6.2 (VALID_MASTER_VERSION) and create cluster:

gcloud container clusters create umiot --cluster-version=1.11.6-gke.3 --node-labels=machinetype=tb --num-nodes=1 --machine-type=n1-standard-2

Create additional node pool for Cassandra and Zookeeper PODs:

gcloud container node-pools create cassandra-pool --cluster=umiot --node-labels=machinetype=other --num-nodes=1 --disk-size=10 --machine-type=n1-standard-2

Create the default credentials file on your local machine:

gcloud auth application-default login

Create common resources that are used by other resources:

kubectl create -f common.yaml

Provision cassandra cluster:

kubectl create -f cassandra.yaml

Monitor provisioning of Cassandra Pods by executing following command:

kubectl get pods -w -l app=cassandra

Please wait until all 2 Pods of Cassandra service become Running:

kubectl create -f cassandra-setup.yaml

Check logs of the cassandra setup node:

kubectl logs -f cassandra-setup

Wait for successful installation message:

Provision ThingsBoard Service:

kubectl get services tb-service




