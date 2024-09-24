%global  qt_version 6.7.2

Summary: Qt6 - LanguageServer component
Name:    qt6-qtlanguageserver
Version: 6.7.2
Release: 0%{?dist}

License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://qt.io

Source0: %{name}-%{version}.tar.bz2

BuildRequires: cmake
BuildRequires: clang
BuildRequires: ninja
BuildRequires: qt6-qtbase-devel >= %{qt_version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

%description
The Qt Language Server component provides an implementation of the Language
Server protocol.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
%{summary}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_qt6

%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
%{_qt6_libdir}/libQt6JsonRpc.so.6*
%{_qt6_libdir}/libQt6LanguageServer.so.6*

%files devel
%{_qt6_headerdir}/QtJsonRpc/
%{_qt6_headerdir}/QtLanguageServer/
%{_qt6_libdir}/libQt6JsonRpc.prl
%{_qt6_libdir}/libQt6JsonRpc.so
%{_qt6_libdir}/libQt6LanguageServer.prl
%{_qt6_libdir}/libQt6LanguageServer.so
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtLanguageServer*
%{_qt6_libdir}/cmake/Qt6JsonRpcPrivate/
%{_qt6_libdir}/cmake/Qt6LanguageServerPrivate/
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_jsonrpc*.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_languageserver*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/qt6/modules/JsonRpcPrivate.json
%{_qt6_libdir}/qt6/modules/LanguageServerPrivate.json
#{_qt6_libdir}/pkgconfig/*.pc
