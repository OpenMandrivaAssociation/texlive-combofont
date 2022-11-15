Name:		texlive-combofont
Version:	51348
Release:	1
Summary:	Add NFSS-declarations of combo fonts to LuaLaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/combofont
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/combofont.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/combofont.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This highly experimental package can be used to add
NFSS-declarations of combo fonts to LuaLaTeX documents. This
package may disappear without notice, e.g. if luaotfload
changes in a way so that it no longer works, or if LuaTeX
changes, or if fontspec itself includes the code. It is also
possible that the package's syntax and commands may change in
an incompatible way. So if you use it in a production
environment: You have been warned.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/combofont
%doc %{_texmfdistdir}/doc/lualatex/combofont

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
