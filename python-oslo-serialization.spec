%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name oslo.serialization
%global pkg_name oslo-serialization

%if 0%{?fedora} >= 24
%global with_python3 1
%endif

%global common_desc \
An OpenStack library for representing objects in transmittable and \
storable formats.

Name:           python-%{pkg_name}
Version:        2.24.0
Release:        1%{?dist}
Summary:        OpenStack oslo.serialization library

License:        ASL 2.0
URL:            https://launchpad.net/oslo
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch

%description
%{common_desc}

%package -n python2-%{pkg_name}
Summary:        OpenStack oslo.serialization library
%{?python_provide:%python_provide python2-%{pkg_name}}

BuildRequires:  git
BuildRequires:  python2-devel
BuildRequires:  python2-pbr
# test requirements
BuildRequires:  python2-hacking
BuildRequires:  python2-mock
BuildRequires:  python2-oslotest
BuildRequires:  python2-oslo-i18n
%if 0%{?fedora} > 0
BuildRequires:  python2-netaddr
BuildRequires:  python2-simplejson
BuildRequires:  python2-ipaddress
%else
BuildRequires:  python-netaddr
BuildRequires:  python-simplejson
BuildRequires:  python-ipaddress
%endif

Requires:       python2-babel
Requires:       python2-iso8601
Requires:       python2-oslo-utils >= 3.33.0
Requires:       python2-six
%if 0%{?fedora} > 0
Requires:       python2-msgpack
Requires:       python2-ipaddress
%else
Requires:       python-msgpack
Requires:       python-ipaddress
%endif

%description -n python2-%{pkg_name}
%{common_desc}


%package -n python2-%{pkg_name}-tests
Summary:   Tests for OpenStack Oslo serialization library
%{?python_provide:%python_provide python2-%{pkg_name}}

Requires:  python2-%{pkg_name} = %{version}-%{release}
Requires:  python2-hacking
Requires:  python2-mock
Requires:  python2-oslotest
Requires:  python2-oslo-i18n
%if 0%{?fedora} > 0
Requires:  python2-netaddr
Requires:  python2-simplejson
%else
Requires:  python-netaddr
Requires:  python-simplejson
%endif

%description -n python2-%{pkg_name}-tests
Tests for OpenStack Oslo serialization library

%if 0%{?with_python3}
%package -n python3-%{pkg_name}-tests
Summary:    Tests for OpenStack Oslo serialization library

Requires:  python3-%{pkg_name} = %{version}-%{release}
Requires:  python3-hacking
Requires:  python3-mock
Requires:  python3-netaddr
Requires:  python3-oslotest
Requires:  python3-simplejson
Requires:  python3-oslo-i18n

%description -n python3-%{pkg_name}-tests
Tests for OpenStack Oslo serialization library
%endif

%if 0%{?with_python3}
%package -n python3-%{pkg_name}
Summary:        OpenStack oslo.serialization library
%{?python_provide:%python_provide python3-%{pkg_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
# test requirements
BuildRequires:  python3-hacking
BuildRequires:  python3-mock
BuildRequires:  python3-netaddr
BuildRequires:  python3-oslotest
BuildRequires:  python3-simplejson
BuildRequires:  python3-oslo-i18n

Requires:       python3-babel
Requires:       python3-iso8601
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-six
Requires:       python3-msgpack

%description -n python3-%{pkg_name}
%{common_desc}
%endif

%package -n python-%{pkg_name}-doc
Summary:    Documentation for the Oslo serialization library

BuildRequires:  python2-sphinx
BuildRequires:  python2-openstackdocstheme
BuildRequires:  python2-oslo-utils
%if 0%{?fedora} > 0
BuildRequires:  python2-msgpack
%else
BuildRequires:  python-msgpack
%endif

Requires:  python2-%{pkg_name} = %{version}-%{release}

%description -n python-%{pkg_name}-doc
Documentation for the Oslo serialization library.

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git
# Let RPM handle the dependencies
rm -f requirements.txt

%build
%py2_build

# doc
python setup.py build_sphinx -b html
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install

%if 0%{?with_python3}
%py3_install
%endif

%check
%{__python2} setup.py test
%if 0%{?with_python3}
rm -rf .testrepository
%{__python3} setup.py test
%endif

%files -n python2-%{pkg_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/oslo_serialization
%{python2_sitelib}/*.egg-info
%exclude %{python2_sitelib}/oslo_serialization/tests


%if 0%{?with_python3}
%files -n python3-%{pkg_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/oslo_serialization
%{python3_sitelib}/*.egg-info
%exclude %{python3_sitelib}/oslo_serialization/tests
%endif

%files -n python-%{pkg_name}-doc
%doc doc/build/html
%license LICENSE

%files -n python2-%{pkg_name}-tests
%{python2_sitelib}/oslo_serialization/tests

%if 0%{?with_python3}
%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_serialization/tests
%endif

%changelog
* Sat Feb 10 2018 RDO <dev@lists.rdoproject.org> 2.24.0-1
- Update to 2.24.0

