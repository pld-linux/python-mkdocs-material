#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Material Design theme for MkDocs
Summary(pl.UTF-8):	Motyw Material Design do MkDocs
Name:		python-mkdocs-material
Version:	4.1.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/mkdocs-metarial/
Source0:	https://files.pythonhosted.org/packages/source/m/mkdocs-material/mkdocs-material-%{version}.tar.gz
# Source0-md5:	18d4f27eae59f89ae5a38495e226fcb2
URL:		https://squidfunk.github.io/mkdocs-material/
%if %{with python2}
BuildRequires:	python-mkdocs >= 1
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pygments >= 2.2
BuildRequires:	python-pymdown-extensions >= 4.11
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-mkdocs >= 1
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-pygments >= 2.2
BuildRequires:	python3-pymdown-extensions >= 4.11
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Material Design theme for MkDocs.

%description -l pl.UTF-8
Motyw Material Design do MkDocs.

%package -n python3-mkdocs-material
Summary:	Material Design theme for MkDocs
Summary(pl.UTF-8):	Motyw Material Design do MkDocs
Group:		Libraries/Python

%description -n python3-mkdocs-material
Material Design theme for MkDocs.

%description -n python3-mkdocs-material -l pl.UTF-8
Motyw Material Design do MkDocs.

%prep
%setup -q -n mkdocs-material-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%py3_install
%endif

%if %{with python2}
%py_install

%py_postclean
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/material
%{py_sitescriptdir}/mkdocs_material-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-mkdocs-material
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/material
%{py3_sitescriptdir}/mkdocs_material-%{version}-py*.egg-info
%endif
