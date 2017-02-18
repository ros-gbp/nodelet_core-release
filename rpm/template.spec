Name:           ros-kinetic-nodelet
Version:        1.9.9
Release:        0%{?dist}
Summary:        ROS nodelet package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/nodelet
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       libuuid-devel
Requires:       ros-kinetic-bondcpp
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-pluginlib >= 1.10.0
Requires:       ros-kinetic-rosconsole
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-std-msgs
BuildRequires:  boost-devel
BuildRequires:  libuuid-devel
BuildRequires:  ros-kinetic-bondcpp
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cmake-modules >= 0.3.2
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-pluginlib >= 1.10.0
BuildRequires:  ros-kinetic-rosconsole
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-std-msgs

%description
The nodelet package is designed to provide a way to run multiple algorithms in
the same process with zero copy transport between algorithms. This package
provides both the nodelet base class needed for implementing a nodelet, as well
as the NodeletLoader class used for instantiating nodelets.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Feb 17 2017 Mikael Arguedas <mikael@osrfoundation.org> - 1.9.9-0
- Autogenerated by Bloom

* Tue Nov 15 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.9.8-0
- Autogenerated by Bloom

* Mon Oct 24 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.9.7-0
- Autogenerated by Bloom

* Tue Sep 20 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.9.6-0
- Autogenerated by Bloom

* Wed Jun 22 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.9.5-0
- Autogenerated by Bloom

* Tue Mar 15 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.9.4-0
- Autogenerated by Bloom

