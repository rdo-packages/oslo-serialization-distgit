# Created by pyp2rpm-1.0.1
%global pypi_name oslo.serialization
%global pname oslo-serialization

%if 0%{?fedora}
%global with_python3 1
%endif

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-oslo-serialization
Version:        1.9.0
Release:        1%{?dist}
Summary:        OpenStack oslo.serialization library

License:        ASL 2.0
URL:            https://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
An OpenStack library for representing objects in transmittable and
storable formats.

%package -n     python2-%{pname}
Summary:        OpenStack oslo.serialization library
%{?python_provide:%python_provide python2-%{pname}}

BuildRequires:  python2-devel
BuildRequires:  python-pbr

Requires:       python-babel
Requires:       python-iso8601
Requires:       python-oslo-utils
Requires:       python-six
Requires:       python-msgpack
Requires:       pytz

%description -n python2-%{pname}
An OpenStack library for representing objects in transmittable and
storable formats.

%package -n python2-%{pname}-doc
Summary:    Documentation for the Oslo serialization library
Group:      Documentation

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-oslo-utils
BuildRequires:  python-msgpack

%description -n python2-%{pname}-doc
Documentation for the Oslo serialization library.

%if 0%{?with_python3}
%package -n     python3-%{pname}
Summary:        OpenStack oslo.serialization library
%{?python_provide:%python_provide python3-%{pname}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr

Requires:       python3-babel
Requires:       python3-iso8601
Requires:       python3-oslo-utils
Requires:       python3-six
Requires:       python3-msgpack
Requires:       python3-pytz

%description -n python3-%{pname}
An OpenStack library for representing objects in transmittable and
storable formats.
%endif

%prep
%setup -q -n %{pypi_name}-%{upstream_version}

# Let RPM handle the dependencies
rm -rf {test-,}requirements.txt

%build
%{__python2} setup.py build
%if 0%{?with_python3}
%{__python3} setup.py build
%endif

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
%if 0%{?with_python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
%endif

%check
%{__python2} setup.py test
%if 0%{?with_python3}
%{__python3} setup.py test
%endif

%files -n python2-%{pname}
%doc README.rst
%license LICENSE
%{python2_sitelib}/oslo_serialization
%{python2_sitelib}/*.egg-info

%if 0%{?with_python3}
%files -n python3-%{pname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/oslo_serialization
%{python3_sitelib}/*.egg-info
%endif

%files -n python2-%{pname}-doc
%doc html
%license LICENSE


%changelog
* Tue Sep 15 2015 Lukas Bezdicka <lbezdick@redhat.com> 1.9.0-1
- Update to upstream 1.9.0
- Add python3 subpackage
- Enable tests

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
