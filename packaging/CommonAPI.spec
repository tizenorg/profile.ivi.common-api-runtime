Name:       CommonAPI
Summary:    GENIVI IPC Common API C++ Runtime
Version:    2.1.6
Release:    0
Group:      Automotive/GENIVI
License:    MPL-2.0
Source0:    %{name}-%{version}.tar.gz
Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
GENIVI IPC Common API C++ Runtime components

%package -n libCommonAPI
Summary:    CommonAPI C++ Runtime libraries

%description -n libCommonAPI
GENIVI IPC CommonAPI C++ Runtime libraries

%package devel
Summary:    CommonAPI C++ Runtime devel package
Requires:   libCommonAPI = %{version}-%{release}

%description devel
Files needed to build against CommonAPI.

%prep
%setup -q

%build
autoreconf -i
%configure

make %{?jobs:-j%jobs}

%install
%make_install

%post -n libCommonAPI -p /sbin/ldconfig

%postun -n libCommonAPI -p /sbin/ldconfig

%files -n libCommonAPI
%defattr(-,root,root,-)
%{_libdir}/*so.*
%license LICENSE

%files devel
%defattr(-,root,root,-)
%{_includedir}/CommonAPI-2.1/CommonAPI/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
