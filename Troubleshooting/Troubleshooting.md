# Troubleshooting

## 1. Resize volume

It is likely your Cloud9 instance will not have a large enough volume to download the docker container. To increase the volume, navigate to the EC2 management panel, under Elastic Block storage select Volume and increase the size of the EBS attached to the Cloud9. Next follow this [tutorial](https://aws.amazon.com/premiumsupport/knowledge-center/ebs-volume-size-increase/) to resize your filesystem.
