# Script generated with Bloom
pkgdesc="ROS - <p> ROS Industrial libraries/plugins for filtering trajectories. </p> <p> This package is part of the ROS Industrial program and contains libraries and moveit plugins for filtering robot trajectories. </p>"
url='http://ros.org/wiki/industrial_trajectory_filters'

pkgname='ros-kinetic-industrial-trajectory-filters'
pkgver='0.6.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-moveit-core'
'ros-kinetic-moveit-ros-planning'
'ros-kinetic-orocos-kdl'
'ros-kinetic-pluginlib'
'ros-kinetic-trajectory-msgs'
)

depends=('ros-kinetic-moveit-core'
'ros-kinetic-moveit-ros-planning'
'ros-kinetic-orocos-kdl'
'ros-kinetic-pluginlib'
'ros-kinetic-trajectory-msgs'
)

conflicts=()
replaces=()

_dir=industrial_trajectory_filters
source=()
md5sums=()

prepare() {
    cp -R $startdir/industrial_trajectory_filters $srcdir/industrial_trajectory_filters
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

