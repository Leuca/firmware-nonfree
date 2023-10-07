%define debug_package %{nil}

Name:       raspberrypi-firmware-nonfree
Version:    {{{ get_version_from_changelog }}}
Release:    1%{?dist}
Summary:    Firmware for Rasbperry Pi Wi-Fi

BuildArch:  noarch

%global workdir debian/config

License:    binary-redist-Broadcom-wifi
URL:        https://github.com/Leuca/firmware-nonfree/tree/bullseye/debian/config/brcm80211/brcm
VCS:        {{{ git_dir_vcs }}}

Source:     {{{ git_dir_pack }}}

%description
Binary firmware for Raspberry Pi wireless drivers in the Linux kernel.
This package depends on both free and non-free firmware which may
be used with drivers in the Linux kernel.

%prep
{{{ git_dir_setup_macro }}}

%install
mkdir -p %{buildroot}%{_prefix}/lib/firmware/cypress
mkdir %{buildroot}%{_prefix}/lib/firmware/brcm

# Install Cypress files
for cypress_file in $( ls %{workdir}/brcm80211/cypress );
do
	cp %{workdir}/brcm80211/cypress/$cypress_file %{buildroot}%{_prefix}/lib/firmware/cypress
	echo "%{_prefix}/lib/firmware/cypress/$cypress_file" >> file_list.txt
done

# Install Broadcom files
for brcm_file in $( ls %{workdir}/brcm80211/brcm );
do
	cp -P %{workdir}/brcm80211/brcm/$brcm_file %{buildroot}%{_prefix}/lib/firmware/brcm
	echo "%{_prefix}/lib/firmware/brcm/$brcm_file" >> file_list.txt
done

%files -f file_list.txt
%license debian/copyright

%changelog
{{{ git_dir_changelog }}}
