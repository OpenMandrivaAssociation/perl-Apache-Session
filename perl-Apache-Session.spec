%define module	Apache-Session
%define name	perl-%{module}
%define epoch	2
%define version	1.81
%define release	%mkrel 1

Name:		%{name}
Epoch:		%{epoch}
Version:	%{version}
Release:	%{release}
Summary:	A persistence framework for session data
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		http://www.cpan.org/modules/by-module/Apache/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
Requires:	perl(Digest::MD5)
BuildRequires:	perl(DB_File)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Apache::Session is a persistence framework which is particularly useful
for tracking session data between httpd requests.  Apache::Session is
designed to work with Apache and mod_perl, but it should work under CGI
and other web servers, and it also works outside of a web server alto-
gether.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc INSTALL README
%{perl_vendorlib}/Apache
%{_mandir}/*/*



