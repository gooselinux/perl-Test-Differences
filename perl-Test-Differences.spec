Name:           perl-Test-Differences
Version:        0.4801
Release:        3%{?dist}
Summary:        Test strings and data structures and show differences if not ok

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Test-Differences/
Source0:        http://search.cpan.org/CPAN/authors/id/O/OV/OVID/Test-Differences-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Text::Diff) >= 0.34
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
When the code you're testing returns multiple lines, records or data
structures and they're just plain wrong, an equivalent to the Unix
diff utility may be just what's needed.


%prep
%setup -q -n Test-Differences-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes eg/
%{perl_vendorlib}/Test/
%{_mandir}/man3/*.3pm*


%changelog
* Wed Aug 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4801-3
- fix source url

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4801-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4801-1
- update to 0.4801

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.47-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.47-4
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.47-3
- rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.47-2.2
- add BR: perl(Test::More)

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.47-2.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Sun May 14 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.47-2
- Bumping release (repodata checksum inconsistency for previous release).

* Mon May 01 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.47-1
- First build.
