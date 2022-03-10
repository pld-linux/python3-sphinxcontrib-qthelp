#
# Conditional build:
%bcond_with	tests	# unit tests (failing?)

Summary:	Sphinx extension which outputs QtHelp documents
Summary(pl.UTF-8):	Rozszerzenie Sphinksa zapisujące dokumenty QtHelp
Name:		python3-sphinxcontrib-qthelp
Version:	1.0.3
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-qthelp/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-qthelp/sphinxcontrib-qthelp-%{version}.tar.gz
# Source0-md5:	93216721f3e154cce12d1e9c3307b415
URL:		https://pypi.org/project/sphinxcontrib-qthelp/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp
documents.

%description -l pl.UTF-8
sphinxcontrib-qthelp to rozszerzenie Sphinksa, zapisujące dokumenty
QtHelp.

%prep
%setup -q -n sphinxcontrib-qthelp-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%{py3_sitescriptdir}/sphinxcontrib/qthelp
%{py3_sitescriptdir}/sphinxcontrib_qthelp-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_qthelp-%{version}-py*-nspkg.pth
