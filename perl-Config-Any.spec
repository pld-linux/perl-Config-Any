#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Config
%define	pnam	Any
Summary:	Config::Any - Load configuration from different file formats, transparently
Summary(pl.UTF-8):	Config::Any - przezroczyste wczytywanie konfiguracji z różnych formatów plików
Name:		perl-Config-Any
Version:	0.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Config/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ce026e51bee3e5d109e97225a2a370a6
URL:		http://search.cpan.org/dist/Config-Any/
BuildRequires:	perl-Module-Build
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

%description -l pl.UTF-8
Config::Any ułatwia aplikacjom i bibliotekom perlowym wczytywanie
danych konfiguracyjnych z wielu różnych formatów plików. Obsługuje
XML, YAML, JSON, konfigurację w stylu Apache'a, pliki Windows INI, a
nawet kod perlowy.

Uzasadnienie istnienia tego modułu jest takie, że programy w Perlu są
wdrażane na wielu różnych platformach i integrowane z wieloma różnymi
systemami. Administratorzy i użytkownicy końcowi mogą preferować inne
formaty konfiguracyjne niż programiści. Elastyczność tkwiąca w
możliwości wczytywania wielu formatów pozwala różnym użytkownikom
dokonywać różnych wyborów bez generowania dodatkowej pracy dla
programistów. Wystarczy, że programista nauczy się jednego interfejsu
i może wykorzystać potęgę różnych formatów konfiguracji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	installdirs=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Config/*.pm
%{perl_vendorlib}/Config/Any
%{_mandir}/man3/*
