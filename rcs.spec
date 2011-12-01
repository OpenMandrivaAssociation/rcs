%define name	rcs
%define version	5.7

Name:		%{name}
Summary:	Revision Control System (RCS) file version management tools
Version:	%{version}
Release:	%mkrel 16
License:	GPL
Group:		Development/Other
Source0:	ftp://ftp.gnu.org/pub/gnu/rcs-5.7.tar.bz2
Patch0:		rcs-5.7-stupidrcs.patch
Patch1:		rcs-5.7-security.patch
Url:		http://www.cs.purdue.edu/homes/trinkle/RCS/
BuildRequires:	autoconf2.1
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%patch0 -p1 -b .stupidrcs
%patch1 -p1 -b .security

%build
autoconf
%configure --with-diffutils

touch src/conf.h
%make

%install
rm -rf %{buildroot}

%makeinstall man1dir=%{buildroot}%{_mandir}/man1 man5dir=%{buildroot}%{_mandir}/man5

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc NEWS REFS
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*

