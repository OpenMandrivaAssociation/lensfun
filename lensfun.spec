%define major	0
%define libname %mklibname lensfun %{major}
%define devname %mklibname lensfun -d

Summary:	A library to rectifying the defects introduced by your photographic equipment
Name:		lensfun
Version:	0.2.8
Release:	1
License:	GPLv3
Group:		System/Libraries
Url:		http://lensfun.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0:		lensfun-0.2.8-x32.patch
Patch1:		lensfun-0.2.3-64bits.patch

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
# failed with clang
# need investigation
export CC=gcc
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

