Name:           ros-indigo-industrial-robot-simulator
Version:        0.4.2
Release:        0%{?dist}
Summary:        ROS industrial_robot_simulator package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/industrial_robot_simulator
Source0:        %{name}-%{version}.tar.gz

Requires:       python-rospkg
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-industrial-msgs
Requires:       ros-indigo-industrial-robot-client
Requires:       ros-indigo-rospy
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-industrial-msgs
BuildRequires:  ros-indigo-roslaunch >= 1.9.55
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-trajectory-msgs

%description
The industrial robot simulator is a stand in for industrial robot driver
node(s). It adheres to the driver specification for industrial robot
controllers.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Oct 21 2015 Shaun Edwards <sedwards@swri.org> - 0.4.2-0
- Autogenerated by Bloom

* Mon Mar 23 2015 Shaun Edwards <sedwards@swri.org> - 0.4.1-0
- Autogenerated by Bloom

* Sat Mar 21 2015 Shaun Edwards <sedwards@swri.org> - 0.4.0-0
- Autogenerated by Bloom

* Sat Mar 21 2015 Shaun Edwards <sedwards@swri.org> - 0.3.4-0
- Autogenerated by Bloom

