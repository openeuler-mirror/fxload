Name:    fxload
Version: 2008_10_13
Release: 14
Summary: A program which downloads firmware to USB devices
License: GPLv2+
URL:     http://linux-hotplug.sourceforge.net/
Source0: https://sourceforge.net/projects/linux-hotplug/files/fxload/2008_10_13/%{name}-%{version}.tar.gz

BuildRequires: git
Requires:      udev

%description
It is conveniently able to download firmware into FX, FX2, and FX2LP EZ-USB devices,
as well as the original AnchorChips EZ-USB. It is intended to be invoked by hotplug
scripts when the unprogrammed device appears on the bus.


%package        help
Summary:        Including man files for fxload
Requires:       man

%description    help
This contains man files for the using of fxload.

%prep
%autosetup -n %{name}-%{version} -p1 -S git

%build
make CC=gcc CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"

%install
install -D -m 755 fxload %{buildroot}/sbin/fxload
install -D -m 644 fxload.8 %{buildroot}/%{_mandir}/man8/fxload.8

%files
%license COPYING
%doc README.txt
%attr(0755, root, root) /sbin/fxload

%files help
%{_mandir}/*/*

%changelog
* Mon Jan 7 2020 openEuler Buildteam <buildteam@openeuler.org> - 2008_10_13-14
- rePackage

* Wed Sep 11 2019 openEuler Buildteam <buildteam@openeuler.org> - 2008_10_13-13
- Package init
