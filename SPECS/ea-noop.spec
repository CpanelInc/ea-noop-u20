Name:           ea-noop
Version:        1.0
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4552 for more details
%define release_prefix 1
Release:        %{release_prefix}%{?dist}.cpanel
Summary:        Noop package for U20
License:        GPL
Group:          System Environment/Libraries
URL:            http://www.cpanel.net
Vendor:         cPanel, Inc.
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package does nothing but satisfy required dependencies in other Ubuntu versions.

%build
echo "Nothing to build"

%install
echo "Nothing to install"

%clean
rm -rf %{buildroot}

%changelog
* Thu Mar 14 2024 Brian Mendoza <brian.mendoza@cpanel.net> - 1.0-1
- ZC-11698: Initial build
