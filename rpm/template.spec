Name:           ros-lunar-nodelet-topic-tools
Version:        1.9.14
Release:        0%{?dist}
Summary:        ROS nodelet_topic_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/nodelet_topic_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-lunar-dynamic-reconfigure
Requires:       ros-lunar-message-filters
Requires:       ros-lunar-nodelet
Requires:       ros-lunar-pluginlib
Requires:       ros-lunar-roscpp
BuildRequires:  boost-devel
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-dynamic-reconfigure

%description
This package contains common nodelet tools such as a mux, demux and throttle.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Wed Nov 15 2017 Mikael Arguedas <mikael@osrfoundation.org> - 1.9.14-0
- Autogenerated by Bloom

* Fri Oct 27 2017 Mikael Arguedas <mikael@osrfoundation.org> - 1.9.13-0
- Autogenerated by Bloom

* Fri Aug 04 2017 Mikael Arguedas <mikael@osrfoundation.org> - 1.9.12-0
- Autogenerated by Bloom

* Thu Jul 27 2017 Mikael Arguedas <mikael@osrfoundation.org> - 1.9.11-0
- Autogenerated by Bloom

* Mon Mar 27 2017 Mikael Arguedas <mikael@osrfoundation.org> - 1.9.10-0
- Autogenerated by Bloom

* Wed Feb 22 2017 Mikael Arguedas <mikael@osrfoundation.org> - 1.9.9-0
- Autogenerated by Bloom

