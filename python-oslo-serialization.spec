# Created by pyp2rpm-1.0.1
%global pypi_name oslo.serialization

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-oslo-serialization
Version:        1.8.0
Release:        1%{?dist}
Summary:        OpenStack oslo.serialization library

License:        ASL 2.0
URL:            https://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
Requires:       python-babel
Requires:       python-iso8601
Requires:       python-oslo-utils
Requires:       python-six
Requires:       python-msgpack
Requires:       pytz

%description
An OpenStack library for representing objects in transmittable and
storable formats.

%package doc
Summary:    Documentation for the Oslo serialization library
Group:      Documentation

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-oslo-utils
BuildRequires:  python-msgpack

%description doc
Documentation for the Oslo serialization library.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Let RPM handle the dependencies
rm -f requirements.txt


%build
%{__python2} setup.py build

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%{__python2} setup.py install --skip-build --root %{buildroot}

#delete tests
rm -fr %{buildroot}%{python2_sitelib}/%{pypi_name}/tests/

%files
%doc README.rst LICENSE
%{python2_sitelib}/oslo_serialization
%{python2_sitelib}/*.egg-info
%{python2_sitelib}/*.egg-info

%files doc
%doc html LICENSE


%changelog
* Tue Aug 18 2015 Alan Pevec <alan.pevec@redhat.com> 1.8.0-1
- Update to upstream 1.8.0

* Mon Jun 29 2015 Alan Pevec <alan.pevec@redhat.com> 1.6.0-1
- Update to upstream 1.6.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 01 2015 Alan Pevec <alan.pevec@redhat.com> 1.4.0-1
- Update to upstream 1.4.0

* Tue Feb 24 2015 Alan Pevec <alan.pevec@redhat.com> 1.3.0-1
- Update to upstream 1.3.0

* Fri Dec 19 2014 Alan Pevec <apevec@redhat.com> - 1.1.0-1
- update to 1.1.0

* Wed Sep 17 2014 Nejc Saje <nsaje@redhat.com> - 0.3.0-1
- Initial package (#1142753)
