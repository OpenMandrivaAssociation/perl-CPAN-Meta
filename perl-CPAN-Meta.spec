%define upstream_name    CPAN-Meta
%define upstream_version 2.110930

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Validate CPAN distribution metadata structures
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CPAN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(IO::Dir)
BuildRequires: perl(JSON)
BuildRequires: perl(Parse::CPAN::Meta) >= 1.420.0
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Storable)
BuildRequires: perl(Test::More)
BuildRequires: perl(Version::Requirements)
BuildRequires: perl(autodie)
BuildRequires: perl(version) >= 1:0.820.0
BuildRequires: perl-JSON-PP
BuildRequires: perl(CPAN::Meta::YAML)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Software distributions released to the CPAN include a _META.json_ or, for
older distributions, _META.yml_, which describes the distribution, its
contents, and the requirements for building and installing the
distribution. The data structure stored in the _META.json_ file is
described in the CPAN::Meta::Spec manpage.

CPAN::Meta provides a simple class to represent this distribution metadata
(or _distmeta_), along with some helpful methods for interrogating that
data.

The documentation below is only for the methods of the CPAN::Meta object.
For information on the meaning of individual fields, consult the spec.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README META.json
%{_mandir}/man3/*
%perl_vendorlib/*


