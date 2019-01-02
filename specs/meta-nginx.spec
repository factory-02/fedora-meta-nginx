Name:                           meta-nginx
Version:                        1.0.0
Release:                        1%{?dist}
Summary:                        META-package for install NGINX

License:                        GPLv3

Source10:                       nginx.custom.conf

Requires:                       nginx

%description
META-package for install NGINX.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%install
install -p -m 0644 %{SOURCE10} \
    %{buildroot}%{_sysconfdir}/nginx/conf.d/00-nginx.custom.conf

%files
%config(noreplace) %{_sysconfdir}/nginx/00-nginx.custom.conf

%changelog
* Wed Jan 02 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.0-1
- Initial build.
