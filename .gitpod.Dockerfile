FROM gitpod/workspace-full

USER root



RUN apt-get -y update && apt-get install -y pkg-config zip g++ zlib1g-dev unzip python

USER gitpod

RUN wget https://github.com/bazelbuild/bazel/releases/download/3.7.1/bazel-0.24.1-installer-linux-x86_64.sh
RUN chmod +x bazel-0.24.1-installer-linux-x86_64.sh
RUN ./bazel-0.24.1-installer-linux-x86_64.sh --user
