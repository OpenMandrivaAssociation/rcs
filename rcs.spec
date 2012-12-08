%define name	rcs
%define version	5.7

Name:		%{name}
Summary:	Revision Control System (RCS) file version management tools
Version:	%{version}
Release:	%mkrel 18
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
rm -rf $RPM_BUILD_ROOT

%makeinstall man1dir=$RPM_BUILD_ROOT%{_mandir}/man1 man5dir=$RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc NEWS REFS
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*



%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 5.7-16mdv2011.0
+ Revision: 669410
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 5.7-15mdv2011.0
+ Revision: 607319
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 5.7-14mdv2010.1
+ Revision: 520207
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 5.7-13mdv2010.0
+ Revision: 426877
- rebuild

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 5.7-12mdv2009.1
+ Revision: 317560
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 5.7-11mdv2009.0
+ Revision: 225312
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 5.7-10mdv2008.1
+ Revision: 179417
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot


* Thu Aug 10 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/10/06 00:57:14 (55267)
- %%mkrel
- rebuild

* Thu Aug 10 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/10/06 00:55:27 (55266)
Import rcs

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 5.7-8mdk
- Rebuild

* Mon Jun 14 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 5.7-7mdk
- fix buildrequires
- added url
- cosmetics

