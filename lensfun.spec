%define major	0
%define libname %mklibname lensfun %{major}
%define devname %mklibname lensfun -d

Summary:	A library to rectifying the defects introduced by your photographic equipment
Name:		lensfun
Version:	0.2.6
Release:	2
License:	GPLv3
Group:		System/Libraries
Url:		http://lensfun.berlios.de/
Source0:	http://download.berlios.de/lensfun/%{name}-%{version}.tar.bz2
# (fc) 0.2.3-1mdv fix build on 64bits
Patch0:		lensfun-0.2.6-cmake_LIB_SUFFIX.patch
Patch1:		lensfun-0.2.3-64bits.patch
Patch2:		lensfun-0.2.6-cmake_pkgconfig.patch

BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	python
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)

%description
A library to rectifying the defects introduced by your photographic equipment.

%package -n	%{libname}
Summary:	A library to rectifying the defects introduced by your photographic equipment
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n	%{libname}
A library to rectifying the defects introduced by your photographic equipment.

%package -n	%{devname}
Summary:	Development tools for programs which will use the %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the header files and .so
libraries for developing %{name}.

%prep
%setup -q
%apply_patches

%build
%cmake \
	-DBUILD_DOC:BOOL=ON \
	-DBUILD_TESTS:BOOL=OFF

%make all

%install
mkdir -p %{buildroot}/%{_datadir}/doc/%{name}
make install/fast DESTDIR=%{buildroot} -C build
cp -r  docs/*.txt %{buildroot}%{_datadir}/doc/%{name}/

%files
%{_datadir}/lensfun
%doc %{_docdir}/*

%files -n %{libname}
%{_libdir}/liblensfun.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}/*.h*
%{_libdir}/*.so
%{_libdir}/pkgconfig/lensfun.pc

