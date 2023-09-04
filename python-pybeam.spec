Name:		python-pybeam
Version:	0.7
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pybeam/pybeam-%{version}.tar.gz
Summary:	Python module to parse Erlang BEAM files
URL:		https://pypi.org/project/pybeam/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Python module to parse Erlang BEAM files

%prep
%autosetup -p1 -n pybeam-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/pybeam
%{py_sitedir}/pybeam-*.*-info
