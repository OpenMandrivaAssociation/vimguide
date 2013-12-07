%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	Vim editor reference guide
Name:		vimguide
Version:	0.7
Release:	18
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




%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7-11mdv2011.0
+ Revision: 670767
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7-10mdv2011.0
+ Revision: 608125
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7-9mdv2010.1
+ Revision: 524309
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.7-8mdv2010.0
+ Revision: 427494
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.7-7mdv2009.0
+ Revision: 225918
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7-6mdv2008.1
+ Revision: 179680
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Mar 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0.7-5mdv2007.1
+ Revision: 145174
- Import vimguide

* Fri Mar 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0.7-5mdv2007.1
- use the %%mrel macro
- it's a noarch package

