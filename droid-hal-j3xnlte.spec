# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device j3xnlte
%define vendor samsung

%define vendor_pretty Samsung
%define device_pretty Galaxy J3 (2016)

%define installable_zip 1

%define enable_kernel_update 1

%define makefstab_skip_entries /dev/cpuctl /dev/stune

%define android_config \
#define MALI_QUIRKS 1 \
%{nil}

%define straggler_files \
/selinux_version\
/file_contexts.bin\
/property_contexts\
/service_contexts\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

