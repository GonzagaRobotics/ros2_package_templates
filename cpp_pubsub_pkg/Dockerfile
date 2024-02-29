FROM ros:humble

ENV DEBIAN_FRONTEND noninteractive


RUN apt-get update > /dev/null \
	&& apt-get install -y --no-install-recommends apt-utils > /dev/null \
	&& apt-get install -y build-essential > /dev/null \
	&& apt-get install -y afl > /dev/null \
	&& apt-get install -y vim > /dev/null \
	&& apt-get install -y nano > /dev/null \
	&& apt-get install -y git > /dev/null \
	&& apt-get install -y clang > /dev/null \
	&& apt-get install -y lcov > /dev/null \
	&& apt-get install -y cmake > /dev/null \
	&& apt-get install -y software-properties-common > /dev/null \

RUN /bin/bash -c "source /opt/ros/humble/setup.bash"
ENV ROS_WS /opt/ros_ws
RUN mkdir -p $ROS_WS/src
WORKDIR $ROS_WS
COPY . src/cpp_pubsub_pkg
RUN chmod +x src/cpp_pubsub_pkg/afl-config.bash
RUN chmod +x src/cpp_pubsub_pkg/run.sh
RUN apt-get update && rosdep update && \
    rosdep install --from-paths src --ignore-src -r -y && \
    rm -rf /var/lib/apt/lists/*

RUN /bin/bash -c "source /opt/ros/humble/setup.bash && \
                  colcon build --packages-select cpp_pubsub_pkg"
