%define upstream_name	Apache-Session
%define upstream_version	1.88
%define epoch	2

Name:		perl-%{upstream_name}
Epoch:		2
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1
Summary:	A persistence framework for session data
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source:		http://www.cpan.org/modules/by-module/Apache/%{upstream_name}-%{upstream_version}.zip
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
%setup -q -n %{upstream_name}-%{upstream_version}

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



