%define upstream_name    CPAN-Meta
%define upstream_version 2.132830

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2

Summary:    Validate CPAN distribution metadata structures
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CPAN/CPAN-Meta-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::Dir)
BuildRequires:	perl(JSON)
BuildRequires:	perl-Parse-CPAN-Meta >= 1.440.3
#BuildRequires:	perl(Parse::CPAN::Meta) >= 1.440.3
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Storable)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Version::Requirements)
BuildRequires:	perl(autodie)
# BuildRequires:	perl(version) >= 1:0.820.0
BuildRequires:	perl(CPAN::Meta::YAML)
BuildRequires:	perl(CPAN::Meta::Requirements) >= 2.121

BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Tue Jan 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.113.640-1
+ Revision: 759479
- version update 2.113640

* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.110.930-1
+ Revision: 662018
- update to new version 2.110930

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 2.110.330-2
+ Revision: 655678
- add br
- fix br
- rebuild for updated spec-helper

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - new version

* Tue Aug 31 2010 Jérôme Quelin <jquelin@mandriva.org> 2.102.400-1mdv2011.0
+ Revision: 574781
- update to 2.102400

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 2.102.160-1mdv2011.0
+ Revision: 569928
- update to 2.102160

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 2.101.670-1mdv2011.0
+ Revision: 553059
- adding minimum version in buildrequires
- import perl-CPAN-Meta



