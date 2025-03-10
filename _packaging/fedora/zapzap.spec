# Arquivo .spec para Fedora

%global srcname zapzap
%global srcversion  4.5.5.2

%global __python /usr/bin/python3
%global _rpmfilename %%{NAME}-%%{VERSION}-%%{RELEASE}.rpm

Name:           %{srcname}
Version:        %{srcversion}
Release:        2%{?dist}
Summary:        Zapzap - Whatsapp Desktop for Linux

License:        GNU General Public License v3.0
URL:            https://github.com/zapzap-linux/%{srcname}
Source0:        https://github.com/zapzap-linux/zapzap/archive/refs/tags/%{srcversion}.tar.gz


# Requisitos de construção
BuildArch:     noarch
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  python3-setuptools

BuildRequires:   python3-pyqt6
Requires:   python3-pyqt6-base
Requires:   python3-pyqt6-sip
Requires:   python3-pyqt6-webengine
Requires:   python3-dbus

%description
Zapzap - Whatsapp Desktop for Linux

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%python3 setup.py install --root %{buildroot}
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/scalable/apps/
cp -R share/applications/com.rtosta.zapzap.desktop $RPM_BUILD_ROOT/usr/share/applications/com.rtosta.zapzap.desktop
cp -R share/icons/com.rtosta.zapzap.svg $RPM_BUILD_ROOT/usr/share/icons/hicolor/scalable/apps/com.rtosta.zapzap.svg


%check

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%{_bindir}/%{srcname}
/usr/share/applications/com.rtosta.zapzap.desktop
/usr/share/icons/hicolor/scalable/apps/com.rtosta.zapzap.svg

%changelog
* Wed may 31 2023 Rafael Tosta <rafa.ecomp@gmail.com> 
- 1.0
- Initial package release

%changelog
* Thu ago 17 2023 Rafael Tosta <rafa.ecomp@gmail.com> 
- Update UserAgent 
- Fix close chat
- Zap Decoration deactivated by default

%changelog
* Fri sept 15 2023 Rafael Tosta <rafa.ecomp@gmail.com> 
- Update UserAgent 
- Support to Wayland or X11 in FedoraCopr
- Improve the menu decoration when running in Wayland
- Fix F5 does not work outside the chat
- Notification in the background when starting minimized
- Disable notifications in Users management

%changelog
* Thu sept 21 2023 Rafael Tosta <rafa.ecomp@gmail.com> 
- Improvements in user experience (UX/UI)

%changelog
* Mon oct 02 2023 Rafael Tosta <rafa.ecomp@gmail.com> 
- Fix: Improve the menu decoration when running in Wayland 
- Fix: Message number doesnt show on the tray icon

%changelog
* Wed oct 18 2023 Rafael Tosta <rafa.ecomp@gmail.com> 
- Some fix

%changelog
* Mon oct 23 2023 Rafael Tosta <rafa.ecomp@gmail.com> 
- Update translations

%changelog
* Thu nov 02 2023 Rafael Tosta <rafa.ecomp@gmail.com> 
- Copy URLs with the right-click of the mouse
- Fix: Notifications do not disappear after viewing on another device
- Display the last message on system notifications