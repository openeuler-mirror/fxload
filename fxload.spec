Name:    fxload
Version: 2008_10_13
Release: 20
Summary: A program which downloads firmware to USB devices
License: GPLv2+
URL:     http://linux-hotplug.sourceforge.net/
Source0: https://netix.dl.sourceforge.net/project/linux-hotplug/fxload/2008_10_13/%{name}-%{version}.tar.gz

BuildRequires:  gcc
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
%autosetup -n %{name}-%{version} -p1

%build
make CC=$CC CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"

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
* Thu Apr 13 2023 SaltyFruit <saltyfruit255@gmail.com> - 2008_10_13-20
- Fix CC compiler support

* Thu May 19 2022 chengwenzhe <chengwenzhe@uniontech.com> - 2008_10_13-19
- fix spec changelog date time

* Fri Jul 30 2021 chenyanpanHW <chenyanpan@huawei.com> - 2008_10_13-18
- DESC: delete -S git from %autosetup, and delete BuildRequires git

* Tue Jun 29 2021 zhouwenpei <zhouwenpei1@huawei.com> - 2008_10_13-17
- add buildrequire gcc.

* Thu Sep 3 2020 lihaotian<lihaotian9@huawei.com> - 2008_10_13-16
- Fix source0 url

* Wed Sep 2 2020 lihaotian<lihaotian9@huawei.com> - 2008_10_13-15
- Update source0 url.

* Tue Jan 7 2020 openEuler Buildteam <buildteam@openeuler.org> - 2008_10_13-14
- rePackage

* Wed Sep 11 2019 openEuler Buildteam <buildteam@openeuler.org> - 2008_10_13-13
- Package init
