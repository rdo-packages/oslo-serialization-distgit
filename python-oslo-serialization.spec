# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name oslo.serialization
%global pkg_name oslo-serialization
%global with_doc 1

%global common_desc \
An OpenStack library for representing objects in transmittable and \
storable formats.

Name:           python-%{pkg_name}
Version:        XXX
Release:        XXX
Summary:        OpenStack oslo.serialization library

License:        ASL 2.0
URL:            https://launchpad.net/oslo
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch

%description
%{common_desc}

%package -n python%{pyver}-%{pkg_name}
Summary:        OpenStack oslo.serialization library
%{?python_provide:%python_provide python%{pyver}-%{pkg_name}}

BuildRequires:  git
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
# test requirements
BuildRequires:  python%{pyver}-hacking
BuildRequires:  python%{pyver}-mock
BuildRequires:  python%{pyver}-oslotest
BuildRequires:  python%{pyver}-oslo-i18n
BuildRequires:  python%{pyver}-stestr
BuildRequires:  python%{pyver}-oslo-utils
BuildRequires:  python%{pyver}-msgpack >= 0.5.2
BuildRequires:  python%{pyver}-netaddr
BuildRequires:  python%{pyver}-simplejson
# Handle python2 exception
%if %{pyver} == 2
BuildRequires:  python-ipaddress
%endif

Requires:       python%{pyver}-babel
Requires:       python%{pyver}-oslo-utils >= 3.33.0
Requires:       python%{pyver}-msgpack >= 0.5.2
Requires:       python%{pyver}-pytz
Requires:       python%{pyver}-debtcollector >= 1.2.0
# Handle python2 exception
%if %{pyver} == 2
Requires:       python-ipaddress
%endif

%description -n python%{pyver}-%{pkg_name}
%{common_desc}


%package -n python%{pyver}-%{pkg_name}-tests
Summary:   Tests for OpenStack Oslo serialization library
%{?python_provide:%python_provide python2-%{pkg_name}}

Requires:  python%{pyver}-%{pkg_name} = %{version}-%{release}
Requires:  python%{pyver}-hacking
Requires:  python%{pyver}-mock
Requires:  python%{pyver}-oslotest
Requires:  python%{pyver}-oslo-i18n
Requires:  python%{pyver}-stestr
Requires:  python%{pyver}-netaddr
Requires:  python%{pyver}-simplejson

%description -n python%{pyver}-%{pkg_name}-tests
Tests for OpenStack Oslo serialization library

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:    Documentation for the Oslo serialization library

BuildRequires:  python%{pyver}-sphinx
BuildRequires:  python%{pyver}-openstackdocstheme

Requires:  python%{pyver}-%{pkg_name} = %{version}-%{release}

%description -n python-%{pkg_name}-doc
Documentation for the Oslo serialization library.
%endif

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git
# Let RPM handle the dependencies
rm -f requirements.txt

%build
%{pyver_build}

%if 0%{?with_doc}
# doc
sphinx-build-%{pyver} -W -b html doc/source doc/build/html
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{pyver_install}

%check
export OS_TEST_PATH="./oslo_serialization/tests"
PYTHON=python%{pyver} stestr-%{pyver} --test-path $OS_TEST_PATH run

%files -n python%{pyver}-%{pkg_name}
%doc README.rst
%license LICENSE
%{pyver_sitelib}/oslo_serialization
%{pyver_sitelib}/*.egg-info
%exclude %{pyver_sitelib}/oslo_serialization/tests

%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%files -n python%{pyver}-%{pkg_name}-tests
%{pyver_sitelib}/oslo_serialization/tests

%changelog
