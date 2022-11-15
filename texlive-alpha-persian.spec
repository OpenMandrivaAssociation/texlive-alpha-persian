Name:		texlive-alpha-persian
Version:	50316
Release:	1
Summary:	Persian version of alpha.bst
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/alpha-persian
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alpha-persian.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alpha-persian.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a Persian version of the alpha BibTeX
style and offers several enhancements. It is compatible with
the hyperref, url, natbib, and cite packages.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/bibtex/bst/alpha-persian
%doc %{_texmfdistdir}/doc/bibtex/alpha-persian

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
