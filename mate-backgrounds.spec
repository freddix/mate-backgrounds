Summary:	Set of backgrounds for MATE desktop
Name:		mate-backgrounds
Version:	1.8.0
Release:	1
License:	GPL v2
Group:		Themes
Source0:	http://pub.mate-desktop.org/releases/1.8/%{name}-%{version}.tar.xz
# Source0-md5:	1b6adb6f732941afbf8f0f722b361fe4
URL:		http://mate-desktop.org/
BuildRequires:	intltool
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of backgrounds for MATE desktop.

# subpackages created to save some space on live media
# default "Stripes.jpg" included in desktop subpkg

%package abstract
Summary:	MATE abstract backgrounds
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description abstract
MATE abstract backgrounds.

%package desktop
Summary:	MATE desktop backgrounds
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description desktop
MATE desktop backgrounds.

%package nature
Summary:	MATE nature backgrounds
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description nature
MATE nature backgrounds.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{as,ca@valencia,en@shaw}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/backgrounds/mate

%files abstract
%defattr(644,root,root,755)
%{_datadir}/mate-background-properties/mate-abstract.xml
%{_datadir}/backgrounds/mate/abstract

%files desktop
%defattr(644,root,root,755)
%{_datadir}/mate-background-properties/mate-desktop.xml
%{_datadir}/backgrounds/mate/desktop

%files nature
%defattr(644,root,root,755)
%{_datadir}/mate-background-properties/mate-nature.xml
%{_datadir}/backgrounds/mate/nature

