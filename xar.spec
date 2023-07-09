%define subversion 417.1

%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	The XAR project aims to provide an easily extensible archive format
Name:		xar
Version:	496
Release:	1
License:	BSD
Group:		Archiving/Compression
URL:		https://mackyle.github.io/xar/
Source0:	https://opensource.apple.com/tarballs/xar/xar-%{subversion}.tar.gz
Patch0:         xar-1.6.1-ext2.patch
Patch1:         xar-1.8-safe_dirname.patch
Patch2:         xar-1.8-arm-ppc.patch
Patch3:         xar-1.8-openssl-1.1.patch
Patch4:         xar-1.8-Add-OpenSSL-To-Configuration.patch
	
 
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	acl-devel
BuildRequires:	pkgconfig(libssl)
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	pkgconfig(zlib)

%description
The XAR project aims to provide an easily extensible archive format. Important
design decisions include an easily extensible XML table of contents for random
access to archived files, storing the toc at the beginning of the archive to
allow for efficient handling of streamed archives, the ability to handle files
of arbitrarily large sizes, the ability to choose independent encodings for
individual files in the archive, the ability to store checksums for individual
files in both compressed and uncompressed form, and the ability to query the
table of content's rich meta-data.

%package -n %{libname}
Summary:	Libraries required for xar
Group:		System/Libraries

%description -n %{libname}
The XAR project aims to provide an easily extensible archive format. Important
design decisions include an easily extensible XML table of contents for random
access to archived files, storing the toc at the beginning of the archive to
allow for efficient handling of streamed archives, the ability to handle files
of arbitrarily large sizes, the ability to choose independent encodings for
individual files in the archive, the ability to store checksums for individual
files in both compressed and uncompressed form, and the ability to query the
table of content's rich meta-data.

%package -n %{develname}
Summary:	Libraries and header files required for xar
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel

%description -n %{develname}
The XAR project aims to provide an easily extensible archive format. Important
design decisions include an easily extensible XML table of contents for random
access to archived files, storing the toc at the beginning of the archive to
allow for efficient handling of streamed archives, the ability to handle files
of arbitrarily large sizes, the ability to choose independent encodings for
individual files in the archive, the ability to store checksums for individual
files in both compressed and uncompressed form, and the ability to query the
table of content's rich meta-data.

Libraries and header files required for xar.

%prep
%setup -q -n xar-%{subversion}
pushd xar
	
%patch0 -p1
	
%patch1 -p1
	
%patch2 -p1
	
%patch3 -p1
	
%patch4 -p1
sed 's:-Wl,-rpath,::g' -i configure.ac #No rpath
	
sed 's:filetree.h:../lib/filetree.h:g' -i src/xar.c #Fix path
	
sed 's:util.h:../lib/util.h:g' -i src/xar.c #Fix path
	
popd
# nuke rpath
perl -pi -e "s|RPATH=.*|RPATH=\"\"|g" configure*

%build
pushd xar
	
env NOCONFIGURE=1 ./autogen.sh

%configure

%make_build

%install
pushd xar
%make_install

# make it able to strip the library and binary
chmod 755 %{buildroot}%{_libdir}/lib%{name}.so.%{major}
chmod 755 %{buildroot}%{_bindir}/%{name}

%files
%defattr(-,root,root)
%doc README xar/ChangeLog xar/TODO xar/LICENSE
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0644,root,root) %{_mandir}/man1/*

%files -n %{libname}
%attr(0755,root,root) %{_libdir}/lib%{name}.so.%{major}

%files -n %{develname}
%dir %{_includedir}/%{name}
%attr(0644,root,root) %{_includedir}/%{name}/%{name}.h
%attr(0755,root,root) %{_libdir}/lib*.so
