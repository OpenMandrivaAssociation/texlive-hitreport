Name:		texlive-hitreport
Version:	58357
Release:	2
Summary:	Harbin Institute of Technology Report LaTeX Template
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hitreport
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hitreport.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hitreport.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hitreport.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an assignment and experiment report
template free of configuration designed for undergraduates on
the three campuses of Harbin Institute of Technology.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/hitreport
%{_texmfdistdir}/tex/latex/hitreport
%doc %{_texmfdistdir}/doc/latex/hitreport

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
