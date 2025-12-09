Name:		python-pybeam
Version:	0.8.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pybeam/pybeam-%{version}.tar.gz
Summary:	Python module to parse Erlang BEAM files
URL:		https://pypi.org/project/pybeam/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Python module to parse Erlang BEAM files

%files
%{py_sitedir}/pybeam
%{py_sitedir}/pybeam-*.*-info
