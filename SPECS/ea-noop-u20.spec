Name:           ea-noop-u20
Version:        1.0
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4552 for more details
%define release_prefix 2
Release:        %{release_prefix}%{?dist}.cpanel
Summary:        Noop package that helps solve dep issue
License:        GPL
Group:          System Environment/Libraries
URL:            http://www.cpanel.net
Vendor:         cPanel, Inc.
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Provides: libavif-bin, libavif-dev, ea-wappspector

%description
This package does nothing but satisfy required dependencies in other Ubuntu versions.

%build
echo "Nothing to build"

%install
echo "Nothing to install"

%clean
rm -rf %{buildroot}

%changelog
* Fri Sep 26 2025 Brian Mendoza <brian.mendoza@webpros.com> - 1.0-2
- EA4-112: Add ea-wappspector

* Thu Mar 14 2024 Brian Mendoza <brian.mendoza@cpanel.net> - 1.0-1
- ZC-11698: Initial build
