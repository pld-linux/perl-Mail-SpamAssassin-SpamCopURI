#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Mail
%define		pnam	SpamAssassin-SpamCopURI
Summary:	Mail::SpamAssassin::SpamCopURI - blacklist checking of URLs in email
Name:		perl-Mail-SpamAssassin-SpamCopURI
Version:	0.24
Release:	0.1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mail/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	12e0f6c5f4db1d5be8d335d9b1e06be4
URL:		http://search.cpan.org/dist/Mail-SpamAssassin-SpamCopURI/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The first checks that SpamCopURI does is against the whitelist/blacklist.
If the URL's host appears in the whitelist, then the test is an
immediate miss.  If the URL's host is in the blacklist, then the
test is an immediate hit.

This currently only checks URIs that support methods for host. 
These are typically just http, https, and ftp.

If the spamcop_uri_limit is set (which it is by default)
and the number of URLs in the message exceeds this limit,
the URLs are shuffled and testing is done only up to the
limit.  The limit is to prevent DOS attacks, the shuffling
is done to prevent front-loading of URLs that will fill
the limit up with valid URLs.


The network method tests the domain portion of the URI against
a RHS RBL DNS rbl list that is specified in a conf file. If
the domain appears in the RBL, then the test scores a hit.

If open redirect resolution is enabled, then the url's host
will be compared against the open_redirect_list_spamcop_uri
and if a match is found, then the an attempt is made to 
get the Location header from the redirect service without actually
fetching from the destination site.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%{perl_vendorlib}/Mail/SpamAssassin/*.pm
%{perl_vendorlib}/Mail/SpamAssassin/SpamCopURI
%{_mandir}/man3/*
