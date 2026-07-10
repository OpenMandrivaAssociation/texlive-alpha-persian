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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a Persian version of the alpha BibTeX style and
offers several enhancements. It is compatible with the hyperref, url,
natbib, and cite packages.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/bibtex
%dir %{_datadir}/texmf-dist/bibtex/bst/alpha-persian
%dir %{_datadir}/texmf-dist/doc/bibtex/alpha-persian
%dir %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/image
%{_datadir}/texmf-dist/bibtex/bst/alpha-persian/alpha-persian.bst
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/README.txt
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/alpha-persian-l.userguide.pdf
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/alpha-persian-l.userguide.tex
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/alpha-persian-p.userguide.pdf
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/alpha-persian-p.userguide.tex
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/image/21.jpg
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/image/sh11.jpg
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/image/sh12.jpg
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/image/sh13.jpg
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/image/sh14.PNG
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/image/sh15.PNG
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/image/sh16.PNG
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/image/sh17.PNG
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/image/sh18.jpg
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/image/sh2.jpg
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/image/sh20.jpg
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/image/sh3.jpg
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/image/sh4.jpg
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/image/sh5.jpg
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/image/sh6.jpg
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/image/sh7.jpg
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/image/sh8.jpg
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/image/sh9.jpg
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/image/sht.jpg
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/pdflatexsample.tex
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/sample1.bib
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/sample10.bib
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/sample2.bib
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/sample3.bib
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/sample4.bib
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/sample5.bib
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/sample6.bib
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/sample7.bib
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/sample8.bib
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/sample9.bib
%doc %{_datadir}/texmf-dist/doc/bibtex/alpha-persian/xelatexsample.tex
