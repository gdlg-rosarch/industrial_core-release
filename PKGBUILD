# Script generated with Bloom
pkgdesc="ROS - industrial robot client contains generic clients for connecting to industrial robot controllers with servers that adhere to the simple message protocol."
url='http://ros.org/wiki/industrial_robot_client'

pkgname='ros-kinetic-industrial-robot-client'
pkgver='0.6.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-catkin'
'ros-kinetic-control-msgs'
'ros-kinetic-industrial-msgs'
'ros-kinetic-industrial-utils'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-simple-message'
'ros-kinetic-std-msgs'
'ros-kinetic-trajectory-msgs'
'ros-kinetic-urdf'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-control-msgs'
'ros-kinetic-industrial-msgs'
'ros-kinetic-industrial-utils'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-simple-message'
'ros-kinetic-std-msgs'
'ros-kinetic-trajectory-msgs'
'ros-kinetic-urdf'
)

conflicts=()
replaces=()

_dir=industrial_robot_client
source=()
md5sums=()

prepare() {
    cp -R $startdir/industrial_robot_client $srcdir/industrial_robot_client
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

