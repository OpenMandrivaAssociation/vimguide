%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	Vim editor reference guide
Name:		vimguide
Version:	0.7
Release:	%mkrel 7
Group:		Books/Other
License:	OpenSource
URL:		ftp://ftp.vim.org/pub/vim/doc/
Source0:	ftp://ftp.vim.org/pub/vim/doc/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This is a command and feature reference guide to VIM 5.6 but can also be used
for higher version of vim.

VIM (stands for Vi IMproved) - greatly improved (over original UNIX vi) text
editor with GUI, syntax highlighting, visual mode and many more new features
you won't find in the original vi.

This guide is designed and typeset by Oleg Raisky using LaTeX. The text of the
guide is comprised of various VIM documentation files, sometimes modified for
better consistency with overall style of the guide.

*NOTE*: this is NOT a complete user guide or tutorial. The only purpose of this
guide is to give a VIM user a quick and handy reference.

%prep

%setup -q -n %{name}-%{version}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc * 


