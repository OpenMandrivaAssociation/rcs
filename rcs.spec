Summary:	Revision Control System (RCS) file version management tools
Name:		rcs
Version:	5.9.2
Release:	1
License:	GPLv2
Group:		Development/Other
Url:		http://www.cs.purdue.edu/homes/trinkle/RCS/
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.xz
Patch0:		rcs-5.7-stupidrcs.patch
#Patch1:		rcs-5.7-security.patch
BuildRequires:	groff

%description
The Revision Control System (RCS) is a system for managing multiple
versions of files.  RCS automates the storage, retrieval, logging,
identification and merging of file revisions.  RCS is useful for text
files that are revised frequently (for example, programs,
documentation, graphics, papers and form letters).

The rcs package should be installed if you need a system for managing
different versions of files.

%prep
%setup -q
%apply_patches
autoreconf -fi

%build
%configure2_5x --with-diffutils

touch src/conf.h
%make

%install
%makeinstall man1dir=%{buildroot}%{_mandir}/man1 man5dir=%{buildroot}%{_mandir}/man5

%files
%doc NEWS
%{_bindir}/*
%{_infodir}/%{name}.info*
%{_mandir}/man1/*
%{_mandir}/man5/*

