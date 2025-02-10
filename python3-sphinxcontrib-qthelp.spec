#
# Conditional build:
%bcond_with	tests	# unit tests (failing?)

Summary:	Sphinx extension which outputs QtHelp documents
Summary(pl.UTF-8):	Rozszerzenie Sphinksa zapisujące dokumenty QtHelp
Name:		python3-sphinxcontrib-qthelp
Version:	2.0.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-qthelp/
Source0:	https://pypi.debian.net/sphinxcontrib-qthelp/sphinxcontrib_qthelp-%{version}.tar.gz
# Source0-md5:	ed4f32003b71a54ac3d68aa651cb6573
URL:		https://pypi.org/project/sphinxcontrib-qthelp/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.5
%if %{with tests}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
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
%setup -q -n sphinxcontrib_qthelp-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENCE.rst README.rst
%{py3_sitescriptdir}/sphinxcontrib/qthelp
%{py3_sitescriptdir}/sphinxcontrib_qthelp-%{version}.dist-info
