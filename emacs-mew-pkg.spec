Summary:	Great MIME mail reader for Emacs/XEmacs 
Summary(pl):	Wspania³y czytnik poczty MIME dla Emacs/XEmacs
Name:		emacs-mew-pkg
%define 	srcname	mew
Version:	2.2
Release:	1
License:	BSD
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.mew.org/pub/Mew/release/mew-2.2.tar.gz
URL:		http://www.mew.org/
BuildRequires:	emacs
Requires:	emacs >= 20.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Messaging in an Emacs World.

%description -l pl
Komunikowanie w ¦wiecie Emacsa.

%prep
%setup -q -n %{srcname}-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	prefix=%{__prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc 00* contrib
%attr(755,root,root) %{_bindir}/*
%{_libdir}/emacs/etc/Mew
%{_mandir}/man?/*
%dir %{_datadir}/emacs/site-lisp/mew
%{_datadir}/emacs/site-lisp/mew/*.elc
%{_datadir}/emacs/site-lisp/mew/mew-gemacs.el*
%{_datadir}/emacs/site-lisp/mew/mew-lang-jp.el*
%{_datadir}/emacs/site-lisp/mew/mew-mule*.el*
%{_datadir}/emacs/site-lisp/mew/mew-unix.el*
%{_datadir}/emacs/site-lisp/mew/mew-win32.el*
%{_datadir}/emacs/site-lisp/mew/mew-xemacs.el*
%{_infodir}/mew*
