Summary:	Great MIME mail reader for Emacs/XEmacs
Summary(pl.UTF-8):	Wspaniały czytnik poczty MIME dla Emacs/XEmacs
Name:		emacs-mew-pkg
%define 	srcname	mew
Version:	4.2
Release:	1
License:	BSD
Group:		Applications/Editors/Emacs
Source0:	http://www.mew.org/Release/mew-%{version}.tar.gz
# Source0-md5:	713e45d6358330309414adbaad3944f5
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.mew.org/
BuildRequires:	emacs
Requires:	emacs >= 20.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Messaging in an Emacs World.

%description -l pl.UTF-8
Komunikowanie w Świecie Emacsa.

%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p0

%build
cd bin
%{__autoconf}
%{__autoheader}
%configure
cd ..
%{__autoconf}
%configure

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc 00* contrib
%attr(755,root,root) %{_bindir}/*
%{_emacs_lispdir}/mew
%{_mandir}/man?/*
%{_infodir}/*.info*
