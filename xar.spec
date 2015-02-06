%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	The XAR project aims to provide an easily extensible archive format
Name:		xar
Version:	1.5.2
Release:	8
License:	BSD
Group:		Archiving/Compression
URL:		http://xar.googlecode.com/
Source0:	http://xar.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	libxml2-devel >= 2.6.11
BuildRequires:	acl-devel
BuildRequires:	openssl-devel
BuildRequires:	bzip2-devel
BuildRequires:	zlib-devel

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

%package -n	%{develname}
Summary:	Libraries and header files required for xar
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel

%description -n	%{develname}
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
%makeinstall_std

# make it able to strip the library and binary
chmod 755 %{buildroot}%{_libdir}/lib%{name}.so.%{major}
chmod 755 %{buildroot}%{_bindir}/%{name}

%files
%defattr(-,root,root)
%doc INSTALL LICENSE TODO test
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0644,root,root) %{_mandir}/man1/*

%files -n %{libname}
%attr(0755,root,root) %{_libdir}/lib%{name}.so.%{major}

%files -n %{develname}
%dir %{_includedir}/%{name}
%attr(0644,root,root) %{_includedir}/%{name}/%{name}.h
%attr(0755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.a


%changelog
* Mon Apr 19 2010 Funda Wang <fwang@mandriva.org> 1.5.2-6mdv2010.1
+ Revision: 536657
- rebuild

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.5.2-5mdv2010.0
+ Revision: 435030
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 1.5.2-4mdv2009.0
+ Revision: 262228
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.5.2-3mdv2009.0
+ Revision: 256564
- rebuild
- fix no-buildroot-tag

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Dec 30 2007 Funda Wang <fwang@mandriva.org> 1.5.2-1mdv2008.1
+ Revision: 139462
- add missing files
- New version 1.5.2

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 13 2007 Funda Wang <fwang@mandriva.org> 1.5.1-1mdv2008.0
+ Revision: 62745
- New version 1.5.1

* Tue May 29 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 1.5-1mdv2008.0
+ Revision: 32561
- upgrade to version 1.5


* Mon Feb 26 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4-1mdv2007.0
+ Revision: 126028
- Import xar

* Mon Feb 26 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4-1mdv2007.1
- initial Mandriva package (packaged at 10k feet)

