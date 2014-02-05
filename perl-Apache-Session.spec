%define upstream_name	 Apache-Session
%define upstream_version 1.91
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
Epoch:		2

Summary:	A persistence framework for session data
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Apache/Apache-Session-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DB_File)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)

BuildArch:	noarch

%description
Apache::Session is a persistence framework which is particularly useful
for tracking session data between httpd requests.  Apache::Session is
designed to work with Apache and mod_perl, but it should work under CGI
and other web servers, and it also works outside of a web server alto-
gether.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc INSTALL README META.yml
%{perl_vendorlib}/Apache
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 2:1.890.0-2mdv2011.0
+ Revision: 680458
- mass rebuild

* Sat Nov 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.890.0-1mdv2011.0
+ Revision: 597210
- update to 1.89

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2:1.880.0-2mdv2011.0
+ Revision: 402535
- forgot to bump mkrel
- rebuild + fix license field

* Sun Jun 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2:1.880.0-1mdv2010.0
+ Revision: 387863
- new version

* Tue Aug 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2:1.87-1mdv2009.0
+ Revision: 271044
- update to new version 1.87

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2:1.86-3mdv2009.0
+ Revision: 255283
- rebuild

* Mon Feb 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2:1.86-1mdv2008.1
+ Revision: 161928
- update to new version 1.86

* Fri Dec 28 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2:1.85-1mdv2008.1
+ Revision: 138796
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2:1.84-1mdv2008.1
+ Revision: 97361
- update to new version 1.84

* Thu Jul 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2:1.83-1mdv2008.0
+ Revision: 53362
- update to new version 1.83

* Sun Apr 29 2007 Olivier Thauvin <nanardon@mandriva.org> 2:1.82_04-1mdv2008.0
+ Revision: 19313
- 1.82_04

* Sun Apr 29 2007 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 2:1.82-1mdv2008.0
+ Revision: 19180
-New version


* Fri Oct 27 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1.81-1mdv2007.0
+ Revision: 73203
- import perl-Apache-Session-1.81-1mdv2007.0

* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2:1.81-1mdv2007.0
- New version 1.81
- spec cleanup
- fix directory ownership

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.80-3mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- URL && Source URL

* Mon Nov 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.80-2mdk
- Fix BuildRequires
- Fix Source
- %%{1}mdv2007.1

* Wed Oct 12 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2:1.80-1mdk
- New version 1.80
- Some spec fixes

* Thu May 20 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.6-1mdk
- new version
- set epoch = 2 (if not, 1.54 > 1.6)



