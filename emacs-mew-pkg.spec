Summary:	Great MIME mail reader for Emacs/XEmacs
Summary(pl):	Wspania³y czytnik poczty MIME dla Emacs/XEmacs
Name:		emacs-mew-pkg
%define 	srcname	mew
Version:	3.3
Release:	1
License:	BSD
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.mew.org/pub/Mew/release/mew-%{version}.tar.gz
# Source0-md5:	81b986698d5d356df19442546a6c993e
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
%{_datadir}/emacs/site-lisp/mew/mew*.el*
%{_infodir}/mew*
