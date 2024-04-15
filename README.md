# Purpose

This package was created in order to allow the installation of package dependencies on other Ubuntu versions that are not available on U20.

Example: `libavif-bin` and `libavif-dev` are available on u22 and higher but not u20, therefore we need a way for a package that Requires it, such as `ea-php81-php-gd`, to install it only on u22 and higher otherwise install this package which does nothing besides satisfy the requirement.

