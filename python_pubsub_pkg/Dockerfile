FROM ros:humble

ENV DEBIAN_FRONTEND noninteractive

# Suppress output only when needed; remove for debugging if necessary
RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get install -y build-essential afl vim nano git clang lcov cmake software-properties-common

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3-pip

# Install Python packages
RUN pip3 install numpy pytest


RUN /bin/bash -c "source /opt/ros/humble/setup.bash"
ENV ROS_WS /opt/ros_ws
RUN mkdir -p $ROS_WS/src
WORKDIR $ROS_WS
COPY . src/python_pubsub_pkg
RUN chmod +x src/python_pubsub_pkg/afl-config.bash
RUN chmod +x src/python_pubsub_pkg/run.sh
RUN apt-get update && rosdep update && \
    rosdep install --from-paths src --ignore-src -r -y && \
    rm -rf /var/lib/apt/lists/*
RUN /bin/bash -c "source /opt/ros/humble/setup.bash && \
                  colcon build --packages-select python_pubsub_pkg"