
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name oslo.serialization
%global pkg_name oslo-serialization
%global with_doc 1

%global common_desc \
An OpenStack library for representing objects in transmittable and \
storable formats.

Name:           python-%{pkg_name}
Version:        3.1.1
Release:        1%{?dist}
Summary:        OpenStack oslo.serialization library

License:        ASL 2.0
URL:            https://launchpad.net/oslo
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch

%description
%{common_desc}

%package -n python3-%{pkg_name}
Summary:        OpenStack oslo.serialization library
%{?python_provide:%python_provide python3-%{pkg_name}}

BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
# test requirements
BuildRequires:  python3-hacking
BuildRequires:  python3-mock
BuildRequires:  python3-oslotest
BuildRequires:  python3-oslo-i18n
BuildRequires:  python3-stestr
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-msgpack >= 0.5.2
BuildRequires:  python3-netaddr
BuildRequires:  python3-simplejson

Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-msgpack >= 0.5.2
Requires:       python3-pytz
Requires:       python3-debtcollector >= 1.2.0

%description -n python3-%{pkg_name}
%{common_desc}


%package -n python3-%{pkg_name}-tests
Summary:   Tests for OpenStack Oslo serialization library
%{?python_provide:%python_provide python2-%{pkg_name}}

Requires:  python3-%{pkg_name} = %{version}-%{release}
Requires:  python3-hacking
Requires:  python3-mock
Requires:  python3-oslotest
Requires:  python3-oslo-i18n
Requires:  python3-stestr
Requires:  python3-netaddr
Requires:  python3-simplejson

%description -n python3-%{pkg_name}-tests
Tests for OpenStack Oslo serialization library

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:    Documentation for the Oslo serialization library

BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme

Requires:  python3-%{pkg_name} = %{version}-%{release}

%description -n python-%{pkg_name}-doc
Documentation for the Oslo serialization library.
%endif

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git
# Let RPM handle the dependencies
rm -f requirements.txt

%build
%{py3_build}

%if 0%{?with_doc}
# doc
sphinx-build-3 -W -b html doc/source doc/build/html
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

%check
export OS_TEST_PATH="./oslo_serialization/tests"
PYTHON=python3 stestr-3 --test-path $OS_TEST_PATH run

%files -n python3-%{pkg_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/oslo_serialization
%{python3_sitelib}/*.egg-info
%exclude %{python3_sitelib}/oslo_serialization/tests

%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_serialization/tests

%changelog
* Thu Apr 23 2020 RDO <dev@lists.rdoproject.org> 3.1.1-1
- Update to 3.1.1

