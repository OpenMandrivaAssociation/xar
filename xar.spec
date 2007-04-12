%define major 1
%define libname %mklibname %{name} %{major}

Summary:	The XAR project aims to provide an easily extensible archive format
Name:		xar
Version:	1.4
Release:	%mkrel 1
License:	BSD
Group:		Archiving/Compression
URL:		http://xar.googlecode.com/
Source0:	http://xar.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	libxml2-devel >= 2.6.11
BuildRequires:	libacl-devel
BuildRequires:	openssl-devel
BuildRequires:	bzip2-devel
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-root

%description
The XAR project aims to provide an easily extensible archive format. Important
design decisions include an easily extensible XML table of contents for random
access to archived files, storing the toc at the beginning of the archive to
allow for efficient handling of streamed archives, the ability to handle files
of arbitrarily large sizes, the ability to choose independent encodings for
individual files in the archive, the ability to store checksums for individual
files in both compressed and uncompressed form, and the ability to query the
table of content's rich meta-data.

%package -n	%{libname}
Summary:	Libraries required for xar
Group:		System/Libraries

%description -n	%{libname}
The XAR project aims to provide an easily extensible archive format. Important
design decisions include an easily extensible XML table of contents for random
access to archived files, storing the toc at the beginning of the archive to
allow for efficient handling of streamed archives, the ability to handle files
of arbitrarily large sizes, the ability to choose independent encodings for
individual files in the archive, the ability to store checksums for individual
files in both compressed and uncompressed form, and the ability to query the
table of content's rich meta-data.

%package -n	%{libname}-devel
Summary:	Libraries and header files required for xar
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n	%{libname}-devel
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

%setup -q -n %{name}-%{version}

# nuke rpath
perl -pi -e "s|RPATH=.*|RPATH=\"\"|g" configure*

%build

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

# make it able to strip the library and binary
chmod 755 %{buildroot}%{_libdir}/lib%{name}.so.%{major}
chmod 755 %{buildroot}%{_bindir}/%{name}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL LICENSE TODO test
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0644,root,root) %{_mandir}/man1/*

%files -n %{libname}
%attr(0755,root,root) %{_libdir}/lib%{name}.so.%{major}

%files -n %{libname}-devel
%dir %{_includedir}/%{name}
%attr(0644,root,root) %{_includedir}/%{name}/%{name}.h
%attr(0755,root,root) %{_libdir}/lib*.so


