#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Config
%define	pnam	Any
Summary:	Config::Any - Load configuration from different file formats, transparently
#Summary(pl.UTF-8):	
Name:		perl-Config-Any
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/R/RA/RATAXIS/Config-Any-0.07.tar.gz
# Source0-md5:	f4233adfa8abb621be7a68f172be000a
URL:		http://search.cpan.org/dist/Config-Any/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Config-General
BuildRequires:	perl-Config-Tiny
BuildRequires:	perl-JSON
BuildRequires:	perl-Module-Pluggable >= 3.01
BuildRequires:	perl-XML-Simple
BuildRequires:	perl-YAML
BuildRequires:	perl-version
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config::Any provides a facility for Perl applications and libraries
to load configuration data from multiple different file formats. It
supports XML, YAML, JSON, Apache-style configuration, Windows INI
files, and even Perl code.

The rationale for this module is as follows: Perl programs are deployed
on many different platforms and integrated with many different
systems. Systems administrators and end users may prefer different
configuration formats than the developers. The flexibility inherent
in a multiple format configuration loader allows different users
to make different choices, without generating extra work for the
developers. As a developer you only need to learn a single interface
to be able to use the power of different configuration formats.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Config/*.pm
%{perl_vendorlib}/Config/Any
%{_mandir}/man3/*
