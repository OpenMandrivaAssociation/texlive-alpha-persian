%global tl_name alpha-persian
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Persian version of alpha.bst
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/alpha-persian
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alpha-persian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alpha-persian.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a Persian version of the alpha BibTeX style and
offers several enhancements. It is compatible with the hyperref, url,
natbib, and cite packages.

