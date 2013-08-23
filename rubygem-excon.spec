%global gem_name excon

Summary: Http(s) EXtended CONnections
Name: rubygem-%{gem_name}
Version: 0.20.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/geemus/excon
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
#Requires: ruby(abi) = 1.9.1
Requires: ruby
Requires: ruby(rubygems)
Requires: ca-certificates
BuildRequires: rubygems-devel
BuildRequires: ca-certificates
# For the tests
BuildRequires: rubygem(activesupport)
BuildRequires: rubygem(delorean)
BuildRequires: rubygem(open4)
BuildRequires: rubygem(shindo)
BuildRequires: rubygem(sinatra)
BuildRequires: rubygem(eventmachine)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
EXtended http(s) CONnections

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force --rdoc %{SOURCE0}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

# fix the benchmark file not to be executable
#chmod a-x %{buildroot}%{gem_instdir}/benchmarks/has_key-vs-hash[key].rb

# kill bundled cacert.pem
#ln -sf %{_sysconfdir}/pki/tls/cert.pem \
	#%{buildroot}%{gem_instdir}/data/cacert.pem

#%check
#pushd .%{gem_instdir}
# we need to remove the dependency on bundler and add the missing requires (workaround for not using the Rakefile)
# do not require bundler
#sed -i -e "s/'bundler'/'open4'\nrequire 'delorean'/" -e '/Bundler.require(:default, :development)/d' tests/test_helper.rb

# require the other needed libs
# https://github.com/geemus/excon/issues/135#issuecomment-7181061
#RUBYOPT="-r./lib/excon -rsecurerandom" shindo
#popd

%files
%dir %{gem_instdir}
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Gemfile.lock
%{gem_spec}
%doc %{gem_instdir}/README.md

%files doc
%{gem_instdir}/benchmarks
%{gem_instdir}/tests
%{gem_instdir}/excon.gemspec
%{gem_instdir}/Rakefile
%doc %{gem_docdir}
%doc %{gem_instdir}/changelog.txt


%changelog
* Fri Aug 23 2013 Dan Prince <dprince@redhat.com> - 0.20.1-1
- Updates to build on Fedora 19.

* Thu May 2 2013 Dan Prince <dprince@redhat.com> - 0.20.1-1
- Changes to follow the latest upstream code.

* Mon Jul 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.14.3-1
- Update to Excon 0.14.3.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.14.1-1
- Update to Excon 0.14.1
- Removed no longer needed patch for downgrading dependencies.
- Remove newly bundled certificates and link to system ones.

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.5-2
- Fixed the changelog.

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.5-1
- Update to version 0.9.5
- Fixed the dependencies for the new version.

* Mon Dec 05 2011 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.12-1
- Update to version 0.7.12.

* Mon Nov 28 2011 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.8-1
- Update to version 0.7.8.
- Replaced defines with more appropriate globals.
- Added Build dependency on rubygem-eventmachine.
- Fixed running tests for the new version.

* Wed Oct 12 2011 bkabrda <bkabrda@redhat.com> - 0.7.6-1
- Update to version 0.7.6
- Introduced doc subpackage
- Introduced check section

* Tue Jul 05 2011 Chris Lalancette <clalance@redhat.com> - 0.6.3-1
- Initial package
