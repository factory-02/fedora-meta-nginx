Name:                           meta-nginx
Version:                        1.0.0
Release:                        1%{?dist}
Summary:                        META-package for install and configure NGINX

License:                        GPLv3

Source10:                       nginx.custom.conf

Requires:                       nginx

%description
META-package for install and configure NGINX.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%install
install -p -d -m 0755 %{buildroot}%{_sysconfdir}/nginx/conf.d
install -p -m 0644 %{SOURCE10} \
    %{buildroot}%{_sysconfdir}/nginx/conf.d/00-nginx.custom.conf

%files
%config(noreplace) %{_sysconfdir}/nginx/conf.d/00-nginx.custom.conf

%changelog
* Wed Jan 02 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.0-1
- Initial build.
