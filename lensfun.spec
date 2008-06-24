%define _disable_ld_as_needed 1

%define lib_major 0
%define lib_name %mklibname lensfun %{lib_major}
%define lib_dev %mklibname lensfun -d

Name: lensfun
Version: 0.2.2b
Summary: A library to rectifying the defects introduced by your photographic equipment
Release: %mkrel 1
License: GPLv3
Group: System/Libraries
URL: http://lensfun.berlios.de/
Source0: %{name}-%{version}.tar.bz2
BuildRequires: python
BuildRequires: glib2-devel
BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
A library to rectifying the defects introduced by your photographic equipment.

%files
%defattr(-,root,root,-)
%_datadir/lensfun
%_docdir/*

#------------------------------------------------------------------

%package -n	%{lib_name}
Summary: A library to rectifying the defects introduced by your photographic equipment
Group: System/Libraries
Requires: %{name}

%description -n	%{lib_name}
A library to rectifying the defects introduced by your photographic equipment.

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files -n %{lib_name}
%defattr(-,root,root,-)
%{_libdir}/*.so.*

#------------------------------------------------------------------

%package -n	%{lib_dev}
Summary: Development tools for programs which will use the %{name}
Group: Development/C
Requires: %{lib_name} = %{version}
Provides: %{name}-devel = %{version}-%{release}

%description -n	%{lib_dev}
This package contains the header files and .so libraries for developing %{name}.

%files -n %{lib_dev}
%defattr(-,root,root,755)
%{_includedir}/*.h*
%{_libdir}/*.so
%{_libdir}/pkgconfig/lensfun.pc

#------------------------------------------------------------------

%prep

%setup -q 

%build
# We can't use macro configure
%setup_compile_flags \
	./configure \
	--prefix=%buildroot%_prefix \
	--libdir=%buildroot%_libdir \
	--sysconfdir=%buildroot%_sysconfdir

%make all

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

