%global tl_name hitreport
%global tl_revision 58357

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.0
Release:	%{tl_revision}.1
Summary:	Harbin Institute of Technology Report LaTeX Template
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hitreport
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hitreport.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hitreport.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hitreport.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides an assignment and experiment report template free
of configuration designed for undergraduates on the three campuses of
Harbin Institute of Technology.

