# Script generated with Bloom
pkgdesc="ROS - The industrial robot simulator is a stand in for industrial robot driver node(s). It adheres to the driver specification for industrial robot controllers."
url='http://ros.org/wiki/industrial_robot_simulator'

pkgname='ros-kinetic-industrial-robot-simulator'
pkgver='0.6.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-control-msgs'
'ros-kinetic-industrial-msgs'
'ros-kinetic-industrial-robot-client'
'ros-kinetic-roslaunch>=1.9.55'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-trajectory-msgs'
)

depends=('python2-rospkg'
'ros-kinetic-control-msgs'
'ros-kinetic-industrial-msgs'
'ros-kinetic-industrial-robot-client'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-trajectory-msgs'
)

conflicts=()
replaces=()

_dir=industrial_robot_simulator
source=()
md5sums=()

prepare() {
    cp -R $startdir/industrial_robot_simulator $srcdir/industrial_robot_simulator
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

