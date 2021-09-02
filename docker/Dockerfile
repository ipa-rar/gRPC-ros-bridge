FROM ros:foxy
LABEL maintainer "Ragesh Ramachandran <ragesh.ramachandran@ipa.fraunhofer.de>"
SHELL ["/bin/bash","-c"]
# ROS2 related updates
RUN apt update && \
    apt install -y --no-install-recommends python3-pip python3-apt && \
    apt install -y --no-install-recommends ros-foxy-gazebo-ros-pkgs ros-foxy-rviz2&& \
    apt install -y --no-install-recommends xvfb x11vnc x11-apps && \
    pip3 install -U setuptools colcon-common-extensions colcon-ros-bundle && \
    rm -rf /var/lib/apt/lists/*

# Python3 related updates
RUN apt-get update -y \
    && apt-get install -y python3-pip python3-dev \
    && pip3 install --upgrade pip
# Install grpc dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install --upgrade protobuf
# Setup package to build
ENV ROS2_WS=/home/ros2_ws
RUN mkdir -p ${ROS2_WS}/src
WORKDIR ${ROS2_WS}/src
COPY ./ ./

WORKDIR ${ROS2_WS}
# Build packages
RUN rosdep update
RUN rosdep install --from-paths src --ignore-src -y --rosdistro foxy
RUN cd ${ROS2_WS} \
    && . /opt/ros/foxy/setup.sh \
    && colcon build 

#Entrypoint commands
WORKDIR ${ROS2_WS}
COPY ./docker/entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash"]



