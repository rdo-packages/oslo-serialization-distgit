%global pypi_name oslo.serialization
%global pkg_name oslo-serialization

%if 0%{?fedora} >= 24
%global with_python3 1
%endif

Name:           python-%{pkg_name}
Version:        XXX
Release:        XXX
Summary:        OpenStack oslo.serialization library

License:        ASL 2.0
URL:            https://launchpad.net/oslo
Source0:        https://pypi.io/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
An OpenStack library for representing objects in transmittable and
storable formats.

%package -n python2-%{pkg_name}
Summary:        OpenStack oslo.serialization library
%{?python_provide:%python_provide python2-%{pkg_name}}

BuildRequires:  python2-devel
BuildRequires:  python-pbr
# test requirements
BuildRequires:  python-hacking
BuildRequires:  python-mock
BuildRequires:  python-netaddr
BuildRequires:  python-oslotest
BuildRequires:  python-simplejson
BuildRequires:  python-oslo-i18n
BuildRequires:  python-coverage
BuildRequires:  python-ipaddress

Requires:       python-babel
Requires:       python-iso8601
Requires:       python-oslo-utils
Requires:       python-six
Requires:       python-msgpack
Requires:       python-ipaddress

%description -n python2-%{pkg_name}
An OpenStack library for representing objects in transmittable and
storable formats.


%package -n python-%{pkg_name}-tests
Summary:   Tests for OpenStack Oslo serialization library

Requires:  python-%{pkg_name} = %{version}-%{release}
Requires:  python-hacking
Requires:  python-mock
Requires:  python-netaddr
Requires:  python-oslotest
Requires:  python-simplejson
Requires:  python-oslo-i18n
Requires:  python-coverage

%description -n python-%{pkg_name}-tests
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
Requires:  python3-coverage

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
BuildRequires:  python3-coverage

Requires:       python3-babel
Requires:       python3-iso8601
Requires:       python3-oslo-utils
Requires:       python3-six
Requires:       python3-msgpack

%description -n python3-%{pkg_name}
An OpenStack library for representing objects in transmittable and
storable formats.
%endif

%package -n python-%{pkg_name}-doc
Summary:    Documentation for the Oslo serialization library

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-oslo-utils
BuildRequires:  python-msgpack

Requires:  python-%{pkg_name} = %{version}-%{release}

%description -n python-%{pkg_name}-doc
Documentation for the Oslo serialization library.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Let RPM handle the dependencies
rm -f requirements.txt

%build
%py2_build

# doc
export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees   source build/html
popd
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

%files -n python-%{pkg_name}-tests
%{python2_sitelib}/oslo_serialization/tests

%if 0%{?with_python3}
%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_serialization/tests
%endif

%changelog
