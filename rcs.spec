Name:		rcs
Summary:	Revision Control System (RCS) file version management tools
Version:	5.10.0
Release:	2
License:	GPL
Group:		Development/Other
Source0:	ftp://ftp.gnu.org:21/pub/gnu/rcs/%{name}-%{version}.tar.xz
Patch0:		rcs-5.8-build-tweaks.patch
Patch1:		rcs-5.10.0-formatstring.patch
Url:		https://www.cs.purdue.edu/homes/trinkle/RCS/
BuildRequires:	autoconf
BuildRequires:	ed
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
%autopatch -p1

%build
#export CC=gcc
autoreconf -fi
%configure --with-diffutils
%make_build

%install
%make_install

install -m 755 src/rcsfreeze %{buildroot}%{_bindir}

rm -f %{buildroot}/%{_infodir}/dir

%clean

%files
%doc NEWS
%{_bindir}/*
%{_mandir}/man?/*
%{_infodir}/*


