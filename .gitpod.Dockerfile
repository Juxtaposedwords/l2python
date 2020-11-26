FROM gitpod/workspace-full

USER gitpod



# Add Bazel to the known packages
RUN sudo apt install curl gnupg && \
 curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > bazel.gpg && \
 sudo mv bazel.gpg /etc/apt/trusted.gpg.d/  && \
 sudo apt update && sudo apt install bazel && sudo apt full-upgrade

